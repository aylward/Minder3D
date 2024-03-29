
import sys
import subprocess

import numpy as np

from PySide6.QtWidgets import (
    QWidget,
    QMessageBox,
)

from ui_sovLungAIPanelWidget import Ui_LungAIPanelWidget

import importlib.util as imp

import itk


class LungAIPanelWidget(QWidget, Ui_LungAIPanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.ai_first_run = True

        self.lungAISegmentButton.clicked.connect(
            self.segment_lungs
        )

        # https://pytorch.org/get-started/locally/

    def segment_lungs(self):
        if self.ai_first_run and imp.find_spec("totalsegmentator") is None:
            print(sys.modules)
            self.ai_first_run = False
            message = QMessageBox()
            message.setWindowTitle("Intial setup...")
            message.setText("This method works best with NVidia GPUs.  First install CUDA (https://developer.nvidia.com/cuda-downloads) and then install PyTorch (https://pytorch.org/get-started/locally/)")
            message.exec()
            return

        if imp.find_spec("torch") is None:
            message = QMessageBox()
            message.setWindowTitle("AI not loaded")
            message.setText("PyTorch not found: First install CUDA (https://developer.nvidia.com/cuda-downloads) and then PyTorch (https://pytorch.org/get-started/locally/)")
            message.exec()
            return
        import torch

        if not torch.cuda.is_available():
            message = QMessageBox()
            message.setWindowTitle("GPU support not loaded")
            message.setText("WARNING: PyTorch installed without CUDA support. The AI methods will run on the CPU and be very slow. Continue?")
            message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            ret = message.exec()
            if ret == QMessageBox.No:
                return

        if imp.find_spec("totalsegmentator") is None:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "TotalSegmentator"]) 

        from totalsegmentator.python_api import totalsegmentator
        import nibabel as nib

        self.gui.log("Making isotropic 1.5mm image...")
        self.gui.preProcessPanel.preProcessIsoSpinBox.setValue(1.5)
        self.gui.preProcessPanel.make_iso()
        self.gui.save_image()

        data = self.state.image_array[self.state.current_image_num]
        mat = np.eye(4)
        mat = mat * 1.5
        mat[3, 3] = 1
        nifti_nib = nib.Nifti1Image(np.transpose(data, (2, 1, 0)).copy(), mat)
        nib.save(nifti_nib, "temp.nii.gz")
        seg_nib = totalsegmentator(input=nifti_nib, output=None, task="lung_vessels")

        seg_array = seg_nib.get_fdata().astype(np.uint8)
        seg_image = itk.GetImageFromArray(np.transpose(seg_array, (2, 1, 0)).copy())
        seg_image.CopyInformation(self.state.image[self.state.current_image_num])

        self.gui.create_new_image(seg_image, tag="Seg")
        self.gui.save_image()
