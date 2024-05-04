# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovScreenCapturePanelWidgetekAshP.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QPushButton, QSizePolicy,
    QWidget)

class Ui_ScreenCapturePanelWidget(object):
    def setupUi(self, ScreenCapturePanelWidget):
        if not ScreenCapturePanelWidget.objectName():
            ScreenCapturePanelWidget.setObjectName(u"ScreenCapturePanelWidget")
        ScreenCapturePanelWidget.resize(283, 123)
        self.scNextImage = QPushButton(ScreenCapturePanelWidget)
        self.scNextImage.setObjectName(u"scNextImage")
        self.scNextImage.setGeometry(QRect(170, 50, 31, 24))
        self.scCapture2DButton = QPushButton(ScreenCapturePanelWidget)
        self.scCapture2DButton.setObjectName(u"scCapture2DButton")
        self.scCapture2DButton.setGeometry(QRect(130, 0, 71, 24))
        self.scDeleteButton = QPushButton(ScreenCapturePanelWidget)
        self.scDeleteButton.setObjectName(u"scDeleteButton")
        self.scDeleteButton.setGeometry(QRect(220, 50, 61, 24))
        self.scPreviousImage = QPushButton(ScreenCapturePanelWidget)
        self.scPreviousImage.setObjectName(u"scPreviousImage")
        self.scPreviousImage.setGeometry(QRect(130, 50, 31, 24))
        self.scGraphicsView = QGraphicsView(ScreenCapturePanelWidget)
        self.scGraphicsView.setObjectName(u"scGraphicsView")
        self.scGraphicsView.setGeometry(QRect(0, 0, 121, 121))
        self.scCapture3DButton = QPushButton(ScreenCapturePanelWidget)
        self.scCapture3DButton.setObjectName(u"scCapture3DButton")
        self.scCapture3DButton.setGeometry(QRect(210, 0, 71, 24))

        self.retranslateUi(ScreenCapturePanelWidget)

        QMetaObject.connectSlotsByName(ScreenCapturePanelWidget)
    # setupUi

    def retranslateUi(self, ScreenCapturePanelWidget):
        ScreenCapturePanelWidget.setWindowTitle(QCoreApplication.translate("ScreenCapturePanelWidget", u"Form", None))
        self.scNextImage.setText(QCoreApplication.translate("ScreenCapturePanelWidget", u">", None))
        self.scCapture2DButton.setText(QCoreApplication.translate("ScreenCapturePanelWidget", u"Capture 2D", None))
        self.scDeleteButton.setText(QCoreApplication.translate("ScreenCapturePanelWidget", u"Delete", None))
        self.scPreviousImage.setText(QCoreApplication.translate("ScreenCapturePanelWidget", u"<", None))
        self.scCapture3DButton.setText(QCoreApplication.translate("ScreenCapturePanelWidget", u"Capture 3D", None))
    # retranslateUi

