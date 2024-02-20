from vtkmodules.vtkCommonCore import vtkDoubleArray, vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkPolyData,
    vtkPolyLine,
)
from vtkmodules.vtkFiltersCore import vtkTubeFilter

from soViewerUtils import get_children_as_list


def convert_tubes_to_polylines(tube_list):
    tube_polylines = []

    for tube in tube_list:
        tube.Update()
        tube.RemoveDuplicatePointsInObjectSpace()
        tube.ComputeTangentsAndNormals()

        tube_num_points = tube.GetNumberOfPoints()

        data_point = vtkPoints()
        data_point.SetNumberOfPoints(tube_num_points)

        data_radius = vtkDoubleArray()
        data_radius.SetName("Radius")
        data_radius.SetNumberOfTuples(tube_num_points)

        data_id = vtkDoubleArray()
        data_id.SetName("Id")
        data_id.SetNumberOfTuples(tube_num_points)

        data_color = vtkDoubleArray()
        data_color.SetName("Color")
        data_color.SetNumberOfComponents(4)
        data_color.SetNumberOfTuples(tube_num_points)

        data_a1 = vtkDoubleArray()
        data_a1.SetName("Alpha1")
        data_a1.SetNumberOfTuples(tube_num_points)

        data_a2 = vtkDoubleArray()
        data_a2.SetName("Alpha2")
        data_a2.SetNumberOfTuples(tube_num_points)

        data_a3 = vtkDoubleArray()
        data_a3.SetName("Alpha3")
        data_a3.SetNumberOfTuples(tube_num_points)

        data_ridgeness = vtkDoubleArray()
        data_ridgeness.SetName("Ridgeness")
        data_ridgeness.SetNumberOfTuples(tube_num_points)

        data_medialness = vtkDoubleArray()
        data_medialness.SetName("Medialness")
        data_medialness.SetNumberOfTuples(tube_num_points)

        data_branchness = vtkDoubleArray()
        data_branchness.SetName("Branchness")
        data_branchness.SetNumberOfTuples(tube_num_points)

        data_intensity = vtkDoubleArray()
        data_intensity.SetName("Intensity")
        data_intensity.SetNumberOfTuples(tube_num_points)

        data_curvature = vtkDoubleArray()
        data_curvature.SetName("Curvature")
        data_curvature.SetNumberOfTuples(tube_num_points)

        data_roundness = vtkDoubleArray()
        data_roundness.SetName("Roundness")
        data_roundness.SetNumberOfTuples(tube_num_points)

        data_levelness = vtkDoubleArray()
        data_levelness.SetName("Levelness")
        data_levelness.SetNumberOfTuples(tube_num_points)

        tube_line = vtkPolyLine()
        tube_line.GetPointIds().SetNumberOfIds(tube_num_points)
        for point_num, point in enumerate(tube.GetPoints()):
            tube_line.GetPointIds().SetId(point_num, point_num)
            data_point.SetPoint(point_num, *point.GetPositionInWorldSpace())

            data_id.SetTuple1(point_num, tube.GetId())
            data_radius.SetTuple1(point_num, point.GetRadiusInWorldSpace())
            data_color.SetTuple4(point_num, *point.GetColor())

            data_ridgeness.SetTuple1(point_num, point.GetRidgeness())
            data_medialness.SetTuple1(point_num, point.GetMedialness())
            data_branchness.SetTuple1(point_num, point.GetBranchness())
            data_curvature.SetTuple1(point_num, point.GetCurvature())
            data_intensity.SetTuple1(point_num, point.GetIntensity())
            data_roundness.SetTuple1(point_num, point.GetRoundness())
            data_levelness.SetTuple1(point_num, point.GetLevelness())
            data_a1.SetTuple1(point_num, point.GetAlpha1())
            data_a2.SetTuple1(point_num, point.GetAlpha2())
            data_a3.SetTuple1(point_num, point.GetAlpha3())

        tube_line_array = vtkCellArray()
        tube_line_array.InsertNextCell(tube_line)

        tube_polylines.append(vtkPolyData())
        tube_polylines[-1].SetPoints(data_point)
        tube_polylines[-1].SetLines(tube_line_array)
        tube_polylines[-1].GetPointData().AddArray(data_id)
        tube_polylines[-1].GetPointData().AddArray(data_radius)
        tube_polylines[-1].GetPointData().AddArray(data_color)
        tube_polylines[-1].GetPointData().AddArray(data_ridgeness)
        tube_polylines[-1].GetPointData().AddArray(data_medialness)
        tube_polylines[-1].GetPointData().AddArray(data_branchness)
        tube_polylines[-1].GetPointData().AddArray(data_curvature)
        tube_polylines[-1].GetPointData().AddArray(data_intensity)
        tube_polylines[-1].GetPointData().AddArray(data_roundness)
        tube_polylines[-1].GetPointData().AddArray(data_levelness)
        tube_polylines[-1].GetPointData().AddArray(data_a1)
        tube_polylines[-1].GetPointData().AddArray(data_a2)
        tube_polylines[-1].GetPointData().AddArray(data_a3)
        
        color_by = "Radius"
        tube.GetProperty().GetTagStringValue("ColorBy", color_by)
        tube_polylines[-1].GetPointData().SetActiveScalars(color_by)

    return tube_polylines


def convert_tubes_to_surfaces(tube_list, number_of_sides=5):
    num_tubes = len(tube_list)
    tube_surfaces = []
    if num_tubes > 0:
        tube_polylines = convert_tubes_to_polylines(tube_list)
        for i in range(num_tubes):
            tube_filter = vtkTubeFilter()
            tube_filter.SetVaryRadiusToVaryRadiusByAbsoluteScalar()
            tube_filter.CappingOn()
            tube_filter.SetNumberOfSides(number_of_sides)
            tube_filter.SetInputData(tube_polylines[i])
            tube_filter.Update()
            tube_surfaces.append(tube_filter.GetOutput())

    return tube_surfaces


def convert_scene_to_surfaces(scene):
    surfaces = None
    tube_list = get_children_as_list(scene, "Tube")
    if len(tube_list) > 0:
        surfaces = convert_tubes_to_surfaces(tube_list)
    return surfaces
