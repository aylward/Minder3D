# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovView3DPanelWidgetsmQRpG.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_View3DPanelWidget(object):
    def setupUi(self, View3DPanelWidget):
        if not View3DPanelWidget.objectName():
            View3DPanelWidget.setObjectName(u"View3DPanelWidget")
        View3DPanelWidget.resize(410, 522)
        self.verticalLayout = QVBoxLayout(View3DPanelWidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.view3DLayout = QVBoxLayout()
        self.view3DLayout.setObjectName(u"view3DLayout")

        self.verticalLayout_2.addLayout(self.view3DLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.view3DColorShiftSlider = QSlider(View3DPanelWidget)
        self.view3DColorShiftSlider.setObjectName(u"view3DColorShiftSlider")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view3DColorShiftSlider.sizePolicy().hasHeightForWidth())
        self.view3DColorShiftSlider.setSizePolicy(sizePolicy)
        self.view3DColorShiftSlider.setMinimumSize(QSize(100, 12))
        font = QFont()
        font.setPointSize(7)
        self.view3DColorShiftSlider.setFont(font)
        self.view3DColorShiftSlider.setMaximum(100)
        self.view3DColorShiftSlider.setValue(99)
        self.view3DColorShiftSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.view3DColorShiftSlider, 1, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)

        self.label = QLabel(View3DPanelWidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.view3DOpacitySlicer = QSlider(View3DPanelWidget)
        self.view3DOpacitySlicer.setObjectName(u"view3DOpacitySlicer")
        sizePolicy.setHeightForWidth(self.view3DOpacitySlicer.sizePolicy().hasHeightForWidth())
        self.view3DOpacitySlicer.setSizePolicy(sizePolicy)
        self.view3DOpacitySlicer.setMinimumSize(QSize(100, 12))
        self.view3DOpacitySlicer.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.view3DOpacitySlicer, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 5, 1, 1)

        self.view3DResetButton = QPushButton(View3DPanelWidget)
        self.view3DResetButton.setObjectName(u"view3DResetButton")
        sizePolicy.setHeightForWidth(self.view3DResetButton.sizePolicy().hasHeightForWidth())
        self.view3DResetButton.setSizePolicy(sizePolicy)
        self.view3DResetButton.setMinimumSize(QSize(30, 0))
        self.view3DResetButton.setMaximumSize(QSize(30, 16777215))
        self.view3DResetButton.setFont(font)

        self.gridLayout.addWidget(self.view3DResetButton, 1, 6, 1, 1)

        self.label_3 = QLabel(View3DPanelWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)

        self.view3DViewComboBox = QComboBox(View3DPanelWidget)
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.setObjectName(u"view3DViewComboBox")
        sizePolicy.setHeightForWidth(self.view3DViewComboBox.sizePolicy().hasHeightForWidth())
        self.view3DViewComboBox.setSizePolicy(sizePolicy)
        self.view3DViewComboBox.setMinimumSize(QSize(75, 0))
        self.view3DViewComboBox.setFont(font)

        self.gridLayout.addWidget(self.view3DViewComboBox, 1, 0, 1, 1)

        self.label_2 = QLabel(View3DPanelWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(View3DPanelWidget)

        QMetaObject.connectSlotsByName(View3DPanelWidget)
    # setupUi

    def retranslateUi(self, View3DPanelWidget):
        View3DPanelWidget.setWindowTitle(QCoreApplication.translate("View3DPanelWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("View3DPanelWidget", u"Image View", None))
        self.view3DResetButton.setText(QCoreApplication.translate("View3DPanelWidget", u"Reset", None))
        self.label_3.setText(QCoreApplication.translate("View3DPanelWidget", u"Color Shift", None))
        self.view3DViewComboBox.setItemText(0, QCoreApplication.translate("View3DPanelWidget", u"None", None))
        self.view3DViewComboBox.setItemText(1, QCoreApplication.translate("View3DPanelWidget", u"Axial", None))
        self.view3DViewComboBox.setItemText(2, QCoreApplication.translate("View3DPanelWidget", u"Coronal", None))
        self.view3DViewComboBox.setItemText(3, QCoreApplication.translate("View3DPanelWidget", u"Sagittal", None))
        self.view3DViewComboBox.setItemText(4, QCoreApplication.translate("View3DPanelWidget", u"All Planes", None))
        self.view3DViewComboBox.setItemText(5, QCoreApplication.translate("View3DPanelWidget", u"Volume: CTA", None))
        self.view3DViewComboBox.setItemText(6, "")

        self.label_2.setText(QCoreApplication.translate("View3DPanelWidget", u"Opacity", None))
    # retranslateUi

