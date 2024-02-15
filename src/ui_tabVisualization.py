# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabVisualizationnRzYjs.ui'
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

class Ui_tabVisualizationWidget(object):
    def setupUi(self, tabVisualizationWidget):
        if not tabVisualizationWidget.objectName():
            tabVisualizationWidget.setObjectName(u"tabVisualizationWidget")
        tabVisualizationWidget.resize(307, 54)
        self.vizIntensityMinMaxReset = QPushButton(tabVisualizationWidget)
        self.vizIntensityMinMaxReset.setObjectName(u"vizIntensityMinMaxReset")
        self.vizIntensityMinMaxReset.setGeometry(QRect(260, 18, 41, 20))
        self.vizIntensityMinSpinBox = QDoubleSpinBox(tabVisualizationWidget)
        self.vizIntensityMinSpinBox.setObjectName(u"vizIntensityMinSpinBox")
        self.vizIntensityMinSpinBox.setGeometry(QRect(170, 0, 81, 22))
        self.vizIntensityMaxSlider = QSlider(tabVisualizationWidget)
        self.vizIntensityMaxSlider.setObjectName(u"vizIntensityMaxSlider")
        self.vizIntensityMaxSlider.setGeometry(QRect(0, 30, 160, 22))
        self.vizIntensityMaxSlider.setAutoFillBackground(True)
        self.vizIntensityMaxSlider.setMinimum(-50)
        self.vizIntensityMaxSlider.setMaximum(150)
        self.vizIntensityMaxSlider.setValue(99)
        self.vizIntensityMaxSlider.setTracking(True)
        self.vizIntensityMaxSlider.setOrientation(Qt.Horizontal)
        self.vizIntensityMaxSlider.setInvertedControls(False)
        self.vizIntensityMaxSpinBox = QDoubleSpinBox(tabVisualizationWidget)
        self.vizIntensityMaxSpinBox.setObjectName(u"vizIntensityMaxSpinBox")
        self.vizIntensityMaxSpinBox.setGeometry(QRect(170, 30, 81, 22))
        self.vizIntensityMinSlider = QSlider(tabVisualizationWidget)
        self.vizIntensityMinSlider.setObjectName(u"vizIntensityMinSlider")
        self.vizIntensityMinSlider.setGeometry(QRect(0, 0, 160, 22))
        self.vizIntensityMinSlider.setMouseTracking(False)
        self.vizIntensityMinSlider.setAutoFillBackground(True)
        self.vizIntensityMinSlider.setMinimum(-50)
        self.vizIntensityMinSlider.setMaximum(150)
        self.vizIntensityMinSlider.setSliderPosition(2)
        self.vizIntensityMinSlider.setOrientation(Qt.Horizontal)
        self.vizIntensityMinSlider.setInvertedAppearance(False)

        self.retranslateUi(tabVisualizationWidget)

        QMetaObject.connectSlotsByName(tabVisualizationWidget)
    # setupUi

    def retranslateUi(self, tabVisualizationWidget):
        tabVisualizationWidget.setWindowTitle(QCoreApplication.translate("tabVisualizationWidget", u"Form", None))
        self.vizIntensityMinMaxReset.setText(QCoreApplication.translate("tabVisualizationWidget", u"Reset", None))
    # retranslateUi

