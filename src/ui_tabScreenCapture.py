# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabScreenCapturepWVvXk.ui'
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

class Ui_tabScreenCaptureWidget(object):
    def setupUi(self, tabScreenCaptureWidget):
        if not tabScreenCaptureWidget.objectName():
            tabScreenCaptureWidget.setObjectName(u"tabScreenCaptureWidget")
        tabScreenCaptureWidget.resize(283, 123)
        self.scNextImage = QPushButton(tabScreenCaptureWidget)
        self.scNextImage.setObjectName(u"scNextImage")
        self.scNextImage.setGeometry(QRect(170, 50, 31, 24))
        self.scCapture2DButton = QPushButton(tabScreenCaptureWidget)
        self.scCapture2DButton.setObjectName(u"scCapture2DButton")
        self.scCapture2DButton.setGeometry(QRect(130, 0, 71, 24))
        self.scDeleteButton = QPushButton(tabScreenCaptureWidget)
        self.scDeleteButton.setObjectName(u"scDeleteButton")
        self.scDeleteButton.setGeometry(QRect(220, 50, 61, 24))
        self.scPreviousImage = QPushButton(tabScreenCaptureWidget)
        self.scPreviousImage.setObjectName(u"scPreviousImage")
        self.scPreviousImage.setGeometry(QRect(130, 50, 31, 24))
        self.scGraphicsView = QGraphicsView(tabScreenCaptureWidget)
        self.scGraphicsView.setObjectName(u"scGraphicsView")
        self.scGraphicsView.setGeometry(QRect(0, 0, 121, 121))
        self.scCapture3DButton = QPushButton(tabScreenCaptureWidget)
        self.scCapture3DButton.setObjectName(u"scCapture3DButton")
        self.scCapture3DButton.setGeometry(QRect(210, 0, 71, 24))

        self.retranslateUi(tabScreenCaptureWidget)

        QMetaObject.connectSlotsByName(tabScreenCaptureWidget)
    # setupUi

    def retranslateUi(self, tabScreenCaptureWidget):
        tabScreenCaptureWidget.setWindowTitle(QCoreApplication.translate("tabScreenCaptureWidget", u"Form", None))
        self.scNextImage.setText(QCoreApplication.translate("tabScreenCaptureWidget", u">", None))
        self.scCapture2DButton.setText(QCoreApplication.translate("tabScreenCaptureWidget", u"Capture 2D", None))
        self.scDeleteButton.setText(QCoreApplication.translate("tabScreenCaptureWidget", u"Delete", None))
        self.scPreviousImage.setText(QCoreApplication.translate("tabScreenCaptureWidget", u"<", None))
        self.scCapture3DButton.setText(QCoreApplication.translate("tabScreenCaptureWidget", u"Capture 3D", None))
    # retranslateUi

