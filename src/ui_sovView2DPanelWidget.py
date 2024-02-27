# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovView2DPanelWidgetveubfP.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

class Ui_View2DPanelWidget(object):
    def setupUi(self, View2DPanelWidget):
        if not View2DPanelWidget.objectName():
            View2DPanelWidget.setObjectName(u"View2DPanelWidget")
        View2DPanelWidget.resize(391, 388)
        self.view2DYZButton = QPushButton(View2DPanelWidget)
        self.view2DYZButton.setObjectName(u"view2DYZButton")
        self.view2DYZButton.setGeometry(QRect(160, 358, 31, 21))
        font = QFont()
        font.setPointSize(7)
        self.view2DYZButton.setFont(font)
        self.view2DXZButton = QPushButton(View2DPanelWidget)
        self.view2DXZButton.setObjectName(u"view2DXZButton")
        self.view2DXZButton.setGeometry(QRect(130, 358, 31, 21))
        self.view2DXZButton.setFont(font)
        self.view2DOverlayOpacitySlider = QSlider(View2DPanelWidget)
        self.view2DOverlayOpacitySlider.setObjectName(u"view2DOverlayOpacitySlider")
        self.view2DOverlayOpacitySlider.setGeometry(QRect(250, 370, 101, 16))
        self.view2DOverlayOpacitySlider.setMaximum(100)
        self.view2DOverlayOpacitySlider.setValue(50)
        self.view2DOverlayOpacitySlider.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget = QWidget(View2DPanelWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 351, 351))
        self.view2DLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.view2DLayout.setObjectName(u"view2DLayout")
        self.view2DLayout.setContentsMargins(0, 0, 0, 0)
        self.view2DOverlayOpacityLabel = QLabel(View2DPanelWidget)
        self.view2DOverlayOpacityLabel.setObjectName(u"view2DOverlayOpacityLabel")
        self.view2DOverlayOpacityLabel.setGeometry(QRect(270, 351, 71, 20))
        self.view2DOverlayOpacityLabel.setFont(font)
        self.view2DOverlayOpacityLabel.setWordWrap(True)
        self.view2DXYButton = QPushButton(View2DPanelWidget)
        self.view2DXYButton.setObjectName(u"view2DXYButton")
        self.view2DXYButton.setGeometry(QRect(100, 358, 31, 21))
        self.view2DXYButton.setFont(font)
        self.view2DSliceText = QPlainTextEdit(View2DPanelWidget)
        self.view2DSliceText.setObjectName(u"view2DSliceText")
        self.view2DSliceText.setGeometry(QRect(355, 326, 31, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view2DSliceText.sizePolicy().hasHeightForWidth())
        self.view2DSliceText.setSizePolicy(sizePolicy)
        self.view2DSliceText.setMinimumSize(QSize(31, 21))
        self.view2DSliceText.setBaseSize(QSize(31, 21))
        self.view2DSliceText.setFont(font)
        self.view2DSliceText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view2DSliceText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view2DSliceText.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.view2DSliceText.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.view2DSliceSlider = QSlider(View2DPanelWidget)
        self.view2DSliceSlider.setObjectName(u"view2DSliceSlider")
        self.view2DSliceSlider.setGeometry(QRect(360, 10, 22, 311))
        self.view2DSliceSlider.setOrientation(Qt.Vertical)
        self.view2DFlipXCheckBox = QCheckBox(View2DPanelWidget)
        self.view2DFlipXCheckBox.setObjectName(u"view2DFlipXCheckBox")
        self.view2DFlipXCheckBox.setGeometry(QRect(200, 353, 41, 16))
        self.view2DFlipXCheckBox.setFont(font)
        self.view2DFlipXCheckBox.setIconSize(QSize(10, 10))
        self.view2DFlipYCheckBox = QCheckBox(View2DPanelWidget)
        self.view2DFlipYCheckBox.setObjectName(u"view2DFlipYCheckBox")
        self.view2DFlipYCheckBox.setGeometry(QRect(200, 369, 41, 16))
        self.view2DFlipYCheckBox.setFont(font)
        self.view2DFlipYCheckBox.setIconSize(QSize(10, 10))
        self.view2DViewLabel = QLabel(View2DPanelWidget)
        self.view2DViewLabel.setObjectName(u"view2DViewLabel")
        self.view2DViewLabel.setGeometry(QRect(0, 360, 21, 16))
        self.view2DViewLabel.setFont(font)
        self.view2DViewComboBox = QComboBox(View2DPanelWidget)
        self.view2DViewComboBox.addItem("")
        self.view2DViewComboBox.addItem("")
        self.view2DViewComboBox.setObjectName(u"view2DViewComboBox")
        self.view2DViewComboBox.setGeometry(QRect(23, 358, 69, 22))
        self.view2DViewComboBox.setFont(font)

        self.retranslateUi(View2DPanelWidget)

        QMetaObject.connectSlotsByName(View2DPanelWidget)
    # setupUi

    def retranslateUi(self, View2DPanelWidget):
        View2DPanelWidget.setWindowTitle(QCoreApplication.translate("View2DPanelWidget", u"Form", None))
        self.view2DYZButton.setText(QCoreApplication.translate("View2DPanelWidget", u"YZ", None))
        self.view2DXZButton.setText(QCoreApplication.translate("View2DPanelWidget", u"XZ", None))
        self.view2DOverlayOpacityLabel.setText(QCoreApplication.translate("View2DPanelWidget", u"Overlay Opacity", None))
        self.view2DXYButton.setText(QCoreApplication.translate("View2DPanelWidget", u"XY", None))
        self.view2DSliceText.setPlainText(QCoreApplication.translate("View2DPanelWidget", u"100", None))
        self.view2DFlipXCheckBox.setText(QCoreApplication.translate("View2DPanelWidget", u"Flip X", None))
        self.view2DFlipYCheckBox.setText(QCoreApplication.translate("View2DPanelWidget", u"Flip Y", None))
        self.view2DViewLabel.setText(QCoreApplication.translate("View2DPanelWidget", u"View:", None))
        self.view2DViewComboBox.setItemText(0, QCoreApplication.translate("View2DPanelWidget", u"Loaded Image", None))
        self.view2DViewComboBox.setItemText(1, QCoreApplication.translate("View2DPanelWidget", u"Pre-processed Image", None))

    # retranslateUi

