# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovView3DPanelWidgetpNIAAr.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_View3DPanelWidget(object):
    def setupUi(self, View3DPanelWidget):
        if not View3DPanelWidget.objectName():
            View3DPanelWidget.setObjectName(u"View3DPanelWidget")
        View3DPanelWidget.resize(351, 390)
        self.verticalLayoutWidget_2 = QWidget(View3DPanelWidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 351, 351))
        self.view3DLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.view3DLayout.setObjectName(u"view3DLayout")
        self.view3DLayout.setContentsMargins(0, 0, 0, 0)
        self.view3DResetButton = QPushButton(View3DPanelWidget)
        self.view3DResetButton.setObjectName(u"view3DResetButton")
        self.view3DResetButton.setGeometry(QRect(314, 360, 31, 24))
        font = QFont()
        font.setPointSize(7)
        self.view3DResetButton.setFont(font)
        self.view3DViewComboBox = QComboBox(View3DPanelWidget)
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.addItem("")
        self.view3DViewComboBox.setObjectName(u"view3DViewComboBox")
        self.view3DViewComboBox.setGeometry(QRect(30, 361, 61, 21))
        self.view3DViewComboBox.setFont(font)
        self.view3DViewLabel = QLabel(View3DPanelWidget)
        self.view3DViewLabel.setObjectName(u"view3DViewLabel")
        self.view3DViewLabel.setGeometry(QRect(0, 360, 31, 16))
        self.view3DViewLabel.setFont(font)
        self.view3DBkgLabel = QLabel(View3DPanelWidget)
        self.view3DBkgLabel.setObjectName(u"view3DBkgLabel")
        self.view3DBkgLabel.setGeometry(QRect(230, 360, 21, 16))
        self.view3DBkgLabel.setFont(font)
        self.view3DBkgComboBox = QComboBox(View3DPanelWidget)
        self.view3DBkgComboBox.addItem("")
        self.view3DBkgComboBox.addItem("")
        self.view3DBkgComboBox.addItem("")
        self.view3DBkgComboBox.addItem("")
        self.view3DBkgComboBox.setObjectName(u"view3DBkgComboBox")
        self.view3DBkgComboBox.setGeometry(QRect(248, 361, 51, 21))
        self.view3DBkgComboBox.setFont(font)
        self.view3DOpacitySlider = QSlider(View3DPanelWidget)
        self.view3DOpacitySlider.setObjectName(u"view3DOpacitySlider")
        self.view3DOpacitySlider.setGeometry(QRect(100, 362, 81, 20))
        self.view3DOpacitySlider.setFont(font)
        self.view3DOpacitySlider.setMaximum(100)
        self.view3DOpacitySlider.setValue(99)
        self.view3DOpacitySlider.setOrientation(Qt.Horizontal)

        self.retranslateUi(View3DPanelWidget)

        QMetaObject.connectSlotsByName(View3DPanelWidget)
    # setupUi

    def retranslateUi(self, View3DPanelWidget):
        View3DPanelWidget.setWindowTitle(QCoreApplication.translate("View3DPanelWidget", u"Form", None))
        self.view3DResetButton.setText(QCoreApplication.translate("View3DPanelWidget", u"Reset", None))
        self.view3DViewComboBox.setItemText(0, QCoreApplication.translate("View3DPanelWidget", u"None", None))
        self.view3DViewComboBox.setItemText(1, QCoreApplication.translate("View3DPanelWidget", u"Axial", None))
        self.view3DViewComboBox.setItemText(2, QCoreApplication.translate("View3DPanelWidget", u"Coronal", None))
        self.view3DViewComboBox.setItemText(3, QCoreApplication.translate("View3DPanelWidget", u"Sagittal", None))
        self.view3DViewComboBox.setItemText(4, QCoreApplication.translate("View3DPanelWidget", u"All Planes", None))
        self.view3DViewComboBox.setItemText(5, QCoreApplication.translate("View3DPanelWidget", u"Volume", None))

        self.view3DViewLabel.setText(QCoreApplication.translate("View3DPanelWidget", u"View:", None))
        self.view3DBkgLabel.setText(QCoreApplication.translate("View3DPanelWidget", u"Bkg:", None))
        self.view3DBkgComboBox.setItemText(0, QCoreApplication.translate("View3DPanelWidget", u"Black", None))
        self.view3DBkgComboBox.setItemText(1, QCoreApplication.translate("View3DPanelWidget", u"Grey", None))
        self.view3DBkgComboBox.setItemText(2, QCoreApplication.translate("View3DPanelWidget", u"White", None))
        self.view3DBkgComboBox.setItemText(3, QCoreApplication.translate("View3DPanelWidget", u"Blue-Grey", None))

    # retranslateUi

