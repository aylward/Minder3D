from PySide6.QtWidgets import QWidget

from .sovImageProcessPanelWidget import ImageProcessPanelWidget
from .sovLungCTAPanelWidget import LungCTAPanelWidget
from .sovOtsuPanelWidget import OtsuPanelWidget
from .sovUtils import time_and_log
from .ui_sovNewTaskPanelWidget import Ui_NewTaskPanelWidget


class NewTaskPanelWidget(QWidget, Ui_NewTaskPanelWidget):
    def __init__(self, gui, state, parent=None):
        """Initialize the GUI and state for the parent widget.

        Args:
            gui: The graphical user interface object.
            state: The state object.
            parent: The parent widget (default is None).
        """

        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.newTaskLungCTAButton.clicked.connect(self.add_lung_cta_panel)
        self.newTaskOtsuButton.clicked.connect(self.add_otsu_panel)
        self.newTaskImageProcessButton.clicked.connect(
            self.add_image_process_panel
        )

    @time_and_log
    def add_lung_cta_panel(self):
        """Add the Lung CTA panel to the GUI tab widget if it is not already added.

        If the Lung CTA panel is not already created, it creates a new instance of LungCTAPanelWidget and adds it to the tab widget.
        If the Lung CTA panel is already added, it sets the current widget to the Lung CTA panel.

        Args:
            self (object): The instance of the class.
        """

        if self.gui.lungCTAPanel is None:
            self.gui.lungCTAPanel = LungCTAPanelWidget(self.gui, self.state)
        if self.gui.tabWidget.indexOf(self.gui.lungCTAPanel) == -1:
            indx = self.gui.tabWidget.indexOf(self.gui.newTaskTab)
            self.gui.tabWidget.insertTab(
                indx, self.gui.lungCTAPanel, 'Lung CTA'
            )
            self.gui.tabWidget.setCurrentWidget(self.gui.lungCTAPanel)

    @time_and_log
    def add_image_process_panel(self):
        """Add an image processing panel to the GUI if it does not already exist.

        If the image processing panel does not exist, it creates a new ImageProcessPanelWidget and adds it to the tab widget.
        If the image processing panel already exists, it sets the current widget to the existing panel.

        Args:
            self (object): The current instance of the class.
        """

        if self.gui.imageProcessPanel is None:
            self.gui.imageProcessPanel = ImageProcessPanelWidget(
                self.gui, self.state
            )
        if self.gui.tabWidget.indexOf(self.gui.imageProcessPanel) == -1:
            indx = self.gui.tabWidget.indexOf(self.gui.newTaskTab)
            self.gui.tabWidget.insertTab(
                indx, self.gui.imageProcessPanel, 'Image Processing'
            )
            self.gui.tabWidget.setCurrentWidget(self.gui.imageProcessPanel)

    @time_and_log
    def add_otsu_panel(self):
        """Add Otsu panel to the GUI tab widget if it doesn't already exist.

        If the Otsu panel does not exist, it creates a new OtsuPanelWidget and adds it to the tab widget.
        If the Otsu panel already exists, it sets the current widget to the Otsu panel.

        Args:
            self (object): The instance of the class.
        """

        if self.gui.otsuPanel is None:
            self.gui.otsuPanel = OtsuPanelWidget(self.gui, self.state)
        if self.gui.tabWidget.indexOf(self.gui.otsuPanel) == -1:
            indx = self.gui.tabWidget.indexOf(self.gui.newTaskTab)
            self.gui.tabWidget.insertTab(
                indx, self.gui.otsuPanel, 'Otsu Threshold'
            )
            self.gui.tabWidget.setCurrentWidget(self.gui.otsuPanel)
