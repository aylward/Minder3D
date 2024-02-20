import numpy as np

import itk

import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtk.util.numpy_support import numpy_to_vtk

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from soViewer2D import render_scene_in_overlay_array

from ui_tabView2D import Ui_tabView2DWidget


class View2DRenderWindowInteractor(QVTKRenderWindowInteractor):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)

        self.gui = gui
        self.state = state

        self.view2D = None

    def mousePressEvent(self, event):
        ctrl, shift = self._GetCtrlShift(event)
        if ctrl is False and shift is True:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        ctrl, shift = self._GetCtrlShift(event)
        if ctrl is False and shift is True:
            super().mouseMoveEvent(event)

    def update_image(self):
        if self.view2D is None:
            self.view2D = vtk.vtkImageViewer2()
            self.view2D.SetupInteractor(self)
            self.view2D.SetRenderWindow(self.GetRenderWindow())
            self.update_view()
            self.view2D.GetRenderer().ResetCamera()
            self.view2D.Render()
            self.view2D.GetRenderWindow().Render()

    def update_view(self):
        if self.view2D is not None and self.state.image is not None:
            if self.state.image_array is None:
                self.state.image_array = itk.GetArrayFromImage(
                    self.state.image
                )
            if self.state.overlay_array is None:
                self.state.overlay_array = itk.GetArrayFromImage(
                    self.state.overlay
                )
            spacing = self.state.image.GetSpacing()
            overlay_slice_rgba = []
            slice_axis_order = [0, 1, 2]
            if self.state.image.shape[0] == 1:
                image_slice = self.state.image_array[0, ::-1, :]
                overlay_slice_rgba = self.state.overlay_array[0, ::-1, :]
                slice_axis_order = [0, 1, 2]
            elif self.state.image_axis == 2:
                image_slice = self.state.image_array[
                    self.state.image_slice[self.state.image_axis], ::-1, :
                ]
                overlay_slice_rgba = self.state.overlay_array[
                    self.state.image_slice[self.state.image_axis], ::-1, :
                ]
                slice_axis_order = [0, 1, 2]
            elif self.state.image_axis == 1:
                image_slice = self.state.image_array[
                    :, self.state.image_slice[self.state.image_axis], :
                ]
                overlay_slice_rgba = self.state.overlay_array[
                    :, self.state.image_slice[self.state.image_axis], :
                ]
                slice_axis_order = [0, 2, 1]
            elif self.state.image_axis == 0:
                image_slice = self.state.image_array[
                    :, ::-1, self.state.image_slice[self.state.image_axis]
                ]
                overlay_slice_rgba = self.state.overlay_array[
                    :, ::-1, self.state.image_slice[self.state.image_axis]
                ]
                slice_axis_order = [1, 2, 0]

            image_view_min = self.state.image_intensity_window_min
            image_view_max = self.state.image_intensity_window_max

            image_slice = (
                (image_slice - image_view_min) /
                (image_view_max - image_view_min) * 255
            )
            image_slice = np.clip(image_slice, 0, 255)

            image_slice_rgba = np.empty(
                (image_slice.shape[0], image_slice.shape[1], 4),
                dtype=np.uint8
            )
            image_slice_rgba[:, :, 0] = image_slice
            image_slice_rgba[:, :, 1] = image_slice
            image_slice_rgba[:, :, 2] = image_slice
            image_slice_rgba[:, :, 3] = np.ones(image_slice.shape) * 255

            # Import image directly to gray RGBA
            image_slice_vtk = vtk.vtkImageData()
            image_slice_vtk.SetSpacing(
                spacing[slice_axis_order[0]],
                spacing[slice_axis_order[1]],
                spacing[slice_axis_order[2]]
            )
            image_slice_vtk.SetDimensions(
                image_slice.shape[1],
                image_slice.shape[0],
                1
            )
            vtk_data = numpy_to_vtk(
                num_array=image_slice_rgba.reshape(-1, image_slice_rgba.shape[-1]),
                deep=False,
                array_type=vtk.VTK_UNSIGNED_CHAR
            )
            image_slice_vtk.GetPointData().SetScalars(vtk_data)

            # Import overlay to RGBA
            overlay_slice_vtk = vtk.vtkImageData()
            overlay_slice_vtk.SetSpacing(
                spacing[slice_axis_order[0]],
                spacing[slice_axis_order[1]],
                spacing[slice_axis_order[2]]
            )
            overlay_slice_vtk.SetDimensions(
                image_slice.shape[1],
                image_slice.shape[0],
                1
            )
            vtk_data = numpy_to_vtk(
                num_array=overlay_slice_rgba.reshape(
                    -1,
                    overlay_slice_rgba.shape[-1]
                ),
                deep=False,
                array_type=vtk.VTK_UNSIGNED_CHAR
            )
            overlay_slice_vtk.GetPointData().SetScalars(vtk_data)

            imgBlender = vtk.vtkImageBlend()
            imgBlender.AddInputData(image_slice_vtk)
            imgBlender.AddInputData(overlay_slice_vtk)
            imgBlender.SetOpacity(1, self.state.overlay_opacity)
            imgBlender.SetOpacity(0, 0.5)
            imgBlender.Update()
            blended_slice_vtk = imgBlender.GetOutput()

            self.view2D.SetInputData(blended_slice_vtk)

            self.view2D.Render()
            self.view2D.GetRenderWindow().Render()


class TabView2DWidget(QWidget, Ui_tabView2DWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.vtk2DViewWidget = View2DRenderWindowInteractor(gui, state, self)
        self.view2DLayout.addWidget(self.vtk2DViewWidget)

        self.view2DSliceSlider.valueChanged.connect(self.update_slice_from_slider)
        self.view2DSliceText.textChanged.connect(self.update_slice_from_text)
        self.view2DOverlayOpacitySlider.valueChanged.connect(self.update_overlay_opacity)

        self.view2DXYButton.clicked.connect(self.update_axis_xy)
        self.view2DXZButton.clicked.connect(self.update_axis_xz)
        self.view2DYZButton.clicked.connect(self.update_axis_yz)

        self.redraw_slice = True

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.vtk2DViewWidget.close()

    def initialize(self):
        self.vtk2DViewWidget.Initialize()

    def update_overlay_opacity(self):
        self.state.overlay_opacity = self.view2DOverlayOpacitySlider.value() / 100.0
        self.update()

    def update_axis_xy(self):
        self.state.image_axis = 2
        self.redraw_slice = False
        self.view2DSliceSlider.setMaximum(
            self.state.image_array.shape[2-self.state.image_axis]-1
        )
        self.view2DSliceSlider.setValue(
            self.state.image_slice[self.state.image_axis]
        )
        self.view2DSliceText.setPlainText(
            f"{self.state.image_slice[self.state.image_axis]}"
        )
        self.redraw_slice = True
        self.update()

    def update_axis_xz(self):
        self.state.image_axis = 1
        self.redraw_slice = False
        self.view2DSliceSlider.setMaximum(
            self.state.image_array.shape[2-self.state.image_axis]-1
        )
        self.view2DSliceSlider.setValue(
            self.state.image_slice[self.state.image_axis]
        )
        self.view2DSliceText.setPlainText(
            f"{self.state.image_slice[self.state.image_axis]}"
        )
        self.redraw_slice = True
        self.update()

    def update_axis_yz(self):
        self.state.image_axis = 0
        self.redraw_slice = False
        self.view2DSliceSlider.setMaximum(
            self.state.image_array.shape[2-self.state.image_axis]-1
        )
        self.view2DSliceSlider.setValue(
            self.state.image_slice[self.state.image_axis]
        )
        self.view2DSliceText.setPlainText(
            f"{self.state.image_slice[self.state.image_axis]}"
        )
        self.redraw_slice = True
        self.update()

    def update_image(self):
        self.state.image_intensity_window_min = self.state.image_min
        self.state.image_intensity_window_max = self.state.image_max

        self.view2DSliceSlider.setMinimum(0)
        self.view2DSliceSlider.setMaximum(
            self.state.image_array.shape[2-self.state.image_axis]-1
        )

        self.view2DSliceSlider.setValue(0)
        self.view2DSliceText.setPlainText("0")

        self.state.image_slice = [0, 0, 0]
        self.state.image_axis = 2

        self.vtk2DViewWidget.update_image()

    def update_overlay(self):
        if self.state.scene is not None:
            render_scene_in_overlay_array(
                self.state.scene,
                self.state.image,
                self.state.overlay_array,
            )
            self.state.overlay = itk.GetImageFromArray(
                self.state.overlay_array,
                ttype=self.state.overlay_type,
            )
            self.state.overlay.CopyInformation(self.state.image)
            self.update()

    def update_scene(self):
        if self.state.scene is not None:
            render_scene_in_overlay_array(
                self.state.scene,
                self.state.image,
                self.state.overlay_array,
            )
            self.state.overlay = itk.GetImageFromArray(
                self.state.overlay_array,
                ttype=self.state.overlay_type,
            )
            self.state.overlay.CopyInformation(self.state.image)
            self.update()

    def update_slice_from_slider(self):
        if (self.redraw_slice and self.view2DSliceSlider.value() != self.state.image_slice[self.state.image_axis]):
            self.redraw_slice = False
            self.state.image_slice[self.state.image_axis] = self.view2DSliceSlider.value()
            update_slider = False
            if self.state.image_slice[self.state.image_axis] < 0:
                self.state.image_slice[self.state.image_axis] = 0
                update_slider = True
            if self.state.image_slice[self.state.image_axis] >= self.state.image_array.shape[
                2-self.state.image_axis
            ]:
                self.state.image_slice[self.state.image_axis] = self.state.image_array.shape[
                    2-self.state.image_axis
                ]-1
                update_slider = True
            if update_slider:
                self.view2DSliceSlider.setValue(self.state.image_slice[self.state.image_axis])
            self.view2DSliceText.setPlainText(f"{self.state.image_slice[self.state.image_axis]}")
            self.redraw_slice = True
            self.update()

    def update_slice_from_text(self):
        if self.redraw_slice == True and int(self.view2DSliceText.toPlainText()) != self.state.image_slice[self.state.image_axis]:
            self.redraw_slice = False
            self.state.image_slice[self.state.image_axis] = int(self.view2DSliceText.toPlainText())
            update_text = False
            if self.state.image_slice[self.state.image_axis] < 0:
                self.state.image_slice[self.state.image_axis] = 0
                update_text = True
            if self.state.image_slice[self.state.image_axis] >= self.state.image_array.shape[
                2-self.state.image_axis
            ]:
                self.state.image_slice[self.state.image_axis] = self.state.image_array.shape[
                    2-self.state.image_axis
                ]-1
                update_text = True
            if update_text:
                self.view2DSliceText.setPlainText(f"{self.state.image_slice[self.state.image_axis]}")
            self.view2DSliceSlider.setValue(self.state.image_slice[self.state.image_axis])
            self.redraw_slice = True
            self.update()

    def update(self):
        self.vtk2DViewWidget.update_view()
