import importlib.util as imp

import numpy as np
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QWidget

from sovOtsuLogic import OtsuLogic
from sovUtils import add_objects_in_mask_image_to_scene, time_and_log
from ui_sovOtsuPanelWidget import Ui_OtsuPanelWidget


class OtsuPanelWidget(QWidget, Ui_OtsuPanelWidget):
    def __init__(self, gui, state, parent=None):
        """Initialize the OtsuThresholdDialog.

        Args:
            gui: The GUI object.
            state: The state object.
            parent: The parent widget (default is None).
        """

        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state
        self.logic = OtsuLogic()

        self.otsuRunButton.clicked.connect(self.otsu_threshold)
        self.otsuRunButton.setStyleSheet('background-color: #00aa00')

    @time_and_log
    def otsu_threshold(self):
        """Apply Otsu's thresholding to the current image.

        This function applies Otsu's thresholding to the current image using the specified number of thresholds.
        It then updates the scene with the segmented image.

        Args:
            self: The instance of the class.
        """

        numberOfThresholds = self.otsuNumberOfThresholdsSpinBox.value()

        self.gui.log('Running...')
        seg_image = self.logic.run(
            self.state.image[self.state.current_image_num], numberOfThresholds
        )

        self.gui.log('Done.')

        add_objects_in_mask_image_to_scene(seg_image, self.state.scene)
        self.gui.update_scene()
