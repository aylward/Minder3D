# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preProcessPanelfuzErn.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_PreProcessPanelWidget(object):
    def setupUi(self, PreProcessPanelWidget):
        if not PreProcessPanelWidget.objectName():
            PreProcessPanelWidget.setObjectName(u"PreProcessPanelWidget")
        PreProcessPanelWidget.resize(390, 142)
        self.preprocLowResIsoButton = QPushButton(PreProcessPanelWidget)
        self.preprocLowResIsoButton.setObjectName(u"preprocLowResIsoButton")
        self.preprocLowResIsoButton.setGeometry(QRect(0, 0, 181, 24))
        self.preprocMedianFilterButton = QPushButton(PreProcessPanelWidget)
        self.preprocMedianFilterButton.setObjectName(u"preprocMedianFilterButton")
        self.preprocMedianFilterButton.setGeometry(QRect(210, 0, 121, 24))
        self.preprocHighResIsoButton = QPushButton(PreProcessPanelWidget)
        self.preprocHighResIsoButton.setObjectName(u"preprocHighResIsoButton")
        self.preprocHighResIsoButton.setGeometry(QRect(0, 30, 181, 24))
        self.preprocMedianRadiusBox = QSpinBox(PreProcessPanelWidget)
        self.preprocMedianRadiusBox.setObjectName(u"preprocMedianRadiusBox")
        self.preprocMedianRadiusBox.setGeometry(QRect(340, 0, 42, 22))

        self.retranslateUi(PreProcessPanelWidget)

        QMetaObject.connectSlotsByName(PreProcessPanelWidget)
    # setupUi

    def retranslateUi(self, PreProcessPanelWidget):
        PreProcessPanelWidget.setWindowTitle(QCoreApplication.translate("PreProcessPanelWidget", u"Form", None))
        self.preprocLowResIsoButton.setText(QCoreApplication.translate("PreProcessPanelWidget", u"Make Low-Res Isotropic", None))
        self.preprocMedianFilterButton.setText(QCoreApplication.translate("PreProcessPanelWidget", u"Median Filter", None))
        self.preprocHighResIsoButton.setText(QCoreApplication.translate("PreProcessPanelWidget", u"Make High-Res Isotropic", None))
    # retranslateUi

