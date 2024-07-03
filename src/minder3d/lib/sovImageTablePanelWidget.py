"""This module provides the ImageTablePanelWidget class."""

import os

from itk import imread
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QHeaderView,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)

from .sovImageTableSettings import ImageTableSettings
from .sovUtils import time_and_log
from .ui_sovImageTablePanelWidget import Ui_ImageTablePanelWidget


class ImageTablePanelWidget(QWidget, Ui_ImageTablePanelWidget):
    @time_and_log
    def __init__(self, gui, state, parent=None):
        """Initialize the GUI and state for the application.

        Args:
            gui: The graphical user interface object.
            state: The state object for the application.
            parent: The parent widget (default is None).
        """

        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.settings = ImageTableSettings()

        self.imageTableWidget.setRowCount(0)
        self.imageTableWidget.setColumnCount(6)
        self.imageTableWidget.setHorizontalHeaderLabels(
            ['Loaded', 'Type', 'Thumbnail', 'Filename', 'Size', 'Spacing']
        )
        self.imageTableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.imageTableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.imageTableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.imageTableWidget.setShowGrid(True)
        self.imageTableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )
        self.imageTableWidget.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )
        self.imageTableWidget.setIconSize(QSize(75, 75))
        self.imageTableWidget.verticalHeader().hide()
        self.imageTableWidget.setStyleSheet(
            'QTableView{ selection-background-color: rgba(0, 50, 0, 50);  }'
        )

        self.imageTableWidget.cellClicked.connect(self.select_data_by_table)

        self.imageTableUnloadButton.clicked.connect(self.unload_image)
        self.imageTableRemoveButton.clicked.connect(self.remove_image)
        self.imageTableRemoveAllButton.clicked.connect(self.remove_all)
        self.imageTableExpandButton.clicked.connect(self.expand_table)

        self.enlarged_table = None

        self.fill_table()

    @time_and_log
    def unload_image(self):
        self.gui.unload_image(self.state.current_image_num, False)
        self.fill_table()

    def remove_image(self):
        self.settings.remove_data(
            self.state.image_filename[self.state.current_image_num]
        )
        self.gui.unload_image(self.state.current_image_num, False)
        self.fill_table()

    def remove_all(self):
        num_images = len(self.state.image_filename)
        for i in range(num_images - 1, 0, -1):
            self.settings.remove_data(self.state.image_filename[i])
        self.gui.unload_image(self.state.current_image_num, False)
        self.settings.clear_data()
        self.fill_table()

    def close_expanded_table(self):
        self.enlarged_table.close()
        self.enlarged_table = None

    def expand_table(self):
        if self.enlarged_table is None:
            self.enlarged_table = ImageTablePanelWidget(self.gui, self.state)
            self.enlarged_table.setWindowTitle('Image Table')
            self.enlarged_table.imageTableExpandButton.setText('CLOSE')
            self.enlarged_table.imageTableExpandButton.setMinimumWidth(75)
            self.enlarged_table.imageTableExpandButton.clicked.disconnect()
            self.enlarged_table.imageTableExpandButton.clicked.connect(
                self.close_expanded_table
            )
            self.enlarged_table.show()
        else:
            self.enlarged_table.show()

    @time_and_log
    def update_image(self):
        self.fill_table()
        self.imageTableWidget.selectRow(self.state.current_image_num)

    @time_and_log
    def update_scene(self):
        self.fill_table()
        self.imageTableWidget.selectRow(self.state.current_image_num)

    @time_and_log
    def redraw_image_row(self, row_num):
        """Redraws the image at the specified index in the image table widget.

        This function updates the information displayed in the image table
        widget for the image at the specified index.

        Args:
            self: The object instance.
            img_num (int): The index of the image to be redrawn.


        Raises:
            IndexError: If the specified img_num is out of range.
        """

        img_num = row_num
        if img_num < len(self.state.image_filename):
            self.imageTableWidget.setItem(
                row_num, 0, QTableWidgetItem(str('X'))
            )
        else:
            self.imageTableWidget.setItem(row_num, 0, QTableWidgetItem(str('')))
        self.imageTableWidget.setItem(
            row_num, 1, QTableWidgetItem(str('Image'))
        )
        self.imageTableWidget.setItem(
            row_num,
            2,
            QTableWidgetItem(QIcon(self.state.image_thumbnail[img_num]), ''),
        )
        filename = self.state.image_filename[img_num]
        self.imageTableWidget.setItem(row_num, 3, QTableWidgetItem(filename))
        size_str = [
            str(i)
            for i in self.state.image[img_num]
            .GetLargestPossibleRegion()
            .GetSize()
        ]
        self.imageTableWidget.setItem(
            row_num, 4, QTableWidgetItem('x'.join(size_str))
        )
        spacing_str = [
            f'{i:.4f}' for i in self.state.image[img_num].GetSpacing()
        ]
        self.imageTableWidget.setItem(
            row_num, 5, QTableWidgetItem(','.join(spacing_str))
        )

    @time_and_log
    def redraw_scene_row(self, row_num, selected=False):
        if selected or (
            self.imageTableWidget.item(row_num, 3) is not None
            and self.imageTableWidget.item(row_num, 3).text()
            == self.state.scene_filename
        ):
            self.imageTableWidget.setItem(
                row_num, 0, QTableWidgetItem(str('X'))
            )
        else:
            self.imageTableWidget.setItem(row_num, 0, QTableWidgetItem(str('')))
        self.imageTableWidget.setItem(
            row_num, 1, QTableWidgetItem(str('Scene'))
        )
        self.imageTableWidget.setItem(
            row_num, 2, QTableWidgetItem(QIcon(self.state.scene_thumbnail), '')
        )
        self.imageTableWidget.setItem(
            row_num, 3, QTableWidgetItem(str(self.state.scene_filename))
        )
        size = self.state.scene.GetNumberOfChildren()
        self.imageTableWidget.setItem(row_num, 4, QTableWidgetItem(str(size)))
        self.imageTableWidget.setItem(row_num, 5, QTableWidgetItem(str('')))

    @time_and_log
    def fill_table(self):
        """Fill the image table with images from the state and from settings.

        This method clears the existing image table and fills it with image
        records from the state. It then retrieves file records from the
        settings and adds them to the table if they are not already present.
        For each file record, it populates the table with the file's thumbnail,
        filename, size, and spacing.

        Args:
            self: The instance of the class.
        """

        self.imageTableWidget.clear()
        self.imageTableWidget.setRowCount(0)
        self.imageTableWidget.setHorizontalHeaderLabels(
            ['Loaded', 'Type', 'Thumbnail', 'Filename', 'Size', 'Spacing']
        )
        row_num = 0
        for _ in range(len(self.state.image)):
            self.imageTableWidget.insertRow(row_num)
            self.redraw_image_row(row_num)
            row_num += 1
        if self.state.scene.GetNumberOfChildren() > 0:
            self.imageTableWidget.insertRow(row_num)
            self.redraw_scene_row(row_num, selected=True)
            row_num += 1

        file_records = self.settings.get_file_records()
        for file in file_records:
            if (
                file.filename not in self.state.image_filename
                and file.file_type == 'image'
            ):
                self.imageTableWidget.insertRow(row_num)
                self.imageTableWidget.setItem(
                    row_num, 1, QTableWidgetItem('Image')
                )
                if file.file_thumbnail != '':
                    qthumb = QPixmap(file.file_thumbnail)
                    self.imageTableWidget.setItem(
                        row_num, 2, QTableWidgetItem(QIcon(qthumb), '')
                    )
                self.imageTableWidget.setItem(
                    row_num, 3, QTableWidgetItem(str(file.filename))
                )
                self.imageTableWidget.setItem(
                    row_num, 4, QTableWidgetItem(str(file.file_size))
                )
                self.imageTableWidget.setItem(
                    row_num, 5, QTableWidgetItem(str(file.file_spacing))
                )
                row_num += 1
            elif (
                file.filename != self.state.scene_filename
                and file.file_type == 'scene'
            ):
                self.imageTableWidget.insertRow(row_num)
                self.imageTableWidget.setItem(
                    row_num, 1, QTableWidgetItem('Scene')
                )
                qthumb = QPixmap(file.file_thumbnail)
                self.imageTableWidget.setItem(
                    row_num, 2, QTableWidgetItem(QIcon(qthumb), '')
                )
                self.imageTableWidget.setItem(
                    row_num, 3, QTableWidgetItem(file.filename)
                )
                self.imageTableWidget.setItem(
                    row_num, 4, QTableWidgetItem(file.file_size)
                )
                row_num += 1

    @time_and_log
    def create_new_image(self):
        self.state.image_thumbnail.append(
            self.settings.get_thumbnail(
                self.state.image[-1], self.state.image_filename[-1], 'image'
            )
        )
        self.settings.add_data(
            self.state.image[-1],
            self.state.image_filename[-1],
            'image',
            self.state.image_thumbnail[-1],
        )
        self.fill_table()

    @time_and_log
    def save_image(self, filename):
        self.settings.add_data(
            self.state.image[self.state.current_image_num],
            filename,
            'image',
            self.state.image_thumbnail[self.state.current_image_num],
        )
        self.fill_table()

    @time_and_log
    def load_scene(self):
        self.state.scene_thumbnail = self.settings.get_thumbnail(
            self.state.scene, self.state.scene_filename, 'scene'
        )
        self.settings.add_data(
            self.state.scene,
            self.state.scene_filename,
            'scene',
            self.state.scene_thumbnail,
        )
        self.fill_table()

    @time_and_log
    def save_scene(self, filename):
        self.settings.add_data(
            self.state.scene, filename, 'scene', self.state.scene_thumbnail
        )

    @time_and_log
    def replace_image(self, img_num):
        self.redraw_image_row(img_num)

    @time_and_log
    def select_data_by_table(self, row, _):
        if row < len(self.state.image_filename):
            self.state.current_image_num = row
            self.gui.update_image()
            if self.state.view2D_overlay_auto_update:
                self.gui.update_overlay()
        elif (
            row > 0
            and row == len(self.state.image_filename)
            and self.state.scene_filename
            == self.imageTableWidget.item(row, 3).text()
        ):
            # current scene
            return
        else:
            if self.imageTableWidget.item(row, 1).text() == 'Image':
                self.gui.load_image(self.imageTableWidget.item(row, 3).text())
            elif self.imageTableWidget.item(row, 1).text() == 'Scene':
                self.gui.load_scene(self.imageTableWidget.item(row, 3).text())

    @time_and_log
    def register_images(self, dir, first=True):
        files = [
            os.path.join(dir, f)
            for f in os.listdir(dir)
            if os.path.isfile(os.path.join(dir, f))
        ]
        dicom_dir = False
        for filename in files:
            if filename.lower().endswith('.dcm') or filename.endswith(''):
                if dicom_dir:
                    continue
                else:
                    print(f"Adding DICOM object '{filename}' to settings")
                    filename = dir
                    dicom_dir = True
            else:
                print(f"Adding NON-DICOM image '{filename}' to settings")
            try:
                img = imread(filename)
            except Exception:
                continue
            thumbnail = self.settings.get_thumbnail(img, filename, 'image')
            print(f'Adding {filename} to settings')
            self.settings.add_data(
                img,
                filename,
                'image',
                thumbnail,
            )

        dirs = [
            os.path.join(dir, d)
            for d in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, d))
        ]
        for dirname in dirs:
            self.register_images(dirname, False)

        if first:
            self.fill_table()
