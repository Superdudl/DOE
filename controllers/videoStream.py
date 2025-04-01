import sys

sys.path.append(__file__)

import numpy as np
from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtGui import QImage, QPixmap, Qt
from utils import VideoCapture, Inference


class CameraStream(QThread):
    frame_grabbed = Signal(np.uint8)

    def __init__(self, ui):
        super().__init__()
        self.cam = VideoCapture()
        self.running = True

    def run(self):
        self.cam.start()
        while True:
            img = self.cam.get_frame()
            if img is None:
                continue
            self.frame_grabbed.emit(img)


class VideoStream(QObject):
    def __init__(self, ui, parent=None):
        super().__init__(parent)
        self.stream = None
        self.ui = ui
        self.frame = None
        self.setupUI()

    def setupUI(self):
        self.start_stream()

    def start_stream(self):
        self.stream = CameraStream(self.ui)
        self.stream.start()

        # Slot connection
        self.stream.frame_grabbed.connect(lambda img: self.frame)

    def stop_stream(self):
        if self.stream is not None:
            self.stream.running = False
            self.stream.wait()

    def update_frame(self, img):
        self.frame = img
        h, w, c = img.shape
        qimage = QImage(self.frame, w, h, c * w, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        h_label, w_label = self.ui.videoCaptureLabel.height(), self.ui.videoCaptureLabel.width()
        pixmap = pixmap.scaled(h_label, w_label, Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.videoCaptureLabel.setPixmap(pixmap)
