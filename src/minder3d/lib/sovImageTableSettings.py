import os
import uuid

import itk
import numpy as np
from PySide6.QtCore import QSettings, QStandardPaths, Qt
from PySide6.QtGui import QImage, QPixmap

from .sovUtils import time_and_log


class ImageTableSettingsFileRecord:
    def __init__(
        self,
        filename,
        file_type,
        file_spacing='',
        file_size='',
        file_thumbnail='',
    ):
        """Initialize the object with the provided file details.

        Args:
            filename (str): The name of the file.
            file_type (str): The type of the file.
            file_spacing (str): A list of spacing details. Defaults to ''.
            file_size (str): A list of size details. Defaults to ''.
            file_thumbnail (str): The thumbnail of the file. Defaults to ''.
        """

        self.filename = filename
        self.file_type = file_type
        self.file_spacing = file_spacing
        self.file_size = file_size
        self.file_thumbnail = file_thumbnail


class ImageTableSettings(QSettings):
    def __init__(self):
        settings_file = os.path.join(
            QStandardPaths.writableLocation(QStandardPaths.AppDataLocation),
            'settings_imagetable.ini',
        )
        os.makedirs(os.path.dirname(settings_file), exist_ok=True)
        super().__init__(settings_file, QSettings.IniFormat)

    @time_and_log
    def clear_data(self):
        self.clear()
        self.sync()

    @time_and_log
    def get_file_records(self):
        """Get file records from the settings.

        This function retrieves file records from the settings and returns a list of file records.

        Returns:
            list: A list of file records retrieved from the settings.
        """

        file_records = []
        size = self.beginReadArray('files')
        for i in range(size):
            self.setArrayIndex(i)
            filename = self.value('filename', '')
            if os.path.exists(filename):
                file_type = self.value('file_type', '')
                file_spacing = self.value('file_spacing', '')
                file_size = self.value('file_size', '')
                file_thumbnail = self.value('file_thumbnail', '')
                file = ImageTableSettingsFileRecord(
                    filename, file_type, file_spacing, file_size, file_thumbnail
                )
                file_records.append(file)
        self.endArray()
        return file_records

    @time_and_log
    def add_data(self, obj, filename, file_type, thumbnail_pixmap=None):
        """Add a file to the settings.

        This function adds a file to the settings, including its filename, type,
        spacing, size, and thumbnail.

        Args:
            obj: The object representing the file.
            filename (str): The name of the file.
            file_type (str): The type of the file.
            thumbnail_pixmap (Optional[QPixmap]): The thumbnail of the file.


        Raises:
            IndexError: If the input list is empty.
        """
        filename = os.path.abspath(filename)

        file_records = self.get_file_records()

        file_spacing = ''
        file_size = ''
        file_thumbnail = ''
        if file_type == 'image':
            file_spacing = ','.join([str(s) for s in obj.GetSpacing()])
            file_size = 'x'.join(
                [str(s) for s in obj.GetLargestPossibleRegion().GetSize()]
            )
        elif file_type == 'scene':
            file_size = str(obj.GetNumberOfChildren())
        if thumbnail_pixmap is not None:
            data_dir = QStandardPaths.writableLocation(
                QStandardPaths.AppDataLocation
            )
            file_thumbnail = str(uuid.uuid4()) + '.png'
            file_thumbnail = os.path.join(data_dir, file_thumbnail)
            if not thumbnail_pixmap.save(file_thumbnail):
                file_thumbnail = ''

        self.beginWriteArray('files')
        for i, file in enumerate(file_records):
            if file.filename == filename:
                self.setArrayIndex(i)
                self.setValue('file_type', file_type)
                self.setValue('file_spacing', file_spacing)
                self.setValue('file_size', file_size)
                if file.file_thumbnail != '' and os.path.exists(
                    file.file_thumbnail
                ):
                    os.remove(file.file_thumbnail)
                self.setValue('file_thumbnail', file_thumbnail)
                self.setArrayIndex(len(file_records) - 1)
                self.endArray()
                self.sync()
                return
        if len(file_records) > 10:
            if file_records[-1].file_thumbnail != '' and os.path.exists(
                file_records[-1].file_thumbnail
            ):
                os.remove(file_records[-1].file_thumbnail)
            file_records.pop(-1)
            for i, file in enumerate(file_records):
                self.setArrayIndex(i)
                self.setValue('filename', file.filename)
                self.setValue('file_type', file.file_type)
                self.setValue('file_spacing', file.file_spacing)
                self.setValue('file_size', file.file_size)
                self.setValue('file_thumbnail', file.file_thumbnail)
        self.setArrayIndex(len(file_records))
        self.setValue('filename', filename)
        self.setValue('file_type', file_type)
        self.setValue('file_spacing', file_spacing)
        self.setValue('file_size', file_size)
        self.setValue('file_thumbnail', file_thumbnail)
        self.setArrayIndex(len(file_records) - 1)
        self.endArray()
        self.sync()

    @time_and_log
    def remove_data(self, filename):
        """Remove a file from the settings.

        This function removes a file from the settings.

        Args:
            filename: The name of the file to be removed from settings.

        Raises:
            IndexError: If the input list is empty.
        """
        file_records = self.get_file_records()
        if len(file_records) == 1 and file_records[0].filename == filename:
            self.clear()
            self.sync()
            return
        self.beginWriteArray('files')
        for i, file in enumerate(file_records):
            if file.filename == filename:
                if file.file_thumbnail != '' and os.path.exists(
                    file.file_thumbnail
                ):
                    os.remove(file.file_thumbnail)
                for j in range(i + 1, len(file_records)):
                    next_file = file_records[j]
                    self.setArrayIndex(j - 1)
                    self.setValue('file_filename', next_file.file_filename)
                    self.setValue('file_type', next_file.file_type)
                    self.setValue('file_spacing', next_file.file_spacing)
                    self.setValue('file_size', next_file.file_size)
                    self.setValue('file_thumbnail', next_file.file_thumbnail)
                self.sync()
                return
            else:
                self.setArrayIndex(i)
                self.setValue('filename', file.filename)
                self.setValue('file_type', next_file.file_type)
                self.setValue('file_spacing', next_file.file_spacing)
                self.setValue('file_size', next_file.file_size)
                self.setValue('file_thumbnail', next_file.file_thumbnail)
        self.sync()
        return

    @time_and_log
    def get_thumbnail(self, obj, filename, file_type):
        """Get the thumbnail of a file.

        This function retrieves the thumbnail of a file from the settings.
        """
        files = self.get_file_records()
        for file in files:
            if file.filename == filename:
                return QPixmap(file.file_thumbnail)
        if file_type == 'image':
            return self.get_thumbnail_pixmap_from_image(obj)
        elif file_type == 'scene':
            return QPixmap(':/icons/scene.png')

    @time_and_log
    def get_thumbnail_pixmap_from_image(self, img):
        """Get a thumbnail pixmap from an image."""
        arr = itk.GetArrayFromImage(img)
        flipX = int(np.sign(np.sum(img.GetDirection(), axis=1)[0]))
        flipY = int(np.sign(np.sum(img.GetDirection(), axis=1)[1]))
        thumb_array = arr[arr.shape[0] // 2, ::flipY, ::flipX]
        if len(thumb_array.shape) == 3:
            thumb_array = thumb_array.mean(axis=2).astype(np.uint8)
        auto_range = np.quantile(thumb_array, [0.05, 0.95])
        thumb_array = np.clip(thumb_array, auto_range[0], auto_range[1])
        thumb_array = (
            (thumb_array - auto_range[0])
            / (auto_range[1] - auto_range[0])
            * 255
        ).astype(np.uint8)
        thumb_image = QImage(
            thumb_array.data,
            thumb_array.shape[1],
            thumb_array.shape[0],
            thumb_array.strides[0],
            QImage.Format_Grayscale8,
        )
        thumb_image.setDotsPerMeterX(10 / img.GetSpacing()[0])
        thumb_image.setDotsPerMeterY(10 / img.GetSpacing()[1])
        thumb_pixmap = QPixmap.fromImage(thumb_image).scaled(
            100, 100, Qt.KeepAspectRatio
        )
        return thumb_pixmap
