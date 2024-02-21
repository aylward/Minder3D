from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCellPicker,
    vtkPolyDataMapper,
    vtkRenderer,
)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera

from soViewer3D import convert_scene_to_surfaces
from soViewerUtils import get_so_index_in_list


class SOViewer3DRenderWindowInteractor(QVTKRenderWindowInteractor):
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
            self.select_actor(
                pickedPos, pickedActor, obj.GetRenderWindow()
            )

        return 0

    def update_scene(self):
        point_data = convert_scene_to_surfaces(self.state.scene)
        for idx, so in enumerate(self.state.scene_list):
            actor = vtkActor()
            color = so.GetProperty().GetColor()
            actor.GetProperty().SetColor(color[0], color[1], color[2])
            actor.GetProperty().SetOpacity(color[3])
            form = self.state.scene_list_properties[idx]["Form"]
            color_by = self.state.scene_list_properties[idx]["ColorBy"]
            self.state.scene_list_properties[idx]["Actor"] = actor
            mapper = vtkPolyDataMapper()
            mapper.SetInputData(point_data[idx])
            if color_by == "Color":
                mapper.ScalarVisibilityOff()
            else:
                mapper.ScalarVisibilityOn()
                point_data[idx].GetPointData().SetActiveScalars(color_by)
            if form == "Points":
                actor.GetProperty().SetRepresentationToPoints()
            elif form == "Wireframe":
                actor.GetProperty().SetRepresentationToWireframe()
            else:
                actor.GetProperty().SetRepresentationToSurface()
            actor.SetMapper(mapper)
            self.scene_renderer.AddActor(actor)
        self.scene_renderer.ResetCamera()
        self.Render()
        self.GetRenderWindow().Render()

    def update_actor(self, actor, so, color=None):
        idx = get_so_index_in_list(so.GetId(), self.state.scene_list)
        form = self.state.scene_list_properties[idx]["Form"]
        color_by = self.state.scene_list_properties[idx]["ColorBy"]
        if color_by == "Color" or color is not None:
            actor.GetMapper().ScalarVisibilityOff()
            if color is None:
                color = so.GetProperty().GetColor()
            actor.GetProperty().SetColor(color[0], color[1], color[2])
            actor.GetProperty().SetOpacity(color[3])
        else:
            actor.GetMapper().ScalarVisibilityOn()
        if form == "Points":
            actor.GetProperty().SetRepresentationToPoints()
        elif form == "Wireframe":
            actor.GetProperty().SetRepresentationToWireframe()
        else:
            actor.GetProperty().SetRepresentationToSurface()
        actor.GetMapper().Update()
        actor.Modified()

    def select_actor(self, pickedPos, actor, renwin):
        """
        Private function to updated the viz of currently selected spatial objects.
        """
        if len(self.state.selected_so_actors) > 0:
            if (
                self.state.multiple_selections_enabled is False and
                not ([actor] == self.state.selected_so_actors)
            ):
                for idx,so_actor in enumerate(self.state.selected_so_actors):
                    so_id = self.state.selected_so_ids[idx]
                    so = self.state.scene_list[
                        get_so_index_in_list(so_id, self.state.scene_list)
                    ]
                    self.update_actor(so_actor, so)
                    self.state.selected_so_ids[idx] = -1
                    self.gui.update_object(so, update_2D=True, update_3D=False)
                self.state.selected_so_actors = []
                self.state.selected_so_ids = []
                self.state.selected_so_point_ids = []
            elif (
                self.state.multiple_selections_enabled is True and
                actor in self.state.selected_so_actors
            ):
                idx = self.state.selected_so_actors.index(actor)
                so_id = self.state.selected_so_ids[idx]
                so = self.state.scene_list[
                    get_so_index_in_list(so_id, self.state.scene_list)
                ]
                self.update_actor(actor, so)
                del self.state.selected_so_ids[idx]
                del self.state.selected_so_point_ids[idx]
                del self.state.selected_so_actors[idx]
                self.gui.update_object(so, update_2D=True, update_3D=False)
                actor = None
        if actor is not None:
            pos = [pickedPos[0], pickedPos[1], pickedPos[2]]
            so_poly_data = actor.GetMapper().GetInput()
            so_id = so_poly_data.GetPointData().GetScalars(
                "Id"
            ).GetTuple(0)[0]
            idx = get_so_index_in_list(so_id, self.state.scene_list)
            so = self.state.scene_list[idx]
            point = so.ClosestPointInWorldSpace(pos)
            point_id = point.GetId()
            if actor not in self.state.selected_so_actors:
                self.state.selected_so_ids.append(so_id)
                self.state.selected_so_point_ids.append(point_id)
                self.state.selected_so_actors.append(actor)
                self.update_actor(actor, so, [0, 1, 0, 1])
            self.gui.update_object(so, update_2D=True, update_3D=False)
            renwin.Render()

    def update_object(self, so):
        so_id = so.GetId()
        idx = get_so_index_in_list(so_id, self.state.scene_list)
        actor = self.state.scene_list_properties[idx]["Actor"]
        if so_id in self.state.selected_so_ids:
            self.update_actor(actor, so, [0, 1, 0, 1])
        else:
            self.update_actor(actor, so)
        self.GetRenderWindow().Render()
