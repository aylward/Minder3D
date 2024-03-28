# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pytubeviewkhQzma.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1037, 676)
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
        self.view2DPanelLayout = QVBoxLayout()
        self.view2DPanelLayout.setObjectName(u"view2DPanelLayout")
        self.view2DPanelLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.view2DPanelSpacer = QSpacerItem(391, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.view2DPanelLayout.addItem(self.view2DPanelSpacer)


        self.topPanelLayout.addLayout(self.view2DPanelLayout)

        self.topPanelSpacer = QSpacerItem(0, 391, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.topPanelLayout.addItem(self.topPanelSpacer)

        self.view3DPanelLayout = QVBoxLayout()
        self.view3DPanelLayout.setObjectName(u"view3DPanelLayout")
        self.view3DPanelSpacer = QSpacerItem(361, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.view3DPanelLayout.addItem(self.view3DPanelSpacer)


        self.topPanelLayout.addLayout(self.view3DPanelLayout)

        self.tablePanelLayout = QVBoxLayout()
        self.tablePanelLayout.setObjectName(u"tablePanelLayout")
        self.tablePanelSpacer = QSpacerItem(165, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.tablePanelLayout.addItem(self.tablePanelSpacer)


        self.topPanelLayout.addLayout(self.tablePanelLayout)


        self.verticalLayout.addLayout(self.topPanelLayout)

        self.middlePanelLayout = QHBoxLayout()
        self.middlePanelLayout.setObjectName(u"middlePanelLayout")
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
        self.objectNameLabel = QLabel(self.objectGroupBox)
        self.objectNameLabel.setObjectName(u"objectNameLabel")

        self.gridLayout_2.addWidget(self.objectNameLabel, 1, 0, 1, 1)

        self.objectColorByLabel = QLabel(self.objectGroupBox)
        self.objectColorByLabel.setObjectName(u"objectColorByLabel")

        self.gridLayout_2.addWidget(self.objectColorByLabel, 4, 0, 1, 1)

        self.objectColorByComboBox = QComboBox(self.objectGroupBox)
        self.objectColorByComboBox.setObjectName(u"objectColorByComboBox")

        self.gridLayout_2.addWidget(self.objectColorByComboBox, 4, 1, 1, 3)

        self.objectColorLabel = QLabel(self.objectGroupBox)
        self.objectColorLabel.setObjectName(u"objectColorLabel")

        self.gridLayout_2.addWidget(self.objectColorLabel, 5, 0, 1, 1)

        self.objectColorComboBox = QComboBox(self.objectGroupBox)
        self.objectColorComboBox.setObjectName(u"objectColorComboBox")

        self.gridLayout_2.addWidget(self.objectColorComboBox, 5, 1, 1, 3)

        self.objectOpacityLabel = QLabel(self.objectGroupBox)
        self.objectOpacityLabel.setObjectName(u"objectOpacityLabel")

        self.gridLayout_2.addWidget(self.objectOpacityLabel, 6, 0, 1, 1)

        self.objectOpacitySlider = QSlider(self.objectGroupBox)
        self.objectOpacitySlider.setObjectName(u"objectOpacitySlider")
        font = QFont()
        font.setPointSize(5)
        self.objectOpacitySlider.setFont(font)
        self.objectOpacitySlider.setMaximum(100)
        self.objectOpacitySlider.setValue(50)
        self.objectOpacitySlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.objectOpacitySlider, 6, 1, 1, 3)

        self.objectApplyToLabel = QLabel(self.objectGroupBox)
        self.objectApplyToLabel.setObjectName(u"objectApplyToLabel")

        self.gridLayout_2.addWidget(self.objectApplyToLabel, 7, 0, 1, 1)

        self.objectPropertiesToChildrenButton = QPushButton(self.objectGroupBox)
        self.objectPropertiesToChildrenButton.setObjectName(u"objectPropertiesToChildrenButton")
        font1 = QFont()
        font1.setPointSize(7)
        self.objectPropertiesToChildrenButton.setFont(font1)

        self.gridLayout_2.addWidget(self.objectPropertiesToChildrenButton, 7, 1, 1, 1)

        self.objectPropertiesToAllButton = QPushButton(self.objectGroupBox)
        self.objectPropertiesToAllButton.setObjectName(u"objectPropertiesToAllButton")
        self.objectPropertiesToAllButton.setFont(font1)

        self.gridLayout_2.addWidget(self.objectPropertiesToAllButton, 7, 2, 1, 2)

        self.objectDeleteButton = QPushButton(self.objectGroupBox)
        self.objectDeleteButton.setObjectName(u"objectDeleteButton")
        self.objectDeleteButton.setFont(font1)

        self.gridLayout_2.addWidget(self.objectDeleteButton, 3, 3, 1, 1)

        self.objectNameComboBox = QComboBox(self.objectGroupBox)
        self.objectNameComboBox.setObjectName(u"objectNameComboBox")

        self.gridLayout_2.addWidget(self.objectNameComboBox, 1, 1, 1, 3)

        self.objectHightlightSelectedCheckBox = QCheckBox(self.objectGroupBox)
        self.objectHightlightSelectedCheckBox.setObjectName(u"objectHightlightSelectedCheckBox")
        font2 = QFont()
        font2.setPointSize(9)
        self.objectHightlightSelectedCheckBox.setFont(font2)
        self.objectHightlightSelectedCheckBox.setChecked(True)

        self.gridLayout_2.addWidget(self.objectHightlightSelectedCheckBox, 3, 1, 1, 1)


        self.middlePanelLayout.addWidget(self.objectGroupBox)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setMinimumSize(QSize(701, 181))
        self.visualizationPanel = QWidget()
        self.visualizationPanel.setObjectName(u"visualizationPanel")
        self.visualizationPanelLayout = QHBoxLayout(self.visualizationPanel)
        self.visualizationPanelLayout.setObjectName(u"visualizationPanelLayout")
        self.tabWidget.addTab(self.visualizationPanel, "")
        self.preProcessPanel = QWidget()
        self.preProcessPanel.setObjectName(u"preProcessPanel")
        self.preProcessPanelLayout = QVBoxLayout(self.preProcessPanel)
        self.preProcessPanelLayout.setObjectName(u"preProcessPanelLayout")
        self.tabWidget.addTab(self.preProcessPanel, "")
        self.lungAIPanel = QWidget()
        self.lungAIPanel.setObjectName(u"lungAIPanel")
        self.lungAIPanelLayout = QVBoxLayout(self.lungAIPanel)
        self.lungAIPanelLayout.setObjectName(u"lungAIPanelLayout")
        self.tabWidget.addTab(self.lungAIPanel, "")
        self.tubePanel = QWidget()
        self.tubePanel.setObjectName(u"tubePanel")
        self.tubePanelLayout = QHBoxLayout(self.tubePanel)
        self.tubePanelLayout.setObjectName(u"tubePanelLayout")
        self.tabWidget.addTab(self.tubePanel, "")

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
        self.statusMinorProgressBar = QProgressBar(self.statusGroupBox)
        self.statusMinorProgressBar.setObjectName(u"statusMinorProgressBar")
        sizePolicy1.setHeightForWidth(self.statusMinorProgressBar.sizePolicy().hasHeightForWidth())
        self.statusMinorProgressBar.setSizePolicy(sizePolicy1)
        self.statusMinorProgressBar.setMinimumSize(QSize(150, 12))
        self.statusMinorProgressBar.setValue(0)
        self.statusMinorProgressBar.setTextVisible(False)

        self.gridLayout.addWidget(self.statusMinorProgressBar, 0, 4, 1, 1)

        self.statusGroupBoxSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.statusGroupBoxSpacer, 0, 5, 1, 1)

        self.status = QLabel(self.statusGroupBox)
        self.status.setObjectName(u"status")
        self.status.setMinimumSize(QSize(200, 0))
        self.status.setFont(font2)
        self.status.setAutoFillBackground(True)
        self.status.setFrameShape(QFrame.NoFrame)
        self.status.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.status, 0, 1, 2, 1)

        self.statusMajorProgressBar = QProgressBar(self.statusGroupBox)
        self.statusMajorProgressBar.setObjectName(u"statusMajorProgressBar")
        sizePolicy1.setHeightForWidth(self.statusMajorProgressBar.sizePolicy().hasHeightForWidth())
        self.statusMajorProgressBar.setSizePolicy(sizePolicy1)
        self.statusMajorProgressBar.setMinimumSize(QSize(150, 12))
        self.statusMajorProgressBar.setValue(0)
        self.statusMajorProgressBar.setTextVisible(False)

        self.gridLayout.addWidget(self.statusMajorProgressBar, 0, 3, 1, 1)

        self.statusLabel = QLabel(self.statusGroupBox)
        self.statusLabel.setObjectName(u"statusLabel")

        self.gridLayout.addWidget(self.statusLabel, 0, 0, 2, 1)

        self.statusViewLogButton = QPushButton(self.statusGroupBox)
        self.statusViewLogButton.setObjectName(u"statusViewLogButton")
        self.statusViewLogButton.setFont(font1)

        self.gridLayout.addWidget(self.statusViewLogButton, 0, 6, 2, 1)


        self.bottomPanelLayout.addWidget(self.statusGroupBox)


        self.verticalLayout.addLayout(self.bottomPanelLayout)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1037, 22))
        self.fileMenu = QMenu(self.menubar)
        self.fileMenu.setObjectName(u"fileMenu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.fileMenu.menuAction())
        self.fileMenu.addAction(self.loadSceneMenuItem)
        self.fileMenu.addAction(self.loadImageMenuItem)
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
        self.objectNameLabel.setText(QCoreApplication.translate("MainWindow", u"Object:", None))
        self.objectColorByLabel.setText(QCoreApplication.translate("MainWindow", u"Color by:", None))
#if QT_CONFIG(accessibility)
        self.objectColorByComboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.objectColorByComboBox.setCurrentText("")
        self.objectColorLabel.setText(QCoreApplication.translate("MainWindow", u"Solid Color:", None))
#if QT_CONFIG(accessibility)
        self.objectColorComboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.objectColorComboBox.setCurrentText("")
        self.objectOpacityLabel.setText(QCoreApplication.translate("MainWindow", u"Opacity:", None))
        self.objectApplyToLabel.setText(QCoreApplication.translate("MainWindow", u"Apply to:", None))
        self.objectPropertiesToChildrenButton.setText(QCoreApplication.translate("MainWindow", u"Children", None))
        self.objectPropertiesToAllButton.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.objectDeleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(accessibility)
        self.objectNameComboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.objectNameComboBox.setCurrentText("")
        self.objectHightlightSelectedCheckBox.setText(QCoreApplication.translate("MainWindow", u"Highlight", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.visualizationPanel), QCoreApplication.translate("MainWindow", u"Visualization", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.preProcessPanel), QCoreApplication.translate("MainWindow", u"Pre-process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lungAIPanel), QCoreApplication.translate("MainWindow", u"Lung AI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tubePanel), QCoreApplication.translate("MainWindow", u"Tubes", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"Ready", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.statusViewLogButton.setText(QCoreApplication.translate("MainWindow", u"View Log", None))
        self.fileMenu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

