#!/usr/bin/env python

"""
Launch the minder3D application
"""


from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication

from .minder3DWindow import Minder3DWindow
from .parse_args import parse_args


def main():
    """
    Application entrypoint.

    Parse arguments and pass them to the application
    """
    cli_args = parse_args()

    app = QApplication()

    minder3D = Minder3DWindow()

    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Base, QColor(42, 42, 42))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Dark, QColor(35, 35, 35))
    palette.setColor(QPalette.ColorRole.Shadow, QColor(20, 20, 20))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.black)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(127, 127, 127))
    app.setPalette(palette)
    app.setStyle('Fusion')

    if cli_args.load_image is not None:
        minder3D.load_image(cli_args.load_image)

    if cli_args.load_scene is not None:
        minder3D.load_scene(cli_args.load_scene)

    minder3D.show()

    app.exec()


if __name__ == '__main__':
    main()
