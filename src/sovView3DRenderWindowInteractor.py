from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCellPicker,
    vtkPolyDataMapper,
    vtkRenderer,
)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera

from sovView3DUtils import convert_scene_to_surfaces
from sovUtils import (
    get_tag_value_index_in_list_of_dict
)


class View3DRenderWindowInteractor(QVTKRenderWindowInteractor):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)

        self.gui = gui
        self.state = state

        self.scene_renderer = vtkRenderer()
        self.GetRenderWindow().AddRenderer(self.scene_renderer)

        self.SetInteractorStyle(
            vtkInteractorStyleTrackballCamera()
        )

        self.AddObserver(
            "LeftButtonPressEvent", self._leftButtonPressEvent
        )

    def _leftButtonPressEvent(self, obj, event):
        print("3dw _leftButtonPressEvent")
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
                #obj.GetRenderWindow()

        return 0

    def reset_camera(self):
        print("3dw reset_camera")
        self.scene_renderer.ResetCamera()
        self.Render()
        self.GetRenderWindow().Render()

    def update_scene(self):
        print("3dw update_scene")
        point_data = convert_scene_to_surfaces(self.state.scene)
        for scene_idx, so in enumerate(self.state.scene_list):
            actor = vtkActor()
            color = so.GetProperty().GetColor()
            actor.GetProperty().SetColor(color[0], color[1], color[2])
            actor.GetProperty().SetOpacity(color[3])
            color_by = self.state.scene_list_properties[scene_idx]["ColorBy"]
            self.state.scene_list_properties[scene_idx]["Actor"] = actor
            mapper = vtkPolyDataMapper()
            mapper.SetInputData(point_data[scene_idx])
            if color_by == "Solid Color":
                mapper.ScalarVisibilityOff()
            else:
                point_data[scene_idx].GetPointData().SetActiveScalars(color_by)
                mapper.ScalarVisibilityOn()
            actor.SetMapper(mapper)
            self.scene_renderer.AddActor(actor)
        self.scene_renderer.ResetCamera()
        self.Render()
        self.GetRenderWindow().Render()

    def redraw_actor(self, actor, so, color=None):
        print("3dw redraw_actor")
        if actor is None or so is None:
            print("ERROR: redraw_actor: actor or so is None")
            return
        scene_idx = self.state.scene_list_ids.index(so.GetId())
        color_by = self.state.scene_list_properties[scene_idx]["ColorBy"]
        if color_by == "Solid Color" or color is not None:
            actor.GetMapper().ScalarVisibilityOff()
            if color is None:
                color = so.GetProperty().GetColor()
            actor.GetProperty().SetColor(color[0], color[1], color[2])
            actor.GetProperty().SetOpacity(color[3])
        else:
            actor.GetMapper().GetInput().GetPointData().SetActiveScalars(color_by)
            actor.GetMapper().ScalarVisibilityOn()
        actor.GetMapper().Update()
        actor.Modified()

    def select_actor(self, pickedPos, actor):
        """
        Private function to updated the viz of currently selected spatial objects.
        """
        print("3dw select_actor")
        if len(self.state.selected_ids) > 0:
            scene_idx = get_tag_value_index_in_list_of_dict("Actor", actor, self.state.scene_list_properties)
            so = self.state.scene_list[scene_idx]
            so_id = so.GetId()
            if (
                self.state.multiple_selections_enabled is False and
                not([so_id] == self.state.selected_ids)
            ):
                # Unselected already selected objects
                for selected_idx, selected_id in enumerate(self.state.selected_ids):
                    if selected_id != -1:
                        selected_scene_idx = self.state.scene_list_ids.index(selected_id)
                        selected_so = self.state.scene_list[selected_scene_idx]
                        selected_so_actor = self.state.scene_list_properties[selected_scene_idx].get("Actor")
                        self.state.selected_ids[selected_idx] = -1
                        self.redraw_actor(selected_so_actor, selected_so)
                        self.gui.redraw_object(selected_so, update_2D=True, update_3D=False)
                self.state.selected_ids = []
                self.state.selected_point_ids = []
            elif (
                self.state.multiple_selections_enabled is True and
                so_id in self.state.selected_ids
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
            so_id = so_poly_data.GetPointData().GetScalars(
                "Id"
            ).GetTuple(0)[0]
            scene_idx = self.state.scene_list_ids.index(so_id)
            so = self.state.scene_list[scene_idx]
            point = so.ClosestPointInWorldSpace(pos)
            point_id = point.GetId()
            if so_id not in self.state.selected_ids:
                self.state.selected_ids.append(so_id)
                self.state.selected_point_ids.append(point_id)
                if self.state.highlight_selected:
                    self.redraw_actor(actor, so, [0, 1, 0, 1])
                    self.gui.redraw_object(so, update_2D=True, update_3D=False)
        self.GetRenderWindow().Render()

    def redraw_object(self, so):
        print("3dw redraw_object")
        so_id = so.GetId()
        scene_idx = self.state.scene_list_ids.index(so_id)
        actor = self.state.scene_list_properties[scene_idx].get("Actor")
        if self.state.highlight_selected and so_id in self.state.selected_ids:
            self.redraw_actor(actor, so, [0, 1, 0, 1])
        else:
            self.redraw_actor(actor, so)
        self.GetRenderWindow().Render()
