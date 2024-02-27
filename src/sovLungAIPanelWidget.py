from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui_sovLungAIPanelWidget import Ui_LungAIPanelWidget


class LungAIPanelWidget(QWidget, Ui_LungAIPanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.lungAISegmentButton.clicked.connect(
            self.segment_lungs
        )

    def segment_lungs(self):
        print("click")
