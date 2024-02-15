# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabPreProcessPXdzHr.ui'
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

class Ui_tabPreProcessWidget(object):
    def setupUi(self, tabPreProcessWidget):
        if not tabPreProcessWidget.objectName():
            tabPreProcessWidget.setObjectName(u"tabPreProcessWidget")
        tabPreProcessWidget.resize(390, 142)
        self.preprocLowResIsoButton = QPushButton(tabPreProcessWidget)
        self.preprocLowResIsoButton.setObjectName(u"preprocLowResIsoButton")
        self.preprocLowResIsoButton.setGeometry(QRect(0, 0, 181, 24))
        self.preprocMedianFilterButton = QPushButton(tabPreProcessWidget)
        self.preprocMedianFilterButton.setObjectName(u"preprocMedianFilterButton")
        self.preprocMedianFilterButton.setGeometry(QRect(210, 0, 121, 24))
        self.preprocHighResIsoButton = QPushButton(tabPreProcessWidget)
        self.preprocHighResIsoButton.setObjectName(u"preprocHighResIsoButton")
        self.preprocHighResIsoButton.setGeometry(QRect(0, 30, 181, 24))
        self.preprocMedianRadiusBox = QSpinBox(tabPreProcessWidget)
        self.preprocMedianRadiusBox.setObjectName(u"preprocMedianRadiusBox")
        self.preprocMedianRadiusBox.setGeometry(QRect(340, 0, 42, 22))

        self.retranslateUi(tabPreProcessWidget)

        QMetaObject.connectSlotsByName(tabPreProcessWidget)
    # setupUi

    def retranslateUi(self, tabPreProcessWidget):
        tabPreProcessWidget.setWindowTitle(QCoreApplication.translate("tabPreProcessWidget", u"Form", None))
        self.preprocLowResIsoButton.setText(QCoreApplication.translate("tabPreProcessWidget", u"Make Low-Res Isotropic", None))
        self.preprocMedianFilterButton.setText(QCoreApplication.translate("tabPreProcessWidget", u"Median Filter", None))
        self.preprocHighResIsoButton.setText(QCoreApplication.translate("tabPreProcessWidget", u"Make High-Res Isotropic", None))
    # retranslateUi

