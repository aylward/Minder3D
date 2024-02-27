from PySide6.QtWidgets import QWidget

from ui_sovView3DPanelWidget import Ui_View3DPanelWidget

from sovView3DRenderWindowInteractor import View3DRenderWindowInteractor


class View3DPanelWidget(QWidget, Ui_View3DPanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.vtk3DViewWidget = View3DRenderWindowInteractor(gui, state, self)
        self.view3DLayout.addWidget(self.vtk3DViewWidget)
        #self.vtk3DViewWidget.AddObserver('LeftButtonPressEvent', DummyFunc1, 1.0)

        self.view3DResetButton.clicked.connect(self.reset_camera)

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.vtk3DViewWidget.close()

    def initialize(self):
        self.vtk3DViewWidget.Initialize()

    def reset_camera(self):
        self.vtk3DViewWidget.reset_camera()

    def update_image(self):
        print("Updating 3D image")
        #self.update()

    def update_scene(self):
        self.vtk3DViewWidget.update_scene()

    def redraw_object(self, so):
        self.vtk3DViewWidget.redraw_object(so)
