import itk
import numpy as np
from itk import TubeTK as tube


class ImageProcessLogic:
    def make_high_res_iso(self, inputImage):
        """        Make a high resolution isotropic image from the input image.

        This function creates a high resolution isotropic image from the input image using resampling and interpolation.

        Args:
            inputImage: The input image to be processed.

        Returns:
            The high resolution isotropic image.
        """

        isoImageFilter = tube.ResampleImage.New(Input=inputImage)
        isoImageFilter.SetMakeHighResIso(True)
        isoImageFilter.SetInterpolator('Sinc')
        isoImageFilter.Update()
        return isoImageFilter.GetOutput()

    def make_low_res_iso(self, inputImage):
        """        Make the input image isotropic with low resolution.

        This function resamples the input image to make it isotropic with low resolution using the Sinc interpolator.

        Args:
            inputImage: The input image to be made isotropic with low resolution.

        Returns:
            The isotropic low resolution image.
        """

        isoImageFilter = tube.ResampleImage.New(Input=inputImage)
        isoImageFilter.SetMakeIsotropic(True)
        isoImageFilter.SetInterpolator('Sinc')
        isoImageFilter.Update()
        return isoImageFilter.GetOutput()

    def make_iso(self, inputImage, spacingX):
        """        Resamples the input image to have isotropic spacing.

        This function resamples the input image to have isotropic spacing in all three dimensions.

        Args:
            inputImage: vtkImageData - The input image to be resampled.
            spacingX (float): The desired isotropic spacing value.

        Returns:
            vtkImageData: The resampled image with isotropic spacing.
        """

        spacing = [spacingX, spacingX, spacingX]

        isoImageFilter = tube.ResampleImage.New(Input=inputImage)
        isoImageFilter.SetSpacing(spacing)
        isoImageFilter.SetInterpolator('Sinc')
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
