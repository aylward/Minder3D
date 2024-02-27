import numpy as np

import itk

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
)

from ptvState import PTVState

from sovColorMapUtils import (
    get_nearest_color_index_and_name
)

from sovUtils import (
    read_group,
    get_children_as_list,
)

from sovView3DUtils import (
    get_object_forms
)

from sovView2DPanelWidget import View2DPanelWidget
from sovView3DPanelWidget import View3DPanelWidget

from sovVisualizationPanelWidget import VisualizationPanelWidget
from sovPreProcessPanelWidget import PreProcessPanelWidget
from sovLungAIPanelWidget import LungAIPanelWidget
from sovScreenCapturePanelWidget import ScreenCapturePanelWidget
from sovChatPanelWidget import ChatPanelWidget

from ui_pytubeview import Ui_MainWindow


class PTVWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.state = PTVState()

        # File Menu
        self.loadImageMenuItem.triggered.connect(self.load_image)
        self.loadSceneMenuItem.triggered.connect(self.load_scene)

        for color_name, _ in self.state.colormap.items():
            self.objectColorComboBox.addItem(color_name)

        self.connect_object_gui()

        self.objectDeleteButton.pressed.connect(
            self.delete_current_object
            )

        self.objectPropertiesToAllButton.pressed.connect(
            self.propogate_properties_to_all
            )

        self.objectPropertiesToChildrenButton.pressed.connect(
            self.propogate_properties_to_children
            )
        
        self.objectHightlightSelectedCheckBox.stateChanged.connect(
            self.update_highlight_selected
        )

        # View 2D Widget
        self.view2DPanel = View2DPanelWidget(self, self.state)
        self.view2DPanelLayout.addWidget(self.view2DPanel)

        # View 3D Widget
        self.view3DPanel = View3DPanelWidget(self, self.state)
        self.view3DPanelLayout.addWidget(self.view3DPanel)

        # Visualization Tab
        self.visualizationPanel = VisualizationPanelWidget(self, self.state)
        self.visualizationPanelLayout.addWidget(self.visualizationPanel)

        # PreProcess Tab
        self.preProcessPanel = PreProcessPanelWidget(self, self.state)
        self.preProcessPanelLayout.addWidget(self.preProcessPanel)

        # LungAI Tab
        self.lungAIPanel = LungAIPanelWidget(self, self.state)
        self.lungAIPanelLayout.addWidget(self.lungAIPanel)

        # ScreenCapture Tab
        self.screenCapturePanel = ScreenCapturePanelWidget(self, self.state)
        self.screenCapturePanelLayout.addWidget(self.screenCapturePanel)

        # Chat Tab
        self.chatPanel = ChatPanelWidget(self, self.state)
        self.chatPanelLayout.addWidget(self.chatPanel)

        self.show()
        self.view2DPanel.initialize()
        self.view3DPanel.initialize()

    def connect_object_gui(self):
        self.objectNameComboBox.currentIndexChanged.connect(
            self.select_object_by_name_combobox
            )

        self.objectColorByComboBox.currentIndexChanged.connect(
            self.modify_current_object
            )

        self.objectColorComboBox.currentIndexChanged.connect(
            self.modify_current_object
            )

        self.objectOpacitySlider.valueChanged.connect(
            self.modify_current_object
            )

    def disconnect_object_gui(self):
        self.objectNameComboBox.currentIndexChanged.disconnect(
            self.select_object_by_name_combobox
        )

        self.objectColorByComboBox.currentIndexChanged.disconnect(
            self.modify_current_object
        )

        self.objectColorComboBox.currentIndexChanged.disconnect(
            self.modify_current_object
        )

        self.objectOpacitySlider.valueChanged.disconnect(
            self.modify_current_object
        )

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.view2DPanel.close()
        self.view3DPanel.close()

    def load_image(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(
                self,
                "Open File",
                self.state.loaded_image_filename,
                "All Files (*)"
            )
        if filename:
            self.state.loaded_image_filename = filename
            self.state.loaded_image = itk.imread(
                filename,
                self.state.image_pixel_type
            )
            self.state.image = self.state.loaded_image
            self.state.image_array = itk.GetArrayFromImage(self.state.image)
            self.state.overlay = self.state.overlay_type.New()
            self.state.overlay.SetRegions(
                self.state.image.GetLargestPossibleRegion()
            )
            self.state.overlay.CopyInformation(self.state.image)
            self.state.overlay.Allocate()
            self.state.overlay.FillBuffer(self.state.overlay_pixel_type(0))
            self.state.overlay_array = itk.GetArrayFromImage(
                self.state.overlay
            )
            self.update_image()
            self.update_overlay()

    def load_scene(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(
                self,
                "Open File",
                self.state.loaded_scene_filename,
                "All Files (*)"
            )
        if filename:
            self.state.loaded_scene_filename = filename
            self.state.scene = read_group(filename)
        self.update_scene()

    def update_image(self):
        self.state.image_min = float(np.min(self.state.image_array))
        self.state.image_max = float(np.max(self.state.image_array))

        self.view2DPanel.update_image()
        self.view3DPanel.update_image()

        self.visualizationPanel.update_image()

    def update_overlay(self):
        self.view2DPanel.update_overlay()

    def update_scene(self):
        print("ptv update_scene")
        self.state.scene_list = get_children_as_list(self.state.scene)
        self.state.scene_list_ids = []
        self.state.scene_list_properties = []

        self.disconnect_object_gui()
        self.objectNameComboBox.clear()
        self.objectNameComboBox.addItem("None")
        for so in self.state.scene_list:
            self.state.scene_list_ids.append(so.GetId())
            self.state.scene_list_properties.append(
                dict(ColorBy="Solid Color")
                )
            self.objectNameComboBox.addItem(f"{so.GetTypeName()} {so.GetId()}")
        self.view2DPanel.update_scene()
        self.view3DPanel.update_scene()
        self.connect_object_gui()

    def select_object_by_name_combobox(self):
        print("ptv select_object_by_name_combobox")
        idx = self.objectNameComboBox.currentIndex()
        if idx == 0:
            return
        idx -= 1
        so = self.state.scene_list[idx]
        so_id = so.GetId()
        # Unselect currently selected objects
        for selected_idx,selected_so_id in enumerate(self.state.selected_ids):
            if selected_so_id != -1 and selected_so_id != so_id:
                scene_idx = self.state.scene_list_ids.index(selected_so_id)
                selected_so = self.state.scene_list[scene_idx]
                self.state.selected_ids[selected_idx] = -1
                self.redraw_object(selected_so)
        self.state.selected_ids = [so_id]
        self.state.selected_point_ids = [0]
        self.redraw_object(so)

    def redraw_object(self, so, update_2D=True, update_3D=True):
        print("ptv redraw_object")
        so_id = so.GetId()
        if so_id not in self.state.scene_list_ids:
            print("ERROR: so_id not in scene_list_ids")
            return
        scene_idx = self.state.scene_list_ids.index(so_id)

        self.disconnect_object_gui()

        self.objectNameComboBox.setCurrentIndex(scene_idx+1)

        c = so.GetProperty().GetColor()
        color = [c.GetRed(), c.GetGreen(), c.GetBlue(), c.GetAlpha()]
        color[0:3] = np.array(color)[0:3]*self.state.colormap_scale_factor
        color[3] = color[3]*100.0
        self.objectOpacitySlider.setValue(color[3])
        _, color_name = get_nearest_color_index_and_name(
            color[0:3], self.state.colormap
        )
        self.objectColorComboBox.setCurrentText(color_name)

        if update_2D:
            self.view2DPanel.redraw_object(so)
        if update_3D:
            self.view3DPanel.redraw_object(so)

        # Must call after view3DPanel.redraw_object() so that actors defined.
        self.objectColorByComboBox.clear()
        self.objectColorByComboBox.addItem("Solid Color")
        actor = self.state.scene_list_properties[scene_idx].get("Actor")
        if actor is not None:
            pdata = actor.GetMapper().GetInput()
            for i in range(pdata.GetPointData().GetNumberOfArrays()):
                pname = pdata.GetPointData().GetArrayName(i)
                self.objectColorByComboBox.addItem(pname)

            self.objectColorByComboBox.setCurrentText(
                self.state.scene_list_properties[scene_idx]["ColorBy"])

        self.connect_object_gui()

    def modify_current_object(self):
        print("ptv modify_current_object")
        idx = self.objectNameComboBox.currentIndex()
        if idx == 0:
            return
        idx -= 1
        so = self.state.scene_list[idx]
        color = np.empty(4)
        color[0:3] = self.state.colormap[self.objectColorComboBox.currentText()]
        color[0:3] /= self.state.colormap_scale_factor
        color[3] = self.objectOpacitySlider.value()/100.0
        so.GetProperty().SetColor(color)
        self.state.scene_list_properties[idx]["ColorBy"] = self.objectColorByComboBox.currentText()
        
        self.view2DPanel.redraw_object(so)
        self.view3DPanel.redraw_object(so)

    def delete_current_object(self):
        print("ptv delete_current_object")
        scene_idx = self.objectNameComboBox.currentIndex()
        if scene_idx == 0:
            return
        scene_idx -= 1
        self.state.scene_list.pop(scene_idx)
        self.state.scene_list_properties.pop(scene_idx)
        self.objectNameComboBox.removeItem(scene_idx+1)
        self.update_scene()
        if scene_idx in self.state.selected_ids:
            self.state.selected_ids.pop(scene_idx)
            self.state.selected_point_ids.pop(scene_idx)
            if len(self.state.selected_ids) > 0:
                next_so_id = self.state.selected_ids[-1]
                next_scene_idx = self.state.scene_list_ids.index(next_so_id)
                next_so = self.state.scene_list[next_scene_idx]
                self.redraw_object(next_so)

    def propogate_properties_to_all(self):
        print("ptv propogate_properties_to_all")
        scene_idx = self.objectNameComboBox.currentIndex()-1
        color_by = self.objectColorByComboBox.currentText()
        color = np.empty(4)
        color[0:3] = self.state.colormap[self.objectColorComboBox.currentText()]
        color[0:3] /= self.state.colormap_scale_factor
        color[3] = self.objectOpacitySlider.value()/100.0
        for idx in range(len(self.state.scene_list)):
            if idx != scene_idx:
                self.state.scene_list_properties[idx]["ColorBy"] = color_by
                self.state.scene_list[idx].GetProperty().SetColor(color)
                self.redraw_object(self.state.scene_list[idx])

    def propogate_properties_to_children(self):
        print("ptv propogate_properties_to_children")
        idx = self.objectNameComboBox.currentIndex()
        if idx == 0:
            return
        idx -= 1
        so = self.state.scene_list[idx]
        color_by = self.objectColorByComboBox.currentText()
        color = np.empty(4)
        color[0:3] = self.state.colormap[self.objectColorComboBox.currentText()]
        print("color", color)
        color[0:3] /= self.state.colormap_scale_factor
        color[3] = self.objectOpacitySlider.value()/100.0
        print("color", color)
        children = get_children_as_list(so)
        for child_so in children:
            idx = self.state.scene_list.index(child_so)
            self.state.scene_list_properties[idx]["ColorBy"] = color_by
            self.state.scene_list[idx].GetProperty().SetColor(color)
            self.redraw_object(self.state.scene_list[idx])

    def update_highlight_selected(self):
        print("ptv update_highlight_selected")
        self.state.highlight_selected = self.objectHightlightSelectedCheckBox.isChecked()
        idx = self.objectNameComboBox.currentIndex()
        if idx == 0:
            return
        so = self.state.scene_list[idx-1]
        self.redraw_object(so)