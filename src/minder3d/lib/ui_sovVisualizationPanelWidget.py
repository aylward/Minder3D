# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovVisualizationPanelWidgetNqZAHr.ui'
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
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_VisualizationPanelWidget(object):
    def setupUi(self, VisualizationPanelWidget):
        if not VisualizationPanelWidget.objectName():
            VisualizationPanelWidget.setObjectName(u"VisualizationPanelWidget")
        VisualizationPanelWidget.resize(582, 174)
        self.viz2DFrame = QFrame(VisualizationPanelWidget)
        self.viz2DFrame.setObjectName(u"viz2DFrame")
        self.viz2DFrame.setGeometry(QRect(0, 0, 231, 101))
        self.viz2DFrame.setFrameShape(QFrame.StyledPanel)
        self.viz2DFrame.setFrameShadow(QFrame.Raised)
        self.vizUpdate2DOverlayButton = QPushButton(self.viz2DFrame)
        self.vizUpdate2DOverlayButton.setObjectName(u"vizUpdate2DOverlayButton")
        self.vizUpdate2DOverlayButton.setGeometry(QRect(100, 10, 121, 24))
        self.vizView2DFlipXCheckBox = QCheckBox(self.viz2DFrame)
        self.vizView2DFlipXCheckBox.setObjectName(u"vizView2DFlipXCheckBox")
        self.vizView2DFlipXCheckBox.setGeometry(QRect(10, 10, 61, 16))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vizView2DFlipXCheckBox.sizePolicy().hasHeightForWidth())
        self.vizView2DFlipXCheckBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(9)
        self.vizView2DFlipXCheckBox.setFont(font)
        self.vizView2DFlipXCheckBox.setIconSize(QSize(10, 10))
        self.vizView2DFlipYCheckBox = QCheckBox(self.viz2DFrame)
        self.vizView2DFlipYCheckBox.setObjectName(u"vizView2DFlipYCheckBox")
        self.vizView2DFlipYCheckBox.setGeometry(QRect(10, 30, 61, 16))
        sizePolicy.setHeightForWidth(self.vizView2DFlipYCheckBox.sizePolicy().hasHeightForWidth())
        self.vizView2DFlipYCheckBox.setSizePolicy(sizePolicy)
        self.vizView2DFlipYCheckBox.setFont(font)
        self.vizView2DFlipYCheckBox.setIconSize(QSize(10, 10))
        self.vizAutoUpdate2DOverlayCheckBox = QCheckBox(self.viz2DFrame)
        self.vizAutoUpdate2DOverlayCheckBox.setObjectName(u"vizAutoUpdate2DOverlayCheckBox")
        self.vizAutoUpdate2DOverlayCheckBox.setGeometry(QRect(130, 40, 91, 20))
        self.vizView2DFlipZCheckBox = QCheckBox(self.viz2DFrame)
        self.vizView2DFlipZCheckBox.setObjectName(u"vizView2DFlipZCheckBox")
        self.vizView2DFlipZCheckBox.setGeometry(QRect(10, 50, 61, 16))
        sizePolicy.setHeightForWidth(self.vizView2DFlipZCheckBox.sizePolicy().hasHeightForWidth())
        self.vizView2DFlipZCheckBox.setSizePolicy(sizePolicy)
        self.vizView2DFlipZCheckBox.setFont(font)
        self.vizView2DFlipZCheckBox.setIconSize(QSize(10, 10))
        self.vizIntensityMinSpinBox = QDoubleSpinBox(self.viz2DFrame)
        self.vizIntensityMinSpinBox.setObjectName(u"vizIntensityMinSpinBox")
        self.vizIntensityMinSpinBox.setGeometry(QRect(87, 70, 51, 22))
        font1 = QFont()
        font1.setPointSize(7)
        self.vizIntensityMinSpinBox.setFont(font1)
        self.vizIntensityMaxSpinBox = QDoubleSpinBox(self.viz2DFrame)
        self.vizIntensityMaxSpinBox.setObjectName(u"vizIntensityMaxSpinBox")
        self.vizIntensityMaxSpinBox.setGeometry(QRect(170, 70, 51, 22))
        self.vizIntensityMaxSpinBox.setFont(font1)
        self.label = QLabel(self.viz2DFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 73, 81, 16))
        self.label_2 = QLabel(self.viz2DFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(143, 71, 31, 20))
        self.label_2.setFont(font)
        self.viz3DFrame = QFrame(VisualizationPanelWidget)
        self.viz3DFrame.setObjectName(u"viz3DFrame")
        self.viz3DFrame.setGeometry(QRect(240, 0, 151, 71))
        self.viz3DFrame.setFrameShape(QFrame.StyledPanel)
        self.viz3DFrame.setFrameShadow(QFrame.Raised)
        self.vizAutoUpdate3DSceneCheckBox = QCheckBox(self.viz3DFrame)
        self.vizAutoUpdate3DSceneCheckBox.setObjectName(u"vizAutoUpdate3DSceneCheckBox")
        self.vizAutoUpdate3DSceneCheckBox.setGeometry(QRect(40, 40, 91, 20))
        self.vizAutoUpdate3DSceneCheckBox.setChecked(True)
        self.vizUpdate3DSceneButton = QPushButton(self.viz3DFrame)
        self.vizUpdate3DSceneButton.setObjectName(u"vizUpdate3DSceneButton")
        self.vizUpdate3DSceneButton.setGeometry(QRect(10, 10, 121, 24))

        self.retranslateUi(VisualizationPanelWidget)

        QMetaObject.connectSlotsByName(VisualizationPanelWidget)
    # setupUi

    def retranslateUi(self, VisualizationPanelWidget):
        VisualizationPanelWidget.setWindowTitle(QCoreApplication.translate("VisualizationPanelWidget", u"Form", None))
        self.vizUpdate2DOverlayButton.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Update 2D Overlay", None))
        self.vizView2DFlipXCheckBox.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Flip X", None))
        self.vizView2DFlipYCheckBox.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Flip Y", None))
        self.vizAutoUpdate2DOverlayCheckBox.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Auto Update", None))
        self.vizView2DFlipZCheckBox.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Flip Z", None))
        self.label.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Intensity Min:", None))
        self.label_2.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Max:", None))
        self.vizAutoUpdate3DSceneCheckBox.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Auto Update", None))
        self.vizUpdate3DSceneButton.setText(QCoreApplication.translate("VisualizationPanelWidget", u"Update 3D Scene", None))
    # retranslateUi

