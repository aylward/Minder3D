# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabLungAIdGEVFg.ui'
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
    QTextBrowser, QWidget)

class Ui_tabLungAIWidget(object):
    def setupUi(self, tabLungAIWidget):
        if not tabLungAIWidget.objectName():
            tabLungAIWidget.setObjectName(u"tabLungAIWidget")
        tabLungAIWidget.resize(451, 134)
        self.lungAIStatusLabel = QLabel(tabLungAIWidget)
        self.lungAIStatusLabel.setObjectName(u"lungAIStatusLabel")
        self.lungAIStatusLabel.setGeometry(QRect(10, 10, 61, 16))
        self.lungAIStatusTextBrowser = QTextBrowser(tabLungAIWidget)
        self.lungAIStatusTextBrowser.setObjectName(u"lungAIStatusTextBrowser")
        self.lungAIStatusTextBrowser.setGeometry(QRect(70, 10, 261, 101))
        self.lungAIForceLoadButton = QPushButton(tabLungAIWidget)
        self.lungAIForceLoadButton.setObjectName(u"lungAIForceLoadButton")
        self.lungAIForceLoadButton.setGeometry(QRect(340, 10, 91, 24))
        self.lungAISegmentButton = QPushButton(tabLungAIWidget)
        self.lungAISegmentButton.setObjectName(u"lungAISegmentButton")
        self.lungAISegmentButton.setGeometry(QRect(340, 90, 91, 24))

        self.retranslateUi(tabLungAIWidget)

        QMetaObject.connectSlotsByName(tabLungAIWidget)
    # setupUi

    def retranslateUi(self, tabLungAIWidget):
        tabLungAIWidget.setWindowTitle(QCoreApplication.translate("tabLungAIWidget", u"Form", None))
        self.lungAIStatusLabel.setText(QCoreApplication.translate("tabLungAIWidget", u"AI Status:", None))
        self.lungAIForceLoadButton.setText(QCoreApplication.translate("tabLungAIWidget", u"Force Load AI", None))
        self.lungAISegmentButton.setText(QCoreApplication.translate("tabLungAIWidget", u"Segment Lungs", None))
    # retranslateUi

