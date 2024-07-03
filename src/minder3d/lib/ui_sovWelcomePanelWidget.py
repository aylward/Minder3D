# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovWelcomePanelWidgetkiiigT.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_WelcomePanelWidget(object):
    def setupUi(self, WelcomePanelWidget):
        if not WelcomePanelWidget.objectName():
            WelcomePanelWidget.setObjectName(u"WelcomePanelWidget")
        WelcomePanelWidget.resize(667, 153)
        self.welcomeLoadImageButton = QPushButton(WelcomePanelWidget)
        self.welcomeLoadImageButton.setObjectName(u"welcomeLoadImageButton")
        self.welcomeLoadImageButton.setGeometry(QRect(20, 10, 121, 24))
        self.welcomeImportDICOMButton = QPushButton(WelcomePanelWidget)
        self.welcomeImportDICOMButton.setObjectName(u"welcomeImportDICOMButton")
        self.welcomeImportDICOMButton.setGeometry(QRect(20, 70, 121, 24))
        self.welcomeSaveImageButton = QPushButton(WelcomePanelWidget)
        self.welcomeSaveImageButton.setObjectName(u"welcomeSaveImageButton")
        self.welcomeSaveImageButton.setGeometry(QRect(300, 10, 121, 24))
        self.welcomeSaveSceneButton = QPushButton(WelcomePanelWidget)
        self.welcomeSaveSceneButton.setObjectName(u"welcomeSaveSceneButton")
        self.welcomeSaveSceneButton.setGeometry(QRect(160, 10, 121, 24))
        self.welcomeLoadSceneButton = QPushButton(WelcomePanelWidget)
        self.welcomeLoadSceneButton.setObjectName(u"welcomeLoadSceneButton")
        self.welcomeLoadSceneButton.setGeometry(QRect(160, 40, 121, 24))
        self.welcomeSaveOverlayButton = QPushButton(WelcomePanelWidget)
        self.welcomeSaveOverlayButton.setObjectName(u"welcomeSaveOverlayButton")
        self.welcomeSaveOverlayButton.setGeometry(QRect(440, 40, 121, 24))
        self.welcomeSaveVTKModelsButton = QPushButton(WelcomePanelWidget)
        self.welcomeSaveVTKModelsButton.setObjectName(u"welcomeSaveVTKModelsButton")
        self.welcomeSaveVTKModelsButton.setGeometry(QRect(300, 40, 121, 24))
        self.welcomeLoadOverlayButton = QPushButton(WelcomePanelWidget)
        self.welcomeLoadOverlayButton.setObjectName(u"welcomeLoadOverlayButton")
        self.welcomeLoadOverlayButton.setGeometry(QRect(440, 10, 121, 24))

        self.retranslateUi(WelcomePanelWidget)

        QMetaObject.connectSlotsByName(WelcomePanelWidget)
    # setupUi

    def retranslateUi(self, WelcomePanelWidget):
        WelcomePanelWidget.setWindowTitle(QCoreApplication.translate("WelcomePanelWidget", u"Form", None))
        self.welcomeLoadImageButton.setText(QCoreApplication.translate("WelcomePanelWidget", u"Load Image", None))
        self.welcomeImportDICOMButton.setText(QCoreApplication.translate("WelcomePanelWidget", u"Import DICOM Data", None))
        self.welcomeSaveImageButton.setText(QCoreApplication.translate("WelcomePanelWidget", u"Save Image", None))
        self.welcomeSaveSceneButton.setText(QCoreApplication.translate("WelcomePanelWidget", u"Save Scene", None))
        self.welcomeLoadSceneButton.setText(QCoreApplication.translate("WelcomePanelWidget", u"Load Scene", None))
        self.welcomeSaveOverlayButton.setText(QCoreApplication.translate("WelcomePanelWidget", u"Save Overlay", None))
        self.welcomeSaveVTKModelsButton.setText(QCoreApplication.translate("WelcomePanelWidget", u"Save VTK Models", None))
        self.welcomeLoadOverlayButton.setText(QCoreApplication.translate("WelcomePanelWidget", u"Load Overlay", None))
    # retranslateUi

