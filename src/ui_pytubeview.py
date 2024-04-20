# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pytubeviewyLUtjA.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1043, 688)
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
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.topPanelLayout = QHBoxLayout()
        self.topPanelLayout.setObjectName(u"topPanelLayout")
        self.view2DLayout = QVBoxLayout()
        self.view2DLayout.setObjectName(u"view2DLayout")
        self.view2DLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
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
        self.objectGroupBox = QGroupBox(self.centralwidget)
        self.objectGroupBox.setObjectName(u"objectGroupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.objectGroupBox.sizePolicy().hasHeightForWidth())
        self.objectGroupBox.setSizePolicy(sizePolicy1)
        self.objectGroupBox.setMinimumSize(QSize(211, 181))
        self.objectGroupBox.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(self.objectGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.objectPropertiesToChildrenButton = QPushButton(self.objectGroupBox)
        self.objectPropertiesToChildrenButton.setObjectName(u"objectPropertiesToChildrenButton")
        font = QFont()
        font.setPointSize(7)
        self.objectPropertiesToChildrenButton.setFont(font)

        self.gridLayout_2.addWidget(self.objectPropertiesToChildrenButton, 10, 1, 1, 1)

        self.objectColorByComboBox = QComboBox(self.objectGroupBox)
        self.objectColorByComboBox.setObjectName(u"objectColorByComboBox")

        self.gridLayout_2.addWidget(self.objectColorByComboBox, 5, 1, 1, 3)

        self.objectNameLabel = QLabel(self.objectGroupBox)
        self.objectNameLabel.setObjectName(u"objectNameLabel")

        self.gridLayout_2.addWidget(self.objectNameLabel, 1, 0, 1, 1)

        self.objectColorLabel = QLabel(self.objectGroupBox)
        self.objectColorLabel.setObjectName(u"objectColorLabel")

        self.gridLayout_2.addWidget(self.objectColorLabel, 6, 1, 1, 1)

        self.objectNameComboBox = QComboBox(self.objectGroupBox)
        self.objectNameComboBox.setObjectName(u"objectNameComboBox")

        self.gridLayout_2.addWidget(self.objectNameComboBox, 1, 1, 1, 3)

        self.objectColorComboBox = QComboBox(self.objectGroupBox)
        self.objectColorComboBox.setObjectName(u"objectColorComboBox")

        self.gridLayout_2.addWidget(self.objectColorComboBox, 6, 2, 1, 2)

        self.objectRenameButton = QPushButton(self.objectGroupBox)
        self.objectRenameButton.setObjectName(u"objectRenameButton")

        self.gridLayout_2.addWidget(self.objectRenameButton, 3, 1, 1, 1)

        self.objectColorByLabel = QLabel(self.objectGroupBox)
        self.objectColorByLabel.setObjectName(u"objectColorByLabel")

        self.gridLayout_2.addWidget(self.objectColorByLabel, 5, 0, 1, 1)

        self.objectApplyToLabel = QLabel(self.objectGroupBox)
        self.objectApplyToLabel.setObjectName(u"objectApplyToLabel")

        self.gridLayout_2.addWidget(self.objectApplyToLabel, 8, 0, 1, 4)

        self.objectPropertiesToAllButton = QPushButton(self.objectGroupBox)
        self.objectPropertiesToAllButton.setObjectName(u"objectPropertiesToAllButton")
        self.objectPropertiesToAllButton.setFont(font)

        self.gridLayout_2.addWidget(self.objectPropertiesToAllButton, 10, 2, 1, 2)

        self.objectOpacityLabel = QLabel(self.objectGroupBox)
        self.objectOpacityLabel.setObjectName(u"objectOpacityLabel")

        self.gridLayout_2.addWidget(self.objectOpacityLabel, 4, 0, 1, 1)

        self.objectOpacitySlider = QSlider(self.objectGroupBox)
        self.objectOpacitySlider.setObjectName(u"objectOpacitySlider")
        font1 = QFont()
        font1.setPointSize(5)
        self.objectOpacitySlider.setFont(font1)
        self.objectOpacitySlider.setMaximum(100)
        self.objectOpacitySlider.setValue(50)
        self.objectOpacitySlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.objectOpacitySlider, 4, 1, 1, 3)

        self.objectDeleteButton = QPushButton(self.objectGroupBox)
        self.objectDeleteButton.setObjectName(u"objectDeleteButton")
        self.objectDeleteButton.setFont(font)

        self.gridLayout_2.addWidget(self.objectDeleteButton, 3, 3, 1, 1)


        self.rightPanelLayout.addWidget(self.objectGroupBox)

        self.infoTableLayout = QVBoxLayout()
        self.infoTableLayout.setObjectName(u"infoTableLayout")
        self.infoTableVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.infoTableLayout.addItem(self.infoTableVerticalSpacer)


        self.rightPanelLayout.addLayout(self.infoTableLayout)


        self.topPanelLayout.addLayout(self.rightPanelLayout)


        self.verticalLayout.addLayout(self.topPanelLayout)

        self.middlePanelLayout = QHBoxLayout()
        self.middlePanelLayout.setObjectName(u"middlePanelLayout")
        self.imageTableLayout = QVBoxLayout()
        self.imageTableLayout.setObjectName(u"imageTableLayout")
        self.imageTableLayoutHorizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.imageTableLayout.addItem(self.imageTableLayoutHorizontalSpacer)


        self.middlePanelLayout.addLayout(self.imageTableLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setMinimumSize(QSize(300, 181))
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

        self.middlePanelLayout.addWidget(self.tabWidget)


        self.verticalLayout.addLayout(self.middlePanelLayout)

        self.bottomPanelLayout = QHBoxLayout()
        self.bottomPanelLayout.setObjectName(u"bottomPanelLayout")
        self.statusGroupBox = QGroupBox(self.centralwidget)
        self.statusGroupBox.setObjectName(u"statusGroupBox")
        sizePolicy2.setHeightForWidth(self.statusGroupBox.sizePolicy().hasHeightForWidth())
        self.statusGroupBox.setSizePolicy(sizePolicy2)
        self.statusGroupBox.setMinimumSize(QSize(1020, 24))
        self.statusGroupBox.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(self.statusGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.statusLabel = QLabel(self.statusGroupBox)
        self.statusLabel.setObjectName(u"statusLabel")

        self.gridLayout.addWidget(self.statusLabel, 0, 0, 2, 1)

        self.statusViewLogButton = QPushButton(self.statusGroupBox)
        self.statusViewLogButton.setObjectName(u"statusViewLogButton")
        self.statusViewLogButton.setFont(font)

        self.gridLayout.addWidget(self.statusViewLogButton, 0, 5, 2, 1)

        self.statusProgressBar = QProgressBar(self.statusGroupBox)
        self.statusProgressBar.setObjectName(u"statusProgressBar")
        sizePolicy1.setHeightForWidth(self.statusProgressBar.sizePolicy().hasHeightForWidth())
        self.statusProgressBar.setSizePolicy(sizePolicy1)
        self.statusProgressBar.setMinimumSize(QSize(150, 12))
        self.statusProgressBar.setValue(0)
        self.statusProgressBar.setTextVisible(False)

        self.gridLayout.addWidget(self.statusProgressBar, 0, 3, 1, 1)

        self.statusGroupBoxSpacer = QSpacerItem(600, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.statusGroupBoxSpacer, 0, 4, 1, 1)

        self.statusText = QLineEdit(self.statusGroupBox)
        self.statusText.setObjectName(u"statusText")
        sizePolicy2.setHeightForWidth(self.statusText.sizePolicy().hasHeightForWidth())
        self.statusText.setSizePolicy(sizePolicy2)
        self.statusText.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.statusText, 0, 1, 1, 1)


        self.bottomPanelLayout.addWidget(self.statusGroupBox)


        self.verticalLayout.addLayout(self.bottomPanelLayout)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1043, 22))
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

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyTubeView", None))
        self.loadImageMenuItem.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.saveImageMenuItem.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.saveOverlayMenuItem.setText(QCoreApplication.translate("MainWindow", u"Save Overlay", None))
        self.saveVTKModelsMenuItem.setText(QCoreApplication.translate("MainWindow", u"Save VTK Models", None))
        self.loadSceneMenuItem.setText(QCoreApplication.translate("MainWindow", u"Load Spatial Objects", None))
        self.saveSceneMenuItem.setText(QCoreApplication.translate("MainWindow", u"Save Spatial Objects", None))
        self.savePreProcessedOverlayMenuItem.setText(QCoreApplication.translate("MainWindow", u"Save Pre-Processed Overlay", None))
        self.objectPropertiesToChildrenButton.setText(QCoreApplication.translate("MainWindow", u"Children", None))
#if QT_CONFIG(accessibility)
        self.objectColorByComboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.objectColorByComboBox.setCurrentText("")
        self.objectNameLabel.setText(QCoreApplication.translate("MainWindow", u"Object:", None))
        self.objectColorLabel.setText(QCoreApplication.translate("MainWindow", u"Solid Color:", None))
#if QT_CONFIG(accessibility)
        self.objectNameComboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.objectNameComboBox.setCurrentText("")
#if QT_CONFIG(accessibility)
        self.objectColorComboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.objectColorComboBox.setCurrentText("")
        self.objectRenameButton.setText(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.objectColorByLabel.setText(QCoreApplication.translate("MainWindow", u"Visualization:", None))
        self.objectApplyToLabel.setText(QCoreApplication.translate("MainWindow", u"Propogate vizualization properties to:", None))
        self.objectPropertiesToAllButton.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.objectOpacityLabel.setText(QCoreApplication.translate("MainWindow", u"Opacity:", None))
        self.objectDeleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.welcomeTab), QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.visualizationTab), QCoreApplication.translate("MainWindow", u"Visualization", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.newTaskTab), QCoreApplication.translate("MainWindow", u"New Task", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.statusViewLogButton.setText(QCoreApplication.translate("MainWindow", u"View Log", None))
        self.fileMenu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

