# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovLungAIPanelWidgetsRqMzS.ui'
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

class Ui_LungAIPanelWidget(object):
    def setupUi(self, LungAIPanelWidget):
        if not LungAIPanelWidget.objectName():
            LungAIPanelWidget.setObjectName(u"LungAIPanelWidget")
        LungAIPanelWidget.resize(451, 134)
        self.lungAIStatusLabel = QLabel(LungAIPanelWidget)
        self.lungAIStatusLabel.setObjectName(u"lungAIStatusLabel")
        self.lungAIStatusLabel.setGeometry(QRect(50, 50, 51, 16))
        self.lungAIStatusTextBrowser = QTextBrowser(LungAIPanelWidget)
        self.lungAIStatusTextBrowser.setObjectName(u"lungAIStatusTextBrowser")
        self.lungAIStatusTextBrowser.setGeometry(QRect(100, 20, 341, 91))
        self.lungAISegmentButton = QPushButton(LungAIPanelWidget)
        self.lungAISegmentButton.setObjectName(u"lungAISegmentButton")
        self.lungAISegmentButton.setGeometry(QRect(3, 3, 91, 24))

        self.retranslateUi(LungAIPanelWidget)

        QMetaObject.connectSlotsByName(LungAIPanelWidget)
    # setupUi

    def retranslateUi(self, LungAIPanelWidget):
        LungAIPanelWidget.setWindowTitle(QCoreApplication.translate("LungAIPanelWidget", u"Form", None))
        self.lungAIStatusLabel.setText(QCoreApplication.translate("LungAIPanelWidget", u"AI Status:", None))
        self.lungAISegmentButton.setText(QCoreApplication.translate("LungAIPanelWidget", u"Segment Lungs", None))
    # retranslateUi

