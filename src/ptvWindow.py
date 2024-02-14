import sys

import numpy as np

import itk

import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QMainWindow,
    QFileDialog,
)

from ptvState import ptvState

from tabView import tabView

from ui_pytubeview import Ui_MainWindow

class ptvWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.state = ptvState()

        # File Menu
        self.loadImageMenuItem.triggered.connect(self.loadImage)

        # View 2D Widget
        self.vtk2DWidget = QVTKRenderWindowInteractor(self)
        self.view2DWidget.addWidget(self.vtk2DWidget)

        self.view2D = None

        # View 3D Widget
        self.vtk3DWidget = QVTKRenderWindowInteractor(self)
        self.view3DWidget.addWidget(self.vtk3DWidget)

        self.view3D = None

        # View Tab
        self.tabView = tabView(
            self,
            self.state,
        )
        self.tabViewLayout.addWidget(self.tabView)

        self.show()
        self.vtk2DWidget.Initialize()

    def loadImage(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(
                self,
                "Open File",
                self.state.loaded_image_filename,
                "All Files (*)"
            )
        if filename:
            self.state.loaded_image_filename = filename
            self.state.loaded_image = itk.imread(filename, self.state.image_pixel_type)
            self.state.image = self.state.loaded_image
            self.state.overlay = self.state.overlay_type.New()
            self.state.overlay.SetRegions(self.state.image.GetLargestPossibleRegion())
            self.state.overlay.CopyInformation(self.state.image)
            self.state.overlay.Allocate()
            self.updateImage()

    def loadScene(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(
                self, "Open File", self.state.loaded_scene_filename, "All Files (*)"
            )
        if filename:
            self.state.loaded_scene_filename = filename
            soreader = itk.SpatialObjectReader()
            soreader.SetFileName(filename)
            soreader.Update()
            self.state.scene = soreader.GetGroup()
            self.updateOverlay()

    def updateImage(self):
        self.state.image_array = itk.GetArrayFromImage(self.state.image)

        if self.view2D == None:
            self.view2D = vtk.vtkImageViewer2()
            self.view2D.SetupInteractor(self.vtk2DWidget)
            self.view2D.SetRenderWindow(self.vtk2DWidget.GetRenderWindow())
            #interactorStyle = vtk.vtkInteractorStyleImage()
            #interactorStyle.SetInteractionModeToImage2D()
            #self.vtk2DWidget.SetInteractorStyle(interactorStyle)

        self.state.image_min = float(np.min(self.state.image_array))
        self.state.image_max = float(np.max(self.state.image_array))
        self.state.image_intensity_window_min = self.state.image_min
        self.state.image_intensity_window_max = self.state.image_max
        
        self.updateView2D()
        #self.updateView3D()

        self.tabView.updateImage()

    def updateView2D(self):
        if self.state.image is not None:
            spacing = self.state.image.GetSpacing()
            origin = self.state.image.GetOrigin()
            image_slice = self.state.image_array[100, ::-1, :]
            #overlay_slice = self.state.overlay_array[:, :, 0]

            image_view_min = self.state.image_intensity_window_min
            image_view_max = self.state.image_intensity_window_max

            image_slice = (image_slice - image_view_min) / (image_view_max - image_view_min) * 255
            image_slice = np.clip(image_slice, 0, 255)

            image_slice_rgb = np.zeros((image_slice.shape[0], image_slice.shape[1], 3), dtype=np.uint8)
            image_slice_rgb[:, :, 0] = image_slice
            image_slice_rgb[:, :, 1] = image_slice
            image_slice_rgb[:, :, 2] = image_slice

            import_image_slice_vtk = vtk.vtkImageImport()
            import_image_slice_vtk.SetDataSpacing(spacing[0], spacing[1], spacing[2])
            import_image_slice_vtk.SetDataOrigin(origin[0], origin[1], origin[2])
            import_image_slice_vtk.SetWholeExtent(
                0, image_slice.shape[0]-1,
                0, image_slice.shape[1]-1,
                0, 0)
            import_image_slice_vtk.SetDataExtentToWholeExtent()
            import_image_slice_vtk.SetDataScalarTypeToUnsignedChar()
            import_image_slice_vtk.SetNumberOfScalarComponents(3)
            import_image_slice_vtk.SetImportVoidPointer(image_slice_rgb.ravel())
            import_image_slice_vtk.Update()
            image_slice_vtk = import_image_slice_vtk.GetOutput()

            imgBlender = vtk.vtkImageBlend()
            imgBlender.AddInputData(image_slice_vtk)
            imgBlender.AddInputData(image_slice_vtk)
            #imgBlender.AddInputData(overlay_slice_vtk)
            imgBlender.SetOpacity(1, 0.3)
            imgBlender.SetOpacity(0, 0.5)
            imgBlender.Update()
            blended_slice_vtk = imgBlender.GetOutput()

            self.view2D.SetInputData(blended_slice_vtk)
            self.view2D.Render()
            self.view2D.GetRenderer().ResetCamera()
            self.view2D.GetRenderWindow().Render()
