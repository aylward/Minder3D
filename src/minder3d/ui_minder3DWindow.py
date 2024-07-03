# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'minder3DWindownkNdyQ.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1274, 675)
        MainWindow.setMinimumSize(QSize(1024, 0))
        self.loadImageMenuItem = QAction(MainWindow)
        self.loadImageMenuItem.setObjectName(u"loadImageMenuItem")
        self.saveImageMenuItem = QAction(MainWindow)
        self.saveImageMenuItem.setObjectName(u"saveImageMenuItem")
        self.saveOverlayMenuItem = QAction(MainWindow)
        self.saveOverlayMenuItem.setObjectName(u"saveOverlayMenuItem")
        self.saveVTKModelsMenuItem = QAction(MainWindow)
        self.saveVTKModelsMenuItem.setObjectName(u"saveVTKModelsMenuItem")
        self.loadSceneMenuItem = QAction(MainWindow)
        self.loadSceneMenuItem.setObjectName(u"loadSceneMenuItem")
        self.saveSceneMenuItem = QAction(MainWindow)
        self.saveSceneMenuItem.setObjectName(u"saveSceneMenuItem")
        self.savePreProcessedOverlayMenuItem = QAction(MainWindow)
        self.savePreProcessedOverlayMenuItem.setObjectName(u"savePreProcessedOverlayMenuItem")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1024, 0))
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.appLayout = QVBoxLayout()
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.topPanelLayout = QHBoxLayout()
        self.topPanelLayout.setObjectName(u"topPanelLayout")
        self.view2DLayout = QVBoxLayout()
        self.view2DLayout.setObjectName(u"view2DLayout")
        self.view2DSpacer = QSpacerItem(391, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.view2DLayout.addItem(self.view2DSpacer)


        self.topPanelLayout.addLayout(self.view2DLayout)

        self.topPanelSpacer = QSpacerItem(0, 391, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.topPanelLayout.addItem(self.topPanelSpacer)

        self.view3DLayout = QVBoxLayout()
        self.view3DLayout.setObjectName(u"view3DLayout")
        self.view3DSpacer = QSpacerItem(361, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.view3DLayout.addItem(self.view3DSpacer)


        self.topPanelLayout.addLayout(self.view3DLayout)

        self.rightPanelLayout = QVBoxLayout()
        self.rightPanelLayout.setObjectName(u"rightPanelLayout")
        self.objectLayout = QVBoxLayout()
        self.objectLayout.setObjectName(u"objectLayout")

        self.rightPanelLayout.addLayout(self.objectLayout)

        self.infoTableLayout = QVBoxLayout()
        self.infoTableLayout.setObjectName(u"infoTableLayout")

        self.rightPanelLayout.addLayout(self.infoTableLayout)


        self.topPanelLayout.addLayout(self.rightPanelLayout)


        self.appLayout.addLayout(self.topPanelLayout)

        self.bottomPanelLayout = QHBoxLayout()
        self.bottomPanelLayout.setObjectName(u"bottomPanelLayout")
        self.imageTableLayout = QVBoxLayout()
        self.imageTableLayout.setObjectName(u"imageTableLayout")
        self.horizontalSpacer_2 = QSpacerItem(300, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.imageTableLayout.addItem(self.horizontalSpacer_2)


        self.bottomPanelLayout.addLayout(self.imageTableLayout)

        self.bottomRightPanelLayout = QVBoxLayout()
        self.bottomRightPanelLayout.setObjectName(u"bottomRightPanelLayout")
        self.bottomRightPanelLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(830, 194))
        self.tabWidget.setTabsClosable(True)
        self.welcomeTab = QWidget()
        self.welcomeTab.setObjectName(u"welcomeTab")
        self.welcomeTabLayout = QHBoxLayout(self.welcomeTab)
        self.welcomeTabLayout.setObjectName(u"welcomeTabLayout")
        self.tabWidget.addTab(self.welcomeTab, "")
        self.visualizationTab = QWidget()
        self.visualizationTab.setObjectName(u"visualizationTab")
        self.visualizationTabLayout = QHBoxLayout(self.visualizationTab)
        self.visualizationTabLayout.setObjectName(u"visualizationTabLayout")
        self.tabWidget.addTab(self.visualizationTab, "")
        self.newTaskTab = QWidget()
        self.newTaskTab.setObjectName(u"newTaskTab")
        self.newTaskTabLayout = QHBoxLayout(self.newTaskTab)
        self.newTaskTabLayout.setObjectName(u"newTaskTabLayout")
        self.tabWidget.addTab(self.newTaskTab, "")

        self.bottomRightPanelLayout.addWidget(self.tabWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.statusLabel = QLabel(self.centralwidget)
        self.statusLabel.setObjectName(u"statusLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.statusLabel.sizePolicy().hasHeightForWidth())
        self.statusLabel.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(7)
        self.statusLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.statusLabel)

        self.statusText = QLineEdit(self.centralwidget)
        self.statusText.setObjectName(u"statusText")
        sizePolicy2.setHeightForWidth(self.statusText.sizePolicy().hasHeightForWidth())
        self.statusText.setSizePolicy(sizePolicy2)
        self.statusText.setMinimumSize(QSize(150, 0))
        self.statusText.setFont(font)

        self.horizontalLayout_2.addWidget(self.statusText)

        self.statusProgressBar = QProgressBar(self.centralwidget)
        self.statusProgressBar.setObjectName(u"statusProgressBar")
        sizePolicy2.setHeightForWidth(self.statusProgressBar.sizePolicy().hasHeightForWidth())
        self.statusProgressBar.setSizePolicy(sizePolicy2)
        self.statusProgressBar.setMinimumSize(QSize(150, 12))
        self.statusProgressBar.setValue(0)
        self.statusProgressBar.setTextVisible(False)

        self.horizontalLayout_2.addWidget(self.statusProgressBar)

        self.horizontalSpacer = QSpacerItem(250, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.statusViewLogButton = QPushButton(self.centralwidget)
        self.statusViewLogButton.setObjectName(u"statusViewLogButton")
        sizePolicy2.setHeightForWidth(self.statusViewLogButton.sizePolicy().hasHeightForWidth())
        self.statusViewLogButton.setSizePolicy(sizePolicy2)
        self.statusViewLogButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.statusViewLogButton)


        self.bottomRightPanelLayout.addLayout(self.horizontalLayout_2)


        self.bottomPanelLayout.addLayout(self.bottomRightPanelLayout)


        self.appLayout.addLayout(self.bottomPanelLayout)


        self.gridLayout_3.addLayout(self.appLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1274, 22))
        self.fileMenu = QMenu(self.menubar)
        self.fileMenu.setObjectName(u"fileMenu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.fileMenu.menuAction())
        self.fileMenu.addAction(self.loadImageMenuItem)
        self.fileMenu.addAction(self.loadSceneMenuItem)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.saveImageMenuItem)
        self.fileMenu.addAction(self.saveOverlayMenuItem)
        self.fileMenu.addAction(self.saveSceneMenuItem)
        self.fileMenu.addAction(self.saveVTKModelsMenuItem)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Minder3D", None))
        self.loadImageMenuItem.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.saveImageMenuItem.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.saveOverlayMenuItem.setText(QCoreApplication.translate("MainWindow", u"Save Overlay", None))
        self.saveVTKModelsMenuItem.setText(QCoreApplication.translate("MainWindow", u"Save VTK Models", None))
        self.loadSceneMenuItem.setText(QCoreApplication.translate("MainWindow", u"Load Spatial Objects", None))
        self.saveSceneMenuItem.setText(QCoreApplication.translate("MainWindow", u"Save Spatial Objects", None))
        self.savePreProcessedOverlayMenuItem.setText(QCoreApplication.translate("MainWindow", u"Save Pre-Processed Overlay", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.welcomeTab), QCoreApplication.translate("MainWindow", u"Load / Save Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.visualizationTab), QCoreApplication.translate("MainWindow", u"Advanced Visualization", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.newTaskTab), QCoreApplication.translate("MainWindow", u"New Task", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.statusViewLogButton.setText(QCoreApplication.translate("MainWindow", u"View Log", None))
        self.fileMenu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

