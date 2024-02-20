import numpy as np

import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCellPicker,
    vtkPolyDataMapper,
    vtkRenderer,
)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from soViewer3D import convert_scene_to_surfaces
from soViewerUtils import get_so_index_in_list

from ui_tabView3D import Ui_tabView3DWidget


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
        color_by = "Color"
        form = "Surface"
        for so in self.state.scene_list:
            so.GetProperty().SetTagStringValue(str("ColorBy"), color_by)
            so.GetProperty().SetTagStringValue(str("Form"), form)
        point_data = convert_scene_to_surfaces(self.state.scene)
        for i,so in enumerate(self.state.scene_list):
            actor = vtkActor()
            color = so.GetProperty().GetColor()
            actor.GetProperty().SetColor(color[0], color[1], color[2])
            actor.GetProperty().SetOpacity(color[3])
            color_by = "Color"
            so.GetProperty().GetTagStringValue(str("ColorBy"), color_by)
            mapper = vtkPolyDataMapper()
            mapper.SetInputData(point_data[i])
            if color_by == "Color":
                mapper.ScalarVisibilityOff()
            else:
                mapper.ScalarVisibilityOn()
                point_data[i].GetPointData().SetActiveScalars(color_by)
            actor.SetMapper(mapper)
            self.scene_renderer.AddActor(actor)

        self.scene_renderer.ResetCamera()
        self.Render()
        self.GetRenderWindow().Render()

    def update_so_actor(self, actor, so):
        color_by = "Color"
        so.GetProperty().GetTagStringValue(str("ColorBy"), color_by)
        if color_by == "Color":
            actor.GetMapper().ScalarVisibilityOff()
            color = so.GetProperty().GetColor()
            actor.GetProperty().SetColor(color[0], color[1], color[2])
            actor.GetProperty().SetOpacity(color[3])
        else:
            so_actor.GetMapper().ScalarVisibilityOn()
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
                    self.update_so_actor(so_actor, so)
                self.state.selected_so_ids = []
                self.state.selected_so_point_ids = []
                self.state.selected_so_actors = []
            elif (
                self.state.multiple_selections_enabled is True and
                actor in self.state.selected_so_actors
            ):
                idx = self.state.selected_so_actors.index(actor)
                so_id = self.state.selected_so_ids[idx]
                so = self.state.scene_list[
                    get_so_index_in_list(so_id, self.state.scene_list)
                ]
                self.update_so_actor(actor, so)
                del self.state.selected_so_ids[idx]
                del self.state.selected_so_point_ids[idx]
                del self.state.selected_so_actors[idx]
                actor = None
        if actor is not None:
            pos = [pickedPos[0], pickedPos[1], pickedPos[2]]
            so_poly_data = actor.GetMapper().GetInput()
            so_id = so_poly_data.GetPointData().GetScalars(
                "Id"
            ).GetTuple(0)[0]
            so = self.state.scene_list[
                get_so_index_in_list(so_id, self.state.scene_list)
                ]
            point = so.ClosestPointInWorldSpace(pos)
            point_id = point.GetId()
            if actor not in self.state.selected_so_actors:
                self.state.selected_so_ids.append(so_id)
                self.state.selected_so_point_ids.append(point_id)
                self.state.selected_so_actors.append(actor)
                actor.GetMapper().ScalarVisibilityOff()
                actor.GetProperty().SetColor(0, 1, 0)
                actor.GetMapper().Update()
                actor.Modified()
            self.gui.tabView3D.update_current_object()
            renwin.Render()


class TabView3DWidget(QWidget, Ui_tabView3DWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.vtk3DViewWidget = View3DRenderWindowInteractor(gui, state, self)
        self.view3DLayout.addWidget(self.vtk3DViewWidget)
        #self.vtk3DViewWidget.AddObserver('LeftButtonPressEvent', DummyFunc1, 1.0)

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.vtk3DViewWidget.close()

    def initialize(self):
        self.vtk3DViewWidget.Initialize()

    def update_image(self):
        print("Updating 3D image")
        #self.update()

    def update_scene(self):
        self.vtk3DViewWidget.update_scene()
        self.gui.objectComboBox.clear()
        for so in self.state.scene_list:
            self.gui.objectComboBox.addItem(f"{so.GetTypeName()} {so.GetId()}")

    def update_current_object(self):
        print("Updating 3D current object")
        so_id = self.state.selected_so_ids[-1]
        point_id = self.state.selected_so_point_ids[-1]
        so = self.state.scene_list[
            get_so_index_in_list(so_id, self.state.scene_list)
        ]
        so_size = so.GetNumberOfPoints()
        point = so.GetPoint(point_id)
        point_pos = point.GetPositionInWorldSpace()
        print("Selected object: ")
        print("  SO id: ", so_id)
        print("  SO size: ", so_size)
        print("    Point id: ", point_id)
        print("    Point position: ", point_pos)
        if so.GetTypeName() == "Tube":
            point_radius = point.GetRadiusInWorldSpace()
            print("    Point radius: ", point_radius)
        print("", flush=True)
        print("", flush=True)

    def update(self):
        print("Updating 3D view")
        # redraw image slice
