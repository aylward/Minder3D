import numpy as np

import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui_tabView3D import Ui_tabView3DWidget


class View3DRenderWindowInteractor(QVTKRenderWindowInteractor):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)

        self.gui = gui
        self.state = state

    def mousePressEvent(self, event):
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)

    #def mouseReleaseEvent(self, event):


class TabView3DWidget(QWidget, Ui_tabView3DWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.vtk3DViewWidget = View3DRenderWindowInteractor(gui, state, self)
        self.view3DLayout.addWidget(self.vtk3DViewWidget)

        self.view3D = None
        #self.vtk3DViewWidget.AddObserver('LeftButtonPressEvent', DummyFunc1, 1.0)

        ren = vtk.vtkRenderer()
        self.vtk3DViewWidget.GetRenderWindow().AddRenderer(ren)

        cone = vtk.vtkConeSource()
        cone.SetResolution(8)

        coneMapper = vtk.vtkPolyDataMapper()
        coneMapper.SetInputConnection(cone.GetOutputPort())

        coneActor = vtk.vtkActor()
        coneActor.SetMapper(coneMapper)

        ren.AddActor(coneActor)

    def initialize(self):
        self.vtk3DViewWidget.Initialize()

    def update_image(self):
        if self.view3D is None:
            self.update()

    def update(self):
        print("Update 3D View")