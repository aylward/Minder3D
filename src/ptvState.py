import itk

from sovColorMapUtils import (
    standard_anatomy_colormap,
    standard_anatomy_colormap_scale_factor,
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
        self.image = None
        self.image_array = None
        self.image_min = 0
        self.image_max = 1
        self.loaded_image = None
        self.loaded_image_filename = "./test.mha"
        self.image_intensity_window_min = 0
        self.image_intensity_window_max = 0
        self.image_slice = [0,0,0]
        self.image_axis = 2
        self.image_flip_x = False
        self.image_flip_y = False

        # Overlay
        self.overlay = None
        self.overlay_array = None
        self.overlay_opacity = 0.5

        self.colormap = short_colormap
        self.colormap_scale_factor = short_colormap_scale_factor

        # Scene
        self.scene = None
        self.scene_list = []
        self.scene_list_ids = []
        self.scene_list_properties = dict()
        self.loaded_scene_filename = "./test.mha"

        # Selected Spatial Objects
        self.multiple_selections_enabled = False
        self.selected_ids = []
        self.selected_point_ids = []
        self.highlight_selected = True
