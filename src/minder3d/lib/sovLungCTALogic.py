import importlib.util as imp
import subprocess
import sys

import itk
import numpy as np

from .sovImageProcessLogic import ImageProcessLogic
from .sovUtils import time_and_log


class LungCTALogic:
    def __init__(self):
        self.ai_first_run = True
        self.image = None
        self.pre_image = None
        self.mask = None

    @time_and_log
    def initialize(self, image):
        """Initialize the AI model with the given image.

        This method initializes the AI model with the given image. It first checks for the presence of required dependencies and GPU support, and then sets the input image for further processing.

        Args:
            image: The input image for initializing the AI model.

        Returns:
            tuple: A tuple containing the status of initialization (bool), a message (str), and a flag to ask for user confirmation (bool).
        """

        if self.ai_first_run and imp.find_spec('totalsegmentator') is None:
            self.ai_first_run = False
            status = False
            msg = 'This method works best with NVidia GPUs.\nFirst install CUDA (https://developer.nvidia.com/cuda-downloads)\nand then install PyTorch (https://pytorch.org/get-started/locally/)'
            ask_to_continue = False
            return status, msg, ask_to_continue

        if imp.find_spec('torch') is None:
            status = False
            msg = 'PyTorch not found:\nFirst install CUDA (https://developer.nvidia.com/cuda-downloads)\nand then PyTorch (https://pytorch.org/get-started/locally/)'
            ask_to_continue = False
            return status, msg, ask_to_continue

        import torch

        if not torch.cuda.is_available():
            status = False
            msg = 'WARNING: PyTorch installed without CUDA support.\nThe AI methods will run on the CPU and be very slow.\nContinue?'
            ask_to_continue = True
            return status, msg, ask_to_continue

        self.image = image

        status = True
        msg = ''
        ask_to_continue = False
        return status, msg, ask_to_continue

    def preprocess(self):
        """Preprocesses the input image for further analysis.

        If the input image is None, returns None. If the 'totalsegmentator' module is not found, it installs it using pip.
        Then, it checks the spacing of the image and if it does not meet the specified conditions, it preprocesses the image
        using ImageProcessLogic.make_iso method with a spacing of 1.5. Otherwise, it uses the original image for preprocessing.

        Returns:
            SimpleITK.Image: The preprocessed image.

        Raises:
            subprocess.CalledProcessError: If the installation of 'TotalSegmentator' fails.
        """

        if self.image is None:
            return None

        if imp.find_spec('totalsegmentator') is None:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install', 'TotalSegmentator']
            )

        spacing = self.image.GetSpacing()
        if not (
            spacing[0] == 1.5
            and spacing[0] == spacing[1]
            and spacing[1] == spacing[2]
        ):
            preproc = ImageProcessLogic()
            self.pre_image = preproc.make_iso(self.image, 1.5)
        else:
            self.pre_image = self.image
        return self.pre_image

    def run(self):
        """Perform image preprocessing and segmentation using the TotalSegmentator library.

        If the pre_image is not provided, it will be preprocessed before segmentation.
        The preprocessing step includes converting the input image to a NIfTI format and applying a transformation matrix.

        Returns:
            itk.Image: The segmented image after preprocessing and segmentation.
        """

        if self.pre_image is None:
            self.preprocess()
            if self.pre_image is None:
                return None

        import nibabel as nib
        from totalsegmentator.python_api import totalsegmentator

        pre_array = itk.GetArrayFromImage(self.pre_image)
        mat = np.eye(4)
        mat = mat * 1.5
        mat[3, 3] = 1
        nifti_nib = nib.Nifti1Image(
            np.transpose(pre_array, (2, 1, 0)).copy(), mat
        )
        seg_nib = totalsegmentator(
            input=nifti_nib, output=None, task='lung_vessels'
        )

        seg_array = seg_nib.get_fdata().astype(np.uint8)
        seg_image = itk.GetImageFromArray(
            np.transpose(seg_array, (2, 1, 0)).copy()
        )
        seg_image.CopyInformation(self.pre_image)

        return seg_image
