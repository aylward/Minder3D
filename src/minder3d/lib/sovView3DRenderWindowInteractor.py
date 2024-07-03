from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCellPicker,
    vtkPolyDataMapper,
    vtkRenderer,
)

from .sovUtils import get_tag_value_index_in_list_of_dict, time_and_log
from .sovView3DUtils import (
    convert_scene_to_surfaces,
    get_closest_point_in_world_space,
)


class View3DRenderWindowInteractor(QVTKRenderWindowInteractor):
    def __init__(self, gui, state, parent=None):
        """Initialize the class with the provided GUI and state.

        Args:
            gui: The GUI object.
            state: The state object.
            parent: The parent object (default is None).
        """

        super().__init__(parent)

        self.gui = gui
        self.state = state

        self.scene_renderer = vtkRenderer()
        self.GetRenderWindow().AddRenderer(self.scene_renderer)

        self.SetInteractorStyle(vtkInteractorStyleTrackballCamera())

        self.AddObserver('LeftButtonPressEvent', self._leftButtonPressEvent)

    @time_and_log
    def _leftButtonPressEvent(self, obj, event):
        clickPos = obj.GetEventPosition()

        picker = vtkCellPicker()
        picker.SetTolerance(0.0005)
        picker.Pick(
            clickPos[0],
            clickPos[1],
            0,
            self.scene_renderer,
        )
        pickedActor = picker.GetActor()
        pickedPos = picker.GetPickPosition()

        self.state.multiple_selections_enabled = bool(obj.GetShiftKey())
        if pickedActor is not None:
            self.select_actor(pickedPos, pickedActor)
            # obj.GetRenderWindow()

        return 0

    @time_and_log
    def reset_camera(self):
        self.scene_renderer.ResetCamera()
        camera = self.scene_renderer.GetActiveCamera()
        camera.SetViewUp(0, -1, 0)
        self.Render()
        self.GetRenderWindow().Render()

    @time_and_log
    def update_scene(self):
        """Update the scene with the latest changes.

        This function updates the scene by converting the scene to surfaces, removing all view props, and then adding actors
        for each scene in the scene list based on the scene properties.

        Args:
            self: The object instance.
        """

        point_data = convert_scene_to_surfaces(self.state.scene)
        self.scene_renderer.RemoveAllViewProps()
        self.scene_renderer.Render()
        for scene_idx, so in enumerate(self.state.scene_list):
            actor = vtkActor()
            color_by = self.state.scene_list_properties[scene_idx]['ColorBy']
            self.state.scene_list_properties[scene_idx]['Actor'] = actor
            mapper = vtkPolyDataMapper()
            mapper.SetInputData(point_data[scene_idx])
            color = so.GetProperty().GetColor()
            selected = so.GetId() in self.state.selected_ids
            if selected and self.state.highlight_selected:
                color = [0, 1, 0, 1]
            actor.GetProperty().SetColor(color[0], color[1], color[2])
            actor.GetProperty().SetOpacity(color[3])
            if color_by == 'Solid Color':
                mapper.ScalarVisibilityOff()
            else:
                point_data[scene_idx].GetPointData().SetActiveScalars(color_by)
                mapper.ScalarVisibilityOn()
            actor.SetMapper(mapper)
            self.scene_renderer.AddActor(actor)
            self.scene_renderer.Render()
        self.reset_camera()

    @time_and_log
    def redraw_actor(self, actor, so, color=None):
        """Redraws the given actor with the specified state object and color.

        This function updates the appearance of the given actor based on the provided state object and color. It handles various conditions such as solid color, selected state, and scalar visibility.

        Args:
            self: The instance of the class.
            actor: vtkActor object to be redrawn.
            so: State object used to update the actor.
            color (list?): The color to be applied to the actor. Defaults to None.
        """

        if actor is None or so is None:
            self.gui.log('ERROR: redraw_actor: actor or so is None', 'ERROR')
            return
        so_id = so.GetId()
        scene_idx = self.state.scene_list_ids.index(so_id)
        color_by = self.state.scene_list_properties[scene_idx]['ColorBy']
        selected = so_id in self.state.selected_ids
        if (
            color_by == 'Solid Color'
            or color is not None
            or (selected and self.state.highlight_selected)
        ):
            actor.GetMapper().ScalarVisibilityOff()
            if color is None:
                if selected and self.state.highlight_selected:
                    color = [0, 1, 0, 1]
                else:
                    color = so.GetProperty().GetColor()
            actor.GetProperty().SetColor(color[0], color[1], color[2])
            actor.GetProperty().SetOpacity(color[3])
        else:
            actor.GetMapper().GetInput().GetPointData().SetActiveScalars(
                color_by
            )
            actor.GetMapper().ScalarVisibilityOn()
        actor.GetMapper().Update()
        actor.Modified()

    @time_and_log
    def select_actor(self, pickedPos, actor):
        """Private function to updated the viz of currently selected spatial objects.

        Args:
            pickedPos (list): A list containing the x, y, and z coordinates of the picked position.
            actor (object): The actor object to be selected.
        """
        if len(self.state.selected_ids) > 0:
            scene_idx = get_tag_value_index_in_list_of_dict(
                'Actor', actor, self.state.scene_list_properties
            )
            if scene_idx == -1:
                self.gui.log(
                    f"Get_tag_value_index_in_list_of_dict: 'Actor'={actor} not found in list_of_dict",
                    'ERROR',
                )
                return
            so = self.state.scene_list[scene_idx]
            so_id = so.GetId()
            if self.state.multiple_selections_enabled is False and not (
                [so_id] == self.state.selected_ids
            ):
                # Unselected already selected objects
                for selected_idx, selected_id in enumerate(
                    self.state.selected_ids
                ):
                    if selected_id != -1:
                        selected_scene_idx = self.state.scene_list_ids.index(
                            selected_id
                        )
                        selected_so = self.state.scene_list[selected_scene_idx]
                        selected_so_actor = self.state.scene_list_properties[
                            selected_scene_idx
                        ].get('Actor')
                        self.state.selected_ids[selected_idx] = -1
                        self.redraw_actor(selected_so_actor, selected_so)
                        self.gui.redraw_object(
                            selected_so, update_2D=True, update_3D=False
                        )
                self.state.selected_ids = []
                self.state.selected_point_ids = []
            elif (
                self.state.multiple_selections_enabled is True
                and so_id in self.state.selected_ids
            ):
                # Unselect the selected actor
                selected_idx = self.state.selected_ids.index(so_id)
                del self.state.selected_ids[selected_idx]
                del self.state.selected_point_ids[selected_idx]
                self.redraw_actor(actor, so)
                self.gui.redraw_object(so, update_2D=True, update_3D=False)
                actor = None
        if actor is not None:
            pos = [pickedPos[0], pickedPos[1], pickedPos[2]]
            so_poly_data = actor.GetMapper().GetInput()
            so_id = so_poly_data.GetPointData().GetScalars('Id').GetTuple(0)[0]
            scene_idx = self.state.scene_list_ids.index(so_id)
            so = self.state.scene_list[scene_idx]
            point = get_closest_point_in_world_space(so, pos)
            point_id = point.GetId()
            if so_id not in self.state.selected_ids:
                self.state.selected_ids.append(so_id)
                self.state.selected_point_ids.append(point_id)
                self.redraw_actor(actor, so)
                self.gui.redraw_object(so, update_2D=True, update_3D=False)
        self.GetRenderWindow().Render()

    @time_and_log
    def redraw_object(self, so):
        """Redraws the object in the scene.

        This function retrieves the object ID and scene index from the input object, then obtains the corresponding actor
        from the scene list properties. It then triggers a redraw of the actor and updates the render window.

        Args:
            self: The class instance.
            so: The object to be redrawn.
        """

        so_id = so.GetId()
        scene_idx = self.state.scene_list_ids.index(so_id)
        actor = self.state.scene_list_properties[scene_idx].get('Actor')
        self.redraw_actor(actor, so)
        self.GetRenderWindow().Render()
