# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovLungAIPanelWidgetChqglT.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_LungAIPanelWidget(object):
    def setupUi(self, LungAIPanelWidget):
        if not LungAIPanelWidget.objectName():
            LungAIPanelWidget.setObjectName(u"LungAIPanelWidget")
        LungAIPanelWidget.resize(390, 125)
        self.lung1SegAIButton = QPushButton(LungAIPanelWidget)
        self.lung1SegAIButton.setObjectName(u"lung1SegAIButton")
        self.lung1SegAIButton.setGeometry(QRect(10, 30, 261, 24))
        self.lung2SegToModelsButton = QPushButton(LungAIPanelWidget)
        self.lung2SegToModelsButton.setObjectName(u"lung2SegToModelsButton")
        self.lung2SegToModelsButton.setGeometry(QRect(10, 70, 261, 24))

        self.retranslateUi(LungAIPanelWidget)

        QMetaObject.connectSlotsByName(LungAIPanelWidget)
    # setupUi

    def retranslateUi(self, LungAIPanelWidget):
        LungAIPanelWidget.setWindowTitle(QCoreApplication.translate("LungAIPanelWidget", u"Form", None))
        self.lung1SegAIButton.setText(QCoreApplication.translate("LungAIPanelWidget", u"1) Lung Vessel and Airway Segmentation AI", None))
        self.lung2SegToModelsButton.setText(QCoreApplication.translate("LungAIPanelWidget", u"2) Vessel and Airway Segmentations to Models", None))
    # retranslateUi

