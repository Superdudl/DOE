import sys

sys.path.append(__file__)

import numpy as np
from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QIntValidator


class CameraController(QObject):
    def __init__(self, stream, ui):
        super().__init__()
        self.camera = stream.cap.camera
        self.ui = ui
        self.setupUI()
        self.connect_slots()

        # Validators
        self.ui.gainEdit.setValidator(QIntValidator(self.camera.GainRaw.Min, self.camera.GainRaw.Max))
        self.ui.exposureEdit.setValidator(
            QIntValidator(self.camera.ExposureTimeAbs.Min, self.camera.ExposureTimeAbs.Max))

    def setupUI(self):
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

    @Slot()
    def setGain(self):
        value = float(self.ui.gainEdit.text())
        self.camera.GainRaw.Value = int(value)

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
        self.camera.ExposureTimeAbs.Value = value

    @Slot()
    def setExposureAuto(self):
        if self.ui.exposureAuto.isChecked():
            self.ui.exposureEdit.setEnabled(False)
            self.camera.ExposureAuto.Value = "Continuous"
        else:
            self.camera.ExposureAuto.Value = "Off"
            self.ui.exposureEdit.setEnabled(True)
            self.ui.exposureEdit.setText(str(int(self.camera.ExposureTimeAbs.Value)))

