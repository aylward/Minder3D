# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovOtsuPanelWidgetcRnHCP.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_OtsuPanelWidget(object):
    def setupUi(self, OtsuPanelWidget):
        if not OtsuPanelWidget.objectName():
            OtsuPanelWidget.setObjectName(u"OtsuPanelWidget")
        OtsuPanelWidget.resize(390, 125)
        self.otsuRunButton = QPushButton(OtsuPanelWidget)
        self.otsuRunButton.setObjectName(u"otsuRunButton")
        self.otsuRunButton.setGeometry(QRect(100, 50, 161, 24))
        self.otsuNumberOfThresholdsSpinBox = QSpinBox(OtsuPanelWidget)
        self.otsuNumberOfThresholdsSpinBox.setObjectName(u"otsuNumberOfThresholdsSpinBox")
        self.otsuNumberOfThresholdsSpinBox.setGeometry(QRect(150, 10, 42, 22))
        self.otsuNumberOfThresholdsSpinBox.setMinimum(1)
        self.otsuNumberOfThresholdsSpinBox.setValue(1)
        self.otsuNumberOfThresholdsLabel = QLabel(OtsuPanelWidget)
        self.otsuNumberOfThresholdsLabel.setObjectName(u"otsuNumberOfThresholdsLabel")
        self.otsuNumberOfThresholdsLabel.setGeometry(QRect(20, 13, 131, 16))

        self.retranslateUi(OtsuPanelWidget)

        QMetaObject.connectSlotsByName(OtsuPanelWidget)
    # setupUi

    def retranslateUi(self, OtsuPanelWidget):
        OtsuPanelWidget.setWindowTitle(QCoreApplication.translate("OtsuPanelWidget", u"Form", None))
        self.otsuRunButton.setText(QCoreApplication.translate("OtsuPanelWidget", u"Run Otsu Threshold", None))
        self.otsuNumberOfThresholdsLabel.setText(QCoreApplication.translate("OtsuPanelWidget", u"Number of thresholds:", None))
    # retranslateUi

