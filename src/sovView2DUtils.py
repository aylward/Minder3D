import itk
import numpy as np

from sovUtils import get_children_as_list, time_and_log


@time_and_log
def render_tube_in_overlay_array(tube, image, overlay_array, color=None):
    """    Render a tube in an overlay array.

    This function renders a tube in the given overlay array based on the input tube, image, and color.

    Args:
        tube: A tube object representing the tube to be rendered.
        image: An image object representing the base image.
        overlay_array: A numpy array representing the overlay array.
        color: A tuple representing the color of the tube. If not provided, the color from the tube properties is used.
    """

    spacing = image.GetSpacing()
    point_list = tube.GetPoints()
    if color is None:
        color = tube.GetProperty().GetColor() * 255
    for point in point_list:
        point_pos = point.GetPositionInWorldSpace()
        point_index = image.TransformPhysicalPointToIndex(point_pos)
        point_radius = point.GetRadiusInWorldSpace()
        point_radius_index = image.TransformPhysicalPointToIndex(
            [
                point_pos[0] + point_radius,
                point_pos[1] + point_radius,
                point_pos[2] + point_radius,
            ]
        )
        point_radius_index = [
            abs(point_radius_index[i] - point_index[i]) for i in range(3)
        ]
        rr = point_radius**2
        oMin = max(0, point_index[2] - point_radius_index[2]) - point_index[2]
        oMax = (
            min(
                overlay_array.shape[0] - 1,
                point_index[2] + point_radius_index[2],
            )
            - point_index[2]
        )
        o2 = np.arange(oMin, oMax)
        oMin = max(0, point_index[1] - point_radius_index[1]) - point_index[1]
        oMax = (
            min(
                overlay_array.shape[1] - 1,
                point_index[1] + point_radius_index[1],
            )
            - point_index[1]
        )
        o1 = np.arange(oMin, oMax)
        oMin = max(0, point_index[0] - point_radius_index[0]) - point_index[0]
        oMax = (
            min(
                overlay_array.shape[2] - 1,
                point_index[0] + point_radius_index[0],
            )
            - point_index[0]
        )
        o0 = np.arange(oMin, oMax)
        mat = np.meshgrid(o0, o1, o2, indexing='ij')
        dist = (
            (mat[2] * spacing[2]) ** 2
            + (mat[1] * spacing[1]) ** 2
            + (mat[0] * spacing[0]) ** 2
        )
        mask = dist <= rr
        for i in range(4):
            overlay_array[
                point_index[2] + mat[2],
                point_index[1] + mat[1],
                point_index[0] + mat[0],
                i,
            ] = np.where(
                mask,
                color[i],
                overlay_array[
                    point_index[2] + mat[2],
                    point_index[1] + mat[1],
                    point_index[0] + mat[0],
                    i,
                ],
            )


@time_and_log
def render_mask_in_overlay_array(mask, image, overlay_array, color=None):
    resample = itk.ResampleImageFilter.New(mask.GetImage())
    resample.SetReferenceImage(image)
    resample.SetUseReferenceImage(True)
    interpolator = itk.NearestNeighborInterpolateImageFunction.New(
        mask.GetImage()
    )
    resample.SetInterpolator(interpolator)
    resample.Update()
    matched_mask = resample.GetOutput()
    mask_array = itk.GetArrayFromImage(matched_mask)
    if color is None:
        color = mask.GetProperty().GetColor() * 255
    # overlay_array_sum = np.sum(overlay_array, axis=-1)
    id = mask.GetMaskValue()
    blend_conditional = mask_array == id  # & (overlay_array_sum == 0)
    for i in range(4):
        if color[i] > 0:
            overlay_array[:, :, :, i] = np.where(
                blend_conditional, color[i], overlay_array[:, :, :, i]
            )


@time_and_log
def render_scene_in_overlay_array(scene, selected_ids, image, overlay_array):
    """    Render the scene in the overlay array with selected IDs highlighted.

    This function updates the scene, retrieves the masks and tubes as lists, and renders them in the overlay array with specified colors based on whether they are selected or not.

    Args:
        scene (object): The scene to be rendered.
        selected_ids (list): A list of selected IDs.
        image (object): The image to be rendered.
        overlay_array (array): The array for overlay rendering.
    """

    scene.Update()
    mask_list = get_children_as_list(scene, 'ImageMask')
    for mask in mask_list:
        color = None
        if mask.GetId() in selected_ids:
            color = [0, 255, 0, 255]
        render_mask_in_overlay_array(mask, image, overlay_array, color)
    tube_list = get_children_as_list(scene, 'Tube')
    for tube in tube_list:
        color = None
        if tube.GetId() in selected_ids:
            color = [0, 255, 0, 255]
        render_tube_in_overlay_array(tube, image, overlay_array, color)


def render_object_in_overlay_array(so, image, overlay_array, color=None):
    """    Render the object in the overlay array.

    This function renders the given object in the overlay array based on its type.

    Args:
        so: The object to be rendered in the overlay array.
        image: The image to be used for rendering.
        overlay_array: The array representing the overlay.
        color (optional): The color to be used for rendering.
    """

    if 'ImageMask' in so.GetTypeName():
        render_mask_in_overlay_array(so, image, overlay_array, color)
    if 'Tube' in so.GetTypeName():
        render_tube_in_overlay_array(so, image, overlay_array, color)
