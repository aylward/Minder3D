# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovImageTablePanelWidgetobPDfU.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_ImageTablePanelWidget(object):
    def setupUi(self, ImageTablePanelWidget):
        if not ImageTablePanelWidget.objectName():
            ImageTablePanelWidget.setObjectName(u"ImageTablePanelWidget")
        ImageTablePanelWidget.resize(448, 336)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImageTablePanelWidget.sizePolicy().hasHeightForWidth())
        ImageTablePanelWidget.setSizePolicy(sizePolicy)
        ImageTablePanelWidget.setMinimumSize(QSize(190, 0))
        self.horizontalLayout = QHBoxLayout(ImageTablePanelWidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.imageTableWidget = QTableWidget(ImageTablePanelWidget)
        self.imageTableWidget.setObjectName(u"imageTableWidget")

        self.horizontalLayout.addWidget(self.imageTableWidget)


        self.retranslateUi(ImageTablePanelWidget)

        QMetaObject.connectSlotsByName(ImageTablePanelWidget)
    # setupUi

    def retranslateUi(self, ImageTablePanelWidget):
        ImageTablePanelWidget.setWindowTitle(QCoreApplication.translate("ImageTablePanelWidget", u"Form", None))
    # retranslateUi

