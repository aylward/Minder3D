from sovUtils import time_and_log

import itk

from sovPreProcessLogic import PreProcessLogic


class LungCTALogic:
    def __init__(self, gui, state, parent=None):
        self.ai_first_run = True

        self.mask = None

    @time_and_log
    def initialize(self):
        if self.ai_first_run and imp.find_spec("totalsegmentator") is None:
            self.ai_first_run = False
            status = False
            msg = "This method works best with NVidia GPUs.\nFirst install CUDA (https://developer.nvidia.com/cuda-downloads)\nand then install PyTorch (https://pytorch.org/get-started/locally/)"
            ask_to_continue = False
            return status, msg, ask_to_continue

        if imp.find_spec("torch") is None:
            status = False
            msg = "PyTorch not found:\nFirst install CUDA (https://developer.nvidia.com/cuda-downloads)\nand then PyTorch (https://pytorch.org/get-started/locally/)"
            ask_to_continue = False
            return status, msg, ask_to_continue

        import torch

        if not torch.cuda.is_available():
            status = False
            msg = "WARNING: PyTorch installed without CUDA support.\nThe AI methods will run on the CPU and be very slow.\nContinue?"
            ask_to_continue = True
            return status, msg, ask_to_continue
        
        status = True
        msg = ""
        ask_to_continue = False
        return status, msg, ask_to_continue

    def preprocess(self):
        if imp.find_spec("totalsegmentator") is None:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "TotalSegmentator"]) 

        from totalsegmentator.python_api import totalsegmentator
        import nibabel as nib

        spacing = self.state.image[self.state.current_image_num].GetSpacing()
        if not(spacing[0] == 1.5 and spacing[0] == spacing[1] and spacing[1] == spacing[2]):
            preproc = PreProcessLogic()
            preproc_img = preproc.make_iso(self.state.image[self.state.current_image_num], 1.5)
            self.gui.create_new_image(preproc_img, None, "Iso")

    def run(self):
        data = self.state.image_array[self.state.current_image_num]
        mat = np.eye(4)
        mat = mat * 1.5
        mat[3, 3] = 1
        nifti_nib = nib.Nifti1Image(np.transpose(data, (2, 1, 0)).copy(), mat)
        seg_nib = totalsegmentator(input=nifti_nib, output=None, task="lung_vessels")

        seg_array = seg_nib.get_fdata().astype(np.uint8)
        seg_image = itk.GetImageFromArray(np.transpose(seg_array, (2, 1, 0)).copy())
        seg_image.CopyInformation(self.state.image[self.state.current_image_num])

        return seg_image
