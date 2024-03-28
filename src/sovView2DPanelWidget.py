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

        self.view2DFlipXCheckBox.stateChanged.connect(self.update_flip_x)
        self.view2DFlipYCheckBox.stateChanged.connect(self.update_flip_y)

        self.view2DViewImageComboBox.currentIndexChanged.connect(self.update_view_image_num)

        self.update_gui = True

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.vtk2DViewWidget.close()

    @time_and_log
    def initialize(self):
        self.vtk2DViewWidget.Initialize()

    @time_and_log
    def update_overlay_opacity(self, value):
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
        self.view2DFlipXCheckBox.setChecked(self.state.view2D_flip[self.state.current_image_num][0])
        self.view2DFlipXCheckBox.setText("Flip X")
        self.view2DFlipYCheckBox.setChecked(self.state.view2D_flip[self.state.current_image_num][1])
        self.view2DFlipYCheckBox.setText("Flip Y")

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
        self.view2DFlipXCheckBox.setChecked(self.state.view2D_flip[self.state.current_image_num][0])
        self.view2DFlipXCheckBox.setText("Flip X")
        self.view2DFlipYCheckBox.setChecked(self.state.view2D_flip[self.state.current_image_num][2])
        self.view2DFlipYCheckBox.setText("Flip Z")

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
        self.view2DFlipXCheckBox.setChecked(self.state.view2D_flip[self.state.current_image_num][1])
        self.view2DFlipXCheckBox.setText("Flip Y")
        self.view2DFlipYCheckBox.setChecked(self.state.view2D_flip[self.state.current_image_num][2])
        self.view2DFlipYCheckBox.setText("Flip Z")

        self.update_gui = True

        self.update()
        self.vtk2DViewWidget.reset_camera()

    @time_and_log
    def update_flip_x(self, value):
        if not self.update_gui:
            return

        self.state.view2D_flip[self.state.current_image_num][(self.state.view2D_axis[self.state.current_image_num]+1)%3] = value
        self.update()

    @time_and_log
    def update_flip_y(self, value):
        if not self.update_gui:
            return

        self.state.view2D_flip[self.state.current_image_num][(self.state.view2D_axis[self.state.current_image_num]+2)%3] = value
        self.update()
        
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

        img_name = os.path.splitext(self.state.image_filename[-1])
        if img_name[1] == ".mha":
            self.state.view2D_flip.append([False, True, False])
        else:
            self.state.view2D_flip.append([False, False, False])

        self.update_gui = False
        self.view2DViewImageComboBox.addItem(f"{img_name[0]}")
        self.view2DViewImageComboBox.setCurrentIndex(len(self.state.image)-1)
        self.update_gui = True

    @time_and_log
    def update_image(self):
        if not self.update_gui:
            return

        self.update_gui = False

        self.view2DSliceSlider.setMinimum(0)
        self.view2DSliceSlider.setMaximum(
            self.state.image_array[self.state.current_image_num].shape[2-self.state.view2D_axis[self.state.current_image_num]]-1
        )

        self.view2DSliceSlider.setValue(0)
        self.view2DSliceText.setPlainText("0")

        self.state.view2D_slice[self.state.current_image_num] = [0, 0, 0]
        self.state.view2D_axis[self.state.current_image_num] = 2

        self.state.view2D_intensity_window_min[self.state.current_image_num] = self.state.image_min[self.state.current_image_num]
        self.state.view2D_intensity_window_max[self.state.current_image_num] = self.state.image_max[self.state.current_image_num]

        self.vtk2DViewWidget.update_image()

        self.update_gui = True

    @time_and_log
    def update_overlay(self):
        if not self.update_gui:
            return

        if self.state.scene is not None:
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
        if not self.update_gui:
            return

        self.update_overlay()

    @time_and_log
    def update_slice_from_slider(self, value):
        if not self.update_gui:
            return

        current_slice = self.state.view2D_slice[self.state.current_image_num][self.state.view2D_axis[self.state.current_image_num]]
        if (value != current_slice):
            current_slice = value
            update_slider = False
            if current_slice < 0:
                current_slice = 0
                update_slider = True
            max_slice = self.state.image_array[self.state.current_image_num].shape[
                2-self.state.view2D_axis[self.state.current_image_num]]-1
            if current_slice > max_slice:
                current_slice = max_slice
                update_slider = True

            self.state.view2D_slice[self.state.current_image_num][
                self.state.view2D_axis[self.state.current_image_num]] = current_slice

            self.update_gui = False
            if update_slider:
                self.view2DSliceSlider.setValue(current_slice)
            self.view2DSliceText.setPlainText(f"{current_slice}")
            self.update_gui = True

            self.update()

    @time_and_log
    def update_slice_from_text(self):
        if not self.update_gui:
            return

        current_slice = self.state.view2D_slice[self.state.current_image_num][self.state.view2D_axis[self.state.current_image_num]]
        if int(self.view2DSliceText.toPlainText()) != current_slice:
            current_slice = int(self.view2DSliceText.toPlainText())
            update_text = False
            if current_slice < 0:
                current_slice = 0
                update_text = True
            max_slice = self.state.image_array[self.state.current_image_num].shape[
                2-self.state.view2D_axis[self.state.current_image_num]]-1
            if current_slice > max_slice:
                current_slice = max_slice
                update_text = True

            self.state.view2D_slice[self.state.current_image_num][self.state.view2D_axis[self.state.current_image_num]] = current_slice

            self.update_gui = False
            if update_text:
                self.view2DSliceText.setPlainText(f"{current_slice}")
            self.view2DSliceSlider.setValue(current_slice)
            self.update_gui = True

            self.update()

    @time_and_log
    def redraw_object(self, so):
        if not self.update_gui:
            return

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
        if not self.update_gui:
            return

        self.vtk2DViewWidget.update_view()
        super().update()
