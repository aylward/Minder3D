import itk

from soViewerUtils import get_children_as_list


def render_tubes_in_overlay(scene, image, overlay_array):
    tube_list = get_children_as_list(scene, "Tube")
    spacing = image.GetSpacing()
    origin = image.GetOrigin()
    for tube in tube_list:
        point_list = tube.GetPoints()
        for point in point_list:
            point_pos = point.GetPositionInWorldSpace()
            point_index = image.TransformPhysicalPointToIndex(point_pos)
            point_radius = point.GetRadiusInWorldSpace()
            point_radius_index = image.TransformPhysicalPointToIndex(
                [origin[0]+point_radius, origin[1]+point_radius, origin[2]+point_radius]
            )
            point_radius_index = [abs(v) for v in point_radius_index]
            rr = point_radius**2
            c = tube.GetProperty().GetColor() * 255
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
                                        overlay_array[tp[2],tp[1],tp[0]] = c


def render_scene_in_overlay_array(scene, image, overlay_array):
    scene.Update()
    render_tubes_in_overlay(scene, image, overlay_array)
