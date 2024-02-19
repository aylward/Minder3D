# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabView2DquBFIH.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSlider, QVBoxLayout,
    QWidget)

class Ui_tabView2DWidget(object):
    def setupUi(self, tabView2DWidget):
        if not tabView2DWidget.objectName():
            tabView2DWidget.setObjectName(u"tabView2DWidget")
        tabView2DWidget.resize(391, 388)
        self.view2DYZButton = QPushButton(tabView2DWidget)
        self.view2DYZButton.setObjectName(u"view2DYZButton")
        self.view2DYZButton.setGeometry(QRect(140, 360, 61, 24))
        self.view2DXZButton = QPushButton(tabView2DWidget)
        self.view2DXZButton.setObjectName(u"view2DXZButton")
        self.view2DXZButton.setGeometry(QRect(70, 360, 61, 24))
        self.view2DOverlayOpacitySlider = QSlider(tabView2DWidget)
        self.view2DOverlayOpacitySlider.setObjectName(u"view2DOverlayOpacitySlider")
        self.view2DOverlayOpacitySlider.setGeometry(QRect(260, 364, 91, 16))
        self.view2DOverlayOpacitySlider.setValue(50)
        self.view2DOverlayOpacitySlider.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget = QWidget(tabView2DWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 351, 351))
        self.view2DLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.view2DLayout.setObjectName(u"view2DLayout")
        self.view2DLayout.setContentsMargins(0, 0, 0, 0)
        self.view2DOverlayOpacityLabel = QLabel(tabView2DWidget)
        self.view2DOverlayOpacityLabel.setObjectName(u"view2DOverlayOpacityLabel")
        self.view2DOverlayOpacityLabel.setGeometry(QRect(220, 355, 51, 31))
        font = QFont()
        font.setPointSize(7)
        self.view2DOverlayOpacityLabel.setFont(font)
        self.view2DOverlayOpacityLabel.setWordWrap(True)
        self.view2DXYButton = QPushButton(tabView2DWidget)
        self.view2DXYButton.setObjectName(u"view2DXYButton")
        self.view2DXYButton.setGeometry(QRect(0, 360, 61, 24))
        self.view2DSliceText = QPlainTextEdit(tabView2DWidget)
        self.view2DSliceText.setObjectName(u"view2DSliceText")
        self.view2DSliceText.setGeometry(QRect(355, 330, 31, 21))
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
        self.view2DSliceSlider = QSlider(tabView2DWidget)
        self.view2DSliceSlider.setObjectName(u"view2DSliceSlider")
        self.view2DSliceSlider.setGeometry(QRect(360, 10, 22, 311))
        self.view2DSliceSlider.setOrientation(Qt.Vertical)

        self.retranslateUi(tabView2DWidget)

        QMetaObject.connectSlotsByName(tabView2DWidget)
    # setupUi

    def retranslateUi(self, tabView2DWidget):
        tabView2DWidget.setWindowTitle(QCoreApplication.translate("tabView2DWidget", u"Form", None))
        self.view2DYZButton.setText(QCoreApplication.translate("tabView2DWidget", u"YZ", None))
        self.view2DXZButton.setText(QCoreApplication.translate("tabView2DWidget", u"XZ", None))
        self.view2DOverlayOpacityLabel.setText(QCoreApplication.translate("tabView2DWidget", u"Overlay Opacity", None))
        self.view2DXYButton.setText(QCoreApplication.translate("tabView2DWidget", u"XY", None))
        self.view2DSliceText.setPlainText(QCoreApplication.translate("tabView2DWidget", u"100", None))
    # retranslateUi

