import numpy as np

import importlib.util as imp

from PySide6.QtGui import QCloseEvent

from PySide6.QtWidgets import (
    QWidget,
)

from sovUtils import (
    time_and_log,
    add_objects_in_mask_image_to_scene,
)

from sovOtsuLogic import OtsuLogic

from ui_sovOtsuPanelWidget import Ui_OtsuPanelWidget


class OtsuPanelWidget(QWidget, Ui_OtsuPanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state
        self.logic = OtsuLogic()

        self.otsuRunButton.clicked.connect(self.otsu_threshold)
        self.otsuRunButton.setStyleSheet("background-color: #00aa00")

    @time_and_log
    def otsu_threshold(self):
        numberOfThresholds = self.otsuNumberOfThresholdsSpinBox.value()
        
        self.gui.log("Running...")
        seg_image = self.logic.run(self.state.image[self.state.current_image_num], numberOfThresholds)

        self.gui.log("Done.")

        add_objects_in_mask_image_to_scene(seg_image, self.state.scene) 
        self.gui.update_scene()
