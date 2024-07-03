import itk
from vtkmodules.vtkCommonCore import vtkDoubleArray, vtkPoints
from vtkmodules.vtkCommonDataModel import vtkCellArray, vtkPolyData, vtkPolyLine
from vtkmodules.vtkFiltersCore import vtkSurfaceNets3D, vtkTubeFilter

from .sovUtils import get_children_as_list, time_and_log


@time_and_log
def convert_tubes_to_polylines(tube_list):
    """Convert a list of tubes to polylines.

    This function takes a list of tubes and converts them into polylines by extracting various properties of the tubes
    such as points, radius, color, ridgeness, medialness, branchness, curvature, intensity, roundness, levelness,
    alpha1, alpha2, and alpha3.

    Args:
        tube_list (list): A list of tubes to be converted to polylines.

    Returns:
        list: A list of vtkPolyData objects representing the converted polylines.
    """

    tube_polylines = []

    for tube in tube_list:
        tube.Update()
        tube.RemoveDuplicatePointsInObjectSpace()
        tube.ComputeTangentsAndNormals()

        tube_num_points = tube.GetNumberOfPoints()

        data_point = vtkPoints()
        data_point.SetNumberOfPoints(tube_num_points)

        data_radius = vtkDoubleArray()
        data_radius.SetName('Radius')
        data_radius.SetNumberOfTuples(tube_num_points)

        data_id = vtkDoubleArray()
        data_id.SetName('Id')
        data_id.SetNumberOfTuples(tube_num_points)
        data_id.Fill(tube.GetId())

        data_color = vtkDoubleArray()
        data_color.SetName('Color')
        data_color.SetNumberOfComponents(4)
        data_color.SetNumberOfTuples(tube_num_points)

        data_a1 = vtkDoubleArray()
        data_a1.SetName('Alpha1')
        data_a1.SetNumberOfTuples(tube_num_points)

        data_a2 = vtkDoubleArray()
        data_a2.SetName('Alpha2')
        data_a2.SetNumberOfTuples(tube_num_points)

        data_a3 = vtkDoubleArray()
        data_a3.SetName('Alpha3')
        data_a3.SetNumberOfTuples(tube_num_points)

        data_ridgeness = vtkDoubleArray()
        data_ridgeness.SetName('Ridgeness')
        data_ridgeness.SetNumberOfTuples(tube_num_points)

        data_medialness = vtkDoubleArray()
        data_medialness.SetName('Medialness')
        data_medialness.SetNumberOfTuples(tube_num_points)

        data_branchness = vtkDoubleArray()
        data_branchness.SetName('Branchness')
        data_branchness.SetNumberOfTuples(tube_num_points)

        data_intensity = vtkDoubleArray()
        data_intensity.SetName('Intensity')
        data_intensity.SetNumberOfTuples(tube_num_points)

        data_curvature = vtkDoubleArray()
        data_curvature.SetName('Curvature')
        data_curvature.SetNumberOfTuples(tube_num_points)

        data_roundness = vtkDoubleArray()
        data_roundness.SetName('Roundness')
        data_roundness.SetNumberOfTuples(tube_num_points)

        data_levelness = vtkDoubleArray()
        data_levelness.SetName('Levelness')
        data_levelness.SetNumberOfTuples(tube_num_points)

        tube_line = vtkPolyLine()
        tube_line.GetPointIds().SetNumberOfIds(tube_num_points)
        for point_num, point in enumerate(tube.GetPoints()):
            tube_line.GetPointIds().SetId(point_num, point_num)
            data_point.SetPoint(point_num, *point.GetPositionInWorldSpace())

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

        tube_polylines[-1].GetPointData().SetActiveScalars('Radius')

    return tube_polylines


@time_and_log
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


@time_and_log
def convert_masks_to_surfaces(mask_list):
    """Convert a list of masks to surfaces.

    This function takes a list of masks and converts them to surfaces using VTK SurfaceNets3D algorithm.

    Args:
        mask_list (list): A list of itk.Image objects representing masks.

    Returns:
        list: A list of VTK surfaces representing the converted masks.
    """

    num_masks = len(mask_list)
    mask_surfaces = []
    if num_masks > 0:
        for mask in mask_list:
            vtkmask = itk.vtk_image_from_image(mask.GetImage())
            SN = vtkSurfaceNets3D()
            SN.SetInputData(vtkmask)
            mask_id = mask.GetMaskValue()
            SN.SetLabel(0, mask_id)
            SN.Update()
            SN.DeleteSelectedLabel(0)
            mask_surfaces.append(SN.GetOutput())
            data_id = vtkDoubleArray()
            data_id.SetName('Id')
            data_id.SetNumberOfTuples(mask_surfaces[-1].GetNumberOfPoints())
            data_id.Fill(mask.GetId())
            mask_surfaces[-1].GetPointData().AddArray(data_id)

    return mask_surfaces


@time_and_log
def convert_scene_to_surfaces(scene):
    """Convert the given scene into a list of surfaces.

    This function takes a scene as input and converts the tubes and masks within the scene into surfaces. It first retrieves the tubes and masks from the scene and then converts them to surfaces.

    Args:
        scene (object): The scene object containing tubes and masks.

    Returns:
        list: A list of surfaces extracted from the tubes and masks in the scene.
    """

    surfaces = []
    tube_list = get_children_as_list(scene, 'Tube')
    if len(tube_list) > 0:
        surfaces = surfaces + convert_tubes_to_surfaces(tube_list)
    mask_list = get_children_as_list(scene, 'Mask')
    if len(mask_list) > 0:
        surfaces = surfaces + convert_masks_to_surfaces(mask_list)
    return surfaces


@time_and_log
def get_object_forms(obj):
    """Get the forms available for the given object type.

    This function checks the type of the input object and returns the available forms based on the object type.

    Args:
        obj: The input object for which forms are to be retrieved.

    Returns:
        list: A list of available forms for the input object type.
    """

    if 'Tube' in obj.GetTypeName():
        forms = ['Surface', 'Wireframe', 'Points']
    elif 'Mask' in obj.GetTypeName():
        forms = ['Surface', 'Wireframe', 'Points']
    return forms


@time_and_log
def get_closest_point_in_world_space(so, pos):
    """Get the closest point in world space to the given position.

    This function takes a spatial object and a position as input and returns the closest point in world space to the given position.

    Args:
        so (SpatialObject): A spatial object.
        pos (list): A list representing the position in world space.

    Returns:
        SpatialObjectPoint: The closest point in world space to the given position.
    """

    if so.GetTypeName() == 'TubeSpatialObject':
        return so.ClosestPointInWorldSpace(pos)

    if so.GetTypeName() == 'MaskImageSpatialObject':
        for offset in range(0, 5):
            for xs in range(-1, 1):
                for ys in range(-1, 1):
                    for zs in range(-1, 1):
                        pnt = [
                            pos[0] + xs * offset,
                            pos[1] + ys * offset,
                            pos[2] + zs * offset,
                        ]
                        indx = so.GetImage().TransformPhysicalPointToIndex(pnt)
                        if so.GetImage().GetPixel(indx) > 0:
                            point = itk.SpatialObjectPoint[3]()
                            point.SetPositionInObjectSpace(pnt)
                            point.SetId(
                                indx[0]
                                + indx[1]
                                * so.GetImage()
                                .GetLargestPossibleRegion()
                                .GetSize()[0]
                                + indx[2]
                                * so.GetImage()
                                .GetLargestPossibleRegion()
                                .GetSize()[0]
                                * so.GetImage()
                                .GetLargestPossibleRegion()
                                .GetSize()[1]
                            )
                            return point

    point = itk.SpatialObjectPoint[3]()
    point.SetPositionInObjectSpace(pos)
    point.SetId(0)
    return point
