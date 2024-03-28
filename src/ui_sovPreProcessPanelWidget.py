# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovPreProcessPanelWidgetoMQsYf.ui'
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

class Ui_PreProcessPanelWidget(object):
    def setupUi(self, PreProcessPanelWidget):
        if not PreProcessPanelWidget.objectName():
            PreProcessPanelWidget.setObjectName(u"PreProcessPanelWidget")
        PreProcessPanelWidget.resize(583, 145)
        self.frame = QFrame(PreProcessPanelWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 30, 201, 101))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.preProcessHighResIsoButton = QPushButton(self.frame)
        self.preProcessHighResIsoButton.setObjectName(u"preProcessHighResIsoButton")
        self.preProcessHighResIsoButton.setGeometry(QRect(10, 40, 181, 24))
        self.preProcessIsoButton = QPushButton(self.frame)
        self.preProcessIsoButton.setObjectName(u"preProcessIsoButton")
        self.preProcessIsoButton.setGeometry(QRect(10, 70, 101, 24))
        self.preProcessIsoSpinBox = QDoubleSpinBox(self.frame)
        self.preProcessIsoSpinBox.setObjectName(u"preProcessIsoSpinBox")
        self.preProcessIsoSpinBox.setGeometry(QRect(121, 70, 71, 22))
        self.preProcessIsoSpinBox.setValue(1.000000000000000)
        self.preProcessLowResIsoButton = QPushButton(self.frame)
        self.preProcessLowResIsoButton.setObjectName(u"preProcessLowResIsoButton")
        self.preProcessLowResIsoButton.setGeometry(QRect(10, 10, 181, 24))
        self.frame_2 = QFrame(PreProcessPanelWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(230, 20, 201, 51))
        self.frame_2.setAutoFillBackground(True)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.preProcessClipWindowLevelButton = QPushButton(self.frame_2)
        self.preProcessClipWindowLevelButton.setObjectName(u"preProcessClipWindowLevelButton")
        self.preProcessClipWindowLevelButton.setGeometry(QRect(10, 13, 181, 24))
        self.frame_3 = QFrame(PreProcessPanelWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(230, 90, 201, 51))
        self.frame_3.setAutoFillBackground(True)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.preProcessMedianRadiusSpinBox = QSpinBox(self.frame_3)
        self.preProcessMedianRadiusSpinBox.setObjectName(u"preProcessMedianRadiusSpinBox")
        self.preProcessMedianRadiusSpinBox.setGeometry(QRect(121, 10, 71, 22))
        self.preProcessMedianRadiusSpinBox.setValue(1)
        self.preProcessMedianFilterButton = QPushButton(self.frame_3)
        self.preProcessMedianFilterButton.setObjectName(u"preProcessMedianFilterButton")
        self.preProcessMedianFilterButton.setGeometry(QRect(10, 10, 101, 24))
        self.preProcessCreateNewImageCheckBox = QCheckBox(PreProcessPanelWidget)
        self.preProcessCreateNewImageCheckBox.setObjectName(u"preProcessCreateNewImageCheckBox")
        self.preProcessCreateNewImageCheckBox.setGeometry(QRect(20, 0, 161, 20))
        self.preProcessCreateNewImageCheckBox.setChecked(True)

        self.retranslateUi(PreProcessPanelWidget)

        QMetaObject.connectSlotsByName(PreProcessPanelWidget)
    # setupUi

    def retranslateUi(self, PreProcessPanelWidget):
        PreProcessPanelWidget.setWindowTitle(QCoreApplication.translate("PreProcessPanelWidget", u"Form", None))
        self.preProcessHighResIsoButton.setText(QCoreApplication.translate("PreProcessPanelWidget", u"Make High-Res Isotropic", None))
        self.preProcessIsoButton.setText(QCoreApplication.translate("PreProcessPanelWidget", u"Make Isotropic", None))
        self.preProcessLowResIsoButton.setText(QCoreApplication.translate("PreProcessPanelWidget", u"Make Low-Res Isotropic", None))
        self.preProcessClipWindowLevelButton.setText(QCoreApplication.translate("PreProcessPanelWidget", u"Clip to Window and Level", None))
        self.preProcessMedianFilterButton.setText(QCoreApplication.translate("PreProcessPanelWidget", u"Median Filter", None))
        self.preProcessCreateNewImageCheckBox.setText(QCoreApplication.translate("PreProcessPanelWidget", u"Create New Image", None))
    # retranslateUi

