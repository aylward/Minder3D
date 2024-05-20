import os

from dicomsort import DICOMSorter
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QFileDialog, QWidget

from .sovImportDICOMSettings import ImportDICOMSettings
from .sovUtils import time_and_log
from .ui_sovImportDICOMPanelWidget import Ui_ImportDICOMPanelWidget


class ImportDICOMPanelWidget(QWidget, Ui_ImportDICOMPanelWidget):
    @time_and_log
    def __init__(self, gui, state, parent=None):
        """Initialize the GUI and state for the Import DICOM panel.

        Args:
            gui: The graphical user interface object.
            state: The state object for the application.
            parent: The parent widget (default is None).
        """
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state
        self.settings = ImportDICOMSettings()

        input_directory, output_directory, auto_register = (
            self.settings.get_data()
        )

        self.importDICOMInputDirectorySelectButton.pressed.connect(
            self.selectInputDirectory
        )
        self.importDICOMInputDirectoryLineEdit.setText(input_directory)

        self.importDICOMOutputDirectorySelectButton.pressed.connect(
            self.selectOutputDirectory
        )
        self.importDICOMOutputDirectoryLineEdit.setText(output_directory)

        self.importDICOMAutoRegisterCheckBox.setChecked(auto_register)

        self.importDICOMRunButton.pressed.connect(self.run)

        p = self.importDICOMInstructionsTextEdit.palette()
        p.setColor(QPalette.Base, QColor(43, 43, 43))
        p.setColor(QPalette.Text, QColor(200, 200, 200))
        self.importDICOMInstructionsTextEdit.setPalette(p)

    def selectInputDirectory(self):
        """Select the input directory for the DICOM files.

        Args:
            self (object): The instance of the class.
        """
        if self.importDICOMInputDirectoryLineEdit.text() != '':
            dir = self.importDICOMInputDirectoryLineEdit.text()
        dir = QFileDialog.getExistingDirectory(
            self, 'Select Input Directory', dir
        )
        if dir is not None and dir != '':
            self.importDICOMInputDirectoryLineEdit.setText(dir)
            self.settings.add_data(
                dir,
                self.importDICOMOutputDirectoryLineEdit.text(),
                self.importDICOMAutoRegisterCheckBox.isChecked(),
            )

    def selectOutputDirectory(self):
        """Select the ouput directory for the DICOM files.

        Args:
            self (object): The instance of the class.
        """
        dir = '.'
        if self.importDICOMOutputDirectoryLineEdit.text() != '':
            dir = self.importDICOMOutputDirectoryLineEdit.text()
        dir = QFileDialog.getExistingDirectory(
            self, 'Select Output Directory', dir
        )
        if dir is not None and dir != '':
            self.importDICOMOutputDirectoryLineEdit.setText(dir)
            self.settings.add_data(
                self.importDICOMInputDirectoryLineEdit.text(),
                dir,
                self.importDICOMAutoRegisterCheckBox.isChecked(),
            )

    def run(self):
        """Run the DICOM import process.

        Args:
            self (object): The instance of the class.
        """
        input_dir = self.importDICOMInputDirectoryLineEdit.text()
        output_dir = self.importDICOMOutputDirectoryLineEdit.text()
        self.settings.add_data(
            input_dir,
            output_dir,
            self.importDICOMAutoRegisterCheckBox.isChecked(),
        )
        pattern = (
            '%PatientName/%StudyID-%StudyDescription-%StudyDate/'
            + '%Modality/%SeriesNumber-%SeriesDescription/%InstanceNumber.dcm'
        )
        target_pattern = os.path.join(output_dir, pattern)
        args = {
            'sourceDir': input_dir,
            'targetPattern': target_pattern,
            'keepGoing': True,
        }
        dicomSorter = DICOMSorter()
        dicomSorter.setOptions(args)
        dicomSorter.renameFiles()

        if self.importDICOMAutoRegisterCheckBox.isChecked():
            self.gui.imageTablePanel.register_images(output_dir)
