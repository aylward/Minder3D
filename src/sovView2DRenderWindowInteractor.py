import numpy as np

import itk

import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtk.util.numpy_support import numpy_to_vtk

from sovUtils import time_and_log


class View2DRenderWindowInteractor(QVTKRenderWindowInteractor):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)

        self.gui = gui
        self.state = state

        self.view2D = None

    @time_and_log
    def mousePressEvent(self, event):
        ctrl, shift = self._GetCtrlShift(event)
        if ctrl is False and shift is True:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        ctrl, shift = self._GetCtrlShift(event)
        if ctrl is False and shift is True:
            super().mouseMoveEvent(event)

    @time_and_log
    def reset_camera(self):
        self.view2D.GetRenderer().ResetCamera()
        self.view2D.Render()
        self.view2D.GetRenderWindow().Render()

    @time_and_log
    def update_image(self):
        if self.state.view_image_num == 0:
            self.state.view_intensity_window_min = self.state.loaded_image_min
            self.state.view_intensity_window_max = self.state.loaded_image_max
        else:
            self.state.view_intensity_window_min = self.state.image_min
            self.state.view_intensity_window_max = self.state.image_max
        if self.view2D is None:
            self.view2D = vtk.vtkImageViewer2()
            self.view2D.SetupInteractor(self)
            self.view2D.SetRenderWindow(self.GetRenderWindow())
            self.update_view()
            self.view2D.GetRenderer().ResetCamera()
            self.view2D.Render()
            self.view2D.GetRenderWindow().Render()

    @time_and_log
    def update_view(self):
        if self.view2D is not None and self.state.image is not None:
            current_image_array = None
            spacing = []
            if self.state.view_image_num == 0:
                spacing = self.state.loaded_image.GetSpacing()
                current_image_array = self.state.loaded_image_array
            else:
                spacing = self.state.image.GetSpacing()
                current_image_array = self.state.image_array

            if self.state.overlay_array is None:
                self.state.overlay_array = itk.GetArrayFromImage(
                    self.state.overlay
                )

            view_slice = []
            overlay_slice_rgba = []
            slice_axis_order = [0, 1, 2]
            if current_image_array.shape[2] == 1:
                view_slice = current_image_array[0, ::-1, :]
                overlay_slice_rgba = self.state.overlay_array[0, ::-1, :]
                slice_axis_order = [0, 1, 2]
            elif self.state.view_axis == 2:
                view_slice = current_image_array[
                    self.state.view_slice[self.state.view_axis], ::-1, :
                ]
                overlay_slice_rgba = self.state.overlay_array[
                    self.state.view_slice[self.state.view_axis], ::-1, :
                ]
                slice_axis_order = [0, 1, 2]
            elif self.state.view_axis == 1:
                view_slice = current_image_array[
                    :, self.state.view_slice[self.state.view_axis], :
                ]
                overlay_slice_rgba = self.state.overlay_array[
                    :, self.state.view_slice[self.state.view_axis], :
                ]
                slice_axis_order = [0, 2, 1]
            elif self.state.view_axis == 0:
                view_slice = current_image_array[
                    :, ::-1, self.state.view_slice[self.state.view_axis]
                ]
                overlay_slice_rgba = self.state.overlay_array[
                    :, ::-1, self.state.view_slice[self.state.view_axis]
                ]
                slice_axis_order = [1, 2, 0]

            view_intensity_min = self.state.view_intensity_window_min
            view_intensity_max = self.state.view_intensity_window_max
            if view_intensity_min != view_intensity_max:
                view_slice = (
                    (view_slice - view_intensity_min) /
                    (view_intensity_max - view_intensity_min) * 255
                )
                view_slice = np.clip(view_slice, 0, 255)
            else:
                view_slice = np.ones(view_slice.shape)*128

            if self.state.view_flip[(self.state.view_axis+1) % 3]:
                view_slice = np.flip(view_slice, axis=1)

            if self.state.view_flip[(self.state.view_axis+2) % 3]:
                view_slice = np.flip(view_slice, axis=0)

            view_slice_rgba = np.empty(
                (view_slice.shape[0], view_slice.shape[1], 4),
                dtype=np.uint8
            )
            view_slice_rgba[:, :, 0] = view_slice
            view_slice_rgba[:, :, 1] = view_slice
            view_slice_rgba[:, :, 2] = view_slice
            view_slice_rgba[:, :, 3] = np.ones(view_slice.shape) * 255

            # Import image directly to gray RGBA
            view_slice_vtk = vtk.vtkImageData()
            view_slice_vtk.SetSpacing(
                spacing[slice_axis_order[0]],
                spacing[slice_axis_order[1]],
                spacing[slice_axis_order[2]]
            )
            view_slice_vtk.SetDimensions(
                view_slice.shape[1],
                view_slice.shape[0],
                1
            )
            vtk_data = numpy_to_vtk(
                num_array=view_slice_rgba.reshape(-1, view_slice_rgba.shape[-1]),
                deep=False,
                array_type=vtk.VTK_UNSIGNED_CHAR
            )
            view_slice_vtk.GetPointData().SetScalars(vtk_data)

            if self.state.view_flip[(self.state.view_axis+1) % 3]:
                overlay_slice_rgba = np.flip(overlay_slice_rgba, axis=1)

            if self.state.view_flip[(self.state.view_axis+2) % 3]:
                overlay_slice_rgba = np.flip(overlay_slice_rgba, axis=0)

            # Import overlay to RGBA
            overlay_slice_vtk = vtk.vtkImageData()
            overlay_slice_vtk.SetSpacing(
                spacing[slice_axis_order[0]],
                spacing[slice_axis_order[1]],
                spacing[slice_axis_order[2]]
            )
            overlay_slice_vtk.SetDimensions(
                view_slice.shape[1],
                view_slice.shape[0],
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
            imgBlender.AddInputData(view_slice_vtk)
            imgBlender.AddInputData(overlay_slice_vtk)
            imgBlender.SetOpacity(1, self.state.overlay_opacity)
            imgBlender.SetOpacity(0, 1.0)
            imgBlender.Update()
            blended_slice_vtk = imgBlender.GetOutput()

            self.view2D.SetInputData(blended_slice_vtk)

            self.view2D.Render()
            self.view2D.GetRenderWindow().Render()
