"""
Utility functions for working with spatial objects.

This module contains utility functions for working with spatial objects.

Functions:
    get_children_as_list: Finds all children of a given type in a
        GroupSpatialObject and returns them as a list.
    read_group: Reads a group from a file.
    write_group: Writes a group to a file.
"""

import functools
import logging
import os
import time
import uuid
from typing import Union

import itk
import numpy as np
from PySide6.QtCore import QSettings, QStandardPaths
from PySide6.QtWidgets import QMainWindow, QTextEdit

from sovColorMapUtils import short_colormap, short_colormap_scale_factor

logging.basicConfig(level=logging.DEBUG)


class LogHandler(logging.Handler):
    def __init__(self, text_edit):
        super().__init__()
        self.text_edit = text_edit

    def emit(self, record):
        log_entry = self.format(record)
        self.text_edit.append(log_entry)


class LogWindow(QMainWindow):
    def __init__(self, logger, parent=None):
        """Initialize the LogWindow.

        Args:
            logger: The logger object to be used for logging.
            parent: The parent widget (optional).
        """

        super().__init__(parent)

        self.setWindowTitle('Log')
        self.logTextEdit = QTextEdit()
        self.setCentralWidget(self.logTextEdit)

        self.logger = logger
        self.log_handler = LogHandler(self.logTextEdit)
        self.logger.addHandler(self.log_handler)

    def show(self):
        super().show()
        self.logTextEdit.show()

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.logTextEdit.close()

    def log(self, message, level='info'):
        """Log a message with the specified logging level.

        This function logs the given message with the specified logging level using the logger object.

        Args:
            message (str): The message to be logged.
            level (str?): The logging level. Defaults to 'info'.
        """

        if level.lower() == 'debug':
            self.logger.debug(message)
        elif level.lower() == 'info':
            self.logger.info(message)
        elif level.lower() == 'warning':
            self.logger.warning(message)
        elif level.lower() == 'error':
            self.logger.error(message)
        elif level.lower() == 'critical':
            self.logger.critical(message)


def sov_log(message, level='info'):
    """Log a message with the specified logging level.

    This function logs the input message with the specified logging level using the 'sov' logger.

    Args:
        message (str): The message to be logged.
        level (str?): The logging level. Defaults to 'info'.
    """

    logger = logging.getLogger('sov')
    if level.lower() == 'debug':
        logger.debug(message)
    elif level.lower() == 'info':
        logger.info(message)
    elif level.lower() == 'warning':
        logger.warning(message)
    elif level.lower() == 'error':
        logger.error(message)
    elif level.lower() == 'critical':
        logger.critical(message)


def time_and_log(func):
    """Decorator to log the start and end of function execution along with its duration.

    It logs the start of the function execution, then executes the function, logs the end of the function execution
    along with the duration, and returns the result. If an exception occurs during the function execution, it logs
    the exception and re-raises it.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """

    if 'nesting_level' not in time_and_log.__dict__:
        time_and_log.nesting_level = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Log the start and end time of the function execution and handle exceptions.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Any: The result of the function execution.

        Raises:
            Exception: If an exception occurs during the function execution.
        """

        logger = logging.getLogger('sov')
        spacing = '  ' * time_and_log.nesting_level
        filename = os.path.splitext(
            os.path.split(func.__code__.co_filename)[1]
        )[0]
        logger.info(f'{spacing}{filename}:{func.__name__} started.')
        time_and_log.nesting_level += 1
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            time_and_log.nesting_level -= 1
            logger.info(
                f'{spacing}{filename}:{func.__name__} took {(end_time - start_time):.2f} seconds to execute.'
            )
            return result
        except Exception as e:
            end_time = time.time()
            time_and_log.nesting_level -= 1
            logger.error(
                f'{spacing}{filename}:{func.__name__} exception after {(end_time - start_time):.2f} seconds: {str(e)}'
            )
            raise e

    return wrapper


def get_settings():
    """Get the application settings.

    This function retrieves the application settings using QSettings from 'itkSpatialObjectsViewer' and 'QuantAIV'.

    Returns:
        QSettings: The application settings.
    """

    settings = QSettings('itkSpatialObjectsViewer', 'QuantAIV')
    return settings


class SettingsFileRecord:
    def __init__(
        self,
        filename,
        file_type,
        file_spacing=[],
        file_size=[],
        file_thumbnail='',
    ):
        """Initialize the object with the provided file details.

        Args:
            filename (str): The name of the file.
            file_type (str): The type of the file.
            file_spacing (list?): A list of spacing details. Defaults to [].
            file_size (list?): A list of size details. Defaults to [].
            file_thumbnail (str?): The thumbnail of the file. Defaults to ''.
        """

        self.filename = filename
        self.file_type = file_type
        self.file_spacing = file_spacing
        self.file_size = file_size
        self.file_thumbnail = file_thumbnail


def get_file_reccords_from_settings():
    """Get file records from the settings.

    This function retrieves file records from the settings and returns a list of file records.

    Returns:
        list: A list of file records retrieved from the settings.
    """

    settings = get_settings()
    files = []
    size = settings.beginReadArray('files')
    for i in range(size):
        settings.setArrayIndex(i)
        filename = settings.value('filename', '')
        file_type = settings.value('file_type', '')
        file_spacing = settings.value('file_spacing', [], float)
        file_size = settings.value('file_size', [], int)
        file_thumbnail = settings.value('file_thumbnail', '')
        rec = SettingsFileRecord(
            filename, file_type, file_spacing, file_size, file_thumbnail
        )
        files.append(rec)
    settings.endArray()
    return files


def add_file_to_settings(obj, filename, file_type, qthumbnail=None):
    """Add a file to the settings.

    This function adds a file to the settings, including its filename, type, spacing, size, and thumbnail.

    Args:
        obj: The object representing the file.
        filename (str): The name of the file.
        file_type (str): The type of the file.
        qthumbnail (Optional[QImage]): The thumbnail of the file.


    Raises:
        IndexError: If the input list is empty.
    """

    settings = get_settings()
    settings.beginWriteArray('files')
    files = get_file_reccords_from_settings()
    file_spacing = []
    file_size = []
    file_thumbnail = ''
    if file_type == 'image':
        file_spacing = [s for s in obj.GetSpacing()]
        file_size = [s for s in obj.GetLargestPossibleRegion().GetSize()]
        if qthumbnail is not None:
            data_dir = QStandardPaths.writableLocation(
                QStandardPaths.AppDataLocation
            )
            file_thumbnail = str(uuid.uuid4()) + '.png'
            file_thumbnail = os.path.join(data_dir, file_thumbnail)
            qthumbnail.save(file_thumbnail)
    for i, file in enumerate(files):
        if file.filename == filename:
            settings.setArrayIndex(i)
            settings.setValue('file_type', file_type)
            settings.setValue('file_spacing', file_spacing)
            settings.setValue('file_size', file_size)
            os.remove(file.file_thumbnail)
            settings.setValue('file_thumbnail', file_thumbnail)
            settings.endArray()
            return
    if len(files) > 10:
        os.remove(files[-1].file_thumbnail)
        files.pop(-1)
        for i, file in enumerate(files):
            settings.setArrayIndex(i)
            settings.setValue('filename', file.filename)
            settings.setValue('file_type', file.file_type)
            settings.setValue('file_spacing', file.file_spacing)
            settings.setValue('file_size', file.file_size)
            settings.setValue('file_thumbnail', file.file_thumbnail)
    settings.setArrayIndex(len(files))
    settings.setValue('filename', filename)
    settings.setValue('file_type', file_type)
    settings.setValue('file_spacing', file_spacing)
    settings.setValue('file_size', file_size)
    settings.setValue('file_thumbnail', file_thumbnail)
    settings.endArray()


@time_and_log
def resample_overlay_to_match_image(input_overlay, match_image) -> itk.Image:
    """Resamples an overlay to match the geometry of a given image.

    Args:
        input_overlay (itk.Image): The overlay to be resampled.
        match_image (itk.Image): The image to match.

    Returns:
        itk.Image: The resampled overlay.
    """
    # Resample the overlay to match the geometry of the image
    resampler = itk.ResampleImageFilter[
        itk.Image[itk.RGBAPixel[itk.UC], 3], itk.Image[itk.RGBAPixel[itk.UC], 3]
    ].New()
    resampler.SetInput(input_overlay)
    resampler.SetReferenceImage(match_image)
    resampler.SetUseReferenceImage(True)
    interp = itk.NearestNeighborInterpolateImageFunction[
        itk.Image[itk.RGBAPixel[itk.UC], 3], itk.D
    ].New()
    interp.SetInputImage(input_overlay)
    resampler.SetInterpolator(interp)
    resampler.Update()
    return resampler.GetOutput()


@time_and_log
def add_objects_in_mask_image_to_scene(mask_image, scene):
    """Adds objects in a mask to a scene.

    It extracts the objects from the input mask image and adds them to the provided scene.

    Args:
        mask_image (itk.Image): The mask image containing objects to be added to the scene.
        scene: The scene to which the objects will be added.
    """
    mask_array = itk.GetArrayFromImage(mask_image)
    mask_ids = np.unique(mask_array)
    for mask_num, mask_id in enumerate(mask_ids):
        if mask_id == 0:
            continue
        mask_so = itk.ImageMaskSpatialObject[3].New(Image=mask_image)
        color_name = list(short_colormap)[
            int((mask_num + 1) % len(short_colormap))
        ]
        color = np.empty(4)
        color[0:3] = (
            np.array(short_colormap[color_name]) / short_colormap_scale_factor
        )
        color[3] = 1.0
        mask_so.GetProperty().SetColor(color)
        mask_so.GetProperty().SetName(f'Otsu Threshold Mask {mask_id}')
        mask_so.SetUseMaskValue(True)
        mask_so.SetMaskValue(int(mask_id))
        scene.AddChild(mask_so)


@time_and_log
def get_children_as_list(
    grp: itk.GroupSpatialObject, child_type: str = ''
) -> list:
    """Finds all children of a given type in a Group and returns as a list.

    Args:
        grp (itk.GroupSpatialObject): The GroupSpatialObject to search.
        child_type (str?): The type of object to be included.
            Defaults to "" = all objects.

    Returns:
        list: The list of children of the given type.
    """
    soList = grp.GetChildren(grp.GetMaximumDepth(), child_type)
    return [itk.down_cast(soList[i]) for i in range(len(soList))]


@time_and_log
def get_so_index_in_list(so_id: int, so_list: list) -> int:
    """Finds the index of a so in a list of sos.

    Args:
        so_id (int): The id of the so to find.
        so_list (list): The list of sos to search.

    Returns:
        int: The index of the so in the list.
    """
    id_list = [so.GetId() for so in so_list]
    index = id_list.index(so_id)
    return index


@time_and_log
def get_tag_value_index_in_list_of_dict(tag, value, list_of_dict) -> int:
    """Finds the index of a value for a tag in a list of dicts

    Args:
        tag: The dictionary tag to be used
        value: The tag value being sought
        list_of_dict: List of dictionaries to be searched

    Returns:
        int: The index of the dictionary with that tag/value pair in the list.
    """
    list_of_values = [d.get(tag) for d in list_of_dict]
    try:
        idx = list_of_values.index(value)
        return idx
    except ValueError:
        return -1


@time_and_log
def read_group(filename: str, dims: int = 3) -> itk.GroupSpatialObject:
    """Reads a group from a file.

    Args:
        filename (str): The name of the file to read.
        dims (int, optional): The dimensionality of the group. Defaults to 3.

    Returns:
        itk.GroupSpatialObject: The group read from the file.
    """
    GroupFileReaderType = itk.SpatialObjectReader[dims]

    groupFileReader = GroupFileReaderType.New()
    groupFileReader.SetFileName(filename)
    groupFileReader.Update()

    return groupFileReader.GetGroup()


@time_and_log
def write_group(group: itk.GroupSpatialObject, filename: str):
    """Writes a group to a file.

    Args:
        group (itk.GroupSpatialObject): The group to write.
        filename (str): The name of the file to write to.

    Returns:
        itk.GroupSpatialObject: The group read from the file.
    """
    dims = group.GetObjectDimension()
    GroupFileWriterType = itk.SpatialObjectWriter[dims]

    groupFileWriter = GroupFileWriterType.New()
    groupFileWriter.SetFileName(filename)
    groupFileWriter.SetInput(group)
    groupFileWriter.Update()
