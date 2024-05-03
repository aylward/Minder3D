from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QHeaderView,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)

from sovImageTablePanelUtils import get_qthumbnail_from_array
from sovUtils import get_file_reccords_from_settings, time_and_log
from ui_sovImageTablePanelWidget import Ui_ImageTablePanelWidget


class ImageTablePanelWidget(QWidget, Ui_ImageTablePanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.imageTableWidget.setRowCount(0)
        self.imageTableWidget.setColumnCount(5)
        self.imageTableWidget.setHorizontalHeaderLabels(
            ['Loaded', 'Filename', 'Size', 'Spacing', 'Thumbnail']
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

        self.imageTableWidget.cellClicked.connect(self.select_image_by_table)

        self.fill_table()

    def update_image(self):
        self.imageTableWidget.selectRow(self.state.current_image_num)

    @time_and_log
    def redraw_image(self, img_num):
        self.imageTableWidget.setItem(
            img_num, 0, QTableWidgetItem(str(img_num))
        )
        qthumb = get_qthumbnail_from_array(
            self.state.image_array[img_num][
                self.state.image_array[img_num].shape[0] // 2, ::-1, :
            ]
        )
        self.imageTableWidget.setItem(
            img_num, 1, QTableWidgetItem(QIcon(qthumb), '')
        )
        filename = self.state.image_filename[img_num][-20:]
        self.imageTableWidget.setItem(img_num, 2, QTableWidgetItem(filename))
        size_str = [
            str(i)
            for i in self.state.image[img_num]
            .GetLargestPossibleRegion()
            .GetSize()
        ]
        self.imageTableWidget.setItem(
            img_num, 3, QTableWidgetItem('x'.join(size_str))
        )
        spacing_str = [
            f'{i:.4f}' for i in self.state.image[img_num].GetSpacing()
        ]
        self.imageTableWidget.setItem(
            img_num, 4, QTableWidgetItem(', '.join(spacing_str))
        )

    @time_and_log
    def fill_table(self):
        self.imageTableWidget.clear()
        for img_num in range(len(self.state.image)):
            self.imageTableWidget.insertRow(img_num)
            self.redraw_image(img_num)
        file_records = get_file_reccords_from_settings()
        img_num = self.imageTableWidget.rowCount()
        for file in file_records:
            if (
                file.filename not in self.state.image_filename
                and file.file_type == 'image'
            ):
                self.imageTableWidget.insertRow(img_num)
                qthumb = QPixmap(file.file_thumbnail)
                self.imageTableWidget.setItem(
                    img_num, 1, QTableWidgetItem(QIcon(qthumb), '')
                )
                self.imageTableWidget.setItem(
                    img_num, 2, QTableWidgetItem(file.filename)
                )
                if type(file.file_size) == type([]) and len(file.file_size) > 0:
                    size_str = [str(i) for i in file.file_size]
                    self.imageTableWidget.setItem(
                        img_num, 3, QTableWidgetItem('x'.join(size_str))
                    )
                if (
                    type(file.file_spacing) == type([])
                    and len(file.file_spacing) > 0
                ):
                    spacing_str = [f'{i:.4f}' for i in file.file_spacing]
                    self.imageTableWidget.setItem(
                        img_num, 4, QTableWidgetItem(', '.join(spacing_str))
                    )
                img_num += 1

    def create_new_image(self):
        img_num = self.state.current_image_num
        self.imageTableWidget.insertRow(img_num)
        self.redraw_image(img_num)

    def replace_image(self, img_num):
        self.redraw_image(img_num)

    def select_image_by_table(self, row, _):
        sel_num = int(self.imageTableWidget.item(row, 0).text())
        if self.state.current_image_num == sel_num:
            return

        self.state.current_image_num = sel_num
        self.gui.update_image()

        if self.state.view2D_overlay_auto_update:
            self.gui.update_overlay()
