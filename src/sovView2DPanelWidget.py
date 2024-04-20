import os

import itk

from PySide6.QtWidgets import QWidget

from sovView2DUtils import (
    render_scene_in_overlay_array,
    render_object_in_overlay_array,
)

from sovUtils import time_and_log

from ui_sovView2DPanelWidget import Ui_View2DPanelWidget

from sovView2DRenderWindowInteractor import View2DRenderWindowInteractor


class View2DPanelWidget(QWidget, Ui_View2DPanelWidget):
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

        self.view2DIntensityMinSlider.valueChanged.connect(
            self.update_intensity_min_max_sliders
        )
        self.view2DIntensityMaxSlider.valueChanged.connect(
            self.update_intensity_min_max_sliders
        )

        self.view2DIntensityMinSpinBox.valueChanged.connect(
            self.update_intensity_min_max_spin_boxes
        )
        self.view2DIntensityMaxSpinBox.valueChanged.connect(
            self.update_intensity_min_max_spin_boxes
        )

        self.view2DIntensityMinMaxResetButton.pressed.connect(
            self.update_reset_intensity_min_max
        )

        self.update_gui = True

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.vtk2DViewWidget.close()

    @time_and_log
    def initialize(self):
        self.vtk2DViewWidget.Initialize()

    @time_and_log
    def update_overlay_opacity(self, value):
        if not self.update_gui:
            return

        self.state.view2D_overlay_opacity = value / 100.0
        self.update()

    @time_and_log
    def update_axis_xy(self):
        if not self.update_gui:
            return

        self.state.view2D_axis[self.state.current_image_num] = 2

        self.update_gui = False

        self.view2DSliceSlider.setMaximum(
            self.state.image_array[self.state.current_image_num].shape[2-self.state.view2D_axis[self.state.current_image_num]]-1
        )
        self.view2DSliceSlider.setValue(
            self.state.view2D_slice[self.state.current_image_num][self.state.view2D_axis[self.state.current_image_num]]
        )
        self.view2DSliceText.setPlainText(
            f"{self.state.view2D_slice[self.state.current_image_num][self.state.view2D_axis[self.state.current_image_num]]}"
        )

        self.gui.visualizationPanel.update_view2D()

        self.update_gui = True

        self.update()
        self.vtk2DViewWidget.reset_camera()

    @time_and_log
    def update_axis_xz(self):
        if not self.update_gui:
            return

        self.state.view2D_axis[self.state.current_image_num] = 1

        self.update_gui = False

        self.view2DSliceSlider.setMaximum(
            self.state.image_array[self.state.current_image_num].shape[2-self.state.view2D_axis[self.state.current_image_num]]-1
        )
        self.view2DSliceSlider.setValue(
            self.state.view2D_slice[self.state.current_image_num][self.state.view2D_axis[self.state.current_image_num]]
        )
        self.view2DSliceText.setPlainText(
            f"{self.state.view2D_slice[self.state.current_image_num][self.state.view2D_axis[self.state.current_image_num]]}"
        )

        self.gui.visualizationPanel.update_view2D()

        self.update_gui = True

        self.update()
        self.vtk2DViewWidget.reset_camera()

    @time_and_log
    def update_axis_yz(self):
        if not self.update_gui:
            return

        self.state.view2D_axis[self.state.current_image_num] = 0

        self.update_gui = False

        self.view2DSliceSlider.setMaximum(
            self.state.image_array[self.state.current_image_num].shape[2-self.state.view2D_axis[self.state.current_image_num]]-1
        )
        self.view2DSliceSlider.setValue(
            self.state.view2D_slice[self.state.current_image_num][self.state.view2D_axis[self.state.current_image_num]]
        )
        self.view2DSliceText.setPlainText(
            f"{self.state.view2D_slice[self.state.current_image_num][self.state.view2D_axis[self.state.current_image_num]]}"
        )

        self.gui.visualizationPanel.update_view2D()

        self.update_gui = True

        self.update()
        self.vtk2DViewWidget.reset_camera()

    @time_and_log
    def update_view_image_num(self, index):
        if not self.update_gui:
            return

        self.state.current_image_num = index

        self.update_gui = False

        self.view2DSliceSlider.setMaximum(
            self.state.image_array[self.state.current_image_num].shape[2-self.state.view2D_axis[self.state.current_image_num]]-1
        )

        self.update_gui = True

        self.gui.update_image()

    @time_and_log
    def create_new_image(self):
        self.state.view2D_intensity_window_min.append(self.state.image_min[-1])
        self.state.view2D_intensity_window_max.append(self.state.image_max[-1])

        self.state.view2D_slice.append([0, 0, 0])
        self.state.view2D_axis.append(2)

        self.state.view2D_flip.append([False, False, False])



    @time_and_log
    def update_image(self):
        imin = self.state.image_min[self.state.current_image_num]
        imax = self.state.image_max[self.state.current_image_num]
        irange = imax - imin

        self.state.view2D_intensity_window_min[self.state.current_image_num] = imin
        self.state.view2D_intensity_window_max[self.state.current_image_num] = imax

        self.update_gui = False

        self.view2DSliceSlider.setMinimum(0)
        self.view2DSliceSlider.setMaximum(
            self.state.image_array[self.state.current_image_num].shape[2-self.state.view2D_axis[self.state.current_image_num]]-1
        )

        self.view2DSliceSlider.setValue(0)
        self.view2DSliceText.setPlainText("0")

        self.view2DIntensityMinSlider.setValue(0)
        self.view2DIntensityMinSpinBox.setRange(
            imin - 0.5 * irange,
            imax + 0.5 * irange
        )
        self.view2DIntensityMinSpinBox.setSingleStep(irange / 500)
        self.view2DIntensityMinSpinBox.setValue(imin)

        self.view2DIntensityMaxSlider.setValue(100)
        self.view2DIntensityMaxSpinBox.setRange(
            imin - 0.5 * irange,
            imax + 0.5 * irange
        )
        self.view2DIntensityMaxSpinBox.setSingleStep(irange / 500)
        self.view2DIntensityMaxSpinBox.setValue(imax)

        self.update_gui = True

        self.update()

        self.vtk2DViewWidget.update_image()

    @time_and_log
    def update_overlay(self):
        if self.state.scene is None:
            return

        self.state.overlay_array[self.state.current_image_num].fill(0)
        render_scene_in_overlay_array(
            self.state.scene,
            self.state.selected_ids,
            self.state.image[self.state.current_image_num],
            self.state.overlay_array[self.state.current_image_num],
        )
        self.state.overlay[self.state.current_image_num] = itk.GetImageFromArray(
            self.state.overlay_array[self.state.current_image_num],
            ttype=self.state.overlay_type,
        )
        self.state.overlay[self.state.current_image_num].CopyInformation(self.state.image[self.state.current_image_num])

        self.update()

    @time_and_log
    def update_scene(self):
        self.update_overlay()

    @time_and_log
    def update_slice_from_slider(self, value):
        if not self.update_gui:
            return

        current_slice = value
        if current_slice < 0:
            current_slice = 0
        max_slice = self.state.image_array[self.state.current_image_num].shape[
            2-self.state.view2D_axis[self.state.current_image_num]]-1
        if current_slice > max_slice:
            current_slice = max_slice

        self.state.view2D_slice[self.state.current_image_num][
            self.state.view2D_axis[self.state.current_image_num]] = current_slice

        self.update_gui = False
        self.view2DSliceSlider.setValue(current_slice)
        self.view2DSliceText.setPlainText(f"{current_slice}")
        self.update_gui = True

        self.update()

    @time_and_log
    def update_slice_from_text(self):
        if not self.update_gui:
            return

        current_slice = int(self.view2DSliceText.toPlainText())
        if current_slice < 0:
            current_slice = 0
        max_slice = self.state.image_array[self.state.current_image_num].shape[
            2-self.state.view2D_axis[self.state.current_image_num]]-1
        if current_slice > max_slice:
            current_slice = max_slice

        self.state.view2D_slice[self.state.current_image_num][self.state.view2D_axis[self.state.current_image_num]] = current_slice

        self.update_gui = False
        self.view2DSliceText.setPlainText(f"{current_slice}")
        self.view2DSliceSlider.setValue(current_slice)
        self.update_gui = True

        self.update()

    @time_and_log
    def update_intensity_min_max_sliders(self, _):
        if not self.update_gui:
            return

        minI = self.view2DIntensityMinSlider.value()
        maxI = self.view2DIntensityMaxSlider.value()

        imin = float(self.state.image_min[self.state.current_image_num])
        imax = float(self.state.image_max[self.state.current_image_num])
        irange = imax - imin
        intensityMin = (minI / 100.0) * irange + imin
        intensityMax = (maxI / 100.0) * irange + imin

        self.state.view2D_intensity_window_min[self.state.current_image_num] = intensityMin
        self.state.view2D_intensity_window_max[self.state.current_image_num] = intensityMax

        self.update_gui = False
        self.view2DIntensityMinSpinBox.setValue(intensityMin)
        self.view2DIntensityMaxSpinBox.setValue(intensityMax)
        self.update_gui = True

        self.update()

    @time_and_log
    def update_intensity_min_max_spin_boxes(self, _):
        if not self.update_gui:
            return

        intensityMin = float(self.view2DIntensityMinSpinBox.value())
        intensityMax = float(self.view2DIntensityMaxSpinBox.value())

        imin = float(self.state.image_min[self.state.current_image_num])
        imax = float(self.state.image_max[self.state.current_image_num])
        irange = imax - imin
        minI = int(((intensityMin - imin) / irange) * 100 + 0.5)
        maxI = int(((intensityMax - imin) / irange) * 100 + 0.5)

        self.state.view2D_intensity_window_min[self.state.current_image_num] = intensityMin
        self.state.view2D_intensity_window_max[self.state.current_image_num] = intensityMax

        self.update_gui = False
        self.view2DIntensityMinSlider.setValue(minI)
        self.view2DIntensityMaxSlider.setValue(maxI)
        self.update_gui = True

        self.update()

    @time_and_log
    def update_reset_intensity_min_max(self):
        self.update_image()

    @time_and_log
    def redraw_object(self, so):
        if self.state.highlight_selected and so.GetId() in self.state.selected_ids:
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
                self.state.overlay_array[self.state.current_image_num]
            )
        self.state.overlay[self.state.current_image_num] = itk.GetImageFromArray(
            self.state.overlay_array[self.state.current_image_num],
            ttype=self.state.overlay_type,
        )
        self.state.overlay[self.state.current_image_num].CopyInformation(self.state.image[self.state.current_image_num])
        self.update()

    @time_and_log
    def update(self):
        self.vtk2DViewWidget.update_view()
        super().update()
