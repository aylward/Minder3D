import numpy as np

import itk
from itk import TubeTK as tube

from PySide6.QtWidgets import QWidget

from sovUtils import time_and_log, resample_overlay_to_match_image

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
        if self.preProcessUsePreProcessedCheckBox.isChecked():
            isoImageFilter.SetInput(self.state.image)
        else:
            isoImageFilter.SetInput(self.state.loaded_image)
        isoImageFilter.SetMakeHighResIso(True)
        isoImageFilter.SetInterpolator("Sinc")
        isoImageFilter.Update()
        self.state.image = isoImageFilter.GetOutput()
        self.state.image_array = itk.GetArrayFromImage(self.state.image)

        if self.preProcessUsePreProcessedCheckBox.isChecked():
            self.state.overlay = resample_overlay_to_match_image(
                self.state.overlay, self.state.image)
        else:
            self.state.overlay = resample_overlay_to_match_image(
                self.state.loaded_overlay, self.state.image)
        self.state.overlay_array = itk.GetArrayFromImage(
            self.state.overlay)

        self.gui.update_image()
        self.gui.update_overlay()

    @time_and_log
    def make_low_res_iso(self):
        isoImageFilter = tube.ResampleImage[self.state.image_type].New()
        if self.preProcessUsePreProcessedCheckBox.isChecked():
            isoImageFilter.SetInput(self.state.image)
        else:
            isoImageFilter.SetInput(self.state.loaded_image)
        isoImageFilter.SetMakeIsotropic(True)
        isoImageFilter.SetInterpolator("Sinc")
        isoImageFilter.Update()
        self.state.image = isoImageFilter.GetOutput()
        self.state.image_array = itk.GetArrayFromImage(self.state.image)

        if self.preProcessUsePreProcessedCheckBox.isChecked():
            self.state.overlay = resample_overlay_to_match_image(
                self.state.overlay, self.state.image)
        else:
            self.state.overlay = resample_overlay_to_match_image(
                self.state.loaded_overlay, self.state.image)
        self.state.overlay_array = itk.GetArrayFromImage(
            self.state.overlay)

        self.gui.update_image()
        self.gui.update_overlay()

    @time_and_log
    def make_iso(self):
        spacingX = self.preProcessIsoSpinBox.value()
        spacing = [spacingX, spacingX, spacingX]

        isoImageFilter = tube.ResampleImage[self.state.image_type].New()
        if self.preProcessUsePreProcessedCheckBox.isChecked():
            isoImageFilter.SetInput(self.state.image)
        else:
            isoImageFilter.SetInput(self.state.loaded_image)
        isoImageFilter.SetSpacing(spacing)
        isoImageFilter.SetInterpolator("Sinc")
        isoImageFilter.Update()
        self.state.image = isoImageFilter.GetOutput()
        self.state.image_array = itk.GetArrayFromImage(self.state.image)

        self.state.overlay = resample_overlay_to_match_image(
            self.state.loaded_overlay, self.state.image)
        self.state.overlay_array = itk.GetArrayFromImage(
            self.state.overlay)

        self.gui.update_image()
        self.gui.update_overlay()
        
    @time_and_log
    def make_iso(self):
        spacingX = self.preProcessIsoSpinBox.value()
        spacing = [spacingX, spacingX, spacingX]
        
        isoImageFilter = tube.ResampleImage.New(
            Input=self.state.loaded_image)
        isoImageFilter.SetSpacing(spacing)
        isoImageFilter.SetInterpolator("Sinc")
        isoImageFilter.Update()
        self.state.image = isoImageFilter.GetOutput()
        self.state.image_array = itk.GetArrayFromImage(self.state.image)

        if self.preProcessUsePreProcessedCheckBox.isChecked():
            self.state.overlay = resample_overlay_to_match_image(
                self.state.overlay, self.state.image)
        else:
            self.state.overlay = resample_overlay_to_match_image(
                self.state.loaded_overlay, self.state.image)
        self.state.overlay_array = itk.GetArrayFromImage(
            self.state.overlay)

        self.gui.update_image()
        self.gui.update_overlay()

    @time_and_log
    def clip_window_level(self):
        imin = 0
        imax = 1
        flip = False
        if self.state.view_intensity_window_min < self.state.view_intensity_window_max:
            imin = self.state.view_intensity_window_min
            imax = self.state.view_intensity_window_max
            flip = False
        elif self.state.view_intensity_window_min > self.state.view_intensity_window_max:
            imin = self.state.view_intensity_window_max
            imax = self.state.view_intensity_window_min
            flip = True
        else:
            self.gui.log("min and max intensity window values are equal", "warning")
            return
        if self.preProcessUsePreProcessedCheckBox.isChecked():
            self.state.image_array = np.clip(self.state.image_array, imin, imax)
        else:
            self.state.image_array = np.clip(self.state.loaded_image_array, imin, imax)
        if flip:
            self.state.image_array = imax - self.state.image_array
        self.state.image = itk.GetImageFromArray(self.state.image_array)
        self.state.image.CopyInformation(self.state.overlay)

        self.gui.update_image()

    @time_and_log
    def median_filter(self):
        medFilter = itk.MedianImageFilter.New(Input=self.state.image)
        medFilter.SetRadius(self.preProcessMedianRadiusSpinBox.value())
        medFilter.Update()
        self.state.image = medFilter.GetOutput()
        self.state.image_array = itk.GetArrayFromImage(self.state.image)

        self.gui.update_image()
