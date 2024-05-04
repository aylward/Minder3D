# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovView3DPanelWidgeteiJpxx.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_View3DPanelWidget(object):
    def setupUi(self, View3DPanelWidget):
        if not View3DPanelWidget.objectName():
            View3DPanelWidget.setObjectName(u"View3DPanelWidget")
        View3DPanelWidget.resize(410, 467)
        self.verticalLayout = QVBoxLayout(View3DPanelWidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.view3DLayout = QVBoxLayout()
        self.view3DLayout.setObjectName(u"view3DLayout")

        self.verticalLayout_2.addLayout(self.view3DLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.view3DBkgComboBox = QComboBox(View3DPanelWidget)
        self.view3DBkgComboBox.addItem("")
        self.view3DBkgComboBox.addItem("")
        self.view3DBkgComboBox.addItem("")
        self.view3DBkgComboBox.addItem("")
        self.view3DBkgComboBox.setObjectName(u"view3DBkgComboBox")
        font = QFont()
        font.setPointSize(7)
        self.view3DBkgComboBox.setFont(font)

        self.horizontalLayout_2.addWidget(self.view3DBkgComboBox)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.view3DViewComboBox = QComboBox(View3DPanelWidget)
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.setObjectName(u"view3DViewComboBox")
        self.view3DViewComboBox.setFont(font)

        self.horizontalLayout_2.addWidget(self.view3DViewComboBox)

        self.view3DOpacitySlider = QSlider(View3DPanelWidget)
        self.view3DOpacitySlider.setObjectName(u"view3DOpacitySlider")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view3DOpacitySlider.sizePolicy().hasHeightForWidth())
        self.view3DOpacitySlider.setSizePolicy(sizePolicy)
        self.view3DOpacitySlider.setMinimumSize(QSize(0, 12))
        self.view3DOpacitySlider.setFont(font)
        self.view3DOpacitySlider.setMaximum(100)
        self.view3DOpacitySlider.setValue(99)
        self.view3DOpacitySlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.view3DOpacitySlider)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.view3DResetButton = QPushButton(View3DPanelWidget)
        self.view3DResetButton.setObjectName(u"view3DResetButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.view3DResetButton.sizePolicy().hasHeightForWidth())
        self.view3DResetButton.setSizePolicy(sizePolicy1)
        self.view3DResetButton.setMinimumSize(QSize(35, 0))
        self.view3DResetButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.view3DResetButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(View3DPanelWidget)

        QMetaObject.connectSlotsByName(View3DPanelWidget)
    # setupUi

    def retranslateUi(self, View3DPanelWidget):
        View3DPanelWidget.setWindowTitle(QCoreApplication.translate("View3DPanelWidget", u"Form", None))
        self.view3DBkgComboBox.setItemText(0, QCoreApplication.translate("View3DPanelWidget", u"Black", None))
        self.view3DBkgComboBox.setItemText(1, QCoreApplication.translate("View3DPanelWidget", u"Grey", None))
        self.view3DBkgComboBox.setItemText(2, QCoreApplication.translate("View3DPanelWidget", u"White", None))
        self.view3DBkgComboBox.setItemText(3, QCoreApplication.translate("View3DPanelWidget", u"Blue-Grey", None))

        self.view3DViewComboBox.setItemText(0, QCoreApplication.translate("View3DPanelWidget", u"None", None))
        self.view3DViewComboBox.setItemText(1, QCoreApplication.translate("View3DPanelWidget", u"Axial", None))
        self.view3DViewComboBox.setItemText(2, QCoreApplication.translate("View3DPanelWidget", u"Coronal", None))
        self.view3DViewComboBox.setItemText(3, QCoreApplication.translate("View3DPanelWidget", u"Sagittal", None))
        self.view3DViewComboBox.setItemText(4, QCoreApplication.translate("View3DPanelWidget", u"All Planes", None))
        self.view3DViewComboBox.setItemText(5, QCoreApplication.translate("View3DPanelWidget", u"Volume", None))

        self.view3DResetButton.setText(QCoreApplication.translate("View3DPanelWidget", u"Reset", None))
    # retranslateUi

