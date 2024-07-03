import itk
import numpy as np
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget
from vtk import vtkRenderLargeImage
from vtk.util.numpy_support import vtk_to_numpy

from .sovUtils import time_and_log
from .sovView2DRenderWindowInteractor import View2DRenderWindowInteractor
from .sovView2DResources import qCleanupResources  # noqa: F401
from .sovView2DUtils import (
    render_object_in_overlay_array,
    render_scene_in_overlay_array,
)
from .ui_sovView2DPanelWidget import Ui_View2DPanelWidget


class View2DPanelWidget(QWidget, Ui_View2DPanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.mouse_mode_buttons = {
            0: self.view2DPointModeButton,
            1: self.view2DSelectModeButton,
            2: self.view2DWindowLevelModeButton,
            3: self.view2DPaintModeButton,
            4: self.view2DContourModeButton,
            5: self.view2DRulerModeButton,
            6: self.view2DAngleModeButton,
            7: self.view2DCropModeButton,
        }

        self.view2DPointModeButton.clicked.connect(
            lambda: self.update_mouse_mode(0)
        )
        self.view2DPointModeButton.setIcon(
            QIcon(':view2D/icons/tool_point.svg')
        )
        self.view2DPointModeButton.setToolTip('Point')
        self.view2DSelectModeButton.clicked.connect(
            lambda: self.update_mouse_mode(1)
        )
        self.view2DSelectModeButton.setIcon(
            QIcon(':view2D/icons/tool_select.svg')
        )
        self.view2DPointModeButton.setToolTip('Select')
        self.view2DWindowLevelModeButton.clicked.connect(
            lambda: self.update_mouse_mode(2)
        )
        self.view2DWindowLevelModeButton.setIcon(
            QIcon(':view2D/icons/tool_windowlevel.svg')
        )
        self.view2DPointModeButton.setToolTip('Window/Level')
        self.view2DPaintModeButton.clicked.connect(
            lambda: self.update_mouse_mode(3)
        )
        self.view2DPaintModeButton.setIcon(
            QIcon(':view2D/icons/tool_paint.svg')
        )
        self.view2DPointModeButton.setToolTip('Paint')
        self.view2DContourModeButton.clicked.connect(
            lambda: self.update_mouse_mode(4)
        )
        self.view2DContourModeButton.setIcon(
            QIcon(':view2D/icons/tool_contour.svg')
        )
        self.view2DPointModeButton.setToolTip('Contour')
        self.view2DRulerModeButton.clicked.connect(
            lambda: self.update_mouse_mode(5)
        )
        self.view2DRulerModeButton.setIcon(
            QIcon(':view2D/icons/tool_ruler.svg')
        )
        self.view2DPointModeButton.setToolTip('Ruler')
        self.view2DAngleModeButton.clicked.connect(
            lambda: self.update_mouse_mode(6)
        )
        self.view2DAngleModeButton.setIcon(
            QIcon(':view2D/icons/tool_angle.svg')
        )
        self.view2DPointModeButton.setToolTip('Angle')
        self.view2DCropModeButton.clicked.connect(
            lambda: self.update_mouse_mode(7)
        )
        self.view2DCropModeButton.setIcon(QIcon(':view2D/icons/tool_crop.svg'))
        self.view2DPointModeButton.setToolTip('Crop')

        self.vtk2DViewWidget = View2DRenderWindowInteractor(gui, state, self)
        self.view2DLayout.addWidget(self.vtk2DViewWidget)

        self.view2DSliceSlider.valueChanged.connect(
            self.update_slice_from_slider
        )
        self.view2DSliceText.textChanged.connect(self.update_slice_from_text)
        self.view2DOverlayOpacitySlider.valueChanged.connect(
            self.update_overlay_opacity
        )

        self.view2DAxButton.clicked.connect(self.update_view_plane_axial)
        self.view2DCoButton.clicked.connect(self.update_view_plane_coronal)
        self.view2DSaButton.clicked.connect(self.update_view_plane_sagittal)

        self.view2DResetButton.pressed.connect(self.update_reset)

        self.update_gui = True

        self.update_mouse_mode(0)

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.vtk2DViewWidget.close()

    @time_and_log
    def initialize(self):
        self.vtk2DViewWidget.Initialize()

    @time_and_log
    def get_screenshot(self):
        render = vtkRenderLargeImage()
        render.SetMagnification(1)
        render.SetInput(self.vtk2DViewWidget.view2D.GetRenderer())
        render.Update()
        img = render.GetOutput()
        data = img.GetPointData()
        img_scalars = data.GetScalars()
        dims = img.GetDimensions()
        n_comp = img_scalars.GetNumberOfComponents()
        temp = vtk_to_numpy(img_scalars)
        numpy_data = temp.reshape(dims[1], dims[0], n_comp)
        numpy_data = numpy_data.transpose(0, 1, 2)
        numpy_data = np.flipud(numpy_data)
        return numpy_data

    @time_and_log
    def update_mouse_mode(self, mode):
        if self.update_gui is False:
            return

        self.update_gui = False
        for button in self.mouse_mode_buttons.values():
            button.setChecked(False)
        self.mouse_mode_buttons[mode].setChecked(True)
        self.vtk2DViewWidget.current_mouse_mode = mode
        self.update_gui = True

    @time_and_log
    def update_overlay_opacity(self, value):
        if not self.update_gui:
            return

        self.state.view2D_overlay_opacity = value / 100.0
        self.update()

    @time_and_log
    def update_slice_max_value(self):
        img_num = self.state.current_image_num
        view_image_axis = self.state.view2D_image_axis_order[img_num][2]
        slice_max = (
            self.state.image_array[img_num].shape[2 - view_image_axis] - 1
        )
        slice_current = self.state.view2D_slice[img_num][view_image_axis]

        self.update_gui = False

        self.view2DSliceSlider.setMaximum(slice_max)
        self.view2DSliceSlider.setValue(slice_current)
        self.view2DSliceText.setMaximum(slice_max)
        self.view2DSliceText.setValue(slice_current)

        self.gui.visualizationPanel.update_view2D()

        self.update_gui = True

    @time_and_log
    def update_view_plane_coronal(self, redraw=True):
        if not self.update_gui:
            return

        img_num = self.state.current_image_num

        # coronal plane -> x = axial, y = coronal
        self.state.view2D_csa_axis_order[img_num] = [2, 0, 1]
        self.state.view2D_image_axis_order[img_num] = [
            self.state.csa_to_image_axis[img_num][i]
            for i in self.state.view2D_csa_axis_order[img_num]
        ]

        self.update_slice_max_value()

        if redraw:
            self.update()
            self.vtk2DViewWidget.reset_camera()

    @time_and_log
    def update_view_plane_sagittal(self, redraw=True):
        if not self.update_gui:
            return

        img_num = self.state.current_image_num

        # sagittal plane -> x = sagittal, y = coronal
        self.state.view2D_csa_axis_order[img_num] = [1, 0, 2]
        self.state.view2D_image_axis_order[img_num] = [
            self.state.csa_to_image_axis[img_num][i]
            for i in self.state.view2D_csa_axis_order[img_num]
        ]

        self.update_slice_max_value()

        if redraw:
            self.update()
            self.vtk2DViewWidget.reset_camera()

    @time_and_log
    def update_view_plane_axial(self, redraw=True):
        if not self.update_gui:
            return

        img_num = self.state.current_image_num

        # axial plane -> x = axial, y = sagittal
        self.state.view2D_csa_axis_order[img_num] = [2, 1, 0]
        self.state.view2D_image_axis_order[img_num] = [
            self.state.csa_to_image_axis[img_num][i]
            for i in self.state.view2D_csa_axis_order[img_num]
        ]

        self.update_slice_max_value()

        if redraw:
            self.update()
            self.vtk2DViewWidget.reset_camera()

    @time_and_log
    def update_view_image_num(self, index):
        if not self.update_gui:
            return

        self.state.current_image_num = index

        slice_max = 0
        slice_current = 0
        if index > 0:
            slice_max = (
                self.state.image_array[self.state.current_image_num].shape[
                    2
                    - self.state.view2D_image_axis_order[
                        self.state.current_image_num
                    ][2]
                ]
                - 1
            )
            slice_current = self.state.view2D_slice[
                self.state.current_image_num
            ][
                self.state.view2D_image_axis_order[
                    self.state.current_image_num
                ][2]
            ]

        self.update_gui = False

        self.view2DSliceSlider.setMaximum(slice_max)
        self.view2DSliceSlider.setValue(slice_current)
        self.view2DSliceText.setMaximum(slice_max)
        self.view2DSliceSlider.setValue(slice_current)

        self.update_gui = True

        self.update()

        self.gui.update_image()

    @time_and_log
    def create_new_image(self):
        auto_range = np.quantile(self.state.image_array[-1], [0.05, 0.99])
        self.state.view2D_intensity_window_min.append(auto_range[0])
        self.state.view2D_intensity_window_max.append(auto_range[1])

        self.state.view2D_slice.append([0, 0, 0])

        # Default flip is based on the direction of the image
        dir = np.array(self.state.image[-1].GetDirection())
        sign = np.sum(dir, axis=1)
        flip = sign < 0
        self.state.view2D_flip.append(flip)

        # Hueristic to find view plane based on z-axis of the image
        view_plane = (self.state.csa_to_image_axis[-1].index(2) + 2) % 3

        # Allocate space for axis order vars, and then update them
        self.state.view2D_csa_axis_order.append([0, 0, 0])
        self.state.view2D_image_axis_order.append([0, 0, 0])
        if view_plane == 0:
            self.update_view_plane_coronal(redraw=False)
        elif view_plane == 1:
            self.update_view_plane_sagittal(redraw=False)
        else:  # if view_plane == 2:
            self.update_view_plane_axial(redraw=False)

        # Sagittal axis is viewed in the negative direction
        # flip[self.state.view2D_csa_axis_order[-1][1]] = not flip[
        # self.state.view2D_csa_axis_order[-1][1]
        # ]
        # If coronal axis is data axis 2, then it is viewed in the negative direction
        if self.state.view2D_csa_axis_order[-1][0] == 2:
            flip[self.state.view2D_csa_axis_order[-1][0]] = not flip[
                self.state.view2D_csa_axis_order[-1][0]
            ]
        self.state.view2D_flip.append(flip)

    @time_and_log
    def update_image(self):
        slice_max = 0
        if (
            self.state.current_image_num >= 0
            and self.state.current_image_num < len(self.state.image_array)
        ):
            slice_max = (
                self.state.image_array[self.state.current_image_num].shape[
                    2
                    - self.state.view2D_image_axis_order[
                        self.state.current_image_num
                    ][2]
                ]
                - 1
            )

            auto_range = np.quantile(self.state.image_array[-1], [0.05, 0.99])
            self.state.view2D_intensity_window_min[
                self.state.current_image_num
            ] = auto_range[0]
            self.state.view2D_intensity_window_max[
                self.state.current_image_num
            ] = auto_range[1]

        self.update_gui = False

        self.view2DSliceSlider.setMinimum(0)
        self.view2DSliceSlider.setMaximum(slice_max)
        self.view2DSliceSlider.setValue(0)

        self.view2DSliceText.setMinimum(0)
        self.view2DSliceText.setMaximum(slice_max)
        self.view2DSliceText.setValue(0)

        self.update_gui = True

        self.update()

        self.vtk2DViewWidget.update_image()

    @time_and_log
    def update_overlay(self):
        if self.state.scene is None:
            return

        if self.state.current_image_num < 0:
            return

        self.state.overlay_array[self.state.current_image_num].fill(0)
        render_scene_in_overlay_array(
            self.state.scene,
            self.state.selected_ids,
            self.state.image[self.state.current_image_num],
            self.state.overlay_array[self.state.current_image_num],
        )
        self.state.overlay[self.state.current_image_num] = (
            itk.GetImageFromArray(
                self.state.overlay_array[self.state.current_image_num],
                ttype=self.state.overlay_type,
            )
        )
        self.state.overlay[self.state.current_image_num].CopyInformation(
            self.state.image[self.state.current_image_num]
        )

        self.update()

    @time_and_log
    def update_scene(self):
        self.update_overlay()

    @time_and_log
    def update_slice_from_slider(self, value):
        if not self.update_gui:
            return

        if self.state.current_image_num < 0:
            return

        current_slice = value
        if current_slice < 0:
            current_slice = 0

        view_image_axis = self.state.view2D_image_axis_order[
            self.state.current_image_num
        ][2]
        slice_max = (
            self.state.image_array[self.state.current_image_num].shape[
                2 - view_image_axis
            ]
            - 1
        )
        if current_slice > slice_max:
            current_slice = slice_max

        self.state.view2D_slice[self.state.current_image_num][
            view_image_axis
        ] = current_slice

        self.update_gui = False
        self.view2DSliceSlider.setValue(current_slice)
        self.view2DSliceText.setValue(current_slice)
        self.update_gui = True

        self.update()

    @time_and_log
    def update_slice_from_text(self, value):
        if not self.update_gui:
            return

        if self.state.current_image_num < 0:
            return

        current_slice = int(value)
        if current_slice < 0:
            current_slice = 0

        view_image_axis = self.state.view2D_image_axis_order[
            self.state.current_image_num
        ][2]
        slice_max = (
            self.state.image_array[self.state.current_image_num].shape[
                2 - view_image_axis
            ]
            - 1
        )
        if current_slice > slice_max:
            current_slice = slice_max

        self.state.view2D_slice[self.state.current_image_num][
            view_image_axis
        ] = current_slice

        self.update_gui = False
        self.view2DSliceSlider.setValue(current_slice)
        self.view2DSliceText.setValue(current_slice)
        self.update_gui = True

        self.update()

    @time_and_log
    def update_reset(self):
        self.vtk2DViewWidget.reset_camera()
        self.update_image()

    @time_and_log
    def redraw_object(self, so):
        if self.state.current_image_num < 0:
            return

        if (
            self.state.highlight_selected
            and so.GetId() in self.state.selected_ids
        ):
            render_object_in_overlay_array(
                so,
                self.state.image[self.state.current_image_num],
                self.state.overlay_array[self.state.current_image_num],
                color=[0, 255, 0, 255],
            )
        else:
            render_object_in_overlay_array(
                so,
                self.state.image[self.state.current_image_num],
                self.state.overlay_array[self.state.current_image_num],
            )
        self.state.overlay[self.state.current_image_num] = (
            itk.GetImageFromArray(
                self.state.overlay_array[self.state.current_image_num],
                ttype=self.state.overlay_type,
            )
        )
        self.state.overlay[self.state.current_image_num].CopyInformation(
            self.state.image[self.state.current_image_num]
        )
        self.update()

    @time_and_log
    def update(self):
        self.vtk2DViewWidget.update_view()
        super().update()
