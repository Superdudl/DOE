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
        self.running = False

    def run(self):
        if self.cap.camera is None:
            return
        self.running = True
        self.cap.start()
        while self.running:
            img = self.cap.get_frame()
            if img is None:
                continue
            self.frame_grabbed.emit(img)


class VideoFileStream(QThread):
    pass


class VideoStream(QObject):
    sources = {'camera': CameraStream,
               'videofile': VideoFileStream}
    def __init__(self, ui, parent=None):
        super().__init__(parent)
        self.ui = ui
        self.stream = None
        self.frame = None
        self.inference_frame = None
        self.status = None

    def start_stream(self, source):
        assert source in self.sources.keys(), f"Выберите из доступных источников {self.sources.keys()}"
        self.stream = self.sources[source]()
        self.stream.start() # Move to Thread
        self.stream.wait(500)
        self.status = self.stream.running
        # Slot connection
        if self.status:
            self.stream.frame_grabbed.connect(self.update_frame)

    def stop_stream(self):
        if self.stream is not None:
            self.stream.running = False
            self.status = False
            self.stream.wait()

    @Slot()
    def update_frame(self, img):
        self.frame = np.copy(img)
        h, w, c = self.frame.shape
        qimage = QImage(self.frame, w, h, w * c, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(self.ui.videoCaptureLabel.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.videoCaptureLabel.setPixmap(pixmap)

if __name__ == "__main__":
    a = VideoStream