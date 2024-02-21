from PySide6.QtWidgets import QWidget

from soViewerUtils import get_so_index_in_list

from ui_tabView3D import Ui_tabView3DWidget

from soViewer3DRenderWindowInteractor import SOViewer3DRenderWindowInteractor


class TabView3DWidget(QWidget, Ui_tabView3DWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.vtk3DViewWidget = SOViewer3DRenderWindowInteractor(gui, state, self)
        self.view3DLayout.addWidget(self.vtk3DViewWidget)
        #self.vtk3DViewWidget.AddObserver('LeftButtonPressEvent', DummyFunc1, 1.0)

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.vtk3DViewWidget.close()

    def initialize(self):
        self.vtk3DViewWidget.Initialize()

    def update_image(self):
        print("Updating 3D image")
        #self.update()

    def update_scene(self):
        self.vtk3DViewWidget.update_scene()

    def update_object(self, so):
        self.vtk3DViewWidget.update_object(so)