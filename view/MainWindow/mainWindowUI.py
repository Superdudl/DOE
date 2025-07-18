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
        self.actionPSNR_SSIM = QAction(mainWindow)
        self.actionPSNR_SSIM.setObjectName(u"actionPSNR_SSIM")
        self.action = QAction(mainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(mainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(mainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(mainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(mainWindow)
        self.action_5.setObjectName(u"action_5")
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
        self.verticalLayout_6 = QVBoxLayout(self.videoCaptureWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.splitter = QSplitter(self.videoCaptureWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.videoCaptureLabel = QLabel(self.verticalLayoutWidget_2)
        self.videoCaptureLabel.setObjectName(u"videoCaptureLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.videoCaptureLabel.sizePolicy().hasHeightForWidth())
        self.videoCaptureLabel.setSizePolicy(sizePolicy3)
        self.videoCaptureLabel.setMinimumSize(QSize(78, 68))
        self.videoCaptureLabel.setSizeIncrement(QSize(0, 0))
        self.videoCaptureLabel.setFrameShape(QFrame.Shape.Box)
        self.videoCaptureLabel.setFrameShadow(QFrame.Shadow.Sunken)
        self.videoCaptureLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.videoCaptureLabel)

        self.splitter.addWidget(self.verticalLayoutWidget_2)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.inferenceLabel = QLabel(self.verticalLayoutWidget)
        self.inferenceLabel.setObjectName(u"inferenceLabel")
        sizePolicy3.setHeightForWidth(self.inferenceLabel.sizePolicy().hasHeightForWidth())
        self.inferenceLabel.setSizePolicy(sizePolicy3)
        self.inferenceLabel.setMinimumSize(QSize(78, 68))
        self.inferenceLabel.setBaseSize(QSize(0, 0))
        self.inferenceLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.inferenceLabel.setFrameShape(QFrame.Shape.Box)
        self.inferenceLabel.setFrameShadow(QFrame.Shadow.Sunken)
        self.inferenceLabel.setScaledContents(False)
        self.inferenceLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.inferenceLabel)

        self.splitter.addWidget(self.verticalLayoutWidget)

        self.verticalLayout_6.addWidget(self.splitter)

        self.verticalSpacer = QSpacerItem(10, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.infoLabel = QLabel(self.videoCaptureWidget)
        self.infoLabel.setObjectName(u"infoLabel")
        font = QFont()
        font.setPointSize(28)
        self.infoLabel.setFont(font)

        self.verticalLayout_6.addWidget(self.infoLabel)

        self.verticalLayout_6.setStretch(0, 10)
        self.verticalLayout_6.setStretch(1, 3)

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
        self.settingsScrollArea = QScrollArea(self.settingsWidget)
        self.settingsScrollArea.setObjectName(u"settingsScrollArea")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.settingsScrollArea.sizePolicy().hasHeightForWidth())
        self.settingsScrollArea.setSizePolicy(sizePolicy4)
        self.settingsScrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.settingsScrollArea.setWidgetResizable(True)
        self.settingsScrollArea.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.settingsScrollAreaContents = QWidget()
        self.settingsScrollAreaContents.setObjectName(u"settingsScrollAreaContents")
        self.settingsScrollAreaContents.setGeometry(QRect(0, 0, 318, 243))
        self.verticalLayout_2 = QVBoxLayout(self.settingsScrollAreaContents)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(-1, 50, -1, 9)
        self.settingsGridLayout = QGridLayout()
        self.settingsGridLayout.setObjectName(u"settingsGridLayout")
        self.settingsGridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.modelLabel = QLabel(self.settingsScrollAreaContents)
        self.modelLabel.setObjectName(u"modelLabel")

        self.settingsGridLayout.addWidget(self.modelLabel, 0, 0, 1, 1)

        self.savePath = QPushButton(self.settingsScrollAreaContents)
        self.savePath.setObjectName(u"savePath")
        self.savePath.setMaximumSize(QSize(50, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.savePath.setIcon(icon)

        self.settingsGridLayout.addWidget(self.savePath, 6, 2, 1, 1)

        self.gainAuto = QCheckBox(self.settingsScrollAreaContents)
        self.gainAuto.setObjectName(u"gainAuto")
        self.gainAuto.setEnabled(False)

        self.settingsGridLayout.addWidget(self.gainAuto, 3, 2, 1, 1)

        self.gainEdit = QLineEdit(self.settingsScrollAreaContents)
        self.gainEdit.setObjectName(u"gainEdit")
        self.gainEdit.setEnabled(False)

        self.settingsGridLayout.addWidget(self.gainEdit, 3, 1, 1, 1)

        self.saveEdit = QLineEdit(self.settingsScrollAreaContents)
        self.saveEdit.setObjectName(u"saveEdit")
        self.saveEdit.setDragEnabled(False)
        self.saveEdit.setReadOnly(True)
        self.saveEdit.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.saveEdit.setClearButtonEnabled(False)

        self.settingsGridLayout.addWidget(self.saveEdit, 6, 1, 1, 1)

        self.exposureAuto = QCheckBox(self.settingsScrollAreaContents)
        self.exposureAuto.setObjectName(u"exposureAuto")
        self.exposureAuto.setEnabled(False)

        self.settingsGridLayout.addWidget(self.exposureAuto, 2, 2, 1, 1)

        self.exposureLabel = QLabel(self.settingsScrollAreaContents)
        self.exposureLabel.setObjectName(u"exposureLabel")

        self.settingsGridLayout.addWidget(self.exposureLabel, 2, 0, 1, 1)

        self.line_3 = QFrame(self.settingsScrollAreaContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.settingsGridLayout.addWidget(self.line_3, 5, 0, 1, 3)

        self.formatLabel = QLabel(self.settingsScrollAreaContents)
        self.formatLabel.setObjectName(u"formatLabel")

        self.settingsGridLayout.addWidget(self.formatLabel, 4, 0, 1, 1)

        self.line_2 = QFrame(self.settingsScrollAreaContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.settingsGridLayout.addWidget(self.line_2, 1, 0, 1, 3)

        self.exposureEdit = QLineEdit(self.settingsScrollAreaContents)
        self.exposureEdit.setObjectName(u"exposureEdit")
        self.exposureEdit.setEnabled(False)

        self.settingsGridLayout.addWidget(self.exposureEdit, 2, 1, 1, 1)

        self.saveLabel = QLabel(self.settingsScrollAreaContents)
        self.saveLabel.setObjectName(u"saveLabel")

        self.settingsGridLayout.addWidget(self.saveLabel, 6, 0, 1, 1)

        self.formatComboBox = QComboBox(self.settingsScrollAreaContents)
        self.formatComboBox.setObjectName(u"formatComboBox")

        self.settingsGridLayout.addWidget(self.formatComboBox, 4, 1, 1, 1)

        self.modelComboBox = QComboBox(self.settingsScrollAreaContents)
        self.modelComboBox.setObjectName(u"modelComboBox")

        self.settingsGridLayout.addWidget(self.modelComboBox, 0, 1, 1, 1)

        self.gainLabel = QLabel(self.settingsScrollAreaContents)
        self.gainLabel.setObjectName(u"gainLabel")

        self.settingsGridLayout.addWidget(self.gainLabel, 3, 0, 1, 1)

        self.codecLabel = QLabel(self.settingsScrollAreaContents)
        self.codecLabel.setObjectName(u"codecLabel")

        self.settingsGridLayout.addWidget(self.codecLabel, 7, 0, 1, 1)

        self.codecGroupBox = QComboBox(self.settingsScrollAreaContents)
        self.codecGroupBox.setObjectName(u"codecGroupBox")

        self.settingsGridLayout.addWidget(self.codecGroupBox, 7, 1, 1, 1)

        self.settingsGridLayout.setColumnStretch(0, 1)

        self.verticalLayout_2.addLayout(self.settingsGridLayout)

        self.settingsScrollArea.setWidget(self.settingsScrollAreaContents)

        self.verticalLayout.addWidget(self.settingsScrollArea)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.stopButton = QPushButton(self.settingsWidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(32, 32))

        self.gridLayout.addWidget(self.stopButton, 0, 4, 1, 1)

        self.snapshotButton = QPushButton(self.settingsWidget)
        self.snapshotButton.setObjectName(u"snapshotButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/snapshot.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.snapshotButton.setIcon(icon1)
        self.snapshotButton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.snapshotButton, 2, 0, 1, 1)

        self.startButton = QPushButton(self.settingsWidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(32, 32))
        self.startButton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.startButton, 0, 0, 1, 1)

        self.stopRecordButton = QPushButton(self.settingsWidget)
        self.stopRecordButton.setObjectName(u"stopRecordButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stopRecordButton.setIcon(icon2)
        self.stopRecordButton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.stopRecordButton, 2, 5, 1, 1)

        self.recordButton = QPushButton(self.settingsWidget)
        self.recordButton.setObjectName(u"recordButton")
        icon3 = QIcon()
        icon3.addFile(u":/icons/record.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.recordButton.setIcon(icon3)
        self.recordButton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.recordButton, 2, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.horizontalLayout.addWidget(self.settingsWidget)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(2, 2)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(mainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1029, 22))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.analise = QMenu(self.menuBar)
        self.analise.setObjectName(u"analise")
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")
        mainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(mainWindow)
        self.statusBar.setObjectName(u"statusBar")
        mainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.analise.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.connect_camera)
        self.menu.addAction(self.load_video)
        self.analise.addAction(self.actionPSNR_SSIM)
        self.menu_2.addAction(self.action)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)

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
        self.actionPSNR_SSIM.setText(QCoreApplication.translate("mainWindow", u"PSNR \u0438 SSIM", None))
        self.action.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.action_2.setText(QCoreApplication.translate("mainWindow", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.action_3.setText(QCoreApplication.translate("mainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.action_4.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.action_5.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u0441\u0438\u0441\u0442\u0435\u043c\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0441\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u041a\u0430\u043c\u0435\u0440\u0430", None))
        self.videoCaptureLabel.setText("")
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u0441\u0442\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        self.inferenceLabel.setText("")
        self.infoLabel.setText("")
        self.modelLabel.setText(QCoreApplication.translate("mainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.savePath.setText("")
        self.gainAuto.setText(QCoreApplication.translate("mainWindow", u"\u0410\u0432\u0442\u043e", None))
        self.saveEdit.setPlaceholderText("")
        self.exposureAuto.setText(QCoreApplication.translate("mainWindow", u"\u0410\u0432\u0442\u043e", None))
        self.exposureLabel.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u043a\u043e\u043f\u043b\u0435\u043d\u0438\u044f", None))
        self.formatLabel.setText(QCoreApplication.translate("mainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442", None))
        self.saveLabel.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432", None))
        self.gainLabel.setText(QCoreApplication.translate("mainWindow", u"\u0423\u0441\u0438\u043b\u0435\u043d\u0438\u0435", None))
        self.codecLabel.setText(QCoreApplication.translate("mainWindow", u"\u041a\u043e\u0434\u0435\u043a", None))
        self.stopButton.setText(QCoreApplication.translate("mainWindow", u"\u0421\u0442\u043e\u043f", None))
        self.snapshotButton.setText("")
        self.startButton.setText(QCoreApplication.translate("mainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.stopRecordButton.setText("")
        self.recordButton.setText("")
        self.menu.setTitle(QCoreApplication.translate("mainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430", None))
        self.analise.setTitle(QCoreApplication.translate("mainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437", None))
        self.menu_2.setTitle(QCoreApplication.translate("mainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

