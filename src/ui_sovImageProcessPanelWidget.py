# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovImageProcessPanelWidgetYCUdLe.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_ImageProcessPanelWidget(object):
    def setupUi(self, ImageProcessPanelWidget):
        if not ImageProcessPanelWidget.objectName():
            ImageProcessPanelWidget.setObjectName(u"ImageProcessPanelWidget")
        ImageProcessPanelWidget.resize(583, 145)
        self.frame = QFrame(ImageProcessPanelWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 30, 201, 101))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.imageProcessHighResIsoButton = QPushButton(self.frame)
        self.imageProcessHighResIsoButton.setObjectName(u"imageProcessHighResIsoButton")
        self.imageProcessHighResIsoButton.setGeometry(QRect(10, 40, 181, 24))
        self.imageProcessIsoButton = QPushButton(self.frame)
        self.imageProcessIsoButton.setObjectName(u"imageProcessIsoButton")
        self.imageProcessIsoButton.setGeometry(QRect(10, 70, 101, 24))
        self.imageProcessIsoSpinBox = QDoubleSpinBox(self.frame)
        self.imageProcessIsoSpinBox.setObjectName(u"imageProcessIsoSpinBox")
        self.imageProcessIsoSpinBox.setGeometry(QRect(121, 70, 71, 22))
        self.imageProcessIsoSpinBox.setValue(1.000000000000000)
        self.imageProcessLowResIsoButton = QPushButton(self.frame)
        self.imageProcessLowResIsoButton.setObjectName(u"imageProcessLowResIsoButton")
        self.imageProcessLowResIsoButton.setGeometry(QRect(10, 10, 181, 24))
        self.frame_2 = QFrame(ImageProcessPanelWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(230, 20, 201, 51))
        self.frame_2.setAutoFillBackground(True)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.imageProcessClipWindowLevelButton = QPushButton(self.frame_2)
        self.imageProcessClipWindowLevelButton.setObjectName(u"imageProcessClipWindowLevelButton")
        self.imageProcessClipWindowLevelButton.setGeometry(QRect(10, 13, 181, 24))
        self.frame_3 = QFrame(ImageProcessPanelWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(230, 90, 201, 51))
        self.frame_3.setAutoFillBackground(True)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.imageProcessMedianRadiusSpinBox = QSpinBox(self.frame_3)
        self.imageProcessMedianRadiusSpinBox.setObjectName(u"imageProcessMedianRadiusSpinBox")
        self.imageProcessMedianRadiusSpinBox.setGeometry(QRect(121, 10, 71, 22))
        self.imageProcessMedianRadiusSpinBox.setValue(1)
        self.imageProcessMedianFilterButton = QPushButton(self.frame_3)
        self.imageProcessMedianFilterButton.setObjectName(u"imageProcessMedianFilterButton")
        self.imageProcessMedianFilterButton.setGeometry(QRect(10, 10, 101, 24))
        self.imageProcessCreateNewImageCheckBox = QCheckBox(ImageProcessPanelWidget)
        self.imageProcessCreateNewImageCheckBox.setObjectName(u"imageProcessCreateNewImageCheckBox")
        self.imageProcessCreateNewImageCheckBox.setGeometry(QRect(20, 0, 161, 20))
        self.imageProcessCreateNewImageCheckBox.setChecked(True)

        self.retranslateUi(ImageProcessPanelWidget)

        QMetaObject.connectSlotsByName(ImageProcessPanelWidget)
    # setupUi

    def retranslateUi(self, ImageProcessPanelWidget):
        ImageProcessPanelWidget.setWindowTitle(QCoreApplication.translate("ImageProcessPanelWidget", u"Form", None))
        self.imageProcessHighResIsoButton.setText(QCoreApplication.translate("ImageProcessPanelWidget", u"Make High-Res Isotropic", None))
        self.imageProcessIsoButton.setText(QCoreApplication.translate("ImageProcessPanelWidget", u"Make Isotropic", None))
        self.imageProcessLowResIsoButton.setText(QCoreApplication.translate("ImageProcessPanelWidget", u"Make Low-Res Isotropic", None))
        self.imageProcessClipWindowLevelButton.setText(QCoreApplication.translate("ImageProcessPanelWidget", u"Clip to Window and Level", None))
        self.imageProcessMedianFilterButton.setText(QCoreApplication.translate("ImageProcessPanelWidget", u"Median Filter", None))
        self.imageProcessCreateNewImageCheckBox.setText(QCoreApplication.translate("ImageProcessPanelWidget", u"Create New Image", None))
    # retranslateUi

