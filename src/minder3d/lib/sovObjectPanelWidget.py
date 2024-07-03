""" """

import numpy as np
from PySide6.QtWidgets import QInputDialog, QWidget

from .sovColorMapUtils import get_nearest_color_index_and_name
from .sovUtils import get_children_as_list, time_and_log
from .ui_sovObjectPanelWidget import Ui_ObjectPanelWidget


class ObjectPanelWidget(QWidget, Ui_ObjectPanelWidget):
    @time_and_log
    def __init__(self, gui, state, parent=None):
        """Initialize the GUI and state for the application.

        Args:
            gui: The graphical user interface object.
            state: The state object for the application.
            parent: The parent widget (default is None).
        """
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.update_gui = True

        for color_name, _ in self.state.colormap.items():
            self.objectColorComboBox.addItem(color_name)

        self.objectHighlightSelectedObjectsCheckBox.stateChanged.connect(
            self.update_highlight_selected
        )

        self.objectUnselectAllButton.pressed.connect(self.unselect_all_objects)

        self.objectRenameButton.pressed.connect(self.rename_selected_object)

        self.objectDeleteButton.pressed.connect(self.delete_selected_objects)
        self.objectPropertiesToAllButton.pressed.connect(
            self.propogate_properties_to_all
        )
        self.objectPropertiesToChildrenButton.pressed.connect(
            self.propogate_properties_to_children
        )
        self.objectPropertiesToSimilarButton.pressed.connect(
            self.propogate_properties_to_similar
        )

        self.objectNameComboBox.currentIndexChanged.connect(
            self.select_object_by_name_combobox
        )

        self.objectColorByComboBox.currentIndexChanged.connect(
            self.modify_selected_objects
        )

        self.objectColorComboBox.currentIndexChanged.connect(
            self.modify_selected_objects
        )

        self.objectOpacitySlider.valueChanged.connect(
            self.modify_selected_objects
        )

    @time_and_log
    def update_scene(self):
        self.update_gui = False

        self.objectNameComboBox.clear()
        self.objectNameComboBox.addItem('None')
        for so in self.state.scene_list:
            self.objectNameComboBox.addItem(
                str(so.GetProperty().GetTagStringValue('Name'))
            )

        self.update_gui = True

    @time_and_log
    def update_highlight_selected(self, value):
        """Update the highlight selected state and redraw the selected objects.

        Args:
            value (bool): The new value for the highlight selected state.
        """
        self.state.highlight_selected = value
        for selected_id in self.state.selected_ids:
            if selected_id == -1:
                continue
            self.gui.log(f'update_highlight_selected: Id={selected_id}')
            so = self.state.scene_list[
                self.state.scene_list_ids.index(selected_id)
            ]
            self.gui.redraw_object(so)

    @time_and_log
    def unselect_all_objects(self):
        """Unselect all objects in the scene.

        This function unselects all objects in the scene by removing them
        from selected_ids and selected_point_ids.
        """
        for selected_idx, selected_so_id in enumerate(self.state.selected_ids):
            if selected_so_id != -1:
                self.state.selected_ids[selected_idx] = -1
                scene_idx = self.state.scene_list_ids.index(selected_so_id)
                selected_so = self.state.scene_list[scene_idx]
                self.gui.redraw_object(selected_so)
        self.state.selected_ids = []
        self.state.selected_point_ids = []

        self.update_gui = False

        self.objectNameComboBox.setCurrentIndex(0)

        self.update_gui = True

    @time_and_log
    def select_object_by_name_combobox(self, idx):
        if self.update_gui is False:
            return

        so = None
        so_id = -2
        if idx > 0:
            idx -= 1
            so = self.state.scene_list[idx]
            so_id = so.GetId()
        # Unselect currently selected objects
        for selected_idx, selected_so_id in enumerate(self.state.selected_ids):
            if selected_so_id != -1 and selected_so_id != so_id:
                scene_idx = self.state.scene_list_ids.index(selected_so_id)
                selected_so = self.state.scene_list[scene_idx]
                self.state.selected_ids[selected_idx] = -1
                self.gui.redraw_object(selected_so)
        if so_id != -2:
            self.state.selected_ids = [so_id]
            self.state.selected_point_ids = [0]
            self.gui.redraw_object(so)

    @time_and_log
    def redraw_object(self, so):
        """Redraws the specified object in the scene.

        This method updates the visual representation of the specified object in the 2D and 3D views if the corresponding
        update flags are set to True. It also updates the object's properties in the GUI.

        Args:
            self: The object instance.
            so: The object to be redrawn.
            update_2D (bool): Flag indicating whether to update the 2D view (default is True).
            update_3D (bool): Flag indicating whether to update the 3D view (default is True).
        """
        so_id = so.GetId()
        if so_id not in self.state.scene_list_ids:
            self.log('ERROR: so_id not in scene_list_ids', 'error')
            return
        scene_idx = self.state.scene_list_ids.index(so_id)

        self.update_gui = False

        self.objectNameComboBox.setCurrentIndex(scene_idx + 1)

        c = so.GetProperty().GetColor()
        color = [c.GetRed(), c.GetGreen(), c.GetBlue(), c.GetAlpha()]
        color[0:3] = np.array(color)[0:3] * self.state.colormap_scale_factor
        color[3] = color[3] * 100.0
        self.objectOpacitySlider.setValue(color[3])
        _, color_name = get_nearest_color_index_and_name(
            color[0:3], self.state.colormap
        )
        self.objectColorComboBox.setCurrentText(color_name)

        self.objectColorByComboBox.clear()
        self.objectColorByComboBox.addItem('Solid Color')
        actor = self.state.scene_list_properties[scene_idx].get('Actor')
        if actor is not None:
            pdata = actor.GetMapper().GetInput()
            for i in range(pdata.GetPointData().GetNumberOfArrays()):
                pname = pdata.GetPointData().GetArrayName(i)
                self.objectColorByComboBox.addItem(pname)

            self.objectColorByComboBox.setCurrentText(
                self.state.scene_list_properties[scene_idx]['ColorBy']
            )

        self.update_gui = True

    @time_and_log
    def modify_selected_objects(self, _):
        """Modify the selected objects in the scene with new color and properties.

        This function modifies the color and properties of the selected objects in the scene based on the current state
        of the application. It updates the color, opacity, and color-by property of the selected objects.

        Args:
            self: The instance of the class.
        """
        if self.update_gui is False:
            return

        for so_id in self.state.selected_ids:
            scene_idx = self.state.scene_list_ids.index(so_id)
            so = self.state.scene_list[scene_idx]
            color = np.empty(4)
            color[0:3] = self.state.colormap[
                self.objectColorComboBox.currentText()
            ]
            color[0:3] /= self.state.colormap_scale_factor
            color[3] = self.objectOpacitySlider.value() / 100.0
            so.GetProperty().SetColor(color)
            self.state.scene_list_properties[scene_idx]['ColorBy'] = (
                self.objectColorByComboBox.currentText()
            )  # fmt: skip

            self.gui.redraw_object(so)

    @time_and_log
    def rename_selected_object(self):
        """Propagate properties to similar objects in the scene.

        This function updates the properties of all objects in the scene based
        on the current settings.

        Args:
            self: The current instance of the class.
        """
        if len(self.state.selected_ids) == 0:
            return
        so_id = self.state.selected_ids[-1]
        so_name = (
            self.state.scene_list[so_id].GetProperty().GetTagStringValue('Name')
        )
        dlg = QInputDialog(self)
        dlg.setInputMode(QInputDialog.TextInput)
        dlg.setLabelText('New name:')
        dlg.resize(500, 100)
        dlg.setTextValue(so_name)
        valid = dlg.exec_()
        so_name = dlg.textValue()
        if not valid:
            return False
        self.state.scene_list[so_id].SetName(so_name)

    @time_and_log
    def delete_selected_objects(self):
        """Delete the selected objects from the scene.

        This function deletes the selected objects from the scene by removing
        them from the scene list and updating the GUI accordingly.
        """
        for so_id in self.state.selected_ids:
            if so_id == -1:
                continue
            scene_idx = self.state.scene_list_ids.index(so_id)
            so = self.state.scene_list[scene_idx]
            so_parent = so.GetParent()
            so_parent.RemoveChild(so)
            self.state.scene_list.pop(scene_idx)
            self.state.scene_list_properties.pop(scene_idx)
        self.state.selected_ids = []
        self.state.selected_point_ids = []

        self.update_gui = False

        self.objectNameComboBox.clear()
        self.objectNameComboBox.addItem('None')
        for so in self.state.scene_list:
            self.objectNameComboBox.addItem(f'{so.GetTypeName()} {so.GetId()}')

        self.update_gui = True

        self.gui.update_scene()

    @time_and_log
    def propogate_properties_to_all(self):
        """Propagate properties to all objects in the scene.

        This function updates the properties of all objects in the scene based on the current settings.

        Args:
            self: The current instance of the class.
        """
        color_by = self.objectColorByComboBox.currentText()
        color = np.empty(4)
        color[0:3] = self.state.colormap[self.objectColorComboBox.currentText()]
        color[0:3] /= self.state.colormap_scale_factor
        color[3] = self.objectOpacitySlider.value() / 100.0
        for idx in range(len(self.state.scene_list)):
            self.state.scene_list_properties[idx]['ColorBy'] = color_by
            self.state.scene_list[idx].GetProperty().SetColor(color)
            self.gui.redraw_object(self.state.scene_list[idx])

    @time_and_log
    def propogate_properties_to_similar(self):
        """Propagate properties to similar objects in the scene.

        This function updates the properties of all objects in the scene based
        on the current settings.

        Args:
            self: The current instance of the class.
        """
        if len(self.state.selected_ids) == 0:
            return
        so_id = int(self.state.selected_ids[-1])
        so_type = self.state.scene_list[so_id].GetTypeName()
        color_by = self.objectColorByComboBox.currentText()
        color = np.empty(4)
        color[0:3] = self.state.colormap[self.objectColorComboBox.currentText()]
        color[0:3] /= self.state.colormap_scale_factor
        color[3] = self.objectOpacitySlider.value() / 100.0
        for idx in range(len(self.state.scene_list)):
            if self.state.scene_list[idx].GetTypeName() == so_type:
                self.state.scene_list_properties[idx]['ColorBy'] = color_by
                self.state.scene_list[idx].GetProperty().SetColor(color)
                self.redraw_object(self.state.scene_list[idx])

    @time_and_log
    def propogate_properties_to_children(self):
        """Propagate properties to the children objects.

        This function propagates the selected properties to the children
        objects in the scene.
        """
        for so_id in self.state.selected_ids:
            scene_idx = self.state.scene_list_ids.index(so_id)
            so = self.state.scene_list[scene_idx]
            color_by = self.objectColorByComboBox.currentText()
            color = np.empty(4)
            color[0:3] = self.state.colormap[
                self.objectColorComboBox.currentText()
            ]
            color[0:3] /= self.state.colormap_scale_factor
            color[3] = self.objectOpacitySlider.value() / 100.0
            children = get_children_as_list(so)
            for child_so in children:
                idx = self.state.scene_list.index(child_so)
                self.state.scene_list_properties[idx]['ColorBy'] = color_by
                self.state.scene_list[idx].GetProperty().SetColor(color)
                self.redraw_object(child_so)
