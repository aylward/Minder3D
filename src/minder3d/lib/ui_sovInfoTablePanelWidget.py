# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovInfoTablePanelWidgetCuyIch.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHBoxLayout,
    QHeaderView, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_InfoTablePanelWidget(object):
    def setupUi(self, InfoTablePanelWidget):
        if not InfoTablePanelWidget.objectName():
            InfoTablePanelWidget.setObjectName(u"InfoTablePanelWidget")
        InfoTablePanelWidget.resize(190, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InfoTablePanelWidget.sizePolicy().hasHeightForWidth())
        InfoTablePanelWidget.setSizePolicy(sizePolicy)
        InfoTablePanelWidget.setMinimumSize(QSize(190, 0))
        self.horizontalLayout = QHBoxLayout(InfoTablePanelWidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.infoTableWidget = QTableWidget(InfoTablePanelWidget)
        self.infoTableWidget.setObjectName(u"infoTableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.infoTableWidget.sizePolicy().hasHeightForWidth())
        self.infoTableWidget.setSizePolicy(sizePolicy1)
        self.infoTableWidget.setMinimumSize(QSize(180, 0))
        self.infoTableWidget.setAutoFillBackground(True)
        self.infoTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.infoTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.infoTableWidget.setAlternatingRowColors(True)
        self.infoTableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.infoTableWidget.setRowCount(0)
        self.infoTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.infoTableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.infoTableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.horizontalLayout.addWidget(self.infoTableWidget)


        self.retranslateUi(InfoTablePanelWidget)

        QMetaObject.connectSlotsByName(InfoTablePanelWidget)
    # setupUi

    def retranslateUi(self, InfoTablePanelWidget):
        InfoTablePanelWidget.setWindowTitle(QCoreApplication.translate("InfoTablePanelWidget", u"Form", None))
    # retranslateUi

