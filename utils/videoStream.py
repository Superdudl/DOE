import sys

sys.path.append(__file__)

import numpy as np
from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtGui import QImage, QPixmap, Qt
from utils import VideoCapture
from pathlib import Path
import cv2
import time


class CameraStream(QThread):
    """
    Класс для захвата кадров с камеры в отдельном потоке
    """
    frame_grabbed = Signal(np.uint8)

    def __init__(self):
        super().__init__()
        self.cap = VideoCapture()
        self.running = False

    def run(self):
        if self.cap.camera is None:
            return
        self.cap.start()
        self.running = True
        while self.running:
            img = self.cap.get_frame()
            if img is None:
                continue
            self.frame_grabbed.emit(img)
        self.cap.stop()


class CameraSimulation(QThread):
    """
    Класс для симуляции захвата кадров для DEBUG режима в отдельном потоке
    """
    frame_grabbed = Signal(np.uint8)

    def __init__(self):
        super().__init__()
        self.running = False

    def run(self, /):
        self.running = True
        h, w, c = [580, 780, 3]
        while self.running:
            img = np.random.randint(0, 256, (h, w, c), dtype=np.uint8)
            time.sleep(0.033)
            self.frame_grabbed.emit(img)


class VideoStream(QObject):
    sources = {'camera': CameraStream,
               'DEBUG': CameraSimulation}

    def __init__(self, ui, parent=None):
        super().__init__(parent)
        self.ui = ui
        self.stream = None
        self.frame = None
        self.inference_frame = None
        self.status = None

    def start_stream(self, source):
        if self.stream is not None: return
        assert source in self.sources.keys(), f"Выберите из доступных источников {self.sources.keys()}"
        self.stream = self.sources[source]()
        self.stream.start()  # Move to Thread
        self.stream.wait(500)
        self.status = self.stream.running
        # Slot connection
        if self.status:
            self.stream.frame_grabbed.connect(self.update_frame)


    def stop_stream(self):
        if self.stream is None: return
        self.stream.running = False
        self.status = False
        self.stream.wait()
        self.stream = None

    @Slot()
    def update_frame(self, img):
        h, w, c = img.shape
        self.frame = np.copy(img)
        qimage = QImage(self.frame, w, h, w * c, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(self.ui.videoCaptureLabel.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.videoCaptureLabel.setPixmap(pixmap)


if __name__ == "__main__":
    a = VideoStream
