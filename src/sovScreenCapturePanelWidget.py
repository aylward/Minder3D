from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui_sovScreenCapturePanelWidget import Ui_ScreenCapturePanelWidget


class ScreenCapturePanelWidget(QWidget, Ui_ScreenCapturePanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.scCapture2DButton.clicked.connect(self.capture_2d)

    def capture_2d(self):
        print('click')
