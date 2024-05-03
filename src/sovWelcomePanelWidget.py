from PySide6.QtWidgets import QWidget

from ui_sovWelcomePanelWidget import Ui_WelcomePanelWidget


class WelcomePanelWidget(QWidget, Ui_WelcomePanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.welcomeLoadImageButton.pressed.connect(self.gui.load_image)
        self.welcomeLoadImageButton.setStyleSheet("background-color: #00aa00")
        self.welcomeLoadSceneButton.pressed.connect(self.gui.load_scene)
        self.welcomeSaveImageButton.pressed.connect(self.gui.save_image)
        self.welcomeSaveOverlayButton.pressed.connect(self.gui.save_overlay)
        self.welcomeSaveVTKModelsButton.pressed.connect(
            self.gui.save_vtk_models
        )
        self.welcomeSaveSceneButton.pressed.connect(self.gui.save_scene)
