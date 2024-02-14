import sys

import numpy as np

import itk

import vtk

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
)

from ui_tabView import Ui_tabView

class tabView(QWidget, Ui_tabView):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.redraw = True

        self.viewIntensityMinSlider.sliderMoved.connect(
            self.updateViewIntensityMinMaxSliders
        )
        self.viewIntensityMaxSlider.sliderMoved.connect(
            self.updateViewIntensityMinMaxSliders
        )

        self.viewIntensityMinSpinBox.valueChanged.connect(
            self.updateViewIntensityMinMaxSpinBoxes
        )
        self.viewIntensityMaxSpinBox.valueChanged.connect(
            self.updateViewIntensityMinMaxSpinBoxes
        )
 
    def updateViewIntensityMinMaxSliders(self):
        minI = self.viewIntensityMinSlider.value()
        maxI = self.viewIntensityMaxSlider.value()

        intensityRange = self.state.image_max - self.state.image_min
        intensityMin = minI / 100.0 * intensityRange + self.state.image_min
        intensityMax = maxI / 100.0 * intensityRange + self.state.image_min

        if self.redraw:
            self.redraw = False
            self.viewIntensityMinSpinBox.setValue(intensityMin)
            self.viewIntensityMaxSpinBox.setValue(intensityMax)
            self.state.image_intensity_window_min = intensityMin
            self.state.image_intensity_window_max = intensityMax
            self.gui.updateView2D()
            self.redraw = True
            

    def updateViewIntensityMinMaxSpinBoxes(self):
        intensityMin = self.viewIntensityMinSpinBox.value()
        intensityMax = self.viewIntensityMaxSpinBox.value()

        intensityRange = self.state.image_max - self.state.image_min
        minI = int(((intensityMin - self.state.image_min)
            / intensityRange) * 100 + 0.5)
        maxI = int(((intensityMax - self.state.image_min)
            / intensityRange) * 100 + 0.5)

        if self.redraw:
            self.redraw = False
            self.viewIntensityMinSlider.setValue(minI)
            self.viewIntensityMaxSlider.setValue(maxI)
            self.state.image_intensity_window_min = intensityMin
            self.state.image_intensity_window_max = intensityMax
            self.gui.updateView2D()
            self.redraw = True

    def updateImage(self):
        image_range = self.state.image_max - self.state.image_min

        self.viewIntensityMinSlider.setValue(0)
        self.viewIntensityMinSpinBox.setRange(
            self.state.image_min - 0.5 * image_range,
            self.state.image_max + 0.5 * image_range
        )
        self.viewIntensityMinSpinBox.setSingleStep(image_range / 500)
        self.viewIntensityMinSpinBox.setValue(self.state.image_min)
        self.state.intensity_window_min = self.state.image_min

        self.viewIntensityMaxSlider.setValue(100)
        self.viewIntensityMaxSpinBox.setRange(
            self.state.image_min - 0.5 * image_range,
            self.state.image_max + 0.5 * image_range
        )
        self.viewIntensityMaxSpinBox.setSingleStep(image_range / 500)
        self.viewIntensityMaxSpinBox.setValue(self.state.image_max)
        self.state.intensity_window_max = self.state.image_max
