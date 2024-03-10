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
    def update_overlay_opacity(self):
        self.state.overlay_opacity = self.view2DOverlayOpacitySlider.value() / 100.0
        self.update()

    @time_and_log
    def update_axis_xy(self):
        if not self.update_gui:
            return

        self.state.view_axis = 2

        self.update_gui = False

        self.view2DSliceSlider.setMaximum(
            self.state.image_array.shape[2-self.state.view_axis]-1
        )
        self.view2DSliceSlider.setValue(
            self.state.view_slice[self.state.view_axis]
        )
        self.view2DSliceText.setPlainText(
            f"{self.state.view_slice[self.state.view_axis]}"
        )
        self.view2DFlipXCheckBox.setChecked(self.state.view_flip[0])
        self.view2DFlipXCheckBox.setText("Flip X")
        self.view2DFlipYCheckBox.setChecked(self.state.view_flip[1])
        self.view2DFlipYCheckBox.setText("Flip Y")

        self.update_gui = True

        self.update()
        self.vtk2DViewWidget.reset_camera()

    @time_and_log
    def update_axis_xz(self):
        if not self.update_gui:
            return

        self.state.view_axis = 1

        self.update_gui = False

        self.view2DSliceSlider.setMaximum(
            self.state.image_array.shape[2-self.state.view_axis]-1
        )
        self.view2DSliceSlider.setValue(
            self.state.view_slice[self.state.view_axis]
        )
        self.view2DSliceText.setPlainText(
            f"{self.state.view_slice[self.state.view_axis]}"
        )
        self.view2DFlipXCheckBox.setChecked(self.state.view_flip[0])
        self.view2DFlipXCheckBox.setText("Flip X")
        self.view2DFlipYCheckBox.setChecked(self.state.view_flip[2])
        self.view2DFlipYCheckBox.setText("Flip Z")

        self.update_gui = True

        self.update()
        self.vtk2DViewWidget.reset_camera()

    @time_and_log
    def update_axis_yz(self):
        if not self.update_gui:
            return

        self.state.view_axis = 0

        self.update_gui = False

        self.view2DSliceSlider.setMaximum(
            self.state.image_array.shape[2-self.state.view_axis]-1
        )
        self.view2DSliceSlider.setValue(
            self.state.view_slice[self.state.view_axis]
        )
        self.view2DSliceText.setPlainText(
            f"{self.state.view_slice[self.state.view_axis]}"
        )
        self.view2DFlipXCheckBox.setChecked(self.state.view_flip[1])
        self.view2DFlipXCheckBox.setText("Flip Y")
        self.view2DFlipYCheckBox.setChecked(self.state.view_flip[2])
        self.view2DFlipYCheckBox.setText("Flip Z")

        self.update_gui = True

        self.update()
        self.vtk2DViewWidget.reset_camera()

    @time_and_log
    def update_flip_x(self):
        if not self.update_gui:
            return

        self.state.view_flip[(self.state.view_axis+1)%3] = self.view2DFlipXCheckBox.isChecked()
        self.update()

    @time_and_log
    def update_flip_y(self):
        if not self.update_gui:
            return

        self.state.view_flip[(self.state.view_axis+2)%3] = self.view2DFlipYCheckBox.isChecked()
        self.update()
        
    @time_and_log
    def update_view_image_num(self):
        if not self.update_gui:
            return

        self.state.view_image_num = self.view2DViewImageComboBox.currentIndex()

        self.update_gui = False

        if self.state.view_image_num == 0:
            self.view2DSliceSlider.setMaximum(
                self.state.loaded_image_array.shape[2-self.state.view_axis]-1
            )
        else:
            self.view2DSliceSlider.setMaximum(
                self.state.image_array.shape[2-self.state.view_axis]-1
            )

        self.update_gui = True

        self.update()

    @time_and_log
    def update_image(self):
        if not self.update_gui:
            return

        self.update_gui = False

        self.view2DSliceSlider.setMinimum(0)
        if self.state.view_image_num == 0:
            self.view2DSliceSlider.setMaximum(
                self.state.loaded_image_array.shape[2-self.state.view_axis]-1
            )
        else:
            self.view2DSliceSlider.setMaximum(
                self.state.image_array.shape[2-self.state.view_axis]-1
            )

        self.view2DSliceSlider.setValue(0)
        self.view2DSliceText.setPlainText("0")

        self.state.view_slice = [0, 0, 0]
        self.state.view_axis = 2

        self.vtk2DViewWidget.update_image()

        self.update_gui = True

    @time_and_log
    def update_overlay(self):
        if not self.update_gui:
            return

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

    @time_and_log
    def update_scene(self):
        if not self.update_gui:
            return

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

    @time_and_log
    def update_slice_from_slider(self, value):
        if not self.update_gui:
            return

        if (value != self.state.view_slice[self.state.view_axis]):
            self.state.view_slice[self.state.view_axis] = value
            update_slider = False
            if self.state.view_slice[self.state.view_axis] < 0:
                self.state.view_slice[self.state.view_axis] = 0
                update_slider = True
            if self.state.view_slice[self.state.view_axis] >= self.state.image_array.shape[
                2-self.state.view_axis
            ]:
                self.state.view_slice[self.state.view_axis] = self.state.image_array.shape[
                    2-self.state.view_axis
                ]-1
                update_slider = True

            self.update_gui = False
            if update_slider:
                self.view2DSliceSlider.setValue(self.state.view_slice[self.state.view_axis])
            self.view2DSliceText.setPlainText(f"{self.state.view_slice[self.state.view_axis]}")
            self.update_gui = True

            self.update()

    @time_and_log
    def update_slice_from_text(self):
        if not self.update_gui:
            return

        if int(self.view2DSliceText.toPlainText()) != self.state.view_slice[self.state.view_axis]:
            self.state.view_slice[self.state.view_axis] = int(self.view2DSliceText.toPlainText())
            update_text = False
            if self.state.view_slice[self.state.view_axis] < 0:
                self.state.view_slice[self.state.view_axis] = 0
                update_text = True
            if self.state.view_slice[self.state.view_axis] >= self.state.image_array.shape[
                2-self.state.view_axis
            ]:
                self.state.view_slice[self.state.view_axis] = self.state.image_array.shape[
                    2-self.state.view_axis
                ]-1
                update_text = True

            self.update_gui = False
            if update_text:
                self.view2DSliceText.setPlainText(f"{self.state.view_slice[self.state.view_axis]}")
            self.view2DSliceSlider.setValue(self.state.view_slice[self.state.view_axis])
            self.update_gui = True

            self.update()

    @time_and_log
    def redraw_object(self, so):
        if not self.update_gui:
            return

        if self.state.highlight_selected and so.GetId() in self.state.selected_ids:
            render_object_in_overlay_array(
                so,
                self.state.image,
                self.state.overlay_array,
                color=[0, 255, 0, 255],
            )
        else:
            render_object_in_overlay_array(
                so,
                self.state.image,
                self.state.overlay_array
            )
        self.state.overlay = itk.GetImageFromArray(
            self.state.overlay_array,
            ttype=self.state.overlay_type,
        )
        self.state.overlay.CopyInformation(self.state.image)
        self.update()

    @time_and_log
    def update(self):
        if not self.update_gui:
            return

        self.vtk2DViewWidget.update_view()
        super().update()
