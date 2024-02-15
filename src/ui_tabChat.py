# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabChatDqwbKH.ui'
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
from PySide6.QtWidgets import (QApplication, QPlainTextEdit, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_tabChatWidget(object):
    def setupUi(self, tabChatWidget):
        if not tabChatWidget.objectName():
            tabChatWidget.setObjectName(u"tabChatWidget")
        tabChatWidget.resize(289, 212)
        self.chatGoButton = QPushButton(tabChatWidget)
        self.chatGoButton.setObjectName(u"chatGoButton")
        self.chatGoButton.setGeometry(QRect(250, 170, 31, 24))
        self.chatInputTextEdit = QPlainTextEdit(tabChatWidget)
        self.chatInputTextEdit.setObjectName(u"chatInputTextEdit")
        self.chatInputTextEdit.setGeometry(QRect(0, 160, 241, 41))
        self.chatOutputTextBrowser = QTextBrowser(tabChatWidget)
        self.chatOutputTextBrowser.setObjectName(u"chatOutputTextBrowser")
        self.chatOutputTextBrowser.setGeometry(QRect(0, 0, 281, 151))

        self.retranslateUi(tabChatWidget)

        QMetaObject.connectSlotsByName(tabChatWidget)
    # setupUi

    def retranslateUi(self, tabChatWidget):
        tabChatWidget.setWindowTitle(QCoreApplication.translate("tabChatWidget", u"Form", None))
        self.chatGoButton.setText(QCoreApplication.translate("tabChatWidget", u"Go", None))
    # retranslateUi

