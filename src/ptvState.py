import itk

import logging

from sovColorMapUtils import (
    short_colormap,
    short_colormap_scale_factor,
)


class PTVState():
    def __init__(self):
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
        self.scene = None
        self.scene_list = []
        self.scene_list_ids = []
        self.scene_list_properties = dict()
        self.scene_filename = "./scene.tre"

        # Selected Spatial Objects
        self.multiple_selections_enabled = False
        self.selected_ids = []
        self.selected_point_ids = []
        self.highlight_selected = True

        self.logger = logging.getLogger("sov")
