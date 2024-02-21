import itk

from PySide6.QtWidgets import QWidget

from soViewer2D import (
    render_scene_in_overlay_array,
    render_object_in_overlay_array,
)

from ui_tabView2D import Ui_tabView2DWidget

from soViewer2DRenderWindowInteractor import SOViewer2DRenderWindowInteractor


class TabView2DWidget(QWidget, Ui_tabView2DWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.vtk2DViewWidget = SOViewer2DRenderWindowInteractor(gui, state, self)
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

    def update_object(self, so):
        if so.GetId() in self.state.selected_so_ids:
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
