import sys
from pathlib import PurePath, Path

sys.path.append(__file__)
from utils import Inference
from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtGui import QImage, QPixmap, Qt
import numpy as np


class Predict(QThread):
    inference_complete = Signal(np.float32)

    def __init__(self, controller, stream):
        super().__init__()
        self.stream = stream
        self.controller = controller
        self.running = False

    def run(self):
        # if self.inference.model is not None and self.stream.status:
        self.inference = Inference()
        self.inference.create(self.controller.model)
        self.running = True
        while not self.isInterruptionRequested() :
            result = self.inference(self.stream.frame)
            self.inference_complete.emit(result)
        self.inference.clear()


class InferenceController(QObject):
    models_dir = Path(PurePath(__file__).parents[1], 'src', 'pretrained_models')

    def __init__(self, ui, video_stream):
        super().__init__()
        self.video_stream = video_stream
        self.ui = ui
        self.connect_slots()
        if len(self.ui.modelComboBox.currentText()) > 0:
            self.model = self.models_dir / self.ui.modelComboBox.currentText()
            self.inference = Predict(self, self.video_stream)
        else:
            self.model = None

    def connect_slots(self):
        self.ui.modelComboBox.activated.connect(self.update_model)
        self.ui.startButton.clicked.connect(self.start)
        self.ui.stopButton.clicked.connect(self.stop)

    def update_model(self):
        self.model = self.model = self.models_dir / self.ui.modelComboBox.currentText()
        self.inference = Predict(self, self.video_stream)

    def start(self):
        if self.model and self.video_stream.stream is not None:
            if not self.inference.running:
                self.inference.start()
                self.inference.inference_complete.connect(self.update_frame)

    def stop(self):
        if not hasattr(self, 'inference'):
            return
        if self.inference.running:
            self.inference.running = False
            self.inference.inference_complete.disconnect()
            self.inference.requestInterruption()

    def update_frame(self, img):
        self.video_stream.inference_frame = np.copy(img)
        h, w, c = img.shape
        qimage = QImage(img, w, h, w * c, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(self.ui.inferenceLabel.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.inferenceLabel.setPixmap(pixmap)
