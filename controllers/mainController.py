import sys

sys.path.append(__file__)

from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QMessageBox, QFileDialog
from controllers import CameraController, InferenceController, RecordController
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
        self.record_controller = RecordController(self.ui, self.window, self.video_stream)

    def connect_slots(self):
        self.ui.connect_camera.triggered.connect(self.connect_camera)
        self.ui.load_video.triggered.connect(self.open_video)

    def __del__(self):
        self.video_stream.stop_stream()
        self.inference_controller.stop()

    @Slot()
    def connect_camera(self):
        self.video_stream.start_stream('camera')
        if not self.video_stream.status:
            QMessageBox.warning(self.window, "Ошибка", "Камера не подключена")
            return
        self.ui.exposureEdit.setEnabled(True)
        self.ui.gainEdit.setEnabled(True)
        self.ui.formatEdit.setEnabled(True)
        self.ui.exposureAuto.setEnabled(True)
        self.ui.gainAuto.setEnabled(True)
        self.camera_controller = CameraController(self.video_stream.stream, self.ui)

    @Slot()
    def open_video(self):
        self.inference_controller.stop()
        filters = "Видео (*.mp4 *.avi *.mkv)"
        video_path, _ = QFileDialog.getOpenFileName(self.window, "Выберите видео", '', filters)




