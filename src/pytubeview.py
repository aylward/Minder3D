import sys

import numpy as np

import itk

import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
)

from ui_pytubeview import Ui_MainWindow

class Tube_View_Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Types
        self.image_pixel_type = itk.F
        self.image_type = itk.Image[self.image_pixel_type, 3]
        self.overlay_pixel_type = itk.SS
        self.overlay_type = itk.Image[self.overlay_pixel_type, 3]

        # State
        self.image = None
        self.image_vtk = None
        self.image_array = None
        self.overlay = None
        self.overlay_vtk = None

        self.scene = None
        self.actors = None

        # Preservation
        self.loaded_image = None
        self.loaded_image_filename = "./test.mha"

        self.image_min = 0
        self.image_max = 1

        # File Menu
        self.loadImageMenuItem.triggered.connect(self.loadImage)

        # View 2D Widget
        self.vtk2DWidget = QVTKRenderWindowInteractor(self)
        self.view2DWidget.addWidget(self.vtk2DWidget)

        self.view2D = None

        # View 3D Widget
        self.vtk3DWidget = QVTKRenderWindowInteractor(self)
        self.view3DWidget.addWidget(self.vtk3DWidget)

        self.view3D = None

        # View Tab
        self.viewIntensityMinSlider.valueChanged.connect(
            self.updateViewIntensityMinMaxSliders
        )
        self.viewIntensityMaxSlider.valueChanged.connect(
            self.updateViewIntensityMinMaxSliders
        )
        self.viewIntensityMinSpinBox.valueChanged.connect(
            self.updateViewIntensityMinMaxSpinBoxes
        )
        self.viewIntensityMaxSpinBox.valueChanged.connect(
            self.updateViewIntensityMinMaxSpinBoxes
        )

        self.show()
        self.vtk2DWidget.Initialize()


    def loadImage(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            self.loaded_image_filename,
            "All Files (*)"
        )
        if filename:
            self.loaded_image_filename = filename
            self.loaded_image = itk.imread(filename, self.image_pixel_type)
            self.image = self.loaded_image
            self.overlay = self.overlay_type.New()
            self.overlay.SetRegions(self.image.GetLargestPossibleRegion())
            self.overlay.CopyInformation(self.image)
            self.overlay.Allocate()
            self.updateImage()

    def updateViewIntensityMinMaxSliders(self):
        minI = self.viewIntensityMinSlider.value()
        maxI = self.viewIntensityMaxSlider.value()

        intensityRange = self.image_max - self.image_min
        intensityMin = minI/100.0 * intensityRange + self.image_min
        intensityMax = maxI/100.0 * intensityRange + self.image_min
        self.viewIntensityMinSpinBox.setValue(intensityMin)
        self.viewIntensityMaxSpinBox.setValue(intensityMax)

        intensityWindow = intensityMax - intensityMin
        intensityLevel = intensityMin + intensityWindow / 2.0
        self.view2D.SetColorWindow(intensityWindow)
        self.view2D.SetColorLevel(intensityLevel)
        self.view2D.GetRenderWindow().Render()

    def updateViewIntensityMinMaxSpinBoxes(self):
        intensityMin = self.viewIntensityMinSpinBox.value()
        intensityMax = self.viewIntensityMaxSpinBox.value()

        intensityRange = self.image_max - self.image_min
        minI = int(((intensityMin-self.image_min)/intensityRange)*100 + 0.5)
        maxI = int(((intensityMax-self.image_min)/intensityRange)*100 + 0.5)
        
        self.viewIntensityMinSlider.setValue(minI)
        self.viewIntensityMaxSlider.setValue(maxI)

        intensityWindow = intensityMax - intensityMin
        intensityLevel = intensityMin + intensityWindow / 2.0
        self.view2D.SetColorWindow(intensityWindow)
        self.view2D.SetColorLevel(intensityLevel)
        self.view2D.GetRenderWindow().Render()


    def updateImage(self):
        self.image_vtk = itk.vtk_image_from_image(self.image)
        self.image_array = itk.GetArrayFromImage(self.image)

        if self.view2D == None:
            self.view2D = vtk.vtkImageViewer2()
            self.view2D.SetupInteractor(self.vtk2DWidget)
            self.view2D.SetRenderWindow(self.vtk2DWidget.GetRenderWindow())
        self.view2D.SetInputData(self.image_vtk)
        self.view2D.Render()
        self.view2D.GetRenderer().ResetCamera()
        self.view2D.GetRenderWindow().Render()
        
        self.image_min = np.min(self.image_array)
        self.image_max = np.max(self.image_array)
        image_range = self.image_max-self.image_min
        self.viewIntensityMinSlider.setValue(0)
        self.viewIntensityMinSpinBox.setRange(
            self.image_min-0.5*image_range,
            self.image_max+0.5*image_range
        )
        self.viewIntensityMinSpinBox.setSingleStep( image_range/500 )
        self.viewIntensityMinSpinBox.setValue(self.image_min)

        self.viewIntensityMaxSlider.setValue(100)
        self.viewIntensityMaxSpinBox.setRange(
            self.image_min-0.5*image_range,
            self.image_max+0.5*image_range
        )
        self.viewIntensityMaxSpinBox.setSingleStep( image_range/500 )
        self.viewIntensityMaxSpinBox.setValue(self.image_max)

        self.updateViewIntensityMinMaxSpinBoxes()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    pytubeview = Tube_View_Window()

    sys.exit(app.exec())
