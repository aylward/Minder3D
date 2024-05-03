import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from sovUtils import time_and_log
from ui_sovVisualizationPanelWidget import Ui_VisualizationPanelWidget


class VisualizationPanelWidget(QWidget, Ui_VisualizationPanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.update_gui = True

        self.vizUpdate2DOverlayButton.pressed.connect(self.update_2D_overlay)

        self.vizView2DFlipXCheckBox.stateChanged.connect(self.update_flip_x)
        self.vizView2DFlipYCheckBox.stateChanged.connect(self.update_flip_y)
        self.vizView2DFlipZCheckBox.stateChanged.connect(self.update_flip_z)

        self.vizUpdate3DSceneButton.pressed.connect(self.update_3D_scene)

        self.vizAutoUpdate2DOverlayCheckBox.stateChanged.connect(
            self.auto_update_2D_overlay
        )

        self.vizAutoUpdate3DSceneCheckBox.stateChanged.connect(
            self.auto_update_3D_scene
        )

    def update_2D_overlay(self):
        self.gui.view2DPanel.update_overlay()

    def update_3D_scene(self):
        self.gui.view3DPanel.update_scene()

    def auto_update_2D_overlay(self, value):
        self.state.view2D_overlay_auto_update = value
        if self.state.view2D_overlay_auto_update:
            self.update_2D_overlay()

    def auto_update_3D_scene(self, value):
        self.state.view3D_scene_auto_update = value
        if self.state.view3D_scene_auto_update:
            self.update_3D_scene()

    @time_and_log
    def update_flip_x(self, value):
        if self.update_gui == False:
            return

        self.state.view2D_flip[self.state.current_image_num][0] = not (
            value == 0
        )
        self.gui.view2DPanel.update()

    @time_and_log
    def update_flip_y(self, value):
        if self.update_gui == False:
            return

        self.state.view2D_flip[self.state.current_image_num][1] = not (
            value == 0
        )
        self.gui.view2DPanel.update()

    @time_and_log
    def update_flip_z(self, value):
        if self.update_gui == False:
            return

        self.state.view2D_flip[self.state.current_image_num][2] = not (
            value == 0
        )
        self.gui.view2DPanel.update()

    @time_and_log
    def update_view2D(self):
        if self.update_gui == False:
            return

        self.update_gui = False
        self.vizView2DFlipXCheckBox.setChecked(
            self.state.view2D_flip[self.state.current_image_num][0]
        )
        self.vizView2DFlipYCheckBox.setChecked(
            self.state.view2D_flip[self.state.current_image_num][1]
        )
        self.vizView2DFlipZCheckBox.setChecked(
            self.state.view2D_flip[self.state.current_image_num][2]
        )
        self.update_gui = True

    @time_and_log
    def update_image(self):
        self.update_view2D()
