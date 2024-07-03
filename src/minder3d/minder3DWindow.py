import os

import itk
import itk.itkGDCMImageIOPython
import numpy as np
import vtk
from PySide6.QtCore import QCoreApplication, QFileInfo
from PySide6.QtWidgets import (
    QFileDialog,
    QInputDialog,
    QMainWindow,
    QSizePolicy,
    QTabBar,
)

from .lib.sovImageTablePanelWidget import ImageTablePanelWidget
from .lib.sovInfoTablePanelWidget import InfoTablePanelWidget
from .lib.sovNewTaskPanelWidget import NewTaskPanelWidget
from .lib.sovObjectPanelWidget import ObjectPanelWidget
from .lib.sovUtils import (
    LogWindow,
    add_objects_in_mask_image_to_scene,
    compress_scene_for_saving,
    get_children_as_list,
    read_group,
    resample_overlay_to_match_image,
    time_and_log,
    uncompress_scene_after_loading,
    write_group,
)
from .lib.sovView2DPanelWidget import View2DPanelWidget
from .lib.sovView3DPanelWidget import View3DPanelWidget
from .lib.sovVisualizationPanelWidget import VisualizationPanelWidget
from .lib.sovWelcomePanelWidget import WelcomePanelWidget
from .minder3DState import Minder3DState
from .ui_minder3DWindow import Ui_MainWindow


class Minder3DWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """Initialize the parent widget and set up the UI.

        Args:
            parent: The parent widget (default is None).
        """
        super().__init__(parent)
        self.setupUi(self)

        QCoreApplication.setOrganizationName('Aylward')
        QCoreApplication.setApplicationName('Minder3D')

        self.state = Minder3DState()

        self.log_window = LogWindow(self.state.logger)
        self.statusViewLogButton.pressed.connect(self.log_window.show)
        self.log_window.logger.setLevel('WARNING')

        self.state.scene.SetId(self.state.scene.GetNextAvailableId())

        self.file_dir_dialog = None

        # File Menu
        self.loadImageMenuItem.triggered.connect(self.load_image)
        self.loadSceneMenuItem.triggered.connect(self.load_scene)
        self.saveImageMenuItem.triggered.connect(self.save_image)
        self.saveOverlayMenuItem.triggered.connect(self.save_overlay)
        self.saveVTKModelsMenuItem.triggered.connect(self.save_vtk_models)
        self.saveSceneMenuItem.triggered.connect(self.save_scene)

        self.bottomPanelLayout.minimumSize().setHeight(230)
        self.bottomPanelLayout.maximumSize().setHeight(230)

        self.bottomRightPanelLayout.minimumSize().setWidth(830)
        self.bottomRightPanelLayout.maximumSize().setWidth(830)

        # View 2D Widget
        self.view2DPanel = View2DPanelWidget(self, self.state)
        self.view2DLayout.addWidget(self.view2DPanel)

        # View 3D Widget
        self.view3DPanel = View3DPanelWidget(self, self.state)
        self.view3DLayout.addWidget(self.view3DPanel)

        # Object Widget
        self.objectPanel = ObjectPanelWidget(self, self.state)
        self.objectLayout.addWidget(self.objectPanel)

        # Info Table
        self.infoTablePanel = InfoTablePanelWidget(self, self.state)
        self.infoTableLayout.addWidget(self.infoTablePanel)

        # Welcome Tab
        self.welcomePanel = WelcomePanelWidget(self, self.state)
        self.welcomeTabLayout.addWidget(self.welcomePanel)

        # Visualization Tab
        self.visualizationPanel = VisualizationPanelWidget(self, self.state)
        self.visualizationTabLayout.addWidget(self.visualizationPanel)

        # New Task Tab
        self.newTaskPanel = NewTaskPanelWidget(self, self.state)
        self.newTaskTabLayout.addWidget(self.newTaskPanel)

        self.tabWidget.tabCloseRequested.connect(self.tab_close_event)
        self.tabWidget.setFixedHeight(200)
        self.tabWidget.setFixedWidth(700)

        self.importDICOMPanel = None
        self.lungCTAPanel = None
        self.otsuPanel = None
        self.imageProcessPanel = None

        # Remove Close buttons from welcome, visualization, and pre-process
        # and task tabs
        tabBar = self.tabWidget.tabBar()
        for i in range(0, 3):
            tabBar.tabButton(i, QTabBar.RightSide).deleteLater()
            tabBar.setTabButton(i, QTabBar.RightSide, None)

        # Image Table
        self.imageTablePanel = ImageTablePanelWidget(self, self.state)
        self.imageTableLayout.addWidget(self.imageTablePanel)
        self.imageTablePanel.setMinimumWidth(300)
        self.imageTablePanel.setSizePolicy(
            QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.statusText.setText('Ready')

        self.file_dialog = None

        self.show()
        self.view2DPanel.initialize()
        self.view3DPanel.initialize()

    @time_and_log
    def tab_close_event(self, index):
        tab = self.tabWidget.widget(index)
        self.tabWidget.removeTab(index)
        tab.close()

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.view2DPanel.close()
        self.view3DPanel.close()

    def log(self, message, level='info'):
        """Set the status text, and color based on the log level

        Args:
            message (str): The message to be displayed in the status text.
            level (str?): The log level. Defaults to 'info'.
        """
        self.statusText.setText(message)
        if level.lower() == 'error' or level.lower() == 'critical':
            self.statusText.setStyleSheet('background-color: red')
        elif level.lower() == 'warning':
            self.statusText.setStyleSheet('background-color: yellow')
        elif level.lower() == 'debug':
            self.statusText.setStyleSheet('background-color: green')
        else:
            self.statusText.setStyleSheet('background-color: white')
        self.statusText.update()
        self.log_window.log(message, level)

    def file_dir_dialog_switcher(self, str):
        """Open a file dialog to select a directory or a file.

        Returns:
            str: The path of the selected directory.
        """
        info = QFileInfo(str)
        if info.isFile():
            self.file_dialog.setFileMode(QFileDialog.ExistingFile)
            self.file_dialog.selectFile(str)
        elif info.isDir():
            self.file_dialog.setFileMode(QFileDialog.Directory)
            self.file_dialog.selectFile(str)

    @time_and_log
    def load_image(self, filename=None):
        """Load an image from a file.

        If filename is not provided, it opens a file dialog to select an image
        file.  It then creates a new image from the selected file and updates
        the image and overlay.

        Args:
            filename (str?): The path of the image file to be loaded.
        """
        if filename is None:
            if len(self.state.image_filename) > 0:
                filename = self.state.image_filename[-1]
            self.file_dialog = QFileDialog(self)
            self.file_dialog.setOptions(QFileDialog.DontUseNativeDialog)
            self.file_dialog.currentChanged.connect(
                self.file_dir_dialog_switcher
            )
            self.file_dialog.setLabelText(QFileDialog.Accept, 'Select')
            if self.file_dialog.exec() == QFileDialog.Accepted:
                filename = self.file_dialog.selectedFiles()[0]
        if filename is not None:
            imageio = None
            # info = QFileInfo(filename)
            # if info.isDir():
            # print("It's DICOM!")
            # imageio = itk.GDCMImageIO.New()
            # imageio.LoadPrivateTagsOn()
            img = itk.imread(
                filename, self.state.image_pixel_type, imageio=imageio
            )
            # print(img.GetMetaDataDictionary())
            if img is None:
                self.log('Image could not be loaded.', 'error')
                return
            self.create_new_image(img, filename)

            self.update_image()
            self.update_overlay()

    @time_and_log
    def load_overlay(self, filename=None):
        """Load an overlay from a file.

        If filename is not provided, it opens a file dialog to select an image
        file.  It then creates a new overlay from the selected file and updates
        the image and overlay.

        Args:
            filename (str?): The path of the image file to be loaded.
        """
        if filename is None:
            if len(self.state.image_filename) > 0:
                filename = self.state.image_filename[-1]
            filename, _ = QFileDialog.getOpenFileName(
                self, 'Open File', filename, 'All Files (*)'
            )
        if filename is not None:
            img = itk.imread(filename, itk.UC)
            if img is None:
                self.log('Image could not be loaded.', 'error')
                return

        add_objects_in_mask_image_to_scene(img, self.state.scene)
        self.update_scene()
        self.imageTablePanel.load_scene()

    @time_and_log
    def load_scene(self, filename=None):
        """Load a scene from a file and update the application state.

        If filename is not provided, a file dialog is opened to select the
        file.  If a valid filename is provided, the scene is loaded from the
        file and added to the application state.

        Args:
            filename (str?): The name of the file to load the scene from.

        Raises:
            IOError: If the file cannot be read or does not exist.
        """
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(
                self, 'Open File', self.state.scene_filename, 'All Files (*)'
            )
        if filename:
            filename = os.path.abspath(filename)
            self.state.scene_filename = filename
            self.state.scene = read_group(filename)
            if self.state.scene is None:
                self.log('Scene could not be loaded.', 'error')
                return

            self.state.scene = uncompress_scene_after_loading(self.state.scene)
            self.update_scene()

            self.imageTablePanel.load_scene()

    @time_and_log
    def save_image(self, filename=None):
        """Save the current image to a file.

        If no filename is provided, a file dialog will be opened to select the
        save location.

        Args:
            filename (str): The name of the file to save the image to. If not
                provided, a file dialog will be opened.
        """
        if not filename:
            filename, _ = QFileDialog.getSaveFileName(
                self,
                'Save File',
                self.state.image_filename[self.state.current_image_num],
                'All Files (*)',
            )
        if filename:
            filename = os.path.abspath(filename)
            self.state.image_filename[self.state.current_image_num] = filename
            self.log(f'Saving image to {filename}')
            itk.imwrite(
                self.state.image[self.state.current_image_num], filename
            )
            self.imageTablePanel.save_image(filename)

    @time_and_log
    def save_overlay(self, filename=None):
        """Save the overlay of the current image to a file.

        If no filename is provided, it prompts the user to select a file
        location. If a filename is provided, it saves the overlay of the
        current image to that file location.

        Args:
            filename (str): The name of the file to save the overlay to.
                If not provided, a file dialog will be shown.
        """
        if not filename:
            guess_filename, guess_extension = os.path.splitext(
                self.state.image_filename[self.state.current_image_num]
            )
            filename, _ = QFileDialog.getSaveFileName(
                self,
                'Save File',
                guess_filename + '_overlay' + guess_extension,
                'All Files (*)',
            )
        if filename:
            self.log(f'Saving overlay to {filename}')
            itk.imwrite(
                self.state.overlay[self.state.current_image_num], filename
            )

    @time_and_log
    def save_vtk_models(self, filename=None):
        """Save VTK models to a VRML file.

        If no filename is provided, a file dialog is opened to prompt the user
        for a filename. The VTK models are exported to the specified VRML file.

        Args:
            filename (str): The name of the file to save the VTK models to.
                If not provided, a file dialog will be opened.
        """
        if not filename:
            guess_filename, _ = os.path.splitext(self.state.scene_filename)
            filename, _ = QFileDialog.getSaveFileName(
                self,
                'Save File',
                guess_filename + '_models.vrml',
                'All Files (*)',
            )
        if filename:
            exporter = vtk.vtkVRMLExporter()
            exporter.SetRenderWindow(self.view3DPanel.renderWindow)
            exporter.SetFileName(filename)
            exporter.Write()
            exporter.Update()

    @time_and_log
    def save_scene(self, filename=None):
        """Save the current scene to a file.

        If no filename is provided, a file dialog will be shown to select the
        file. If a filename is provided, the scene will be saved to that file.

        Args:
            filename (str?): The name of the file to save the scene to.


        Raises:
            IOError: If there is an issue writing the scene to the file.
        """
        if not filename:
            filename, _ = QFileDialog.getSaveFileName(
                self, 'Save File', self.state.scene_filename, 'All Files (*)'
            )
        if filename:
            self.state.scene_filename = os.path.abspath(filename)
            self.log(f'Saving scene to {filename}')
            new_scene = compress_scene_for_saving(self.state.scene)
            print(new_scene)
            write_group(new_scene, filename)
            self.imageTablePanel.save_scene(filename)

    @time_and_log
    def create_new_image(self, img, filename=None, tag=None):
        """Create a new image and update the state with the new image info

        Args:
            img: The new image to be added.
            filename (str?): The filename for the new image. If not provided,
                a default filename will be generated.
            tag (str?): A tag to be appended to the filename.

        Returns:
            bool: True if the new image is successfully created and added to
                the state, False otherwise.
        """
        if filename is None:
            filename, fileext = os.path.splitext(self.state.image_filename[-1])
            if tag is None:
                filename = filename + '_' + str(len(self.state.image)) + fileext
                dlg = QInputDialog(self)
                dlg.setInputMode(QInputDialog.TextInput)
                dlg.setLabelText("New image's filename:")
                dlg.resize(500, 100)
                dlg.setTextValue(filename)
                valid = dlg.exec_()
                filename = dlg.textValue()
                if not valid:
                    return False
            else:
                filename = filename + '_' + tag + fileext
        self.state.image_filename.append(str(os.path.abspath(filename)))

        self.state.image.append(img)
        self.state.image_array.append(
            itk.GetArrayFromImage(self.state.image[-1])
        )
        self.state.image_min.append(float(np.min(self.state.image_array[-1])))
        self.state.image_max.append(float(np.max(self.state.image_array[-1])))

        dir = np.array(self.state.image[-1].GetDirection())
        axis_c = np.argmax(np.abs(dir), axis=1)[2]
        axis_s = np.argmax(np.abs(dir), axis=1)[1]
        axis_a = np.argmax(np.abs(dir), axis=1)[0]
        self.state.csa_to_image_axis.append([axis_c, axis_s, axis_a])

        if len(self.state.overlay) > 1:
            self.state.overlay.append(
                resample_overlay_to_match_image(
                    self.state.overlay[0], self.state.image[-1]
                )
            )
        else:
            self.state.overlay.append(self.state.overlay_type.New())
            self.state.overlay[-1].SetRegions(
                self.state.image[-1].GetLargestPossibleRegion()
            )
            self.state.overlay[-1].CopyInformation(self.state.image[-1])
            self.state.overlay[-1].Allocate()
            self.state.overlay[-1].FillBuffer(self.state.overlay_pixel_type(0))

        self.state.overlay_array.append(
            itk.GetArrayFromImage(self.state.overlay[-1])
        )

        self.state.current_image_num = len(self.state.image) - 1

        self.view2DPanel.create_new_image()
        self.view3DPanel.create_new_image()
        self.imageTablePanel.create_new_image()

        return True

    @time_and_log
    def replace_image(self, img, update_overlay=True):
        """Replace the current image with a new image and update the overlay.

        This function replaces the current image with the provided image and
        updates the corresponding image array, minimum and maximum values.
        If `update_overlay` is True, it also updates the overlay to match the
        new image.

        Args:
            img: The new image to be set as the current image.
                update_overlay (bool?): Flag to indicate whether to update the
                overlay. Defaults to True.


        Raises:
            TypeError: If the input image is not of the correct type.
        """

        num = self.state.current_image_num
        self.state.image[num] = img

        self.state.image_array[num] = itk.GetArrayFromImage(img)
        self.state.image_min[num] = float(np.min(self.state.image_array[num]))
        self.state.image_max[num] = float(np.max(self.state.image_array[num]))

        if update_overlay:
            self.state.overlay[num] = resample_overlay_to_match_image(
                self.state.overlay[0], self.state.image[num]
            )
            self.state.overlay_array[num] = itk.GetArrayFromImage(
                self.state.overlay[num]
            )

        self.imageTablePanel.replace_image()

    @time_and_log
    def update_pixel(self):
        self.infoTablePanel.update_pixel()

    @time_and_log
    def update_image(self):
        self.view2DPanel.update_image()
        self.view3DPanel.update_image()

        self.infoTablePanel.update_image()
        self.imageTablePanel.update_image()

    @time_and_log
    def update_overlay(self):
        self.view2DPanel.update_overlay()

    @time_and_log
    def update_scene(self):
        """Update the scene with the latest changes.

        This method updates the scene by updating the scene list, scene list
        ids, and scene list properties.  It also clears the object name combo
        box and adds items to it based on the scene list.  Additionally, it
        updates the 2D and 3D views if the corresponding auto-update flags are
        set.

        Args:
            self: The object instance.
        """

        self.state.scene_list = get_children_as_list(self.state.scene)
        self.state.scene_list_ids = []
        self.state.scene_list_properties = []

        self.update_gui = False

        for so in self.state.scene_list:
            self.state.scene_list_ids.append(so.GetId())
            self.state.scene_list_properties.append(
                dict(ColorBy='Solid Color', Actor=None)
            )
            if so.GetProperty().GetTagStringValue('Name') == '':
                so.GetProperty().SetTagStringValue(
                    'Name', f'{so.GetTypeName()} {so.GetId()}'
                )

        if self.state.view2D_overlay_auto_update:
            self.view2DPanel.update_scene()
        if self.state.view3D_scene_auto_update:
            self.view3DPanel.update_scene()
        self.imageTablePanel.update_scene()
        self.objectPanel.update_scene()

    @time_and_log
    def redraw_object(
        self, so, update_2D=True, update_3D=True, update_object=True
    ):
        """Redraws the specified object in the scene.

        This method updates the visual representation of the specified object
        in the 2D and 3D views if the corresponding update flags are set to
        True. It also updates the object's properties in the GUI.

        Args:
            self: The object instance.
            so: The object to be redrawn.
            update_2D (bool): Flag indicating whether to update the 2D view
                (default is True).
            update_3D (bool): Flag indicating whether to update the 3D view
                (default is True).
        """
        if update_2D and self.state.view2D_overlay_auto_update:
            self.view2DPanel.redraw_object(so)
        if update_3D and self.state.view3D_scene_auto_update:
            self.view3DPanel.redraw_object(so)
        if update_object:
            # Must call after view3DPanel.redraw_object() so that actors are
            # defined and color-by options are known.
            self.objectPanel.redraw_object(so)

    @time_and_log
    def unload_image(self, img_num, update_image_table=True):
        """Unload the image with the specified number.

        This method unloads the image with the specified number and updates the
        image and overlay lists.  It also updates the 2D and 3D views.

        Args:
            img_num (int): The number of the image to be unloaded.
        """
        if img_num < 0 or img_num >= len(self.state.image):
            return

        self.state.image.pop(img_num)
        self.state.image_array.pop(img_num)
        self.state.image_min.pop(img_num)
        self.state.image_max.pop(img_num)
        self.state.image_filename.pop(img_num)
        self.state.image_thumbnail.pop(img_num)
        self.state.csa_to_image_axis.pop(img_num)

        self.state.overlay.pop(img_num)
        self.state.overlay_array.pop(img_num)

        self.state.view2D_intensity_window_min.pop(img_num)
        self.state.view2D_intensity_window_max.pop(img_num)
        self.state.view2D_slice.pop(img_num)
        self.state.view2D_flip.pop(img_num)
        self.state.view2D_csa_axis_order.pop(img_num)
        self.state.view2D_image_axis_order.pop(img_num)

        if len(self.state.image) > 0:
            self.state.current_image_num = 0
        else:
            self.state.current_image_num = -1

        if update_image_table:
            self.imageTablePanel.unload_image()

        self.view2DPanel.update_view_image_num(self.state.current_image_num)
