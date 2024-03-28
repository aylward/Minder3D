"""
Utility functions for working with spatial objects.

This module contains utility functions for working with spatial objects.

Functions:
    get_children_as_list: Finds all children of a given type in a
        GroupSpatialObject and returns them as a list.
    read_group: Reads a group from a file.
    write_group: Writes a group to a file.
"""

import itk

import time
import logging
import functools

from PySide6.QtWidgets import (
    QMainWindow,
    QTextEdit,
)

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
        super().__init__(parent)
        self.setWindowTitle("Log")
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

    def log(self, message, level="info"):
        if level.lower() == "debug":
            self.logger.debug(message)
        elif level.lower() == "info":
            self.logger.info(message)
        elif level.lower() == "warning":
            self.logger.warning(message)
        elif level.lower() == "error":
            self.logger.error(message)
        elif level.lower() == "critical":
            self.logger.critical(message)


def sov_log(message, level="info"):
    logger = logging.getLogger("sov")
    if level.lower() == "debug":
        logger.debug(message)
    elif level.lower() == "info":
        logger.info(message)
    elif level.lower() == "warning":
        logger.warning(message)
    elif level.lower() == "error":
        logger.error(message)
    elif level.lower() == "critical":
        logger.critical(message)


def time_and_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger("sov")
        logger.info(f"Function {func.__name__} started.")
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            logger.info(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
            return result
        except Exception as e:
            end_time = time.time()
            logger.error(f"Function {func.__name__} exception after {end_time - start_time} seconds: {str(e)}")
            raise e
    return wrapper


@time_and_log
def resample_overlay_to_match_image( input_overlay, match_image ) -> itk.Image:
    """Resamples an overlay to match the geometry of a given image.

    Args:
        input_overlay (itk.Image): The overlay to be resampled.
        match_image (itk.Image): The image to match.

    Returns:
        itk.Image: The resampled overlay.
    """
    # Resample the overlay to match the geometry of the image
    resampler = itk.ResampleImageFilter[itk.Image[itk.RGBAPixel[itk.UC],3], itk.Image[itk.RGBAPixel[itk.UC],3]].New()
    resampler.SetInput(input_overlay)
    resampler.SetReferenceImage(match_image)
    resampler.SetUseReferenceImage(True)
    interp = itk.NearestNeighborInterpolateImageFunction[itk.Image[itk.RGBAPixel[itk.UC],3], itk.D].New()
    interp.SetInputImage(input_overlay)
    resampler.SetInterpolator(interp)
    resampler.Update()
    return resampler.GetOutput()


@time_and_log
def get_children_as_list(
    grp: itk.GroupSpatialObject, child_type: str = "Tube"
) -> list:
    """Finds all children of a given type in a Group and returns as a list.

    Args:
        grp (itk.GroupSpatialObject): The GroupSpatialObject to search.
        child_type (str, optional): The type of object to be included.
            Defaults to "Tube".

    Returns:
        list: The list of children of the given type.
    """
    soList = grp.GetChildren(
        grp.GetMaximumDepth(),
        child_type
    )
    return [
        itk.down_cast(soList[i])
        for i in range(len(soList))
    ]


@time_and_log
def get_so_index_in_list(
    so_id: int, so_list: list
) -> int:
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
def get_tag_value_index_in_list_of_dict(
    tag, value, list_of_dict
) -> int:
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
