# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabViewFJlRDd.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QPushButton, QSizePolicy,
    QSlider, QWidget)

class Ui_tabViewWidget(object):
    def setupUi(self, tabViewWidget):
        if not tabViewWidget.objectName():
            tabViewWidget.setObjectName(u"tabViewWidget")
        tabViewWidget.resize(307, 54)
        self.viewIntensityMinMaxReset = QPushButton(tabViewWidget)
        self.viewIntensityMinMaxReset.setObjectName(u"viewIntensityMinMaxReset")
        self.viewIntensityMinMaxReset.setGeometry(QRect(260, 18, 41, 20))
        self.viewIntensityMinSpinBox = QDoubleSpinBox(tabViewWidget)
        self.viewIntensityMinSpinBox.setObjectName(u"viewIntensityMinSpinBox")
        self.viewIntensityMinSpinBox.setGeometry(QRect(170, 0, 81, 22))
        self.viewIntensityMaxSlider = QSlider(tabViewWidget)
        self.viewIntensityMaxSlider.setObjectName(u"viewIntensityMaxSlider")
        self.viewIntensityMaxSlider.setGeometry(QRect(0, 30, 160, 22))
        self.viewIntensityMaxSlider.setAutoFillBackground(True)
        self.viewIntensityMaxSlider.setMinimum(-50)
        self.viewIntensityMaxSlider.setMaximum(150)
        self.viewIntensityMaxSlider.setValue(99)
        self.viewIntensityMaxSlider.setTracking(True)
        self.viewIntensityMaxSlider.setOrientation(Qt.Horizontal)
        self.viewIntensityMaxSlider.setInvertedControls(False)
        self.viewIntensityMaxSpinBox = QDoubleSpinBox(tabViewWidget)
        self.viewIntensityMaxSpinBox.setObjectName(u"viewIntensityMaxSpinBox")
        self.viewIntensityMaxSpinBox.setGeometry(QRect(170, 30, 81, 22))
        self.viewIntensityMinSlider = QSlider(tabViewWidget)
        self.viewIntensityMinSlider.setObjectName(u"viewIntensityMinSlider")
        self.viewIntensityMinSlider.setGeometry(QRect(0, 0, 160, 22))
        self.viewIntensityMinSlider.setMouseTracking(False)
        self.viewIntensityMinSlider.setAutoFillBackground(True)
        self.viewIntensityMinSlider.setMinimum(-50)
        self.viewIntensityMinSlider.setMaximum(150)
        self.viewIntensityMinSlider.setSliderPosition(2)
        self.viewIntensityMinSlider.setOrientation(Qt.Horizontal)
        self.viewIntensityMinSlider.setInvertedAppearance(False)

        self.retranslateUi(tabViewWidget)

        QMetaObject.connectSlotsByName(tabViewWidget)
    # setupUi

    def retranslateUi(self, tabViewWidget):
        tabViewWidget.setWindowTitle(QCoreApplication.translate("tabViewWidget", u"Form", None))
        self.viewIntensityMinMaxReset.setText(QCoreApplication.translate("tabViewWidget", u"Reset", None))
    # retranslateUi

