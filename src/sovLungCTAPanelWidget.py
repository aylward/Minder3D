
from PySide6.QtGui import QCloseEvent
import numpy as np

from PySide6.QtWidgets import (
    QWidget,
    QMessageBox,
)

from sovUtils import (
    time_and_log,
    add_objects_in_mask_image_to_scene,
)

from sovLungCTALogic import LungCTALogic

from ui_sovLungCTAPanelWidget import Ui_LungCTAPanelWidget


class LungCTAPanelWidget(QWidget, Ui_LungCTAPanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state
        self.logic = LungCTALogic()

        self.ai_first_run = True

        self.lungStep1Button.clicked.connect(self.segment_ai)
        self.lungStep1Button.setStyleSheet("background-color: #00aa00")

    @time_and_log
    def segment_ai(self):

        status, msg, ask_to_continue = self.logic.initialize(self.state.image[self.state.current_image_num])
        if status is False:
            message = QMessageBox()
            message.setWindowTitle("Verifying AI installation...")
            message.setText(msg)
            if ask_to_continue:
                message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            message.exec()
            if ask_to_continue:
                ret = message.exec()
                if ret == QMessageBox.No:
                    return
            else:
                return

        self.gui.log("Preprocessing...")
        pre_image = self.logic.preprocess()
        self.gui.create_new_image(pre_image, None, "Iso")
        self.gui.update_image()

        self.gui.log("Running...")
        seg_image = self.logic.run()

        self.gui.log("Done.")

        add_objects_in_mask_image_to_scene(seg_image, self.state.scene)
        self.gui.update_scene()