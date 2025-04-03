import sys
sys.path.append(__file__)

import numpy as np
from PySide6.QtCore import QObject, Slot

class CameraController(QObject):
    def __init__(self, stream, ui):
        super().__init__()
        self.camera = stream.cap.camera
        self.ui = ui

    @Slot(float)
    def setGain(self, value: float):
        if self.camera.GainAuto.Value != "Off":
            self.camera.GainAuto.Value = "Off"
        value = np.clip(value, self.camera.GainRaw.Value.Min, self.camera.GainRaw.Value.Max)
        self.camera.GainRaw.Value = value

    @Slot()
    def setGainAuto(self):
        self.camera.GainAuto.Value = "Continuous"

    @Slot(float)
    def setExposure(self, value: float):
        if self.camera.ExposureAuto.Value != "Off":
            self.camera.ExposureAuto.Value = "Off"
        value = np.clip(value, self.camera.ExposureTimeAbs.Min, self.camera.ExposureTimeAbs.Max)
        self.camera.ExposureTimeAbs.Value = value