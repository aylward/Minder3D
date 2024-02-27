import itk

from PySide6.QtWidgets import QWidget

from sovView2DUtils import (
    render_scene_in_overlay_array,
    render_object_in_overlay_array,
)

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

        self.view2DFlipXCheckBox.stateChanged.connect(self.update_flip)
        self.view2DFlipYCheckBox.stateChanged.connect(self.update_flip)

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
        self.vtk2DViewWidget.reset_camera()

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
        self.vtk2DViewWidget.reset_camera()

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
        self.vtk2DViewWidget.reset_camera()

    def update_flip(self):
        self.state.image_flip_x = self.view2DFlipXCheckBox.isChecked()
        self.state.image_flip_y = self.view2DFlipYCheckBox.isChecked()
        self.update()
        
    def update_image(self):
        print("2d update_image")
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
        print("2d update_overlay")
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
        print("2d update_scene")
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
        print("2d update_slice_from_slider")
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
        print("2d update_slice_from_text")
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

    def redraw_object(self, so):
        print("2d redraw_object")
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

    def update(self):
        print("2d update")
        self.vtk2DViewWidget.update_view()
