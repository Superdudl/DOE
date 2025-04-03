# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSplitter, QStatusBar, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1029, 556)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        self.connect_camera = QAction(mainWindow)
        self.connect_camera.setObjectName(u"connect_camera")
        self.connect_camera.setCheckable(False)
        self.load_video = QAction(mainWindow)
        self.load_video.setObjectName(u"load_video")
        self.load_video.setCheckable(False)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.videoCaptureWidget = QWidget(self.centralwidget)
        self.videoCaptureWidget.setObjectName(u"videoCaptureWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.videoCaptureWidget.sizePolicy().hasHeightForWidth())
        self.videoCaptureWidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.videoCaptureWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.splitter = QSplitter(self.videoCaptureWidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setSizeIncrement(QSize(0, 0))
        self.splitter.setFrameShape(QFrame.Shape.NoFrame)
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.videoCaptureLabel = QLabel(self.splitter)
        self.videoCaptureLabel.setObjectName(u"videoCaptureLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.videoCaptureLabel.sizePolicy().hasHeightForWidth())
        self.videoCaptureLabel.setSizePolicy(sizePolicy2)
        self.videoCaptureLabel.setMinimumSize(QSize(78, 68))
        self.videoCaptureLabel.setBaseSize(QSize(0, 0))
        self.videoCaptureLabel.setFrameShape(QFrame.Shape.Box)
        self.videoCaptureLabel.setFrameShadow(QFrame.Shadow.Sunken)
        self.videoCaptureLabel.setScaledContents(False)
        self.splitter.addWidget(self.videoCaptureLabel)
        self.inferenceLabel = QLabel(self.splitter)
        self.inferenceLabel.setObjectName(u"inferenceLabel")
        sizePolicy2.setHeightForWidth(self.inferenceLabel.sizePolicy().hasHeightForWidth())
        self.inferenceLabel.setSizePolicy(sizePolicy2)
        self.inferenceLabel.setMinimumSize(QSize(78, 68))
        self.inferenceLabel.setSizeIncrement(QSize(0, 0))
        self.inferenceLabel.setFrameShape(QFrame.Shape.Box)
        self.inferenceLabel.setFrameShadow(QFrame.Shadow.Sunken)
        self.splitter.addWidget(self.inferenceLabel)

        self.verticalLayout_3.addWidget(self.splitter)

        self.verticalSpacer = QSpacerItem(10, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)

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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.settingsScrollArea.sizePolicy().hasHeightForWidth())
        self.settingsScrollArea.setSizePolicy(sizePolicy3)
        self.settingsScrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.settingsScrollArea.setWidgetResizable(True)
        self.settingsScrollArea.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.settingsScrollAreaContents = QWidget()
        self.settingsScrollAreaContents.setObjectName(u"settingsScrollAreaContents")
        self.settingsScrollAreaContents.setGeometry(QRect(0, 0, 357, 240))
        self.verticalLayout_2 = QVBoxLayout(self.settingsScrollAreaContents)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(-1, 50, -1, 9)
        self.settingsGridLayout = QGridLayout()
        self.settingsGridLayout.setObjectName(u"settingsGridLayout")
        self.settingsGridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.saveLabel = QLabel(self.settingsScrollAreaContents)
        self.saveLabel.setObjectName(u"saveLabel")

        self.settingsGridLayout.addWidget(self.saveLabel, 3, 0, 1, 1)

        self.exposureEdit = QLineEdit(self.settingsScrollAreaContents)
        self.exposureEdit.setObjectName(u"exposureEdit")

        self.settingsGridLayout.addWidget(self.exposureEdit, 1, 1, 1, 1)

        self.modelLabel = QLabel(self.settingsScrollAreaContents)
        self.modelLabel.setObjectName(u"modelLabel")

        self.settingsGridLayout.addWidget(self.modelLabel, 0, 0, 1, 1)

        self.saveEdit = QLineEdit(self.settingsScrollAreaContents)
        self.saveEdit.setObjectName(u"saveEdit")

        self.settingsGridLayout.addWidget(self.saveEdit, 3, 1, 1, 1)

        self.formatLabel = QLabel(self.settingsScrollAreaContents)
        self.formatLabel.setObjectName(u"formatLabel")

        self.settingsGridLayout.addWidget(self.formatLabel, 2, 0, 1, 1)

        self.exposureLabel = QLabel(self.settingsScrollAreaContents)
        self.exposureLabel.setObjectName(u"exposureLabel")

        self.settingsGridLayout.addWidget(self.exposureLabel, 1, 0, 1, 1)

        self.formatEdit = QLineEdit(self.settingsScrollAreaContents)
        self.formatEdit.setObjectName(u"formatEdit")

        self.settingsGridLayout.addWidget(self.formatEdit, 2, 1, 1, 1)

        self.modelComboBox = QComboBox(self.settingsScrollAreaContents)
        self.modelComboBox.setObjectName(u"modelComboBox")

        self.settingsGridLayout.addWidget(self.modelComboBox, 0, 1, 1, 1)

        self.checkBox = QCheckBox(self.settingsScrollAreaContents)
        self.checkBox.setObjectName(u"checkBox")

        self.settingsGridLayout.addWidget(self.checkBox, 1, 2, 1, 1)

        self.settingsGridLayout.setColumnStretch(0, 1)
        self.settingsGridLayout.setColumnStretch(1, 4)
        self.settingsGridLayout.setColumnStretch(2, 1)

        self.verticalLayout_2.addLayout(self.settingsGridLayout)

        self.settingsScrollArea.setWidget(self.settingsScrollAreaContents)

        self.verticalLayout.addWidget(self.settingsScrollArea)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonsLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.startButton = QPushButton(self.settingsWidget)
        self.startButton.setObjectName(u"startButton")

        self.buttonsLayout.addWidget(self.startButton)

        self.pushButton = QPushButton(self.settingsWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.buttonsLayout.addWidget(self.pushButton)

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
        self.menuBar.setGeometry(QRect(0, 0, 1029, 22))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        mainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(mainWindow)
        self.statusBar.setObjectName(u"statusBar")
        mainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.connect_camera)
        self.menu.addAction(self.load_video)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u0421\u041f\u041e", None))
        self.connect_camera.setText(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043a\u0430\u043c\u0435\u0440\u0443", None))
#if QT_CONFIG(shortcut)
        self.connect_camera.setShortcut(QCoreApplication.translate("mainWindow", u"F3", None))
#endif // QT_CONFIG(shortcut)
        self.load_video.setText(QCoreApplication.translate("mainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432\u0438\u0434\u0435\u043e", None))
        self.videoCaptureLabel.setText("")
        self.inferenceLabel.setText("")
        self.saveLabel.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432", None))
        self.modelLabel.setText(QCoreApplication.translate("mainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.formatLabel.setText(QCoreApplication.translate("mainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442", None))
        self.exposureLabel.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u043a\u043e\u043f\u043b\u0435\u043d\u0438\u044f", None))
        self.checkBox.setText(QCoreApplication.translate("mainWindow", u"\u0410\u0432\u0442\u043e", None))
        self.startButton.setText(QCoreApplication.translate("mainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"\u0421\u0442\u043e\u043f", None))
        self.recordButton.setText(QCoreApplication.translate("mainWindow", u"\u0417\u0430\u043f\u0438\u0441\u044c", None))
        self.stopButton.setText(QCoreApplication.translate("mainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.menu.setTitle(QCoreApplication.translate("mainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430", None))
    # retranslateUi

