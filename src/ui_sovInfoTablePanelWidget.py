# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovInfoTablePanelWidgetUjtMFS.ui'
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
    QHeaderView, QSizePolicy, QTableView, QWidget)

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
        self.infoTableView = QTableView(InfoTablePanelWidget)
        self.infoTableView.setObjectName(u"infoTableView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.infoTableView.sizePolicy().hasHeightForWidth())
        self.infoTableView.setSizePolicy(sizePolicy1)
        self.infoTableView.setMinimumSize(QSize(180, 0))
        self.infoTableView.setAutoFillBackground(True)
        self.infoTableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.infoTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.infoTableView.setAlternatingRowColors(True)
        self.infoTableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.infoTableView.horizontalHeader().setVisible(False)
        self.infoTableView.horizontalHeader().setHighlightSections(False)
        self.infoTableView.verticalHeader().setVisible(False)
        self.infoTableView.verticalHeader().setHighlightSections(False)

        self.horizontalLayout.addWidget(self.infoTableView)


        self.retranslateUi(InfoTablePanelWidget)

        QMetaObject.connectSlotsByName(InfoTablePanelWidget)
    # setupUi

    def retranslateUi(self, InfoTablePanelWidget):
        InfoTablePanelWidget.setWindowTitle(QCoreApplication.translate("InfoTablePanelWidget", u"Form", None))
    # retranslateUi

