import numpy as np

import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui_tabView2D import Ui_tabView2DWidget


class View2DRenderWindowInteractor(QVTKRenderWindowInteractor):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)

        self.gui = gui
        self.state = state

    def mousePressEvent(self, event):
        ctrl, shift = self._GetCtrlShift(event)
        if ctrl is False and shift is True:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        ctrl, shift = self._GetCtrlShift(event)
        if ctrl is False and shift is True:
            super().mouseMoveEvent(event)

class TabView2DWidget(QWidget, Ui_tabView2DWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.vtk2DViewWidget = View2DRenderWindowInteractor(gui, state, self)
        self.view2DLayout.addWidget(self.vtk2DViewWidget)

        self.view2D = None

    def initialize(self):
        self.vtk2DViewWidget.Initialize()

    def update_image(self):
        if self.view2D is None:
            self.view2D = vtk.vtkImageViewer2()
            self.view2D.SetupInteractor(self.vtk2DViewWidget)
            self.view2D.SetRenderWindow(self.vtk2DViewWidget.GetRenderWindow())
            #interactorStyle = vtk.vtkInteractorStyleImage()
            #interactorStyle.SetInteractionModeToImage2D()
            #self.vtk2DWidget.SetInteractorStyle(interactorStyle)
            self.update()

    def update(self):
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
