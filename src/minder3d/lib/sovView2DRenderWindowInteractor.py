import numpy as np
from PySide6.QtCore import Qt
from vtk import (
    VTK_UNSIGNED_CHAR,
    vtkImageBlend,
    vtkImageData,
    vtkImageViewer2,
    vtkTextActor,
    vtkWorldPointPicker,
)
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtk.util.numpy_support import numpy_to_vtk

from .sovUtils import time_and_log


class View2DRenderWindowInteractor(QVTKRenderWindowInteractor):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)

        self.gui = gui
        self.state = state

        self.view2D = None
        self.cornerAnnotationTextActor = None

        self.mouse_modes = {
            0: 'Point',
            1: 'Select',
            2: 'WindowLevel',
            3: 'Paint',
            4: 'Contour',
            5: 'Ruler',
            6: 'Angle',
            7: 'Crop',
        }

        self.current_mouse_mode = 0

        self.mouse_pressed = False
        self.mouse_start = []
        self.win_start = 0
        self.lvl_start = 0

    @time_and_log
    def getWorldPosition(self, x, y):
        img_num = self.state.current_image_num
        axis = self.state.view2D_image_axis_order[img_num]
        spacing = np.array(self.state.image[img_num].GetSpacing())
        size = np.array(
            self.state.image[img_num].GetLargestPossibleRegion().GetSize()
        )

        picker = vtkWorldPointPicker()
        picker.Pick(x, y, 0, self.view2D.GetRenderer())
        vtk_world_xy = picker.GetPickPosition()
        vtk_world = [vtk_world_xy[0], vtk_world_xy[1], 0]
        z = self.state.view2D_slice[img_num][axis[2]]
        if self.state.view2D_flip[img_num][axis[2]]:
            z = int(size[axis[2]] - z - 1)
        vtk_world[2] = z * spacing[axis[2]]
        vtk_indx = [int(vtk_world[axis.index(i)]) for i in range(3)]

        indx = [int(vtk_indx[i] / spacing[i] + 0.5) for i in range(3)]
        # y-axis is flipped
        if not self.state.view2D_flip[img_num][axis[1]]:
            indx[1] = int(size[1] - indx[1] - 1)
        for i in [0, 2]:
            if self.state.view2D_flip[img_num][axis[i]]:
                indx[axis[i]] = int(size[axis[i]] - indx[axis[i]] - 1)
        pos = self.state.image[img_num].TransformIndexToPhysicalPoint(indx)
        return indx, pos

    @time_and_log
    def mousePressEvent(self, event):
        if event.button() != Qt.LeftButton:
            super().mousePressEvent(event)
            return

        ctrl, shift = self._GetCtrlShift(event)
        if ctrl is False and shift is True:
            super().mousePressEvent(event)
            return

        if len(self.state.image) == 0:
            return

        if self.current_mouse_mode == 0:
            self.mouse_pressed = True
            x, y = self.GetEventPosition()
            indx, pos = self.getWorldPosition(x, y)
            self.state.current_pixel_index = indx
            self.state.current_pixel_position = pos
            self.gui.update_pixel()
        elif self.current_mouse_mode == 2:
            self.mouse_pressed = True
            self.mouse_start = [event.x(), event.y()]
            self.win_start = (
                self.state.view2D_intensity_window_max[
                    self.state.current_image_num
                ]
                - self.state.view2D_intensity_window_min[
                    self.state.current_image_num
                ]
            )
            self.lvl_start = (
                self.win_start / 2
                + self.state.view2D_intensity_window_min[
                    self.state.current_image_num
                ]
            )

    @time_and_log
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_pressed = False
        super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if not self.mouse_pressed:
            super().mouseMoveEvent(event)
            return

        ctrl, shift = self._GetCtrlShift(event)
        if ctrl is False and shift is True:
            super().mouseMoveEvent(event)
            return

        if len(self.state.image) == 0:
            return

        if self.current_mouse_mode == 0:
            x, y = self.GetEventPosition()
            indx, pos = self.getWorldPosition(x, y)
            self.state.current_pixel_index = indx
            self.state.current_pixel_position = pos
            self.gui.update_pixel()
            super().mouseMoveEvent(event)
        elif self.current_mouse_mode == 1:
            x, y = self.GetEventPosition()
            indx, pos = self.getWorldPosition(x, y)
            self.state.current_pixel_index = indx
            self.state.current_pixel_position = pos
            self.gui.update_pixel()
        elif self.current_mouse_mode == 2:
            winsize = self.GetRenderWindow().GetSize()
            irange = (
                self.state.image_max[self.state.current_image_num]
                - self.state.image_min[self.state.current_image_num]
            )
            x, y = event.x(), event.y()
            winDelta = (
                float(x - self.mouse_start[0]) / (2 * winsize[0]) * irange
            )
            lvlDelta = (
                float(y - self.mouse_start[1]) / (2 * winsize[1]) * irange
            )
            new_win = self.win_start + winDelta
            new_lvl = self.lvl_start + lvlDelta
            new_min = new_lvl - new_win / 2.0
            if (
                new_min
                < self.state.image_min[self.state.current_image_num]
                - irange / 2.0
            ):
                new_min = (
                    self.state.image_min[self.state.current_image_num]
                    - irange / 2.0
                )
            new_max = new_lvl + new_win / 2
            if (
                new_max
                > self.state.image_max[self.state.current_image_num]
                + irange / 2.0
            ):
                new_max = (
                    self.state.image_max[self.state.current_image_num]
                    + irange / 2.0
                )
            self.state.view2D_intensity_window_min[
                self.state.current_image_num
            ] = new_min
            self.state.view2D_intensity_window_max[
                self.state.current_image_num
            ] = new_max
            self.update_view()

    @time_and_log
    def reset_camera(self):
        self.view2D.GetRenderer().ResetCamera()
        self.view2D.Render()
        self.view2D.GetRenderWindow().Render()

    @time_and_log
    def update_image(self):
        if len(self.state.image) == 0:
            return

        if self.view2D is None:
            self.cornerAnnotationTextActor = vtkTextActor()
            prop = self.cornerAnnotationTextActor.GetTextProperty()
            prop.SetFontSize(10)
            prop.SetFontFamilyToCourier()
            prop.SetBackgroundRGBA(0.0, 0.0, 0.0, 1.0)

            self.view2D = vtkImageViewer2()
            self.view2D.SetupInteractor(self)
            self.view2D.SetRenderWindow(self.GetRenderWindow())
            self.update_view()
            self.view2D.GetRenderer().ResetCamera()
            self.view2D.Render()
            self.view2D.GetRenderWindow().Render()
        else:
            self.update_view()

    @time_and_log
    def update_view(self):
        if (
            self.view2D is not None
            and self.state.image is not None
            and self.state.current_image_num >= 0
            and self.state.current_image_num < len(self.state.image)
        ):
            current_image_array = self.state.image_array[
                self.state.current_image_num
            ]
            current_overlay_array = self.state.overlay_array[
                self.state.current_image_num
            ]

            view_slice = []
            overlay_slice_rgba = []

            img_num = self.state.current_image_num
            view_image_axis = self.state.view2D_image_axis_order[img_num][2]

            slice_num = self.state.view2D_slice[img_num][view_image_axis]

            if current_image_array.shape[2 - view_image_axis] == 1:
                view_slice = current_image_array[0, ::-1, :]
                overlay_slice_rgba = current_overlay_array[0, ::-1, :]
            else:
                view_slice = np.take(
                    current_image_array, slice_num, axis=2 - view_image_axis
                )
                overlay_slice_rgba = np.take(
                    current_overlay_array, slice_num, axis=2 - view_image_axis
                )
                if (
                    self.state.view2D_image_axis_order[img_num][0]
                    > self.state.view2D_image_axis_order[img_num][1]
                ):
                    view_slice = np.transpose(view_slice)
                    overlay_slice_rgba = np.transpose(
                        overlay_slice_rgba, axes=(1, 0, 2)
                    )

            view_intensity_min = self.state.view2D_intensity_window_min[img_num]
            view_intensity_max = self.state.view2D_intensity_window_max[img_num]
            if view_intensity_min != view_intensity_max:
                view_slice = (
                    (view_slice - view_intensity_min)
                    / (view_intensity_max - view_intensity_min)
                    * 255
                )
                view_slice = np.clip(view_slice, 0, 255)
            else:
                view_slice = np.ones(view_slice.shape) * 128

            if self.state.view2D_flip[img_num][
                self.state.view2D_image_axis_order[img_num][0]
            ]:
                view_slice = np.flip(view_slice, axis=1)

            # vtk y-axis is flipped, so flip the flip
            if not self.state.view2D_flip[img_num][
                self.state.view2D_image_axis_order[img_num][1]
            ]:
                view_slice = np.flip(view_slice, axis=0)

            view_slice_rgba = np.empty(
                (view_slice.shape[0], view_slice.shape[1], 4), dtype=np.uint8
            )
            view_slice_rgba[:, :, 0] = view_slice
            view_slice_rgba[:, :, 1] = view_slice
            view_slice_rgba[:, :, 2] = view_slice
            view_slice_rgba[:, :, 3] = np.ones(view_slice.shape) * 255

            # Import image directly to gray RGBA
            spacing = np.array(self.state.image[img_num].GetSpacing())
            view_slice_vtk = vtkImageData()
            view_slice_vtk.SetSpacing(
                spacing[self.state.view2D_image_axis_order[img_num][0]],
                spacing[self.state.view2D_image_axis_order[img_num][1]],
                spacing[self.state.view2D_image_axis_order[img_num][2]],
            )
            view_slice_vtk.SetDimensions(
                view_slice.shape[1], view_slice.shape[0], 1
            )
            vtk_data = numpy_to_vtk(
                num_array=view_slice_rgba.reshape(
                    -1, view_slice_rgba.shape[-1]
                ),
                deep=False,
                array_type=VTK_UNSIGNED_CHAR,
            )
            view_slice_vtk.GetPointData().SetScalars(vtk_data)

            if self.state.view2D_flip[img_num][
                self.state.view2D_image_axis_order[img_num][0]
            ]:
                overlay_slice_rgba = np.flip(overlay_slice_rgba, axis=1)

            # vtk y-axis is flipped, so flip the flip
            if not self.state.view2D_flip[img_num][
                self.state.view2D_image_axis_order[img_num][1]
            ]:
                overlay_slice_rgba = np.flip(overlay_slice_rgba, axis=0)

            # Import overlay to RGBA
            overlay_slice_vtk = vtkImageData()
            overlay_slice_vtk.SetSpacing(
                spacing[self.state.view2D_image_axis_order[img_num][0]],
                spacing[self.state.view2D_image_axis_order[img_num][1]],
                spacing[self.state.view2D_image_axis_order[img_num][2]],
            )
            overlay_slice_vtk.SetDimensions(
                view_slice.shape[1], view_slice.shape[0], 1
            )
            vtk_data = numpy_to_vtk(
                num_array=overlay_slice_rgba.reshape(
                    -1, overlay_slice_rgba.shape[-1]
                ),
                deep=False,
                array_type=VTK_UNSIGNED_CHAR,
            )
            overlay_slice_vtk.GetPointData().SetScalars(vtk_data)

            try:
                imgBlender = vtkImageBlend()
                imgBlender.AddInputData(view_slice_vtk)
                imgBlender.AddInputData(overlay_slice_vtk)
                imgBlender.SetOpacity(1, self.state.view2D_overlay_opacity)
                imgBlender.SetOpacity(0, 1.0)
                imgBlender.Update()
                blended_slice_vtk = imgBlender.GetOutput()
            except Exception as e:
                self.gui.log(str(e), 'ERROR')
                assert e

            self.view2D.SetInputData(blended_slice_vtk)

            win_min = self.state.view2D_intensity_window_min[img_num]
            win_max = self.state.view2D_intensity_window_max[img_num]
            lvl = (win_max + win_min) / 2.0
            win = win_max - win_min
            inputStr = f'W:{win:.1f} L:{lvl:.1f}'
            self.cornerAnnotationTextActor.SetInput(inputStr)
            winsize = self.GetRenderWindow().GetSize()
            self.cornerAnnotationTextActor.SetPosition2(
                winsize[0] - 12 * len(inputStr), 40
            )
            self.cornerAnnotationTextActor.GetTextProperty().SetFontSize(10)
            # self.cornerAnnotationTextActor.GetTextProperty().SetColor(
            #     colors.GetColor3d("Gold").GetData())
            self.view2D.GetRenderer().AddActor2D(self.cornerAnnotationTextActor)
            self.view2D.Render()
            self.view2D.GetRenderWindow().Render()
        else:
            if self.view2D is not None:
                self.view2D.GetRenderer().RemoveAllViewProps()
                self.view2D.GetRenderWindow().Render()
                self.view2D = None
