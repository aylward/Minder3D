# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabViewvVaiVq.ui'
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

class Ui_tabView(object):
    def setupUi(self, tabView):
        if not tabView.objectName():
            tabView.setObjectName(u"tabView")
        tabView.resize(322, 69)
        self.widget = QWidget(tabView)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 321, 61))
        self.viewIntensityMaxSpinBox = QDoubleSpinBox(self.widget)
        self.viewIntensityMaxSpinBox.setObjectName(u"viewIntensityMaxSpinBox")
        self.viewIntensityMaxSpinBox.setGeometry(QRect(180, 32, 81, 22))
        self.viewIntensityMinSpinBox = QDoubleSpinBox(self.widget)
        self.viewIntensityMinSpinBox.setObjectName(u"viewIntensityMinSpinBox")
        self.viewIntensityMinSpinBox.setGeometry(QRect(180, 2, 81, 22))
        self.viewIntensityMinMaxReset = QPushButton(self.widget)
        self.viewIntensityMinMaxReset.setObjectName(u"viewIntensityMinMaxReset")
        self.viewIntensityMinMaxReset.setGeometry(QRect(270, 20, 41, 20))
        self.viewIntensityMaxSlider = QSlider(self.widget)
        self.viewIntensityMaxSlider.setObjectName(u"viewIntensityMaxSlider")
        self.viewIntensityMaxSlider.setGeometry(QRect(10, 32, 160, 22))
        self.viewIntensityMaxSlider.setAutoFillBackground(True)
        self.viewIntensityMaxSlider.setMinimum(-50)
        self.viewIntensityMaxSlider.setMaximum(150)
        self.viewIntensityMaxSlider.setValue(99)
        self.viewIntensityMaxSlider.setTracking(True)
        self.viewIntensityMaxSlider.setOrientation(Qt.Horizontal)
        self.viewIntensityMaxSlider.setInvertedControls(False)
        self.viewIntensityMinSlider = QSlider(self.widget)
        self.viewIntensityMinSlider.setObjectName(u"viewIntensityMinSlider")
        self.viewIntensityMinSlider.setGeometry(QRect(10, 2, 160, 22))
        self.viewIntensityMinSlider.setMouseTracking(False)
        self.viewIntensityMinSlider.setAutoFillBackground(True)
        self.viewIntensityMinSlider.setMinimum(-50)
        self.viewIntensityMinSlider.setMaximum(150)
        self.viewIntensityMinSlider.setSliderPosition(2)
        self.viewIntensityMinSlider.setOrientation(Qt.Horizontal)
        self.viewIntensityMinSlider.setInvertedAppearance(False)

        self.retranslateUi(tabView)

        QMetaObject.connectSlotsByName(tabView)
    # setupUi

    def retranslateUi(self, tabView):
        tabView.setWindowTitle(QCoreApplication.translate("tabView", u"Form", None))
        self.viewIntensityMinMaxReset.setText(QCoreApplication.translate("tabView", u"Reset", None))
    # retranslateUi

