import sys

from ptvWindow import ptvWindow

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    pytubeview = ptvWindow()

    if len(sys.argv)>1:
        pytubeview.loadImage(sys.argv[1])

    sys.exit(app.exec())
