import numpy as np
from PySide6.QtWidgets import QWidget
from vtk import vtkRenderLargeImage
from vtk.util.numpy_support import vtk_to_numpy

from .sovUtils import time_and_log
from .sovView3DRenderWindowInteractor import View3DRenderWindowInteractor
from .ui_sovView3DPanelWidget import Ui_View3DPanelWidget


class View3DPanelWidget(QWidget, Ui_View3DPanelWidget):
    @time_and_log
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.vtk3DViewWidget = View3DRenderWindowInteractor(gui, state, self)
        self.view3DLayout.addWidget(self.vtk3DViewWidget)

        self.view3DResetButton.clicked.connect(self.reset_camera)

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.vtk3DViewWidget.close()

    @time_and_log
    def initialize(self):
        self.vtk3DViewWidget.Initialize()

    @time_and_log
    def reset_camera(self):
        self.vtk3DViewWidget.reset_camera()

    def get_screenshot(self):
        render = vtkRenderLargeImage()
        render.SetMagnification(1)
        render.SetInput(self.vtk3DViewWidget.scene_renderer)
        render.Update()
        img = render.GetOutput()
        data = img.GetPointData()
        img_scalars = data.GetScalars()
        dims = img.GetDimensions()
        n_comp = img_scalars.GetNumberOfComponents()
        temp = vtk_to_numpy(img_scalars)
        numpy_data = temp.reshape(dims[1], dims[0], n_comp)
        numpy_data = numpy_data.transpose(0, 1, 2)
        numpy_data = np.flipud(numpy_data)
        return numpy_data

    @time_and_log
    def create_new_image(self):
        pass

    @time_and_log
    def update_image(self):
        pass

    @time_and_log
    def update_scene(self):
        self.vtk3DViewWidget.update_scene()

    @time_and_log
    def redraw_object(self, so):
        self.vtk3DViewWidget.redraw_object(so)
