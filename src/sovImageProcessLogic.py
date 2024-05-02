import numpy as np

import itk
from itk import TubeTK as tube

class ImageProcessLogic:
    def make_high_res_iso(self, inputImage):
        isoImageFilter = tube.ResampleImage.New(Input=inputImage)
        isoImageFilter.SetMakeHighResIso(True)
        isoImageFilter.SetInterpolator("Sinc")
        isoImageFilter.Update()
        return isoImageFilter.GetOutput()

    def make_low_res_iso(self, inputImage):
        isoImageFilter = tube.ResampleImage.New(Input=inputImage)
        isoImageFilter.SetMakeIsotropic(True)
        isoImageFilter.SetInterpolator("Sinc")
        isoImageFilter.Update()
        return isoImageFilter.GetOutput()

    def make_iso(self, inputImage, spacingX):
        spacing = [spacingX, spacingX, spacingX]

        isoImageFilter = tube.ResampleImage.New(Input=inputImage)
        isoImageFilter.SetSpacing(spacing)
        isoImageFilter.SetInterpolator("Sinc")
        isoImageFilter.Update()
        return isoImageFilter.GetOutput()

    def clip_window_level(self, inputImage, inputArray, imin, imax):
        flip = False
        if imin > imax:
            tmp = imin
            imin = imax
            imax = tmp
            flip = True
        image_array = np.clip(inputArray, imin, imax)
        if flip:
            image_array = imax - image_array
        img = itk.GetImageFromArray(image_array)
        img.CopyInformation(inputImage)
        return img

    def median_filter(self, inputImage, radius):
        medFilter = itk.MedianImageFilter.New(Input=inputImage)
        medFilter.SetRadius(radius)
        medFilter.Update()
        return medFilter.GetOutput()
