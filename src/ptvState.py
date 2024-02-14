import itk

import vtk

class ptvState():
    def __init__(self):
        # Types
        self.image_pixel_type = itk.F
        self.image_type = itk.Image[self.image_pixel_type, 3]
        self.overlay_pixel_type = itk.SS
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

        # Overlay
        self.overlay = None
        self.overlay_array = None

        # Scene
        self.scene = None
        self.loaded_scene_filename = "./test.mha"
