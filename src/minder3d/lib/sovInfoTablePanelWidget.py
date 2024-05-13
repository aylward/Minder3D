from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QWidget

from .sovUtils import time_and_log
from .ui_sovInfoTablePanelWidget import Ui_InfoTablePanelWidget


class InfoTablePanelWidget(QWidget, Ui_InfoTablePanelWidget):
    @time_and_log
    def __init__(self, gui, state, parent=None):
        """Initialize the GUI and state for the parent widget.

        Args:
            gui: The graphical user interface object.
            state: The state object.
            parent: The parent widget (default is None).
        """
        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.infoTableWidget.setRowCount(3)
        self.infoTableWidget.setColumnCount(2)
        self.infoTableWidget.setItem(0, 0, QTableWidgetItem('Pixel Coordinate'))
        self.infoTableWidget.setItem(1, 0, QTableWidgetItem('  Image Value'))
        self.infoTableWidget.setItem(2, 0, QTableWidgetItem('  Overlay Value'))
        self.infoTableWidget.setColumnWidth(1, 200)
        self.infoTableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.infoTableWidget.setSelectionMode(QTableWidget.NoSelection)
        self.infoTableWidget.setShowGrid(True)
        self.infoTableWidget.verticalHeader().hide()
        self.infoTableWidget.setStyleSheet(
            'QTableView{ selection-background-color: rgba(0, 50, 0, 50);  }'
        )
        self.infoTableWidget.setUpdatesEnabled(True)

    @time_and_log
    def update_image(self):
        pass

    @time_and_log
    def update_pixel(self):
        """Update the pixel information in the info table widget.

        This function updates the pixel information in the info table widget
        with the current pixel position and default values for other
        attributes.

        Args:
            self (object): The instance of the class.
        """

        pos_str = ', '.join(
            [f'{x:0.1f}' for x in self.state.current_pixel_position]
        )
        self.infoTableWidget.setItem(0, 1, QTableWidgetItem(pos_str))
        print(self.state.current_pixel_index)
        if (
            self.state.image[self.state.current_image_num]
            .GetLargestPossibleRegion()
            .IsInside(self.state.current_pixel_index)
        ):
            img_val = self.state.image[self.state.current_image_num].GetPixel(
                self.state.current_pixel_index
            )
            if (
                self.state.image_max[self.state.current_image_num]
                - self.state.image_min[self.state.current_image_num]
            ) < 1:
                self.infoTableWidget.setItem(
                    1, 1, QTableWidgetItem(f'{img_val:0.4f}')
                )
            else:
                self.infoTableWidget.setItem(
                    1, 1, QTableWidgetItem(f'{img_val:0.1f}')
                )
            self.infoTableWidget.setItem(2, 1, QTableWidgetItem('0'))
        else:
            self.infoTableWidget.setItem(1, 1, QTableWidgetItem('Outside'))
            self.infoTableWidget.setItem(2, 1, QTableWidgetItem('Outside'))
