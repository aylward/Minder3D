import os

import itk
import numpy as np
import vtk
from PySide6.QtWidgets import QFileDialog, QInputDialog, QMainWindow, QTabBar

from ptvState import PTVState
from sovColorMapUtils import get_nearest_color_index_and_name
from sovImageTablePanelUtils import get_qthumbnail_from_array
from sovImageTablePanelWidget import ImageTablePanelWidget
from sovInfoTablePanelWidget import InfoTablePanelWidget
from sovNewTaskPanelWidget import NewTaskPanelWidget
from sovUtils import (
    LogWindow,
    add_file_to_settings,
    get_children_as_list,
    get_file_reccords_from_settings,
    read_group,
    resample_overlay_to_match_image,
    time_and_log,
    write_group,
)
from sovView2DPanelWidget import View2DPanelWidget
from sovView3DPanelWidget import View3DPanelWidget
from sovVisualizationPanelWidget import VisualizationPanelWidget
from sovWelcomePanelWidget import WelcomePanelWidget
from ui_pytubeview import Ui_MainWindow


class PTVWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.state = PTVState()

        # File Menu
        self.loadImageMenuItem.triggered.connect(self.load_image)
        self.loadSceneMenuItem.triggered.connect(self.load_scene)
        self.saveImageMenuItem.triggered.connect(self.save_image)
        self.saveOverlayMenuItem.triggered.connect(self.save_overlay)
        self.saveVTKModelsMenuItem.triggered.connect(self.save_vtk_models)
        self.saveSceneMenuItem.triggered.connect(self.save_scene)

        for color_name, _ in self.state.colormap.items():
            self.objectColorComboBox.addItem(color_name)

        self.connect_object_gui()

        self.objectHighlightSelectedObjectsCheckBox.stateChanged.connect(
            self.update_highlight_selected
        )
        self.objectDeleteButton.pressed.connect(self.delete_selected_objects)
        self.objectPropertiesToAllButton.pressed.connect(
            self.propogate_properties_to_all
        )
        self.objectPropertiesToChildrenButton.pressed.connect(
            self.propogate_properties_to_children
        )

        # View 2D Widget
        self.view2DPanel = View2DPanelWidget(self, self.state)
        self.view2DLayout.addWidget(self.view2DPanel)

        # View 3D Widget
        self.view3DPanel = View3DPanelWidget(self, self.state)
        self.view3DLayout.addWidget(self.view3DPanel)

        # Welcome Tab
        self.welcomePanel = WelcomePanelWidget(self, self.state)
        self.welcomeTabLayout.addWidget(self.welcomePanel)

        # Visualization Tab
        self.visualizationPanel = VisualizationPanelWidget(self, self.state)
        self.visualizationTabLayout.addWidget(self.visualizationPanel)

        # New Task Tab
        self.newTaskPanel = NewTaskPanelWidget(self, self.state)
        self.newTaskTabLayout.addWidget(self.newTaskPanel)

        self.tabWidget.tabCloseRequested.connect(self.tab_close_event)

        # Remove Close buttons from welcome, visualization, and pre-process and task tabs
        tabBar = self.tabWidget.tabBar()
        for i in range(0, 3):
            tabBar.tabButton(i, QTabBar.RightSide).deleteLater()
            tabBar.setTabButton(i, QTabBar.RightSide, None)

        # Info Table
        self.infoTablePanel = InfoTablePanelWidget(self, self.state)
        self.infoTableLayout.addWidget(self.infoTablePanel)

        # Image Table
        self.imageTablePanel = ImageTablePanelWidget(self, self.state)
        self.imageTableLayout.addWidget(self.imageTablePanel)

        self.statusText.setText('Ready')

        self.log_window = LogWindow(self.state.logger)
        self.statusViewLogButton.pressed.connect(self.log_window.show)

        self.show()
        self.view2DPanel.initialize()
        self.view3DPanel.initialize()

    @time_and_log
    def tab_close_event(self, index):
        tab = self.tabWidget.widget(index)
        self.tabWidget.removeTab(index)
        tab.close()

    @time_and_log
    def connect_object_gui(self):
        self.objectNameComboBox.currentIndexChanged.connect(
            self.select_object_by_name_combobox
        )

        self.objectColorByComboBox.currentIndexChanged.connect(
            self.modify_selected_objects
        )

        self.objectColorComboBox.currentIndexChanged.connect(
            self.modify_selected_objects
        )

        self.objectOpacitySlider.valueChanged.connect(
            self.modify_selected_objects
        )

    @time_and_log
    def disconnect_object_gui(self):
        self.objectNameComboBox.currentIndexChanged.disconnect(
            self.select_object_by_name_combobox
        )

        self.objectColorByComboBox.currentIndexChanged.disconnect(
            self.modify_selected_objects
        )

        self.objectColorComboBox.currentIndexChanged.disconnect(
            self.modify_selected_objects
        )

        self.objectOpacitySlider.valueChanged.disconnect(
            self.modify_selected_objects
        )

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.view2DPanel.close()
        self.view3DPanel.close()

    def log(self, message, level='info'):
        self.statusText.setText(message)
        if level.lower() == 'error' or level.lower() == 'critical':
            self.statusText.setStyleSheet('background-color: red')
        elif level.lower() == 'warning':
            self.statusText.setStyleSheet('background-color: yellow')
        elif level.lower() == 'debug':
            self.statusText.setStyleSheet('background-color: green')
        else:
            self.statusText.setStyleSheet('background-color: white')
        self.statusText.update()
        self.log_window.log(message, level)

    @time_and_log
    def load_image(self, filename=None):
        if filename is None:
            if len(self.state.image_filename) > 0:
                filename = self.state.image_filename[-1]
            filename, _ = QFileDialog.getOpenFileName(
                self, 'Open File', filename, 'All Files (*)'
            )
        if filename is not None:
            self.create_new_image(
                itk.imread(filename, self.state.image_pixel_type), filename
            )

            self.update_image()
            self.update_overlay()

            qthumb = get_qthumbnail_from_array(self.state.image_array[-1])
            add_file_to_settings(
                self.state.image[-1], filename, 'image', qthumb
            )

    @time_and_log
    def load_scene(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(
                self, 'Open File', self.state.scene_filename, 'All Files (*)'
            )
        if filename:
            self.state.scene_filename = filename
            self.state.scene = read_group(filename)
            add_file_to_settings(self.state.scene, filename, 'scenes')

        self.update_scene()
        add_file_to_settings(self.state.scene, filename, 'scene')

    @time_and_log
    def save_image(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getSaveFileName(
                self,
                'Save File',
                self.state.image_filename[self.state.current_image_num],
                'All Files (*)',
            )
        if filename:
            self.state.image_filename[self.state.current_image_num] = filename
            self.log(f'Saving image to {filename}')
            itk.imwrite(
                self.state.image[self.state.current_image_num], filename
            )

    @time_and_log
    def save_overlay(self, filename=None):
        if not filename:
            guess_filename, guess_extension = os.path.splitext(
                self.state.image_filename[self.state.current_image_num]
            )
            filename, _ = QFileDialog.getSaveFileName(
                self,
                'Save File',
                guess_filename + '_overlay' + guess_extension,
                'All Files (*)',
            )
        if filename:
            self.log(f'Saving overlay to {filename}')
            itk.imwrite(
                self.state.overlay[self.state.current_image_num], filename
            )

    @time_and_log
    def save_vtk_models(self, filename=None):
        if not filename:
            guess_filename, _ = os.path.splitext(self.state.scene_filename)
            filename, _ = QFileDialog.getSaveFileName(
                self,
                'Save File',
                guess_filename + '_models.vrml',
                'All Files (*)',
            )
        if filename:
            exporter = vtk.vtkVRMLExporter()
            exporter.SetRenderWindow(self.view3DPanel.renderWindow)
            exporter.SetFileName(filename)
            exporter.Write()
            exporter.Update()

    @time_and_log
    def save_scene(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getSaveFileName(
                self, 'Save File', self.state.scene_filename, 'All Files (*)'
            )
        if filename:
            self.state.scene_filename = filename
            self.log(f'Saving scene to {filename}')
            write_group(self.state.scene, filename)

    @time_and_log
    def create_new_image(self, img, filename=None, tag=None):
        if filename is None:
            filename, fileext = os.path.splitext(self.state.image_filename[-1])
            if tag is None:
                filename = filename + '_' + str(len(self.state.image)) + fileext
                dlg = QInputDialog(self)
                dlg.setInputMode(QInputDialog.TextInput)
                dlg.setLabelText("New image's filename:")
                dlg.resize(500, 100)
                dlg.setTextValue(filename)
                valid = dlg.exec_()
                filename = dlg.textValue()
                if not valid:
                    return False
            else:
                filename = filename + '_' + tag + fileext
        self.state.image_filename.append(str(filename))

        self.state.image.append(img)
        self.state.image_array.append(
            itk.GetArrayFromImage(self.state.image[-1])
        )
        self.state.image_min.append(float(np.min(self.state.image_array[-1])))
        self.state.image_max.append(float(np.max(self.state.image_array[-1])))

        if len(self.state.overlay) > 1:
            self.state.overlay.append(
                resample_overlay_to_match_image(
                    self.state.overlay[0], self.state.image[-1]
                )
            )
        else:
            self.state.overlay.append(self.state.overlay_type.New())
            self.state.overlay[-1].SetRegions(
                self.state.image[-1].GetLargestPossibleRegion()
            )
            self.state.overlay[-1].CopyInformation(self.state.image[-1])
            self.state.overlay[-1].Allocate()
            self.state.overlay[-1].FillBuffer(self.state.overlay_pixel_type(0))

        self.state.overlay_array.append(
            itk.GetArrayFromImage(self.state.overlay[-1])
        )

        self.state.current_image_num = len(self.state.image) - 1

        self.imageTablePanel.create_new_image()
        self.view2DPanel.create_new_image()
        self.view3DPanel.create_new_image()

        return True

    @time_and_log
    def replace_image(self, img, update_overlay=True):
        num = self.state.current_image_num
        self.state.image[num] = img

        self.state.image_array[num] = itk.GetArrayFromImage(img)
        self.state.image_min[num] = float(np.min(self.state.image_array[num]))
        self.state.image_max[num] = float(np.max(self.state.image_array[num]))

        if update_overlay:
            self.state.overlay[num] = resample_overlay_to_match_image(
                self.state.overlay[0], self.state.image[num]
            )
            self.state.overlay_array[num] = itk.GetArrayFromImage(
                self.state.overlay[num]
            )

        if os.path.splitext(filename)[1] == '.mha':
            self.state.view2D_flip.append([True, True, False])
        else:
            self.state.view2D_flip.append([False, False, False])

        self.state.current_image_num = len(self.state.image) - 1

        self.imageTablePanel.replace_image()

    @time_and_log
    def update_pixel(self):
        self.infoTablePanel.update_pixel()

    @time_and_log
    def update_image(self):
        self.view2DPanel.update_image()
        self.view3DPanel.update_image()

        self.infoTablePanel.update_image()
        self.imageTablePanel.update_image()

    @time_and_log
    def update_overlay(self):
        self.view2DPanel.update_overlay()

    @time_and_log
    def update_scene(self):
        self.state.scene_list = get_children_as_list(self.state.scene)
        self.state.scene_list_ids = []
        self.state.scene_list_properties = []

        self.disconnect_object_gui()
        self.objectNameComboBox.clear()
        self.objectNameComboBox.addItem('None')
        for so in self.state.scene_list:
            self.state.scene_list_ids.append(so.GetId())
            self.state.scene_list_properties.append(
                dict(ColorBy='Solid Color', Actor=None)
            )
            self.objectNameComboBox.addItem(f'{so.GetTypeName()} {so.GetId()}')
        if self.state.view2D_overlay_auto_update:
            self.view2DPanel.update_scene()
        if self.state.view3D_scene_auto_update:
            self.view3DPanel.update_scene()
        self.connect_object_gui()

    @time_and_log
    def update_highlight_selected(self, value):
        self.state.highlight_selected = value
        for selected_id in self.state.selected_ids:
            self.log(f'update_highlight_selected: Id={selected_id}')
            so = self.state.scene_list[
                self.state.scene_list_ids.index(selected_id)
            ]
            self.redraw_object(so)

    @time_and_log
    def select_object_by_name_combobox(self, idx):
        so = None
        so_id = -2
        if idx > 0:
            idx -= 1
            so = self.state.scene_list[idx]
            so_id = so.GetId()
        # Unselect currently selected objects
        for selected_idx, selected_so_id in enumerate(self.state.selected_ids):
            if selected_so_id != -1 and selected_so_id != so_id:
                scene_idx = self.state.scene_list_ids.index(selected_so_id)
                selected_so = self.state.scene_list[scene_idx]
                self.state.selected_ids[selected_idx] = -1
                self.redraw_object(selected_so)
        if so_id != -2:
            self.state.selected_ids = [so_id]
            self.state.selected_point_ids = [0]
            self.redraw_object(so)

    @time_and_log
    def redraw_object(self, so, update_2D=True, update_3D=True):
        so_id = so.GetId()
        if so_id not in self.state.scene_list_ids:
            self.log('ERROR: so_id not in scene_list_ids', 'error')
            return
        scene_idx = self.state.scene_list_ids.index(so_id)

        self.disconnect_object_gui()

        self.objectNameComboBox.setCurrentIndex(scene_idx + 1)

        c = so.GetProperty().GetColor()
        color = [c.GetRed(), c.GetGreen(), c.GetBlue(), c.GetAlpha()]
        color[0:3] = np.array(color)[0:3] * self.state.colormap_scale_factor
        color[3] = color[3] * 100.0
        self.objectOpacitySlider.setValue(color[3])
        _, color_name = get_nearest_color_index_and_name(
            color[0:3], self.state.colormap
        )
        self.objectColorComboBox.setCurrentText(color_name)

        if update_2D and self.state.view2D_overlay_auto_update:
            self.view2DPanel.redraw_object(so)
        if update_3D and self.state.view3D_scene_auto_update:
            self.view3DPanel.redraw_object(so)

        # Must call after view3DPanel.redraw_object() so that actors defined.
        self.objectColorByComboBox.clear()
        self.objectColorByComboBox.addItem('Solid Color')
        actor = self.state.scene_list_properties[scene_idx].get('Actor')
        if actor is not None:
            pdata = actor.GetMapper().GetInput()
            for i in range(pdata.GetPointData().GetNumberOfArrays()):
                pname = pdata.GetPointData().GetArrayName(i)
                self.objectColorByComboBox.addItem(pname)

            self.objectColorByComboBox.setCurrentText(
                self.state.scene_list_properties[scene_idx]['ColorBy']
            )

        self.connect_object_gui()

    @time_and_log
    def modify_selected_objects(self, _):
        for so_id in self.state.selected_ids:
            scene_idx = self.state.scene_list_ids.index(so_id)
            so = self.state.scene_list[scene_idx]
            color = np.empty(4)
            color[0:3] = self.state.colormap[
                self.objectColorComboBox.currentText()
            ]
            color[0:3] /= self.state.colormap_scale_factor
            color[3] = self.objectOpacitySlider.value() / 100.0
            so.GetProperty().SetColor(color)
            self.state.scene_list_properties[scene_idx][
                'ColorBy'
            ] = self.objectColorByComboBox.currentText()

            if self.state.view2D_overlay_auto_update:
                self.view2DPanel.redraw_object(so)
            if self.state.view3D_scene_auto_update:
                self.view3DPanel.redraw_object(so)

    @time_and_log
    def delete_selected_objects(self):
        for so_id in self.state.selected_ids:
            print('deleting so_id:', so_id)
            scene_idx = self.state.scene_list_ids.index(so_id)
            so = self.state.scene_list[scene_idx]
            so_parent = so.GetParent()
            so_parent.RemoveChild(so)
            self.state.scene_list.pop(scene_idx)
            self.state.scene_list_properties.pop(scene_idx)
        self.state.selected_ids = []
        self.state.selected_point_ids = []

        self.disconnect_object_gui()
        self.objectNameComboBox.clear()
        self.objectNameComboBox.addItem('None')
        for so in self.state.scene_list:
            self.objectNameComboBox.addItem(f'{so.GetTypeName()} {so.GetId()}')
        self.connect_object_gui()
        self.update_scene()

    @time_and_log
    def propogate_properties_to_all(self):
        color_by = self.objectColorByComboBox.currentText()
        color = np.empty(4)
        color[0:3] = self.state.colormap[self.objectColorComboBox.currentText()]
        color[0:3] /= self.state.colormap_scale_factor
        color[3] = self.objectOpacitySlider.value() / 100.0
        for idx in range(len(self.state.scene_list)):
            self.state.scene_list_properties[idx]['ColorBy'] = color_by
            self.state.scene_list[idx].GetProperty().SetColor(color)
            self.redraw_object(self.state.scene_list[idx])

    @time_and_log
    def propogate_properties_to_children(self):
        for so_id in self.state.selected_ids:
            scene_idx = self.state.scene_list_ids.index(so_id)
            so = self.state.scene_list[scene_idx]
            color_by = self.objectColorByComboBox.currentText()
            color = np.empty(4)
            color[0:3] = self.state.colormap[
                self.objectColorComboBox.currentText()
            ]
            color[0:3] /= self.state.colormap_scale_factor
            color[3] = self.objectOpacitySlider.value() / 100.0
            children = get_children_as_list(so)
            for child_so in children:
                idx = self.state.scene_list.index(child_so)
                self.state.scene_list_properties[idx]['ColorBy'] = color_by
                self.state.scene_list[idx].GetProperty().SetColor(color)
                self.redraw_object(child_so)
