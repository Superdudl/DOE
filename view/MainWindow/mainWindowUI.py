# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt)
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QLayout, QLineEdit,
                               QMenuBar, QPushButton, QScrollArea,
                               QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
                               QWidget)


class _MainWindowUI(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1350, 770)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.videoCaptureWidget = QWidget(self.centralwidget)
        self.videoCaptureWidget.setObjectName(u"videoCaptureWidget")
        self.gridLayout = QGridLayout(self.videoCaptureWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.videoCaptureLabel = QLabel(self.videoCaptureWidget)
        self.videoCaptureLabel.setObjectName(u"videoCaptureLabel")
        self.videoCaptureLabel.setScaledContents(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(3)
        sizePolicy1.setHeightForWidth(self.videoCaptureLabel.sizePolicy().hasHeightForWidth())
        self.videoCaptureLabel.setSizePolicy(sizePolicy1)
        self.videoCaptureLabel.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.videoCaptureLabel, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(0, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.horizontalLayout.addWidget(self.videoCaptureWidget)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.settingsWidget = QWidget(self.centralwidget)
        self.settingsWidget.setObjectName(u"settingsWidget")
        self.verticalLayout = QVBoxLayout(self.settingsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.settingsScrollArea = QScrollArea(self.settingsWidget)
        self.settingsScrollArea.setObjectName(u"settingsScrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.settingsScrollArea.sizePolicy().hasHeightForWidth())
        self.settingsScrollArea.setSizePolicy(sizePolicy2)
        self.settingsScrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.settingsScrollArea.setWidgetResizable(True)
        self.settingsScrollArea.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.settingsScrollAreaContents = QWidget()
        self.settingsScrollAreaContents.setObjectName(u"settingsScrollAreaContents")
        self.settingsScrollAreaContents.setGeometry(QRect(0, 0, 421, 347))
        self.verticalLayout_2 = QVBoxLayout(self.settingsScrollAreaContents)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(-1, 50, -1, 9)
        self.settingsGridLayout = QGridLayout()
        self.settingsGridLayout.setObjectName(u"settingsGridLayout")
        self.modelComboBox = QComboBox(self.settingsScrollAreaContents)
        self.modelComboBox.addItem("")
        self.modelComboBox.addItem("")
        self.modelComboBox.addItem("")
        self.modelComboBox.addItem("")
        self.modelComboBox.setObjectName(u"modelComboBox")

        self.settingsGridLayout.addWidget(self.modelComboBox, 0, 1, 1, 1)

        self.exposureEdit = QLineEdit(self.settingsScrollAreaContents)
        self.exposureEdit.setObjectName(u"exposureEdit")

        self.settingsGridLayout.addWidget(self.exposureEdit, 1, 1, 1, 1)

        self.formatEdit = QLineEdit(self.settingsScrollAreaContents)
        self.formatEdit.setObjectName(u"formatEdit")

        self.settingsGridLayout.addWidget(self.formatEdit, 2, 1, 1, 1)

        self.saveEdit = QLineEdit(self.settingsScrollAreaContents)
        self.saveEdit.setObjectName(u"saveEdit")

        self.settingsGridLayout.addWidget(self.saveEdit, 3, 1, 1, 1)

        self.modelLabel = QLabel(self.settingsScrollAreaContents)
        self.modelLabel.setObjectName(u"modelLabel")

        self.settingsGridLayout.addWidget(self.modelLabel, 0, 0, 1, 1)

        self.exposureLabel = QLabel(self.settingsScrollAreaContents)
        self.exposureLabel.setObjectName(u"exposureLabel")

        self.settingsGridLayout.addWidget(self.exposureLabel, 1, 0, 1, 1)

        self.formatLabel = QLabel(self.settingsScrollAreaContents)
        self.formatLabel.setObjectName(u"formatLabel")

        self.settingsGridLayout.addWidget(self.formatLabel, 2, 0, 1, 1)

        self.saveLabel = QLabel(self.settingsScrollAreaContents)
        self.saveLabel.setObjectName(u"saveLabel")

        self.settingsGridLayout.addWidget(self.saveLabel, 3, 0, 1, 1)

        self.verticalLayout_2.addLayout(self.settingsGridLayout)

        self.settingsScrollArea.setWidget(self.settingsScrollAreaContents)

        self.verticalLayout.addWidget(self.settingsScrollArea)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonsLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.startButton = QPushButton(self.settingsWidget)
        self.startButton.setObjectName(u"startButton")

        self.buttonsLayout.addWidget(self.startButton)

        self.recordButton = QPushButton(self.settingsWidget)
        self.recordButton.setObjectName(u"recordButton")

        self.buttonsLayout.addWidget(self.recordButton)

        self.stopButton = QPushButton(self.settingsWidget)
        self.stopButton.setObjectName(u"stopButton")

        self.buttonsLayout.addWidget(self.stopButton)

        self.verticalLayout.addLayout(self.buttonsLayout)

        self.horizontalLayout.addWidget(self.settingsWidget)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(2, 2)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(mainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1350, 22))
        mainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(mainWindow)
        self.statusBar.setObjectName(u"statusBar")
        mainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)

    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u0421\u041f\u041e", None))
        self.videoCaptureLabel.setText("")
        self.modelComboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"New Item", None))
        self.modelComboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"New Item", None))
        self.modelComboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"New Item", None))
        self.modelComboBox.setItemText(3, QCoreApplication.translate("mainWindow", u"New Item", None))

        self.modelLabel.setText(QCoreApplication.translate("mainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.exposureLabel.setText(QCoreApplication.translate("mainWindow",
                                                              u"\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u043a\u043e\u043f\u043b\u0435\u043d\u0438\u044f",
                                                              None))
        self.formatLabel.setText(
            QCoreApplication.translate("mainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442", None))
        self.saveLabel.setText(
            QCoreApplication.translate("mainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432",
                                       None))
        self.startButton.setText(QCoreApplication.translate("mainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.recordButton.setText(
            QCoreApplication.translate("mainWindow", u"\u0417\u0430\u043f\u0438\u0441\u044c", None))
        self.stopButton.setText(QCoreApplication.translate("mainWindow",
                                                           u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c",
                                                           None))
    # retranslateUi
