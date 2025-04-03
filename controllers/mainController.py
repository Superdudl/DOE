import sys

import numpy as np

sys.path.append(__file__)

from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QMessageBox, QFileDialog
from PySide6.QtGui import QImage, QPixmap, Qt
from controllers import CameraController, InferenceController
from utils import VideoStream


class MainController(QObject):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.ui = window.ui
        self.setup_controllers()
        self.connect_slots()

    def setup_controllers(self):
        self.video_stream = VideoStream(self.ui)
        self.inference_controller = InferenceController(self.ui, self.video_stream)

    def connect_slots(self):
        self.ui.connect_camera.triggered.connect(self.connect_camera)
        self.ui.load_video.triggered.connect(self.open_video)

    @Slot()
    def connect_camera(self):
        self.video_stream.start_stream('camera')
        if not self.video_stream.status:
            QMessageBox.warning(self.window, "Ошибка", "Камера не подключена")
            return
        self.camera_controller = CameraController(self.video_stream.stream, self.ui)
        self.ui.exposureEdit.setEnable(True)
        self.ui.gainEdit.setEnable(True)
        self.ui.formatEdit.setEnable(True)
        self.ui.exposureAuto.setEnable(True)
        self.ui.gainAuto.setEnable(True)

    def open_video(self):
        self.inference_controller.stop()
        filters = "Видео (*.mp4 *.avi *.mkv)"
        video_path, _ = QFileDialog.getOpenFileName(self.window, "Выберите видео", '', filters)




