# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovTablePanelWidgetScVxmz.ui'
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

class Ui_TablePanelWidget(object):
    def setupUi(self, TablePanelWidget):
        if not TablePanelWidget.objectName():
            TablePanelWidget.setObjectName(u"TablePanelWidget")
        TablePanelWidget.resize(190, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TablePanelWidget.sizePolicy().hasHeightForWidth())
        TablePanelWidget.setSizePolicy(sizePolicy)
        TablePanelWidget.setMinimumSize(QSize(190, 0))
        self.horizontalLayout = QHBoxLayout(TablePanelWidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.tableTableView = QTableView(TablePanelWidget)
        self.tableTableView.setObjectName(u"tableTableView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableTableView.sizePolicy().hasHeightForWidth())
        self.tableTableView.setSizePolicy(sizePolicy1)
        self.tableTableView.setMinimumSize(QSize(180, 0))
        self.tableTableView.setAutoFillBackground(True)
        self.tableTableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableTableView.setAlternatingRowColors(True)
        self.tableTableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableTableView.horizontalHeader().setVisible(False)
        self.tableTableView.horizontalHeader().setHighlightSections(False)
        self.tableTableView.verticalHeader().setVisible(False)
        self.tableTableView.verticalHeader().setHighlightSections(False)

        self.horizontalLayout.addWidget(self.tableTableView)


        self.retranslateUi(TablePanelWidget)

        QMetaObject.connectSlotsByName(TablePanelWidget)
    # setupUi

    def retranslateUi(self, TablePanelWidget):
        TablePanelWidget.setWindowTitle(QCoreApplication.translate("TablePanelWidget", u"Form", None))
    # retranslateUi

