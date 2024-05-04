import numpy as np
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMessageBox, QWidget

from .sovLungCTALogic import LungCTALogic
from .sovUtils import add_objects_in_mask_image_to_scene, time_and_log
from .ui_sovLungCTAPanelWidget import Ui_LungCTAPanelWidget


class LungCTAPanelWidget(QWidget, Ui_LungCTAPanelWidget):
    def __init__(self, gui, state, parent=None):
        """Initialize the LungCTA application.

        Args:
            gui: The graphical user interface object.
            state: The state object.
            parent: The parent widget (default is None).
        """

        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state
        self.logic = LungCTALogic()

        self.ai_first_run = True

        self.lungStep1Button.clicked.connect(self.segment_ai)
        self.lungStep1Button.setStyleSheet('background-color: #00aa00')

    @time_and_log
    def segment_ai(self):
        """Segment the current image using AI.

        This method initializes the AI logic with the current image and preprocesses it.
        Then it runs the AI logic to segment the image and adds the segmented objects to the scene.
        """

        status, msg, ask_to_continue = self.logic.initialize(
            self.state.image[self.state.current_image_num]
        )
        if status is False:
            message = QMessageBox()
            message.setWindowTitle('Verifying AI installation...')
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

        self.gui.log('Preprocessing...')
        pre_image = self.logic.preprocess()
        self.gui.create_new_image(pre_image, None, 'Iso')
        self.gui.update_image()

        self.gui.log('Running...')
        seg_image = self.logic.run()

        self.gui.log('Done.')

        add_objects_in_mask_image_to_scene(seg_image, self.state.scene)
        self.gui.update_scene()
