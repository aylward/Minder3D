# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovView2DPanelWidgetbqcKAo.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QToolButton, QVBoxLayout,
    QWidget)

class Ui_View2DPanelWidget(object):
    def setupUi(self, View2DPanelWidget):
        if not View2DPanelWidget.objectName():
            View2DPanelWidget.setObjectName(u"View2DPanelWidget")
        View2DPanelWidget.resize(499, 491)
        self.gridLayout = QGridLayout(View2DPanelWidget)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.view2DPointModeButton = QToolButton(View2DPanelWidget)
        self.view2DPointModeButton.setObjectName(u"view2DPointModeButton")
        self.view2DPointModeButton.setIconSize(QSize(20, 20))
        self.view2DPointModeButton.setCheckable(True)

        self.verticalLayout_3.addWidget(self.view2DPointModeButton)

        self.view2DSelectModeButton = QToolButton(View2DPanelWidget)
        self.view2DSelectModeButton.setObjectName(u"view2DSelectModeButton")
        self.view2DSelectModeButton.setIconSize(QSize(20, 20))
        self.view2DSelectModeButton.setCheckable(True)

        self.verticalLayout_3.addWidget(self.view2DSelectModeButton)

        self.view2DWindowLevelModeButton = QToolButton(View2DPanelWidget)
        self.view2DWindowLevelModeButton.setObjectName(u"view2DWindowLevelModeButton")
        self.view2DWindowLevelModeButton.setIconSize(QSize(20, 20))
        self.view2DWindowLevelModeButton.setCheckable(True)

        self.verticalLayout_3.addWidget(self.view2DWindowLevelModeButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.view2DPaintModeButton = QToolButton(View2DPanelWidget)
        self.view2DPaintModeButton.setObjectName(u"view2DPaintModeButton")
        self.view2DPaintModeButton.setIconSize(QSize(20, 20))
        self.view2DPaintModeButton.setCheckable(True)

        self.verticalLayout_3.addWidget(self.view2DPaintModeButton)

        self.view2DContourModeButton = QToolButton(View2DPanelWidget)
        self.view2DContourModeButton.setObjectName(u"view2DContourModeButton")
        self.view2DContourModeButton.setIconSize(QSize(20, 20))
        self.view2DContourModeButton.setCheckable(True)

        self.verticalLayout_3.addWidget(self.view2DContourModeButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.view2DRulerModeButton = QToolButton(View2DPanelWidget)
        self.view2DRulerModeButton.setObjectName(u"view2DRulerModeButton")
        self.view2DRulerModeButton.setIconSize(QSize(20, 20))
        self.view2DRulerModeButton.setCheckable(True)

        self.verticalLayout_3.addWidget(self.view2DRulerModeButton)

        self.view2DAngleModeButton = QToolButton(View2DPanelWidget)
        self.view2DAngleModeButton.setObjectName(u"view2DAngleModeButton")
        self.view2DAngleModeButton.setIconSize(QSize(20, 20))
        self.view2DAngleModeButton.setCheckable(True)

        self.verticalLayout_3.addWidget(self.view2DAngleModeButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.view2DCropModeButton = QToolButton(View2DPanelWidget)
        self.view2DCropModeButton.setObjectName(u"view2DCropModeButton")
        self.view2DCropModeButton.setIconSize(QSize(20, 20))
        self.view2DCropModeButton.setCheckable(True)

        self.verticalLayout_3.addWidget(self.view2DCropModeButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.view2DLayout = QVBoxLayout()
        self.view2DLayout.setSpacing(3)
        self.view2DLayout.setObjectName(u"view2DLayout")
        self.view2DLayout.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.gridLayout_2.addLayout(self.view2DLayout, 0, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.view2DSliceSlider = QSlider(View2DPanelWidget)
        self.view2DSliceSlider.setObjectName(u"view2DSliceSlider")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view2DSliceSlider.sizePolicy().hasHeightForWidth())
        self.view2DSliceSlider.setSizePolicy(sizePolicy)
        self.view2DSliceSlider.setMinimumSize(QSize(10, 422))
        self.view2DSliceSlider.setOrientation(Qt.Vertical)

        self.verticalLayout.addWidget(self.view2DSliceSlider)

        self.view2DSliceText = QSpinBox(View2DPanelWidget)
        self.view2DSliceText.setObjectName(u"view2DSliceText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.view2DSliceText.sizePolicy().hasHeightForWidth())
        self.view2DSliceText.setSizePolicy(sizePolicy1)
        self.view2DSliceText.setMinimumSize(QSize(39, 0))
        self.view2DSliceText.setMaximum(999)
        self.view2DSliceText.setDisplayIntegerBase(10)

        self.verticalLayout.addWidget(self.view2DSliceText)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.view2DAxButton = QPushButton(View2DPanelWidget)
        self.view2DAxButton.setObjectName(u"view2DAxButton")
        sizePolicy1.setHeightForWidth(self.view2DAxButton.sizePolicy().hasHeightForWidth())
        self.view2DAxButton.setSizePolicy(sizePolicy1)
        self.view2DAxButton.setMinimumSize(QSize(30, 0))
        font = QFont()
        font.setPointSize(7)
        self.view2DAxButton.setFont(font)

        self.horizontalLayout.addWidget(self.view2DAxButton)

        self.view2DCoButton = QPushButton(View2DPanelWidget)
        self.view2DCoButton.setObjectName(u"view2DCoButton")
        sizePolicy1.setHeightForWidth(self.view2DCoButton.sizePolicy().hasHeightForWidth())
        self.view2DCoButton.setSizePolicy(sizePolicy1)
        self.view2DCoButton.setMinimumSize(QSize(30, 0))
        self.view2DCoButton.setFont(font)

        self.horizontalLayout.addWidget(self.view2DCoButton)

        self.view2DSaButton = QPushButton(View2DPanelWidget)
        self.view2DSaButton.setObjectName(u"view2DSaButton")
        sizePolicy1.setHeightForWidth(self.view2DSaButton.sizePolicy().hasHeightForWidth())
        self.view2DSaButton.setSizePolicy(sizePolicy1)
        self.view2DSaButton.setMinimumSize(QSize(30, 0))
        self.view2DSaButton.setFont(font)

        self.horizontalLayout.addWidget(self.view2DSaButton)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.view2DOverlayOpacityLabel = QLabel(View2DPanelWidget)
        self.view2DOverlayOpacityLabel.setObjectName(u"view2DOverlayOpacityLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.view2DOverlayOpacityLabel.sizePolicy().hasHeightForWidth())
        self.view2DOverlayOpacityLabel.setSizePolicy(sizePolicy2)
        self.view2DOverlayOpacityLabel.setFont(font)

        self.horizontalLayout.addWidget(self.view2DOverlayOpacityLabel)

        self.view2DOverlayOpacitySlider = QSlider(View2DPanelWidget)
        self.view2DOverlayOpacitySlider.setObjectName(u"view2DOverlayOpacitySlider")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.view2DOverlayOpacitySlider.sizePolicy().hasHeightForWidth())
        self.view2DOverlayOpacitySlider.setSizePolicy(sizePolicy3)
        self.view2DOverlayOpacitySlider.setMinimumSize(QSize(75, 12))
        self.view2DOverlayOpacitySlider.setBaseSize(QSize(0, 0))
        self.view2DOverlayOpacitySlider.setFont(font)
        self.view2DOverlayOpacitySlider.setMaximum(100)
        self.view2DOverlayOpacitySlider.setValue(50)
        self.view2DOverlayOpacitySlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.view2DOverlayOpacitySlider)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.view2DResetButton = QPushButton(View2DPanelWidget)
        self.view2DResetButton.setObjectName(u"view2DResetButton")
        sizePolicy1.setHeightForWidth(self.view2DResetButton.sizePolicy().hasHeightForWidth())
        self.view2DResetButton.setSizePolicy(sizePolicy1)
        self.view2DResetButton.setMinimumSize(QSize(30, 0))
        self.view2DResetButton.setMaximumSize(QSize(30, 16777215))
        self.view2DResetButton.setFont(font)

        self.horizontalLayout.addWidget(self.view2DResetButton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 2)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)


        self.retranslateUi(View2DPanelWidget)

        QMetaObject.connectSlotsByName(View2DPanelWidget)
    # setupUi

    def retranslateUi(self, View2DPanelWidget):
        View2DPanelWidget.setWindowTitle(QCoreApplication.translate("View2DPanelWidget", u"Form", None))
        self.view2DPointModeButton.setText("")
        self.view2DSelectModeButton.setText("")
        self.view2DWindowLevelModeButton.setText("")
        self.view2DPaintModeButton.setText("")
        self.view2DContourModeButton.setText("")
        self.view2DRulerModeButton.setText("")
        self.view2DAngleModeButton.setText("")
        self.view2DCropModeButton.setText("")
#if QT_CONFIG(shortcut)
        self.view2DCropModeButton.setShortcut(QCoreApplication.translate("View2DPanelWidget", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.view2DAxButton.setText(QCoreApplication.translate("View2DPanelWidget", u"Ax", None))
        self.view2DCoButton.setText(QCoreApplication.translate("View2DPanelWidget", u"Co", None))
        self.view2DSaButton.setText(QCoreApplication.translate("View2DPanelWidget", u"Sa", None))
        self.view2DOverlayOpacityLabel.setText(QCoreApplication.translate("View2DPanelWidget", u"Overlay Opacity: ", None))
        self.view2DResetButton.setText(QCoreApplication.translate("View2DPanelWidget", u"Reset", None))
    # retranslateUi

