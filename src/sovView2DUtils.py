import numpy as np

import itk

from sovUtils import (
    get_children_as_list,
    time_and_log,
)


def render_tube_in_overlay_array(tube, image, overlay_array, color=None):
    spacing = image.GetSpacing()
    origin = image.GetOrigin()
    point_list = tube.GetPoints()
    if color is None:
        color = tube.GetProperty().GetColor() * 255
    for point in point_list:
        point_pos = point.GetPositionInWorldSpace()
        point_index = image.TransformPhysicalPointToIndex(point_pos)
        point_radius = point.GetRadiusInWorldSpace()
        point_radius_index = image.TransformPhysicalPointToIndex(
            [origin[0]+point_radius, origin[1]+point_radius, origin[2]+point_radius]
        )
        point_radius_index = [abs(v) for v in point_radius_index]
        rr = point_radius**2
        for o2 in range(-point_radius_index[2],
                        point_radius_index[2]):
            r2 = (o2*spacing[2])**2
            if r2 <= rr:
                for o1 in range(-point_radius_index[1],
                                point_radius_index[1]):
                    r1 = (o1*spacing[1])**2
                    if r2+r1 <= rr:
                        for o0 in range(-point_radius_index[0],
                                        point_radius_index[0]):
                            r0 = (o0*spacing[0])**2
                            if r2+r1+r0 <= rr:
                                tp = [point_index[0]+o0,
                                      point_index[1]+o1,
                                      point_index[2]+o2]
                                if (tp[0] >= 0 and
                                    tp[0] < overlay_array.shape[2] and
                                    tp[1] >= 0 and
                                    tp[1] < overlay_array.shape[1] and
                                    tp[2] >= 0 and
                                    tp[2] < overlay_array.shape[0]):
                                    overlay_array[tp[2], tp[1], tp[0]] = color


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
    overlay_array_sum = np.sum(overlay_array, axis=-1)
    blend_conditional = (mask_array > 0) & (overlay_array_sum == 0)
    for i in range(3):
        print(f"color[{i}]={color[i]}")
        if color[i] > 0:
            overlay_array[:,:,:,i] = np.where(blend_conditional, color[i], overlay_array[:,:,:,i])


@time_and_log
def render_scene_in_overlay_array(scene, selected_ids, image, overlay_array):
    scene.Update()
    tube_list = get_children_as_list(scene, "Tube")
    for tube in tube_list:
        color = None
        if tube.GetId() in selected_ids:
            color = [0, 255, 0, 255]
        render_tube_in_overlay_array(tube, image, overlay_array, color)
    mask_list = get_children_as_list(scene, "Mask")
    for mask in mask_list:
        color = None
        if mask.GetId() in selected_ids:
            color = [0, 255, 0, 255]
        render_mask_in_overlay_array(mask, image, overlay_array, color)


def render_object_in_overlay_array(so, image, overlay_array, color=None):
    if "Tube" in so.GetTypeName():
        render_tube_in_overlay_array(so, image, overlay_array, color)
    if "Mask" in so.GetTypeName():
        render_mask_in_overlay_array(so, image, overlay_array, color)
