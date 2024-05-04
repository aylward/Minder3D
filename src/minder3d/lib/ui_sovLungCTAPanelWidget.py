# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovLungCTAPanelWidgetrCKdJr.ui'
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

class Ui_LungCTAPanelWidget(object):
    def setupUi(self, LungCTAPanelWidget):
        if not LungCTAPanelWidget.objectName():
            LungCTAPanelWidget.setObjectName(u"LungCTAPanelWidget")
        LungCTAPanelWidget.resize(390, 125)
        self.lungStep1Button = QPushButton(LungCTAPanelWidget)
        self.lungStep1Button.setObjectName(u"lungStep1Button")
        self.lungStep1Button.setGeometry(QRect(10, 30, 261, 24))
        self.lungStep2Button = QPushButton(LungCTAPanelWidget)
        self.lungStep2Button.setObjectName(u"lungStep2Button")
        self.lungStep2Button.setGeometry(QRect(10, 70, 261, 24))

        self.retranslateUi(LungCTAPanelWidget)

        QMetaObject.connectSlotsByName(LungCTAPanelWidget)
    # setupUi

    def retranslateUi(self, LungCTAPanelWidget):
        LungCTAPanelWidget.setWindowTitle(QCoreApplication.translate("LungCTAPanelWidget", u"Form", None))
        self.lungStep1Button.setText(QCoreApplication.translate("LungCTAPanelWidget", u"1) Lung Vessel and Airway Segmentation AI", None))
        self.lungStep2Button.setText(QCoreApplication.translate("LungCTAPanelWidget", u"2) Vessel and Airway Segmentations to Models", None))
    # retranslateUi

