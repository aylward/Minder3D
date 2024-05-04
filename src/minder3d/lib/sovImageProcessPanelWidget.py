from PySide6.QtWidgets import QWidget

from .sovImageProcessLogic import ImageProcessLogic
from .sovUtils import time_and_log
from .ui_sovImageProcessPanelWidget import Ui_ImageProcessPanelWidget


class ImageProcessPanelWidget(QWidget, Ui_ImageProcessPanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state
        self.logic = ImageProcessLogic()

        self.imageProcessHighResIsoButton.clicked.connect(
            self.make_high_res_iso
        )

        self.imageProcessLowResIsoButton.clicked.connect(self.make_low_res_iso)

        self.imageProcessIsoButton.clicked.connect(self.make_iso)

        self.imageProcessClipWindowLevelButton.clicked.connect(
            self.clip_window_level
        )

        self.imageProcessMedianFilterButton.clicked.connect(self.median_filter)

    @time_and_log
    def make_high_res_iso(self):
        img = self.logic.make_high_res_iso(
            self.state.image[self.state.current_image_num]
        )
        if self.imageProcessCreateNewImageCheckBox.isChecked():
            self.gui.create_new_image(img)
        else:
            self.gui.replace_image(img)

        self.gui.update_image()
        if self.gui.state.view2D_overlay_auto_update:
            self.gui.update_overlay()

    @time_and_log
    def make_low_res_iso(self):
        img = self.logic.make_low_res_iso(
            self.state.image[self.state.current_image_num]
        )
        if self.imageProcessCreateNewImageCheckBox.isChecked():
            self.gui.create_new_image(img)
        else:
            self.gui.replace_image(img)

        self.gui.update_image()
        if self.gui.state.view2D_overlay_auto_update:
            self.gui.update_overlay()

    @time_and_log
    def make_iso(self):
        spacingX = self.imageProcessIsoSpinBox.value()
        img = self.logic.make_low_res_iso(
            self.state.image[self.state.current_image_num], spacingX
        )
        if self.imageProcessCreateNewImageCheckBox.isChecked():
            self.gui.create_new_image(img)
        else:
            self.gui.replace_image(img)

        self.gui.update_image()
        if self.gui.state.view2D_overlay_auto_update:
            self.gui.update_overlay()

    @time_and_log
    def clip_window_level(self):
        imin = self.state.view2D_intensity_window_min[
            self.state.current_image_num
        ]
        imax = self.state.view2D_intensity_window_max[
            self.state.current_image_num
        ]
        img = self.logic.clip_window_level(
            self.state.image[self.state.current_image_num],
            self.state.image_array[self.state.current_image_num],
            imin,
            imax,
        )
        if self.imageProcessCreateNewImageCheckBox.isChecked():
            self.gui.create_new_image(img)
        else:
            self.gui.replace_image(img, update_overlay=False)

        self.gui.update_image()

    @time_and_log
    def median_filter(self):
        radius = self.imageProcessMedianRadiusSpinBox.value()
        img = self.logic.median_filter(
            self.state.image[self.state.current_image_num], radius
        )
        if self.imageProcessCreateNewImageCheckBox.isChecked():
            self.gui.create_new_image(img)
        else:
            self.gui.replace_image(img, update_overlay=False)

        self.gui.update_image()
