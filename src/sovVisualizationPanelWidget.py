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

        self.redraw = True

        self.vizIntensityMinSlider.sliderMoved.connect(
            self.update_viz_intensity_min_max_sliders
        )
        self.vizIntensityMaxSlider.sliderMoved.connect(
            self.update_viz_intensity_min_max_sliders
        )

        self.vizIntensityMinSpinBox.valueChanged.connect(
            self.update_viz_intensity_min_max_spin_boxes
        )
        self.vizIntensityMaxSpinBox.valueChanged.connect(
            self.update_viz_intensity_min_max_spin_boxes
        )

    def update_viz_intensity_min_max_sliders(self):
        minI = self.vizIntensityMinSlider.value()
        maxI = self.vizIntensityMaxSlider.value()

        intensityRange = self.state.image_max - self.state.image_min
        intensityMin = minI / 100.0 * intensityRange + self.state.image_min
        intensityMax = maxI / 100.0 * intensityRange + self.state.image_min

        if self.redraw:
            self.redraw = False
            self.vizIntensityMinSpinBox.setValue(intensityMin)
            self.vizIntensityMaxSpinBox.setValue(intensityMax)
            self.state.image_intensity_window_min = intensityMin
            self.state.image_intensity_window_max = intensityMax
            self.gui.view2DPanel.update()
            self.redraw = True

    def update_viz_intensity_min_max_spin_boxes(self):
        intensityMin = self.vizIntensityMinSpinBox.value()
        intensityMax = self.vizIntensityMaxSpinBox.value()

        intensityRange = self.state.image_max - self.state.image_min
        minI = int(((intensityMin - self.state.image_min) / intensityRange) * 100 + 0.5)
        maxI = int(((intensityMax - self.state.image_min) / intensityRange) * 100 + 0.5)

        if self.redraw:
            self.redraw = False
            self.vizIntensityMinSlider.setValue(minI)
            self.vizIntensityMaxSlider.setValue(maxI)
            self.state.image_intensity_window_min = intensityMin
            self.state.image_intensity_window_max = intensityMax
            self.gui.view2DPanel.update()
            self.redraw = True

    def update_image(self):
        image_range = self.state.image_max - self.state.image_min

        self.vizIntensityMinSlider.setValue(0)
        self.vizIntensityMinSpinBox.setRange(
            self.state.image_min - 0.5 * image_range,
            self.state.image_max + 0.5 * image_range
        )
        self.vizIntensityMinSpinBox.setSingleStep(image_range / 500)
        self.vizIntensityMinSpinBox.setValue(self.state.image_min)
        self.state.intensity_window_min = self.state.image_min

        self.vizIntensityMaxSlider.setValue(100)
        self.vizIntensityMaxSpinBox.setRange(
            self.state.image_min - 0.5 * image_range,
            self.state.image_max + 0.5 * image_range
        )
        self.vizIntensityMaxSpinBox.setSingleStep(image_range / 500)
        self.vizIntensityMaxSpinBox.setValue(self.state.image_max)
        self.state.intensity_window_max = self.state.image_max
