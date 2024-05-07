# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sovObjectPanelWidgetFfXnUi.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QWidget)

class Ui_ObjectPanelWidget(object):
    def setupUi(self, ObjectPanelWidget):
        if not ObjectPanelWidget.objectName():
            ObjectPanelWidget.setObjectName(u"ObjectPanelWidget")
        ObjectPanelWidget.resize(290, 222)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ObjectPanelWidget.sizePolicy().hasHeightForWidth())
        ObjectPanelWidget.setSizePolicy(sizePolicy)
        ObjectPanelWidget.setMinimumSize(QSize(290, 222))
        self.gridLayoutWidget = QWidget(ObjectPanelWidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 285, 221))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gridLayoutWidget.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.objectUnselectAllButton = QPushButton(self.gridLayoutWidget)
        self.objectUnselectAllButton.setObjectName(u"objectUnselectAllButton")
        font = QFont()
        font.setPointSize(7)
        self.objectUnselectAllButton.setFont(font)

        self.gridLayout.addWidget(self.objectUnselectAllButton, 0, 2, 1, 1)

        self.objectOpacitySlider = QSlider(self.gridLayoutWidget)
        self.objectOpacitySlider.setObjectName(u"objectOpacitySlider")
        font1 = QFont()
        font1.setPointSize(5)
        self.objectOpacitySlider.setFont(font1)
        self.objectOpacitySlider.setMaximum(100)
        self.objectOpacitySlider.setValue(50)
        self.objectOpacitySlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.objectOpacitySlider, 3, 1, 1, 2)

        self.objectColorByLabel = QLabel(self.gridLayoutWidget)
        self.objectColorByLabel.setObjectName(u"objectColorByLabel")

        self.gridLayout.addWidget(self.objectColorByLabel, 4, 0, 1, 1)

        self.objectPropertiesToChildrenButton = QPushButton(self.gridLayoutWidget)
        self.objectPropertiesToChildrenButton.setObjectName(u"objectPropertiesToChildrenButton")
        self.objectPropertiesToChildrenButton.setFont(font)

        self.gridLayout.addWidget(self.objectPropertiesToChildrenButton, 7, 0, 1, 1)

        self.objectNameComboBox = QComboBox(self.gridLayoutWidget)
        self.objectNameComboBox.setObjectName(u"objectNameComboBox")

        self.gridLayout.addWidget(self.objectNameComboBox, 1, 1, 1, 2)

        self.objectColorByComboBox = QComboBox(self.gridLayoutWidget)
        self.objectColorByComboBox.setObjectName(u"objectColorByComboBox")

        self.gridLayout.addWidget(self.objectColorByComboBox, 4, 1, 1, 2)

        self.objectColorLabel = QLabel(self.gridLayoutWidget)
        self.objectColorLabel.setObjectName(u"objectColorLabel")

        self.gridLayout.addWidget(self.objectColorLabel, 5, 1, 1, 1)

        self.objectNameLabel = QLabel(self.gridLayoutWidget)
        self.objectNameLabel.setObjectName(u"objectNameLabel")

        self.gridLayout.addWidget(self.objectNameLabel, 1, 0, 1, 1)

        self.objectHighlightSelectedObjectsCheckBox = QCheckBox(self.gridLayoutWidget)
        self.objectHighlightSelectedObjectsCheckBox.setObjectName(u"objectHighlightSelectedObjectsCheckBox")
        self.objectHighlightSelectedObjectsCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.objectHighlightSelectedObjectsCheckBox, 0, 0, 1, 2)

        self.objectRenameButton = QPushButton(self.gridLayoutWidget)
        self.objectRenameButton.setObjectName(u"objectRenameButton")
        self.objectRenameButton.setFont(font)

        self.gridLayout.addWidget(self.objectRenameButton, 2, 1, 1, 1)

        self.objectOpacityLabel = QLabel(self.gridLayoutWidget)
        self.objectOpacityLabel.setObjectName(u"objectOpacityLabel")

        self.gridLayout.addWidget(self.objectOpacityLabel, 3, 0, 1, 1)

        self.objectColorComboBox = QComboBox(self.gridLayoutWidget)
        self.objectColorComboBox.setObjectName(u"objectColorComboBox")

        self.gridLayout.addWidget(self.objectColorComboBox, 5, 2, 1, 1)

        self.objectPropertiesToSimilarButton = QPushButton(self.gridLayoutWidget)
        self.objectPropertiesToSimilarButton.setObjectName(u"objectPropertiesToSimilarButton")
        self.objectPropertiesToSimilarButton.setFont(font)

        self.gridLayout.addWidget(self.objectPropertiesToSimilarButton, 7, 1, 1, 1)

        self.objectPropertiesToAllButton = QPushButton(self.gridLayoutWidget)
        self.objectPropertiesToAllButton.setObjectName(u"objectPropertiesToAllButton")
        self.objectPropertiesToAllButton.setFont(font)

        self.gridLayout.addWidget(self.objectPropertiesToAllButton, 7, 2, 1, 1)

        self.objectDeleteButton = QPushButton(self.gridLayoutWidget)
        self.objectDeleteButton.setObjectName(u"objectDeleteButton")
        self.objectDeleteButton.setFont(font)

        self.gridLayout.addWidget(self.objectDeleteButton, 2, 2, 1, 1)

        self.objectApplyToLabel = QLabel(self.gridLayoutWidget)
        self.objectApplyToLabel.setObjectName(u"objectApplyToLabel")

        self.gridLayout.addWidget(self.objectApplyToLabel, 6, 0, 1, 3)


        self.retranslateUi(ObjectPanelWidget)

        QMetaObject.connectSlotsByName(ObjectPanelWidget)
    # setupUi

    def retranslateUi(self, ObjectPanelWidget):
        ObjectPanelWidget.setWindowTitle(QCoreApplication.translate("ObjectPanelWidget", u"Form", None))
        self.objectUnselectAllButton.setText(QCoreApplication.translate("ObjectPanelWidget", u"Unselect All", None))
        self.objectColorByLabel.setText(QCoreApplication.translate("ObjectPanelWidget", u"Visualization:", None))
        self.objectPropertiesToChildrenButton.setText(QCoreApplication.translate("ObjectPanelWidget", u"Children", None))
#if QT_CONFIG(accessibility)
        self.objectNameComboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.objectNameComboBox.setCurrentText("")
#if QT_CONFIG(accessibility)
        self.objectColorByComboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.objectColorByComboBox.setCurrentText("")
        self.objectColorLabel.setText(QCoreApplication.translate("ObjectPanelWidget", u"Solid Color:", None))
        self.objectNameLabel.setText(QCoreApplication.translate("ObjectPanelWidget", u"Object:", None))
        self.objectHighlightSelectedObjectsCheckBox.setText(QCoreApplication.translate("ObjectPanelWidget", u"Highlight Selected", None))
        self.objectRenameButton.setText(QCoreApplication.translate("ObjectPanelWidget", u"Rename", None))
        self.objectOpacityLabel.setText(QCoreApplication.translate("ObjectPanelWidget", u"Opacity:", None))
#if QT_CONFIG(accessibility)
        self.objectColorComboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.objectColorComboBox.setCurrentText("")
        self.objectPropertiesToSimilarButton.setText(QCoreApplication.translate("ObjectPanelWidget", u"Similar", None))
        self.objectPropertiesToAllButton.setText(QCoreApplication.translate("ObjectPanelWidget", u"All", None))
        self.objectDeleteButton.setText(QCoreApplication.translate("ObjectPanelWidget", u"Delete", None))
        self.objectApplyToLabel.setText(QCoreApplication.translate("ObjectPanelWidget", u"Propogate vizualization properties to:", None))
    # retranslateUi

