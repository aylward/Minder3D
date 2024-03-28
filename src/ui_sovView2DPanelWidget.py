# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovView2DPanelWidgetStjGsc.ui'
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
    QGridLayout, QGroupBox, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_View2DPanelWidget(object):
    def setupUi(self, View2DPanelWidget):
        if not View2DPanelWidget.objectName():
            View2DPanelWidget.setObjectName(u"View2DPanelWidget")
        View2DPanelWidget.resize(468, 452)
        self.gridLayout = QGridLayout(View2DPanelWidget)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.view2DSliceText = QPlainTextEdit(View2DPanelWidget)
        self.view2DSliceText.setObjectName(u"view2DSliceText")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view2DSliceText.sizePolicy().hasHeightForWidth())
        self.view2DSliceText.setSizePolicy(sizePolicy)
        self.view2DSliceText.setMinimumSize(QSize(30, 20))
        self.view2DSliceText.setBaseSize(QSize(31, 21))
        font = QFont()
        font.setPointSize(7)
        self.view2DSliceText.setFont(font)
        self.view2DSliceText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view2DSliceText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view2DSliceText.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.view2DSliceText.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.gridLayout.addWidget(self.view2DSliceText, 1, 2, 1, 1)

        self.view2DSliceSlider = QSlider(View2DPanelWidget)
        self.view2DSliceSlider.setObjectName(u"view2DSliceSlider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.view2DSliceSlider.sizePolicy().hasHeightForWidth())
        self.view2DSliceSlider.setSizePolicy(sizePolicy1)
        self.view2DSliceSlider.setMinimumSize(QSize(30, 380))
        self.view2DSliceSlider.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.view2DSliceSlider, 0, 2, 1, 1)

        self.view2DGroupBox = QGroupBox(View2DPanelWidget)
        self.view2DGroupBox.setObjectName(u"view2DGroupBox")
        self.view2DGroupBox.setMinimumSize(QSize(0, 40))
        self.view2DGroupBox.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.view2DGroupBox)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.view2DXZButton = QPushButton(self.view2DGroupBox)
        self.view2DXZButton.setObjectName(u"view2DXZButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.view2DXZButton.sizePolicy().hasHeightForWidth())
        self.view2DXZButton.setSizePolicy(sizePolicy2)
        self.view2DXZButton.setMinimumSize(QSize(30, 0))
        self.view2DXZButton.setFont(font)

        self.gridLayout_2.addWidget(self.view2DXZButton, 0, 4, 2, 1)

        self.view2DFlipYCheckBox = QCheckBox(self.view2DGroupBox)
        self.view2DFlipYCheckBox.setObjectName(u"view2DFlipYCheckBox")
        sizePolicy2.setHeightForWidth(self.view2DFlipYCheckBox.sizePolicy().hasHeightForWidth())
        self.view2DFlipYCheckBox.setSizePolicy(sizePolicy2)
        self.view2DFlipYCheckBox.setFont(font)
        self.view2DFlipYCheckBox.setIconSize(QSize(10, 10))

        self.gridLayout_2.addWidget(self.view2DFlipYCheckBox, 1, 6, 1, 1)

        self.view2DFlipXCheckBox = QCheckBox(self.view2DGroupBox)
        self.view2DFlipXCheckBox.setObjectName(u"view2DFlipXCheckBox")
        sizePolicy2.setHeightForWidth(self.view2DFlipXCheckBox.sizePolicy().hasHeightForWidth())
        self.view2DFlipXCheckBox.setSizePolicy(sizePolicy2)
        self.view2DFlipXCheckBox.setFont(font)
        self.view2DFlipXCheckBox.setIconSize(QSize(10, 10))

        self.gridLayout_2.addWidget(self.view2DFlipXCheckBox, 0, 6, 1, 1)

        self.view2DYZButton = QPushButton(self.view2DGroupBox)
        self.view2DYZButton.setObjectName(u"view2DYZButton")
        sizePolicy2.setHeightForWidth(self.view2DYZButton.sizePolicy().hasHeightForWidth())
        self.view2DYZButton.setSizePolicy(sizePolicy2)
        self.view2DYZButton.setMinimumSize(QSize(30, 0))
        self.view2DYZButton.setFont(font)

        self.gridLayout_2.addWidget(self.view2DYZButton, 0, 5, 2, 1)

        self.view2DViewImageComboBox = QComboBox(self.view2DGroupBox)
        self.view2DViewImageComboBox.setObjectName(u"view2DViewImageComboBox")
        sizePolicy2.setHeightForWidth(self.view2DViewImageComboBox.sizePolicy().hasHeightForWidth())
        self.view2DViewImageComboBox.setSizePolicy(sizePolicy2)
        self.view2DViewImageComboBox.setMinimumSize(QSize(60, 0))
        self.view2DViewImageComboBox.setFont(font)

        self.gridLayout_2.addWidget(self.view2DViewImageComboBox, 0, 1, 2, 1)

        self.view2DXYButton = QPushButton(self.view2DGroupBox)
        self.view2DXYButton.setObjectName(u"view2DXYButton")
        sizePolicy2.setHeightForWidth(self.view2DXYButton.sizePolicy().hasHeightForWidth())
        self.view2DXYButton.setSizePolicy(sizePolicy2)
        self.view2DXYButton.setMinimumSize(QSize(30, 0))
        self.view2DXYButton.setFont(font)

        self.gridLayout_2.addWidget(self.view2DXYButton, 0, 3, 2, 1)

        self.view2DOverlayOpacitySlider = QSlider(self.view2DGroupBox)
        self.view2DOverlayOpacitySlider.setObjectName(u"view2DOverlayOpacitySlider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.view2DOverlayOpacitySlider.sizePolicy().hasHeightForWidth())
        self.view2DOverlayOpacitySlider.setSizePolicy(sizePolicy3)
        self.view2DOverlayOpacitySlider.setMinimumSize(QSize(75, 16))
        self.view2DOverlayOpacitySlider.setMaximum(100)
        self.view2DOverlayOpacitySlider.setValue(50)
        self.view2DOverlayOpacitySlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.view2DOverlayOpacitySlider, 0, 8, 2, 1)

        self.view2DViewImageLabel = QLabel(self.view2DGroupBox)
        self.view2DViewImageLabel.setObjectName(u"view2DViewImageLabel")
        sizePolicy2.setHeightForWidth(self.view2DViewImageLabel.sizePolicy().hasHeightForWidth())
        self.view2DViewImageLabel.setSizePolicy(sizePolicy2)
        self.view2DViewImageLabel.setFont(font)

        self.gridLayout_2.addWidget(self.view2DViewImageLabel, 0, 0, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 7, 1, 1)


        self.gridLayout.addWidget(self.view2DGroupBox, 2, 0, 1, 2)

        self.view2DLayout = QVBoxLayout()
        self.view2DLayout.setSpacing(3)
        self.view2DLayout.setObjectName(u"view2DLayout")

        self.gridLayout.addLayout(self.view2DLayout, 0, 0, 1, 2)


        self.retranslateUi(View2DPanelWidget)

        QMetaObject.connectSlotsByName(View2DPanelWidget)
    # setupUi

    def retranslateUi(self, View2DPanelWidget):
        View2DPanelWidget.setWindowTitle(QCoreApplication.translate("View2DPanelWidget", u"Form", None))
        self.view2DSliceText.setPlainText(QCoreApplication.translate("View2DPanelWidget", u"100", None))
        self.view2DGroupBox.setTitle("")
        self.view2DXZButton.setText(QCoreApplication.translate("View2DPanelWidget", u"XZ", None))
        self.view2DFlipYCheckBox.setText(QCoreApplication.translate("View2DPanelWidget", u"Flip Y", None))
        self.view2DFlipXCheckBox.setText(QCoreApplication.translate("View2DPanelWidget", u"Flip X", None))
        self.view2DYZButton.setText(QCoreApplication.translate("View2DPanelWidget", u"YZ", None))
        self.view2DXYButton.setText(QCoreApplication.translate("View2DPanelWidget", u"XY", None))
        self.view2DViewImageLabel.setText(QCoreApplication.translate("View2DPanelWidget", u"Image", None))
    # retranslateUi

