import sys

sys.path.append(__file__)

import numpy as np
from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QRegularExpressionValidator
from pypylon import pylon


class CameraController(QObject):
    def __init__(self, stream, ui):
        super().__init__()
        self.camera = stream.cap.camera
        self.ui = ui
        self.setupUI()
        self.connect_slots()

    def setupUI(self):
        # Validators
        validator = QRegularExpressionValidator('[0-9]*')
        self.ui.gainEdit.setValidator(validator)
        self.ui.exposureEdit.setValidator(validator)

        # Format UI
        self.format_index = {'BayerBG8': 0,
                             'YUV422Packed': 1}
        self.ui.formatComboBox.addItem("")
        self.ui.formatComboBox.setItemText(0, "BayerBG8")
        self.ui.formatComboBox.addItem("")
        self.ui.formatComboBox.setItemText(1, "YUV422Packed")
        format = self.camera.PixelFormat.Value
        self.ui.formatComboBox.setCurrentIndex(self.format_index[f'{format}'])

        # Exposure UI
        if self.camera.ExposureAuto.Value == "Continuous":
            self.ui.exposureAuto.setChecked(True)
            self.ui.exposureEdit.setEnabled(False)
            self.ui.exposureEdit.setText(str(int(self.camera.ExposureTimeAbs.Value)))
        else:
            self.ui.exposureEdit.setText(str(int(self.camera.ExposureTimeAbs.Value)))
        # Gain UI
        if self.camera.GainAuto.Value == "Continuous":
            self.ui.gainAuto.setChecked(True)
            self.ui.gainEdit.setEnabled(False)
            self.ui.gainEdit.setText(str(int(self.camera.GainRaw.Value)))
        else:
            self.ui.gainEdit.setText(str(int(self.camera.GainRaw.Value)))

    def connect_slots(self):
        self.ui.gainEdit.editingFinished.connect(self.setGain)
        self.ui.exposureEdit.editingFinished.connect(self.setExposure)
        self.ui.exposureAuto.clicked.connect(self.setExposureAuto)
        self.ui.gainAuto.clicked.connect(self.setGainAuto)
        self.ui.formatComboBox.activated.connect(self.setFormat)

    @Slot()
    def setFormat(self):
        self.camera.StopGrabbing()
        self.camera.PixelFormat.Value = self.ui.formatComboBox.currentText()
        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

    @Slot()
    def setGain(self):
        value = float(self.ui.gainEdit.text())
        value = np.clip(value, self.camera.GainRaw.Min, self.camera.GainRaw.Max)
        self.camera.GainRaw.Value = int(value)
        self.ui.gainEdit.setText(str(int(self.camera.GainRaw.Value)))

    @Slot()
    def setGainAuto(self):
        if self.ui.gainAuto.isChecked():
            self.ui.gainEdit.setEnabled(False)
            self.camera.GainAuto.Value = "Continuous"
        else:
            self.camera.GainAuto.Value = "Off"
            self.ui.gainEdit.setEnabled(True)
            self.ui.gainEdit.setText(str(int(self.camera.GainRaw.Value)))

    @Slot()
    def setExposure(self):
        value = float(self.ui.exposureEdit.text())
        value = np.clip(value, self.camera.ExposureTimeAbs.Min, self.camera.ExposureTimeAbs.Max)
        self.camera.ExposureTimeAbs.Value = value
        self.ui.exposureEdit.setText(str(int(self.camera.ExposureTimeAbs.Value)))

    @Slot()
    def setExposureAuto(self):
        if self.ui.exposureAuto.isChecked():
            self.ui.exposureEdit.setEnabled(False)
            self.camera.ExposureAuto.Value = "Continuous"
        else:
            self.camera.ExposureAuto.Value = "Off"
            self.ui.exposureEdit.setEnabled(True)
            self.ui.exposureEdit.setText(str(int(self.camera.ExposureTimeAbs.Value)))
