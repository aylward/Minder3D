import itk
import numpy as np


class OtsuLogic:
    def run(self, inputImage, numberOfThresholds):
        if numberOfThresholds <= 1:
            filter = itk.OtsuThresholdImageFilter.New(Input=inputImage)
            filter.Update()
            return filter.GetOutput().astype(np.uint8)
        else:
            filter = itk.OtsuMultipleThresholdsImageFilter.New(Input=inputImage)
            filter.SetNumberOfThresholds(numberOfThresholds)
            filter.Update()
            img = filter.GetOutput().astype(np.uint8)
            return img
