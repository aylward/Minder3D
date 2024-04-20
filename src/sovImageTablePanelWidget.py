from PySide6.QtCore import (
    Qt,
    QAbstractTableModel,
)
from PySide6.QtWidgets import (
    QWidget,
)

from sovUtils import time_and_log

from ui_sovImageTablePanelWidget import Ui_ImageTablePanelWidget


class ImageTableDictionary(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.dict = dict()

    def rowCount(self, index):
        return len(self.dict.keys())

    def columnCount(self, index):
        return 2

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole: #or role == Qt.EditRole:
                if index.column() == 0:
                    return list(self.dict.keys())[index.row()]
                return list(self.dict.values())[index.row()]
        return None

    def setDict(self, key, value):
        row = list(self.dict.keys()).index(key)
        col = 1
        index = self.index(row, col)
        self.setData(index, value, Qt.EditRole)

    def setData(self, index, value, role):
        if role == Qt.EditRole and index.column() == 1:
            key = list(self.dict.keys())[index.row()]
            self.dict[key] = value
            return True
        return False

    def flags(self, index):
        return Qt.NoItemFlags


class ImageTablePanelWidget(QWidget, Ui_ImageTablePanelWidget):
    def __init__(self, gui, state, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.table = ImageTableDictionary()
        self.table.dict["Image Name"] = "0, 0, 0"
        self.imageTableView.setModel(self.table)

    @time_and_log
    def update_image(self):
        img_size = self.state.image[self.state.current_image_num].GetLargestPossibleRegion().GetSize()
        self.table.setDict(
            'Image Name',
            f'{img_size[0]}, {img_size[1]}, {img_size[2]}')
        self.imageTableView.repaint()

    @time_and_log
    def update_pixel(self):
        pass