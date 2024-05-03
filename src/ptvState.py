import logging

import itk

from sovColorMapUtils import short_colormap, short_colormap_scale_factor


class PTVState:
    def __init__(self):
        """        Initialize the attributes of the class.

        Initializes various attributes related to image, overlay, current image, 2D and 3D view settings,
        scene, and selected spatial objects.

        Attributes:
            image_pixel_type: The pixel type of the image.
            image_type: The type of the image.
            overlay_pixel_type: The pixel type of the overlay.
            overlay_type: The type of the overlay.
            image: The image.
            image_array: The array representation of the image.
            image_min: The minimum value in the image.
            image_max: The maximum value in the image.
            image_filename: The filename of the image.
            overlay: The overlay.
            overlay_array: The array representation of the overlay.
            current_image_num: The number of the current image.
            current_pixel: The current pixel.
            view2D_intensity_window_min: The minimum intensity window for 2D view.
            view2D_intensity_window_max: The maximum intensity window for 2D view.
            view2D_slice: The slice for 2D view.
            view2D_axis: The axis for 2D view.
            view2D_flip: The flip setting for 2D view.
            view2D_overlay_opacity: The opacity of the overlay for 2D view.
            view2D_overlay_auto_update: The auto update setting for the overlay in 2D view.
            view3D_scene_auto_update: The auto update setting for the scene in 3D view.
            colormap: The colormap setting for both 2D and 3D views.
            colormap_scale_factor: The scale factor for the colormap.
            scene: The scene for visualization.
            scene_list: The list of scenes.
            scene_list_ids: The list of scene IDs.
            scene_list_properties: The properties of the scene list.
            scene_filename: The filename of the scene.
            multiple_selections_enabled: The setting for enabling multiple selections.
            selected_ids: The selected IDs.
            selected_point_ids: The selected point IDs.
            highlight_selected: The setting for highlighting selected objects.
            logger: The logger for the class.
        """

        # Types
        self.image_pixel_type = itk.F
        self.image_type = itk.Image[self.image_pixel_type, 3]

        self.overlay_pixel_type = itk.RGBAPixel[itk.UC]
        self.overlay_type = itk.Image[self.overlay_pixel_type, 3]

        # Image
        self.image = []
        self.image_array = []
        self.image_min = []
        self.image_max = []
        self.image_filename = []

        # Overlay
        self.overlay = []
        self.overlay_array = []

        # Current image
        self.current_image_num = 0
        self.current_pixel = []

        # 2D View settings
        self.view2D_intensity_window_min = []
        self.view2D_intensity_window_max = []
        self.view2D_slice = []
        self.view2D_axis = []
        self.view2D_flip = []
        self.view2D_overlay_opacity = 0.5
        self.view2D_overlay_auto_update = False

        # 3D View settings
        self.view3D_scene_auto_update = True

        # 2D and 3D View settings
        self.colormap = short_colormap
        self.colormap_scale_factor = short_colormap_scale_factor

        # Scene
        self.scene = itk.GroupSpatialObject[3].New()
        self.scene_list = []
        self.scene_list_ids = []
        self.scene_list_properties = dict()
        self.scene_filename = './scene.tre'

        # Selected Spatial Objects
        self.multiple_selections_enabled = False
        self.selected_ids = []
        self.selected_point_ids = []
        self.highlight_selected = True

        self.logger = logging.getLogger('sov')
