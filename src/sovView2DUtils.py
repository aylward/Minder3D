import numpy as np

import itk

from sovUtils import (
    get_children_as_list,
    time_and_log,
)


@time_and_log
def render_tube_in_overlay_array(tube, image, overlay_array, color=None):
    spacing = image.GetSpacing()
    point_list = tube.GetPoints()
    if color is None:
        color = tube.GetProperty().GetColor() * 255
    for point in point_list:
        point_pos = point.GetPositionInWorldSpace()
        point_index = image.TransformPhysicalPointToIndex(point_pos)
        point_radius = point.GetRadiusInWorldSpace()
        point_radius_index = image.TransformPhysicalPointToIndex(
            [point_pos[0]+point_radius, point_pos[1]+point_radius, point_pos[2]+point_radius]
        )
        point_radius_index = [abs(point_radius_index[i]-point_index[i]) for i in range(3)]
        rr = point_radius**2
        oMin = max(0, point_index[2]-point_radius_index[2]) - point_index[2]
        oMax = min(overlay_array.shape[0]-1, point_index[2]+point_radius_index[2]) - point_index[2]
        o2 = np.arange(oMin, oMax)
        oMin = max(0, point_index[1]-point_radius_index[1]) - point_index[1]
        oMax = min(overlay_array.shape[1]-1, point_index[1]+point_radius_index[1]) - point_index[1]
        o1 = np.arange(oMin, oMax)
        oMin = max(0, point_index[0]-point_radius_index[0]) - point_index[0]
        oMax = min(overlay_array.shape[2]-1, point_index[0]+point_radius_index[0]) - point_index[0]
        o0 = np.arange(oMin, oMax)
        mat = np.meshgrid(o0, o1, o2, indexing='ij')
        dist = (mat[2]*spacing[2])**2 + (mat[1]*spacing[1])**2 + (mat[0]*spacing[0])**2
        mask = dist <= rr
        for i in range(4):
            overlay_array[point_index[2]+mat[2], point_index[1]+mat[1], point_index[0]+mat[0], i] = np.where(mask, color[i], overlay_array[point_index[2]+mat[2], point_index[1]+mat[1], point_index[0]+mat[0], i])


@time_and_log
def render_mask_in_overlay_array(mask, image, overlay_array, color=None):
    resample = itk.ResampleImageFilter.New(mask.GetImage())
    resample.SetReferenceImage(image)
    resample.SetUseReferenceImage(True)
    interpolator = itk.NearestNeighborInterpolateImageFunction.New(mask.GetImage())
    resample.SetInterpolator(interpolator)
    resample.Update()
    matched_mask = resample.GetOutput()
    mask_array = itk.GetArrayFromImage(matched_mask)
    if color is None:
        color = mask.GetProperty().GetColor() * 255
    #overlay_array_sum = np.sum(overlay_array, axis=-1)
    id = mask.GetMaskValue()
    blend_conditional = (mask_array == id) #& (overlay_array_sum == 0)
    for i in range(4):
        if color[i] > 0:
            overlay_array[:,:,:,i] = np.where(blend_conditional, color[i], overlay_array[:,:,:,i])


@time_and_log
def render_scene_in_overlay_array(scene, selected_ids, image, overlay_array):
    scene.Update()
    mask_list = get_children_as_list(scene, "ImageMask")
    for mask in mask_list:
        color = None
        if mask.GetId() in selected_ids:
            color = [0, 255, 0, 255]
        render_mask_in_overlay_array(mask, image, overlay_array, color)
    tube_list = get_children_as_list(scene, "Tube")
    for tube in tube_list:
        color = None
        if tube.GetId() in selected_ids:
            color = [0, 255, 0, 255]
        render_tube_in_overlay_array(tube, image, overlay_array, color)


def render_object_in_overlay_array(so, image, overlay_array, color=None):
    if "ImageMask" in so.GetTypeName():
        render_mask_in_overlay_array(so, image, overlay_array, color)
    if "Tube" in so.GetTypeName():
        render_tube_in_overlay_array(so, image, overlay_array, color)
