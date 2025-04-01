import sys
sys.path.append(__file__)

from pathlib import PurePath, Path
from PySide6.QtCore import QObject
from controllers import VideoStream, CameraController, InferenceController


class MainController(QObject):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.setup_controllers()

    def setup_controllers(self):
        self.video_stream = VideoStream(self.ui)
        self.camera_controller = CameraController(self.video_stream.stream, self.ui)
        self.inference_controller = InferenceController(self.ui)