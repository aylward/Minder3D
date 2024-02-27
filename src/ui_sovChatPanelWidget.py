# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chatPanelRCmywC.ui'
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

class Ui_ChatPanelWidget(object):
    def setupUi(self, ChatPanelWidget):
        if not ChatPanelWidget.objectName():
            ChatPanelWidget.setObjectName(u"ChatPanelWidget")
        ChatPanelWidget.resize(289, 212)
        self.chatGoButton = QPushButton(ChatPanelWidget)
        self.chatGoButton.setObjectName(u"chatGoButton")
        self.chatGoButton.setGeometry(QRect(250, 170, 31, 24))
        self.chatInputTextEdit = QPlainTextEdit(ChatPanelWidget)
        self.chatInputTextEdit.setObjectName(u"chatInputTextEdit")
        self.chatInputTextEdit.setGeometry(QRect(0, 160, 241, 41))
        self.chatOutputTextBrowser = QTextBrowser(ChatPanelWidget)
        self.chatOutputTextBrowser.setObjectName(u"chatOutputTextBrowser")
        self.chatOutputTextBrowser.setGeometry(QRect(0, 0, 281, 151))

        self.retranslateUi(ChatPanelWidget)

        QMetaObject.connectSlotsByName(ChatPanelWidget)
    # setupUi

    def retranslateUi(self, ChatPanelWidget):
        ChatPanelWidget.setWindowTitle(QCoreApplication.translate("ChatPanelWidget", u"Form", None))
        self.chatGoButton.setText(QCoreApplication.translate("ChatPanelWidget", u"Go", None))
    # retranslateUi

