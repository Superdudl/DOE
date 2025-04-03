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
        self.connect_slots()

        # Validators
        self.ui.gainEdit.setValidator(QIntValidator(self.camera.GainRaw.Value.Min, self.camera.GainRaw.Value.Max))
        self.ui.exposureEdit.setValidator(
            QIntValidator(self.camera.ExposureTimeAbs.Min, self.camera.ExposureTimeAbs.Max))

    def connect_slots(self):
        self.ui.exposureEdit.editingFinished.connect(self.setExposure)
        self.ui.gainEdit.editingFinished.connect(self.setGain)
        self.ui.exposureAuto.clicked.connect(self.setExposureAuto)
        self.ui.gainAuto.clicked.connect(self.setGainAuto)

    @Slot(float)
    def setGain(self):
        value = float(self.ui.exposureEdit.text())
        self.camera.GainRaw.Value = value

    @Slot()
    def setGainAuto(self):
        if self.ui.gainAuto.isChecked():
            self.ui.exposureEdit.setEnable(False)
            self.camera.GainAuto.Value = "Continuous"
        else:
            self.camera.GainAuto.Value = "off"
            self.ui.exposureEdit.setEnable(True)

    @Slot(float)
    def setExposure(self):
        value = float(self.ui.exposureEdit.text())
        self.camera.ExposureTimeAbs.Value = value

    @Slot()
    def setExposureAuto(self):
        if self.ui.exposureAuto.isChecked():
            self.ui.gainEdit.setEnable(False)
            self.camera.ExposureAuto.Value = "Continuous"
        else:
            self.camera.ExposureAuto.Value = "off"
            self.ui.gainEdit.setEnable(True)
