from PySide6.QtWidgets import QWidget

from sovUtils import time_and_log

from sovLungCTAPanelWidget import LungCTAPanelWidget
from sovOtsuPanelWidget import OtsuPanelWidget
from sovImageProcessPanelWidget import ImageProcessPanelWidget

from ui_sovNewTaskPanelWidget import Ui_NewTaskPanelWidget


class NewTaskPanelWidget(QWidget, Ui_NewTaskPanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.gui.lungCTAPanel = None
        self.newTaskLungCTAButton.clicked.connect(
            self.add_lung_cta_panel
        )

        self.gui.otsuPanel = None
        self.newTaskOtsuButton.clicked.connect(
            self.add_otsu_panel
        )

        self.gui.imageProcessPanel = None
        self.newTaskImageProcessButton.clicked.connect(
            self.add_image_process_panel
        )

    @time_and_log
    def add_lung_cta_panel(self):
        if self.gui.lungCTAPanel is None:
            self.gui.lungCTAPanel = LungCTAPanelWidget(self.gui, self.state)
        if self.gui.tabWidget.indexOf(self.gui.lungCTAPanel) == -1:
            indx = self.gui.tabWidget.indexOf(self.gui.newTaskTab)
            self.gui.tabWidget.insertTab(indx, self.gui.lungCTAPanel, "Lung CTA")
            self.gui.tabWidget.setCurrentWidget(self.gui.lungCTAPanel)

    @time_and_log
    def add_image_process_panel(self):
        if self.gui.imageProcessPanel is None:
            self.gui.imageProcessPanel = ImageProcessPanelWidget(self.gui, self.state)
        if self.gui.tabWidget.indexOf(self.gui.imageProcessPanel) == -1:
            indx = self.gui.tabWidget.indexOf(self.gui.newTaskTab)
            self.gui.tabWidget.insertTab(indx, self.gui.imageProcessPanel, "Image Processing")
            self.gui.tabWidget.setCurrentWidget(self.gui.imageProcessPanel)

    @time_and_log
    def add_otsu_panel(self):
        if self.gui.otsuPanel is None:
            self.gui.otsuPanel = OtsuPanelWidget(self.gui, self.state)
        if self.gui.tabWidget.indexOf(self.gui.otsuPanel) == -1:
            indx = self.gui.tabWidget.indexOf(self.gui.newTaskTab)
            self.gui.tabWidget.insertTab(indx, self.gui.otsuPanel, "Otsu Threshold")
            self.gui.tabWidget.setCurrentWidget(self.gui.otsuPanel)
