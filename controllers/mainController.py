import sys
sys.path.append(__file__)

from pathlib import PurePath, Path
from PySide6.QtCore import QObject, Slot
from controllers import  CameraController, InferenceController
from utils import VideoStream


class MainController(QObject):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.setup_controllers()
        self.connect_slots()

    def setup_controllers(self):
        self.video_stream = VideoStream()
        self.inference_controller = InferenceController(self.ui)

    def connect_slots(self):
        self.ui.connect_camera.triggered.connect(self.connect_camera)

    @Slot()
    def connect_camera(self):
        self.video_stream.start_stream('camera')
        self.camera_controller = CameraController(self.video_stream.stream, self.ui)


