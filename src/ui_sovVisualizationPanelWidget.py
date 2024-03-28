# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovVisualizationPanelWidgetIndJDn.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QLabel,
    QPushButton, QSizePolicy, QSlider, QWidget)

class Ui_VisualizationPanelWidget(object):
    def setupUi(self, VisualizationPanelWidget):
        if not VisualizationPanelWidget.objectName():
            VisualizationPanelWidget.setObjectName(u"VisualizationPanelWidget")
        VisualizationPanelWidget.resize(673, 151)
        self.vizIntensityMinMaxResetButton = QPushButton(VisualizationPanelWidget)
        self.vizIntensityMinMaxResetButton.setObjectName(u"vizIntensityMinMaxResetButton")
        self.vizIntensityMinMaxResetButton.setGeometry(QRect(340, 25, 41, 20))
        self.vizIntensityMinSpinBox = QDoubleSpinBox(VisualizationPanelWidget)
        self.vizIntensityMinSpinBox.setObjectName(u"vizIntensityMinSpinBox")
        self.vizIntensityMinSpinBox.setGeometry(QRect(260, 7, 71, 22))
        self.vizIntensityMaxSlider = QSlider(VisualizationPanelWidget)
        self.vizIntensityMaxSlider.setObjectName(u"vizIntensityMaxSlider")
        self.vizIntensityMaxSlider.setGeometry(QRect(90, 37, 160, 22))
        self.vizIntensityMaxSlider.setAutoFillBackground(True)
        self.vizIntensityMaxSlider.setMinimum(-50)
        self.vizIntensityMaxSlider.setMaximum(150)
        self.vizIntensityMaxSlider.setValue(99)
        self.vizIntensityMaxSlider.setTracking(True)
        self.vizIntensityMaxSlider.setOrientation(Qt.Horizontal)
        self.vizIntensityMaxSlider.setInvertedControls(False)
        self.vizIntensityMaxSpinBox = QDoubleSpinBox(VisualizationPanelWidget)
        self.vizIntensityMaxSpinBox.setObjectName(u"vizIntensityMaxSpinBox")
        self.vizIntensityMaxSpinBox.setGeometry(QRect(260, 37, 71, 22))
        self.vizIntensityMinSlider = QSlider(VisualizationPanelWidget)
        self.vizIntensityMinSlider.setObjectName(u"vizIntensityMinSlider")
        self.vizIntensityMinSlider.setGeometry(QRect(90, 7, 160, 22))
        self.vizIntensityMinSlider.setMouseTracking(False)
        self.vizIntensityMinSlider.setAutoFillBackground(True)
        self.vizIntensityMinSlider.setMinimum(-50)
        self.vizIntensityMinSlider.setMaximum(150)
        self.vizIntensityMinSlider.setSliderPosition(2)
        self.vizIntensityMinSlider.setOrientation(Qt.Horizontal)
        self.vizIntensityMinSlider.setInvertedAppearance(False)
        self.vizUpdate2DOverlayButton = QPushButton(VisualizationPanelWidget)
        self.vizUpdate2DOverlayButton.setObjectName(u"vizUpdate2DOverlayButton")
        self.vizUpdate2DOverlayButton.setGeometry(QRect(10, 70, 121, 24))
        self.vizAutoUpdate2DOverlayCheckBox = QCheckBox(VisualizationPanelWidget)
        self.vizAutoUpdate2DOverlayCheckBox.setObjectName(u"vizAutoUpdate2DOverlayCheckBox")
        self.vizAutoUpdate2DOverlayCheckBox.setGeometry(QRect(141, 73, 151, 20))
        self.vizUpdate3DSceneButton = QPushButton(VisualizationPanelWidget)
        self.vizUpdate3DSceneButton.setObjectName(u"vizUpdate3DSceneButton")
        self.vizUpdate3DSceneButton.setGeometry(QRect(10, 107, 121, 24))
        self.vizAutoUpdate3DSceneCheckBox = QCheckBox(VisualizationPanelWidget)
        self.vizAutoUpdate3DSceneCheckBox.setObjectName(u"vizAutoUpdate3DSceneCheckBox")
        self.vizAutoUpdate3DSceneCheckBox.setGeometry(QRect(140, 110, 141, 20))
        self.vizAutoUpdate3DSceneCheckBox.setChecked(True)
        self.vizIntensityMinLabel = QLabel(VisualizationPanelWidget)
        self.vizIntensityMinLabel.setObjectName(u"vizIntensityMinLabel")
        self.vizIntensityMinLabel.setGeometry(QRect(8, 7, 71, 20))
        self.vizIntensityMaxLabel = QLabel(VisualizationPanelWidget)
        self.vizIntensityMaxLabel.setObjectName(u"vizIntensityMaxLabel")
        self.vizIntensityMaxLabel.setGeometry(QRect(8, 37, 71, 20))

        self.retranslateUi(VisualizationPanelWidget)

        QMetaObject.connectSlotsByName(VisualizationPanelWidget)
    # setupUi

    def retranslateUi(self, VisualizationPanelWidget):
        VisualizationPanelWidget.setWindowTitle(QCoreApplication.translate("VisualizationPanelWidget", u"Form", None))
        self.vizIntensityMinMaxResetButton.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Reset", None))
        self.vizUpdate2DOverlayButton.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Update 2D Overlay", None))
        self.vizAutoUpdate2DOverlayCheckBox.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Auto Update 2D Overlay", None))
        self.vizUpdate3DSceneButton.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Update 3D Scene", None))
        self.vizAutoUpdate3DSceneCheckBox.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Auto Update 3D Scene", None))
        self.vizIntensityMinLabel.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Intensity Min", None))
        self.vizIntensityMaxLabel.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Intensity Max", None))
    # retranslateUi

