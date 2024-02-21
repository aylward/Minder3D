import numpy as np

import itk

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
)

from ptvState import PTVState

from soViewerUtils import (
    read_group,
    get_children_as_list,
    get_so_index_in_list
)

from tabView2D import TabView2DWidget
from tabView3D import TabView3DWidget

from tabVisualization import TabVisualizationWidget
from tabPreProcess import TabPreProcessWidget
from tabLungAI import TabLungAIWidget
from tabScreenCapture import TabScreenCaptureWidget
from tabChat import TabChatWidget

from ui_pytubeview import Ui_MainWindow


class PTVWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.state = PTVState()

        # File Menu
        self.loadImageMenuItem.triggered.connect(self.load_image)
        self.loadSceneMenuItem.triggered.connect(self.load_scene)

        # View 2D Widget
        self.tabView2D = TabView2DWidget(self, self.state)
        self.tabView2DLayout.addWidget(self.tabView2D)

        # View 3D Widget
        self.tabView3D = TabView3DWidget(self, self.state)
        self.tabView3DLayout.addWidget(self.tabView3D)

        # Visualization Tab
        self.tabVisualization = TabVisualizationWidget(self, self.state)
        self.tabVisualizationLayout.addWidget(self.tabVisualization)

        # PreProcess Tab
        self.tabPreProcess = TabPreProcessWidget(self, self.state)
        self.tabPreProcessLayout.addWidget(self.tabPreProcess)

        # LungAI Tab
        self.tabLungAI = TabLungAIWidget(self, self.state)
        self.tabLungAILayout.addWidget(self.tabLungAI)

        # ScreenCapture Tab
        self.tabScreenCapture = TabScreenCaptureWidget(self, self.state)
        self.tabScreenCaptureLayout.addWidget(self.tabScreenCapture)

        # Chat Tab
        self.tabChat = TabChatWidget(self, self.state)
        self.tabChatLayout.addWidget(self.tabChat)

        self.show()
        self.tabView2D.initialize()
        self.tabView3D.initialize()

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.tabView2D.close()
        self.tabView3D.close()

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

        self.tabView2D.update_image()
        self.tabView3D.update_image()

        self.tabVisualization.update_image()

    def update_overlay(self):
        self.tabView2D.update_overlay()

    def update_scene(self):
        self.state.scene_list = get_children_as_list(self.state.scene)
        self.state.scene_list_properties = []
        self.objectNameComboBox.clear()
        for so in self.state.scene_list:
            self.state.scene_list_properties.append(
                dict(ColorBy="Color", Form="Surface")
                )
            self.objectNameComboBox.addItem(f"{so.GetTypeName()} {so.GetId()}")
        self.tabView2D.update_scene()
        self.tabView3D.update_scene()

    def update_object(self, so, update_2D=True, update_3D=True):
        so_id = so.GetId()
        idx = get_so_index_in_list(so_id, self.state.scene_list)
        so_size = so.GetNumberOfPoints()
        self.objectNameComboBox.setCurrentIndex(idx)
        #self.objectViewComboBox.select(self.state.scene_list_properties[idx]["ColorBy"])
        #self.objectColorComboBox.select(so.GetProperty().GetColor())
        self.objectOpacitySlider.setValue(so.GetProperty().GetAlpha())
        self.objectInfoText.clear()
        self.objectInfoText.insertPlainText(f"Object size: {so_size}\n")
        if so_id in self.state.selected_so_ids:
            selected_idx = self.state.selected_so_ids.index(so_id)
            point_id = self.state.selected_so_point_ids[selected_idx]
            point = so.GetPoint(point_id)
            point_pos = point.GetPositionInWorldSpace()
            self.objectInfoText.insertPlainText(f"   Selected point\n")
            self.objectInfoText.insertPlainText(f"      Id: {point_id}\n")
            self.objectInfoText.insertPlainText(f"      Position: {point_pos}\n")
            if "Tube" in so.GetTypeName():
                point_radius = point.GetRadiusInWorldSpace()
                self.objectInfoText.insertPlainText(f"      Radius: {point_radius}\n")
        if update_2D:
            self.tabView2D.update_object(so)
        if update_3D:
            self.tabView3D.update_object(so)