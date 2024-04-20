# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovView2DPanelWidgetOPYfoK.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDoubleSpinBox, QGridLayout,
    QGroupBox, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_View2DPanelWidget(object):
    def setupUi(self, View2DPanelWidget):
        if not View2DPanelWidget.objectName():
            View2DPanelWidget.setObjectName(u"View2DPanelWidget")
        View2DPanelWidget.resize(476, 492)
        self.gridLayout = QGridLayout(View2DPanelWidget)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.view2DImageGroupBox = QGroupBox(View2DPanelWidget)
        self.view2DImageGroupBox.setObjectName(u"view2DImageGroupBox")
        self.view2DImageGroupBox.setMinimumSize(QSize(0, 40))
        self.view2DImageGroupBox.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.view2DImageGroupBox)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.view2DXYButton = QPushButton(self.view2DImageGroupBox)
        self.view2DXYButton.setObjectName(u"view2DXYButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view2DXYButton.sizePolicy().hasHeightForWidth())
        self.view2DXYButton.setSizePolicy(sizePolicy)
        self.view2DXYButton.setMinimumSize(QSize(30, 0))
        font = QFont()
        font.setPointSize(7)
        self.view2DXYButton.setFont(font)

        self.gridLayout_2.addWidget(self.view2DXYButton, 0, 0, 2, 1)

        self.view2DYZButton = QPushButton(self.view2DImageGroupBox)
        self.view2DYZButton.setObjectName(u"view2DYZButton")
        sizePolicy.setHeightForWidth(self.view2DYZButton.sizePolicy().hasHeightForWidth())
        self.view2DYZButton.setSizePolicy(sizePolicy)
        self.view2DYZButton.setMinimumSize(QSize(30, 0))
        self.view2DYZButton.setFont(font)

        self.gridLayout_2.addWidget(self.view2DYZButton, 0, 2, 2, 1)

        self.view2DXZButton = QPushButton(self.view2DImageGroupBox)
        self.view2DXZButton.setObjectName(u"view2DXZButton")
        sizePolicy.setHeightForWidth(self.view2DXZButton.sizePolicy().hasHeightForWidth())
        self.view2DXZButton.setSizePolicy(sizePolicy)
        self.view2DXZButton.setMinimumSize(QSize(30, 0))
        self.view2DXZButton.setFont(font)

        self.gridLayout_2.addWidget(self.view2DXZButton, 0, 1, 2, 1)


        self.gridLayout.addWidget(self.view2DImageGroupBox, 1, 0, 1, 2)

        self.view2DSliceText = QPlainTextEdit(View2DPanelWidget)
        self.view2DSliceText.setObjectName(u"view2DSliceText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.view2DSliceText.sizePolicy().hasHeightForWidth())
        self.view2DSliceText.setSizePolicy(sizePolicy1)
        self.view2DSliceText.setMinimumSize(QSize(0, 0))
        self.view2DSliceText.setMaximumSize(QSize(30, 20))
        self.view2DSliceText.setBaseSize(QSize(31, 21))
        self.view2DSliceText.setFont(font)
        self.view2DSliceText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view2DSliceText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view2DSliceText.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.view2DSliceText.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.gridLayout.addWidget(self.view2DSliceText, 1, 2, 1, 1)

        self.view2DLayout = QVBoxLayout()
        self.view2DLayout.setSpacing(3)
        self.view2DLayout.setObjectName(u"view2DLayout")

        self.gridLayout.addLayout(self.view2DLayout, 0, 0, 1, 2)

        self.view2DSliceSlider = QSlider(View2DPanelWidget)
        self.view2DSliceSlider.setObjectName(u"view2DSliceSlider")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.view2DSliceSlider.sizePolicy().hasHeightForWidth())
        self.view2DSliceSlider.setSizePolicy(sizePolicy2)
        self.view2DSliceSlider.setMinimumSize(QSize(30, 380))
        self.view2DSliceSlider.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.view2DSliceSlider, 0, 2, 1, 1)

        self.view2DIntensityGroupBox = QGroupBox(View2DPanelWidget)
        self.view2DIntensityGroupBox.setObjectName(u"view2DIntensityGroupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.view2DIntensityGroupBox.sizePolicy().hasHeightForWidth())
        self.view2DIntensityGroupBox.setSizePolicy(sizePolicy3)
        self.view2DIntensityGroupBox.setMinimumSize(QSize(0, 45))
        self.view2DIntensityMinSlider = QSlider(self.view2DIntensityGroupBox)
        self.view2DIntensityMinSlider.setObjectName(u"view2DIntensityMinSlider")
        self.view2DIntensityMinSlider.setGeometry(QRect(42, 3, 160, 16))
        self.view2DIntensityMinSlider.setMouseTracking(False)
        self.view2DIntensityMinSlider.setAutoFillBackground(True)
        self.view2DIntensityMinSlider.setMinimum(-50)
        self.view2DIntensityMinSlider.setMaximum(150)
        self.view2DIntensityMinSlider.setValue(0)
        self.view2DIntensityMinSlider.setSliderPosition(0)
        self.view2DIntensityMinSlider.setOrientation(Qt.Horizontal)
        self.view2DIntensityMinSlider.setInvertedAppearance(False)
        self.view2DIntensityMinLabel = QLabel(self.view2DIntensityGroupBox)
        self.view2DIntensityMinLabel.setObjectName(u"view2DIntensityMinLabel")
        self.view2DIntensityMinLabel.setGeometry(QRect(10, 0, 71, 20))
        self.view2DIntensityMinLabel.setFont(font)
        self.view2DIntensityMaxSlider = QSlider(self.view2DIntensityGroupBox)
        self.view2DIntensityMaxSlider.setObjectName(u"view2DIntensityMaxSlider")
        self.view2DIntensityMaxSlider.setGeometry(QRect(42, 24, 160, 16))
        self.view2DIntensityMaxSlider.setAutoFillBackground(True)
        self.view2DIntensityMaxSlider.setMinimum(-50)
        self.view2DIntensityMaxSlider.setMaximum(150)
        self.view2DIntensityMaxSlider.setValue(99)
        self.view2DIntensityMaxSlider.setTracking(True)
        self.view2DIntensityMaxSlider.setOrientation(Qt.Horizontal)
        self.view2DIntensityMaxSlider.setInvertedControls(False)
        self.view2DIntensityMinMaxResetButton = QPushButton(self.view2DIntensityGroupBox)
        self.view2DIntensityMinMaxResetButton.setObjectName(u"view2DIntensityMinMaxResetButton")
        self.view2DIntensityMinMaxResetButton.setGeometry(QRect(280, 12, 41, 20))
        self.view2DIntensityMinMaxResetButton.setFont(font)
        self.view2DIntensityMaxSpinBox = QDoubleSpinBox(self.view2DIntensityGroupBox)
        self.view2DIntensityMaxSpinBox.setObjectName(u"view2DIntensityMaxSpinBox")
        self.view2DIntensityMaxSpinBox.setGeometry(QRect(212, 24, 61, 16))
        self.view2DIntensityMaxSpinBox.setFont(font)
        self.view2DIntensityMaxLabel = QLabel(self.view2DIntensityGroupBox)
        self.view2DIntensityMaxLabel.setObjectName(u"view2DIntensityMaxLabel")
        self.view2DIntensityMaxLabel.setGeometry(QRect(10, 21, 71, 20))
        self.view2DIntensityMaxLabel.setFont(font)
        self.view2DIntensityMinSpinBox = QDoubleSpinBox(self.view2DIntensityGroupBox)
        self.view2DIntensityMinSpinBox.setObjectName(u"view2DIntensityMinSpinBox")
        self.view2DIntensityMinSpinBox.setGeometry(QRect(212, 3, 61, 16))
        self.view2DIntensityMinSpinBox.setFont(font)
        self.view2DOverlayOpacitySlider = QSlider(self.view2DIntensityGroupBox)
        self.view2DOverlayOpacitySlider.setObjectName(u"view2DOverlayOpacitySlider")
        self.view2DOverlayOpacitySlider.setGeometry(QRect(340, 20, 101, 20))
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.view2DOverlayOpacitySlider.sizePolicy().hasHeightForWidth())
        self.view2DOverlayOpacitySlider.setSizePolicy(sizePolicy4)
        self.view2DOverlayOpacitySlider.setMinimumSize(QSize(75, 16))
        self.view2DOverlayOpacitySlider.setMaximum(100)
        self.view2DOverlayOpacitySlider.setValue(50)
        self.view2DOverlayOpacitySlider.setOrientation(Qt.Horizontal)
        self.view2DOverlayOpacityLabel = QLabel(self.view2DIntensityGroupBox)
        self.view2DOverlayOpacityLabel.setObjectName(u"view2DOverlayOpacityLabel")
        self.view2DOverlayOpacityLabel.setGeometry(QRect(356, 0, 71, 20))
        self.view2DOverlayOpacityLabel.setFont(font)

        self.gridLayout.addWidget(self.view2DIntensityGroupBox, 2, 0, 1, 3)


        self.retranslateUi(View2DPanelWidget)

        QMetaObject.connectSlotsByName(View2DPanelWidget)
    # setupUi

    def retranslateUi(self, View2DPanelWidget):
        View2DPanelWidget.setWindowTitle(QCoreApplication.translate("View2DPanelWidget", u"Form", None))
        self.view2DImageGroupBox.setTitle("")
        self.view2DXYButton.setText(QCoreApplication.translate("View2DPanelWidget", u"XY", None))
        self.view2DYZButton.setText(QCoreApplication.translate("View2DPanelWidget", u"YZ", None))
        self.view2DXZButton.setText(QCoreApplication.translate("View2DPanelWidget", u"XZ", None))
        self.view2DSliceText.setPlainText(QCoreApplication.translate("View2DPanelWidget", u"100", None))
        self.view2DIntensityGroupBox.setTitle("")
        self.view2DIntensityMinLabel.setText(QCoreApplication.translate("View2DPanelWidget", u"Min", None))
        self.view2DIntensityMinMaxResetButton.setText(QCoreApplication.translate("View2DPanelWidget", u"Reset", None))
        self.view2DIntensityMaxLabel.setText(QCoreApplication.translate("View2DPanelWidget", u"Max", None))
        self.view2DOverlayOpacityLabel.setText(QCoreApplication.translate("View2DPanelWidget", u"Overlay Opacity", None))
    # retranslateUi

