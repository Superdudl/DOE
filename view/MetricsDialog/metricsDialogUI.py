# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'metricsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(952, 612)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.imagesWidget = QWidget(Dialog)
        self.imagesWidget.setObjectName(u"imagesWidget")
        self.horizontalLayout = QHBoxLayout(self.imagesWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.originalLayout = QVBoxLayout()
        self.originalLayout.setObjectName(u"originalLayout")
        self.originalLabel = QLabel(self.imagesWidget)
        self.originalLabel.setObjectName(u"originalLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.originalLabel.sizePolicy().hasHeightForWidth())
        self.originalLabel.setSizePolicy(sizePolicy)
        self.originalLabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.originalLabel.setFrameShadow(QFrame.Shadow.Sunken)
        self.originalLabel.setScaledContents(False)
        self.originalLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.originalLayout.addWidget(self.originalLabel)

        self.originalButton = QPushButton(self.imagesWidget)
        self.originalButton.setObjectName(u"originalButton")
        self.originalButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.originalLayout.addWidget(self.originalButton)


        self.horizontalLayout.addLayout(self.originalLayout)

        self.blurredLayout = QVBoxLayout()
        self.blurredLayout.setObjectName(u"blurredLayout")
        self.blurredLabel = QLabel(self.imagesWidget)
        self.blurredLabel.setObjectName(u"blurredLabel")
        sizePolicy.setHeightForWidth(self.blurredLabel.sizePolicy().hasHeightForWidth())
        self.blurredLabel.setSizePolicy(sizePolicy)
        self.blurredLabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.blurredLabel.setFrameShadow(QFrame.Shadow.Sunken)
        self.blurredLabel.setMidLineWidth(0)
        self.blurredLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.blurredLayout.addWidget(self.blurredLabel)

        self.blurredButton = QPushButton(self.imagesWidget)
        self.blurredButton.setObjectName(u"blurredButton")
        self.blurredButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.blurredButton.setAutoDefault(True)
        self.blurredButton.setFlat(False)

        self.blurredLayout.addWidget(self.blurredButton)


        self.horizontalLayout.addLayout(self.blurredLayout)

        self.analyzeLayout = QVBoxLayout()
        self.analyzeLayout.setObjectName(u"analyzeLayout")
        self.analyseLabel = QLabel(self.imagesWidget)
        self.analyseLabel.setObjectName(u"analyseLabel")
        sizePolicy.setHeightForWidth(self.analyseLabel.sizePolicy().hasHeightForWidth())
        self.analyseLabel.setSizePolicy(sizePolicy)
        self.analyseLabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.analyseLabel.setFrameShadow(QFrame.Shadow.Sunken)
        self.analyseLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.analyzeLayout.addWidget(self.analyseLabel)

        self.analyseButton = QPushButton(self.imagesWidget)
        self.analyseButton.setObjectName(u"analyseButton")
        self.analyseButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.analyzeLayout.addWidget(self.analyseButton)


        self.horizontalLayout.addLayout(self.analyzeLayout)


        self.verticalLayout.addWidget(self.imagesWidget)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 5, 1, 1)

        self.psnrLineEdit = QLineEdit(self.widget)
        self.psnrLineEdit.setObjectName(u"psnrLineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.psnrLineEdit.sizePolicy().hasHeightForWidth())
        self.psnrLineEdit.setSizePolicy(sizePolicy1)
        self.psnrLineEdit.setMinimumSize(QSize(0, 28))
        self.psnrLineEdit.setFont(font)
        self.psnrLineEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.psnrLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.psnrLineEdit, 1, 3, 1, 1)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
        self.comboBox.setFont(font)

        self.gridLayout.addWidget(self.comboBox, 0, 3, 1, 2)

        self.ssimLineEdit = QLineEdit(self.widget)
        self.ssimLineEdit.setObjectName(u"ssimLineEdit")
        sizePolicy1.setHeightForWidth(self.ssimLineEdit.sizePolicy().hasHeightForWidth())
        self.ssimLineEdit.setSizePolicy(sizePolicy1)
        self.ssimLineEdit.setMinimumSize(QSize(0, 28))
        self.ssimLineEdit.setFont(font)
        self.ssimLineEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ssimLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.ssimLineEdit, 2, 3, 1, 1)

        self.psnrLabel = QLabel(self.widget)
        self.psnrLabel.setObjectName(u"psnrLabel")
        self.psnrLabel.setFont(font)
        self.psnrLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.psnrLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.psnrLabel, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.ssimLabel = QLabel(self.widget)
        self.ssimLabel.setObjectName(u"ssimLabel")
        self.ssimLabel.setFont(font)
        self.ssimLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ssimLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.ssimLabel, 2, 1, 1, 1)

        self.match_hists_checkbox = QCheckBox(self.widget)
        self.match_hists_checkbox.setObjectName(u"match_hists_checkbox")

        self.gridLayout.addWidget(self.match_hists_checkbox, 1, 4, 1, 1)

        self.deconv_checkbox = QCheckBox(self.widget)
        self.deconv_checkbox.setObjectName(u"deconv_checkbox")

        self.gridLayout.addWidget(self.deconv_checkbox, 2, 4, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(Dialog)

        self.blurredButton.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.originalLabel.setText("")
        self.originalButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043e\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.blurredLabel.setText("")
        self.blurredButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0438\u0441\u043a\u0430\u0436\u0435\u043d\u043d\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.analyseLabel.setText("")
        self.analyseButton.setText(QCoreApplication.translate("Dialog", u"\u0410\u043d\u0430\u043b\u0438\u0437", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.psnrLabel.setText(QCoreApplication.translate("Dialog", u"PSNR", None))
        self.ssimLabel.setText(QCoreApplication.translate("Dialog", u"SSIM", None))
        self.match_hists_checkbox.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u043d\u0438\u0435 \u0433\u0438\u0441\u0442\u043e\u0433\u0440\u0430\u043c\u043c", None))
        self.deconv_checkbox.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0433\u0443\u043b\u044f\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u0422\u0438\u0445\u043e\u043d\u043e\u0432\u0430", None))
    # retranslateUi

