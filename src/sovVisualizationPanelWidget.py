import numpy as np

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui_sovVisualizationPanelWidget import Ui_VisualizationPanelWidget


class VisualizationPanelWidget(QWidget, Ui_VisualizationPanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.update_gui = True

        self.vizIntensityMinSlider.valueChanged.connect(
            self.update_viz_intensity_min_max_sliders
        )
        self.vizIntensityMaxSlider.valueChanged.connect(
            self.update_viz_intensity_min_max_sliders
        )

        self.vizIntensityMinSpinBox.valueChanged.connect(
            self.update_viz_intensity_min_max_spin_boxes
        )
        self.vizIntensityMaxSpinBox.valueChanged.connect(
            self.update_viz_intensity_min_max_spin_boxes
        )

    def update_viz_intensity_min_max_sliders(self):
        if not self.update_gui:
            return

        minI = self.vizIntensityMinSlider.value()
        maxI = self.vizIntensityMaxSlider.value()

        imin = 0
        imax = 1
        if self.state.view_image_num == 0:
            imin = self.state.loaded_image_min
            imax = self.state.loaded_image_max
        else:
            imin = self.state.image_min
            imax = self.state.image_max
        intensityRange = imax - imin
        intensityMin = (minI / 100.0) * intensityRange + imin
        intensityMax = (maxI / 100.0) * intensityRange + imin

        self.state.view_intensity_window_min = intensityMin
        self.state.view_intensity_window_max = intensityMax

        self.update_gui = False
        self.vizIntensityMinSpinBox.setValue(intensityMin)
        self.vizIntensityMaxSpinBox.setValue(intensityMax)
        self.update_gui = True

        self.update()

    def update_viz_intensity_min_max_spin_boxes(self):
        if not self.update_gui:
            return

        intensityMin = self.vizIntensityMinSpinBox.value()
        intensityMax = self.vizIntensityMaxSpinBox.value()

        imin = 0
        imax = 1
        if self.state.view_image_num == 0:
            imin = self.state.loaded_image_min
            imax = self.state.loaded_image_max
        else:
            imin = self.state.image_min
            imax = self.state.image_max
        intensityRange = imax - imin
        minI = int(((intensityMin - imin) / intensityRange) * 100 + 0.5)
        maxI = int(((intensityMax - imin) / intensityRange) * 100 + 0.5)

        self.state.view_intensity_window_min = intensityMin
        self.state.view_intensity_window_max = intensityMax

        self.update_gui = False
        self.vizIntensityMinSlider.setValue(minI)
        self.vizIntensityMaxSlider.setValue(maxI)
        self.update_gui = True

        self.update()

    def update_image(self):
        imin = 0
        imax = 1
        if self.state.view_image_num == 0:
            imin = self.state.loaded_image_min
            imax = self.state.loaded_image_max
        else:
            imin = self.state.image_min
            imax = self.state.image_max
        image_range = imax - imin

        self.state.intensity_window_min = imin
        self.state.intensity_window_max = imax

        self.update_gui = False

        self.vizIntensityMinSlider.setValue(0)
        self.vizIntensityMinSpinBox.setRange(
            imin - 0.5 * image_range,
            imax + 0.5 * image_range
        )
        self.vizIntensityMinSpinBox.setSingleStep(image_range / 500)
        self.vizIntensityMinSpinBox.setValue(imin)

        self.vizIntensityMaxSlider.setValue(100)
        self.vizIntensityMaxSpinBox.setRange(
            imin - 0.5 * image_range,
            imax + 0.5 * image_range
        )
        self.vizIntensityMaxSpinBox.setSingleStep(image_range / 500)
        self.vizIntensityMaxSpinBox.setValue(imax)

        self.update_gui = True

        self.update()

    def update(self):
        if not self.update_gui:
            return

        self.gui.view2DPanel.update()
        super().update()
