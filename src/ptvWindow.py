import sys

import numpy as np

import itk

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
)

from ptvState import PTVState

from ptvUtils import (
    read_group,
    write_group
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
        self.tabView2D.update_scene()
        self.tabView3D.update_scene()
