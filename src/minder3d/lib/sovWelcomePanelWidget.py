from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget

from .sovUtils import time_and_log
from .ui_sovWelcomePanelWidget import Ui_WelcomePanelWidget


class WelcomePanelWidget(QWidget, Ui_WelcomePanelWidget):
    @time_and_log
    def __init__(self, gui, state, parent=None):
        """Initialize the GUI and state for the application.

        Args:
            gui: The graphical user interface object.
            state: The state object for the application.
            parent: The parent widget (default is None).
        """
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.welcomeLoadImageButton.pressed.connect(self.gui.load_image)
        self.welcomeLoadImageButton.setStyleSheet('background-color: #00aa00')
        self.welcomeLoadSceneButton.pressed.connect(self.gui.load_scene)
        self.welcomeSaveImageButton.pressed.connect(self.gui.save_image)
        self.welcomeSaveOverlayButton.pressed.connect(self.gui.save_overlay)
        self.welcomeSaveVTKModelsButton.pressed.connect(
            self.gui.save_vtk_models
        )
        self.welcomeSaveSceneButton.pressed.connect(self.gui.save_scene)

        p = self.welcomeTextEdit.palette()
        p.setColor(QPalette.Base, QColor(43, 43, 43))
        p.setColor(QPalette.Text, QColor(200, 200, 200))
        self.welcomeTextEdit.setPalette(p)
