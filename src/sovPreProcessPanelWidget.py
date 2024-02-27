from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui_sovPreProcessPanelWidget import Ui_PreProcessPanelWidget


class PreProcessPanelWidget(QWidget, Ui_PreProcessPanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.preprocHighResIsoButton.clicked.connect(
            self.make_high_res_iso
        )

    def make_high_res_iso(self):
        print("click")
