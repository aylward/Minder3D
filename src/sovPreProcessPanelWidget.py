import numpy as np

import itk
from itk import TubeTK as tube

from PySide6.QtWidgets import QWidget

from sovUtils import time_and_log 

from ui_sovPreProcessPanelWidget import Ui_PreProcessPanelWidget


class PreProcessPanelWidget(QWidget, Ui_PreProcessPanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.preProcessHighResIsoButton.clicked.connect(
            self.make_high_res_iso
        )

        self.preProcessLowResIsoButton.clicked.connect(
            self.make_low_res_iso
        )

        self.preProcessIsoButton.clicked.connect(
            self.make_iso
        )

        self.preProcessClipWindowLevelButton.clicked.connect(
            self.clip_window_level
        )

        self.preProcessMedianFilterButton.clicked.connect(
            self.median_filter
        )

    @time_and_log
    def make_high_res_iso(self):
        isoImageFilter = tube.ResampleImage[self.state.image_type].New()
        isoImageFilter.SetInput(self.state.image[self.state.current_image_num])
        isoImageFilter.SetMakeHighResIso(True)
        isoImageFilter.SetInterpolator("Sinc")
        isoImageFilter.Update()
        if self.preProcessCreateNewImageCheckBox.isChecked():
            self.gui.create_new_image(isoImageFilter.GetOutput())
        else:
            self.gui.replace_image(isoImageFilter.GetOutput())

        self.gui.update_image()
        self.gui.update_overlay()

    @time_and_log
    def make_low_res_iso(self):
        isoImageFilter = tube.ResampleImage[self.state.image_type].New()
        isoImageFilter.SetInput(self.state.image[self.state.current_image_num])
        isoImageFilter.SetMakeIsotropic(True)
        isoImageFilter.SetInterpolator("Sinc")
        isoImageFilter.Update()
        if self.preProcessCreateNewImageCheckBox.isChecked():
            self.gui.create_new_image(isoImageFilter.GetOutput())
        else:
            self.gui.replace_image(isoImageFilter.GetOutput())

        self.gui.update_image()
        self.gui.update_overlay()

    @time_and_log
    def make_iso(self):
        spacingX = self.preProcessIsoSpinBox.value()
        spacing = [spacingX, spacingX, spacingX]

        isoImageFilter = tube.ResampleImage[self.state.image_type].New()
        isoImageFilter.SetInput(self.state.image[self.state.current_image_num])
        isoImageFilter.SetSpacing(spacing)
        isoImageFilter.SetInterpolator("Sinc")
        isoImageFilter.Update()
        if self.preProcessCreateNewImageCheckBox.isChecked():
            self.gui.create_new_image(isoImageFilter.GetOutput())
        else:
            self.gui.replace_image(isoImageFilter.GetOutput())

        self.gui.update_image()
        self.gui.update_overlay()
        
    @time_and_log
    def clip_window_level(self):
        imin = self.state.view2D_intensity_window_min[self.state.current_image_num]
        imax = self.state.view2D_intensity_window_max[self.state.current_image_num]
        flip = False
        if imin > imax:
            tmp = imin
            imin = imax
            imax = tmp
            flip = True
        else:
            self.gui.log("min and max intensity window values are equal", "warning")
            return
        image_array = np.clip(self.state.image_array[self.state.current_image_num], imin, imax)
        if flip:
            image_array = imax - image_array
        img = itk.GetImageFromArray(image_array)
        img.CopyInformation(self.state.image[self.state.current_image_num])
        if self.preProcessCreateNewImageCheckBox.isChecked():
            self.gui.create_new_image(img)
        else:
            self.gui.replace_image(img, update_overlay=False)

        self.gui.update_image()

    @time_and_log
    def median_filter(self):
        medFilter = itk.MedianImageFilter.New(Input=self.state.image[self.state.current_image_num])
        medFilter.SetRadius(self.preProcessMedianRadiusSpinBox.value())
        medFilter.Update()
        if self.preProcessCreateNewImageCheckBox.isChecked():
            self.gui.create_new_image(medFilter.GetOutput())
        else:
            self.gui.replace_image(medFilter.GetOutput(), update_overlay=False)

        self.gui.update_image()
