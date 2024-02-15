from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui_tabLungAI import Ui_tabLungAIWidget


class TabLungAIWidget(QWidget, Ui_tabLungAIWidget):
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
