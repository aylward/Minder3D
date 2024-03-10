# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovView3DPanelWidgetZwpYip.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_View3DPanelWidget(object):
    def setupUi(self, View3DPanelWidget):
        if not View3DPanelWidget.objectName():
            View3DPanelWidget.setObjectName(u"View3DPanelWidget")
        View3DPanelWidget.resize(373, 388)
        self.verticalLayout = QVBoxLayout(View3DPanelWidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.view3DLayout = QVBoxLayout()
        self.view3DLayout.setObjectName(u"view3DLayout")

        self.verticalLayout.addLayout(self.view3DLayout)

        self.view3DPanelGroup = QGroupBox(View3DPanelWidget)
        self.view3DPanelGroup.setObjectName(u"view3DPanelGroup")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view3DPanelGroup.sizePolicy().hasHeightForWidth())
        self.view3DPanelGroup.setSizePolicy(sizePolicy)
        self.view3DPanelGroup.setMinimumSize(QSize(0, 30))
        self.view3DPanelGroup.setFlat(False)
        self.horizontalLayout = QHBoxLayout(self.view3DPanelGroup)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.view3DViewLabel = QLabel(self.view3DPanelGroup)
        self.view3DViewLabel.setObjectName(u"view3DViewLabel")
        font = QFont()
        font.setPointSize(7)
        self.view3DViewLabel.setFont(font)

        self.horizontalLayout.addWidget(self.view3DViewLabel)

        self.view3DViewComboBox = QComboBox(self.view3DPanelGroup)
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.setObjectName(u"view3DViewComboBox")
        self.view3DViewComboBox.setFont(font)

        self.horizontalLayout.addWidget(self.view3DViewComboBox)

        self.view3DOpacitySlider = QSlider(self.view3DPanelGroup)
        self.view3DOpacitySlider.setObjectName(u"view3DOpacitySlider")
        self.view3DOpacitySlider.setFont(font)
        self.view3DOpacitySlider.setMaximum(100)
        self.view3DOpacitySlider.setValue(99)
        self.view3DOpacitySlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.view3DOpacitySlider)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.view3DBkgComboBox = QComboBox(self.view3DPanelGroup)
        self.view3DBkgComboBox.addItem("")
        self.view3DBkgComboBox.addItem("")
        self.view3DBkgComboBox.addItem("")
        self.view3DBkgComboBox.addItem("")
        self.view3DBkgComboBox.setObjectName(u"view3DBkgComboBox")
        self.view3DBkgComboBox.setFont(font)

        self.horizontalLayout.addWidget(self.view3DBkgComboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.view3DResetButton = QPushButton(self.view3DPanelGroup)
        self.view3DResetButton.setObjectName(u"view3DResetButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.view3DResetButton.sizePolicy().hasHeightForWidth())
        self.view3DResetButton.setSizePolicy(sizePolicy1)
        self.view3DResetButton.setMinimumSize(QSize(50, 0))
        self.view3DResetButton.setFont(font)

        self.horizontalLayout.addWidget(self.view3DResetButton)


        self.verticalLayout.addWidget(self.view3DPanelGroup)


        self.retranslateUi(View3DPanelWidget)

        QMetaObject.connectSlotsByName(View3DPanelWidget)
    # setupUi

    def retranslateUi(self, View3DPanelWidget):
        View3DPanelWidget.setWindowTitle(QCoreApplication.translate("View3DPanelWidget", u"Form", None))
        self.view3DViewLabel.setText(QCoreApplication.translate("View3DPanelWidget", u"View:", None))
        self.view3DViewComboBox.setItemText(0, QCoreApplication.translate("View3DPanelWidget", u"None", None))
        self.view3DViewComboBox.setItemText(1, QCoreApplication.translate("View3DPanelWidget", u"Axial", None))
        self.view3DViewComboBox.setItemText(2, QCoreApplication.translate("View3DPanelWidget", u"Coronal", None))
        self.view3DViewComboBox.setItemText(3, QCoreApplication.translate("View3DPanelWidget", u"Sagittal", None))
        self.view3DViewComboBox.setItemText(4, QCoreApplication.translate("View3DPanelWidget", u"All Planes", None))
        self.view3DViewComboBox.setItemText(5, QCoreApplication.translate("View3DPanelWidget", u"Volume", None))

        self.view3DBkgComboBox.setItemText(0, QCoreApplication.translate("View3DPanelWidget", u"Black", None))
        self.view3DBkgComboBox.setItemText(1, QCoreApplication.translate("View3DPanelWidget", u"Grey", None))
        self.view3DBkgComboBox.setItemText(2, QCoreApplication.translate("View3DPanelWidget", u"White", None))
        self.view3DBkgComboBox.setItemText(3, QCoreApplication.translate("View3DPanelWidget", u"Blue-Grey", None))

        self.view3DResetButton.setText(QCoreApplication.translate("View3DPanelWidget", u"Reset", None))
    # retranslateUi

