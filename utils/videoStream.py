import sys

sys.path.append(__file__)

import numpy as np
from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtGui import QImage, QPixmap, Qt
from utils import VideoCapture, Inference


class CameraStream(QThread):
    frame_grabbed = Signal(np.uint8)

    def __init__(self):
        super().__init__()
        self.cap = VideoCapture()
        self.running = True

    def run(self):
        if self.cap.camera is None: return
        self.cap.start()
        while True:
            img = self.cam.get_frame()
            if img is None:
                continue
            self.frame_grabbed.emit(img)


class VideoFileStream(QThread):
    pass


class VideoStream(QObject):
    sources = {'camera': CameraStream,
               'videofile': VideoFileStream}
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stream = None
        self.frame = None

    def start_stream(self, source):
        assert source in self.sources.keys(), f"Выберите из доступных источников {self.sources.keys()}"
        self.stream = self.sources[source]()
        self.stream.start()

        # Slot connection
        self.stream.frame_grabbed.connect(lambda img: self.frame)

    def stop_stream(self):
        if self.stream is not None:
            self.stream.running = False
            self.stream.wait()

if __name__ == "__main__":
    a = VideoStream