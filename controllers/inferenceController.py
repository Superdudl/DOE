import sys
from pathlib import PurePath, Path

sys.path.append(__file__)
from utils import Inference
from PySide6.QtCore import QThread, Signal, QObject, Slot
from PySide6.QtGui import QImage, QPixmap, Qt
import numpy as np


class Predict(QThread):
    inference_complete = Signal(np.uint8, np.uint8, np.float32)

    def __init__(self, controller, stream):
        super().__init__()
        self.stream = stream
        self.controller = controller
        self.running = False

    def run(self):
        self.inference = Inference()
        self.inference.create(self.controller.model, self.stream.frame.shape)
        self.running = True
        while not self.isInterruptionRequested() and self.stream.status:
            frame = np.copy(self.stream.frame)
            # frame = cv2.resize(frame, (780, 580), interpolation=cv2.INTER_LANCZOS4)
            result, latency = self.inference(frame)
            self.inference_complete.emit(result, frame, latency)
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

    @Slot()
    def update_model(self):
        self.model = self.models_dir / self.ui.modelComboBox.currentText()
        self.inference = Predict(self, self.video_stream)

    @Slot()
    def start(self):
        if self.model is not None and self.video_stream.status:
            if not self.inference.running:
                self.inference.start()
                self.ui.modelComboBox.setEnabled(False)
                # Slot connection
                self.inference.inference_complete.connect(self.update_frame)
                self.inference.inference_complete.connect(self.calculate_psnr)

    @Slot()
    def stop(self):
        if not hasattr(self, 'inference'):
            return
        if self.inference.running:
            self.inference.running = False
            self.inference.inference_complete.disconnect()
            self.inference.requestInterruption()
            self.inference.wait()
            self.ui.modelComboBox.setEnabled(True)
            self.video_stream.inference_frame = None

    @Slot()
    def update_frame(self, img, frame):
        self.video_stream.inference_frame = np.copy(img)
        h, w, c = img.shape
        qimage = QImage(img, w, h, w * c, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(self.ui.inferenceLabel.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.inferenceLabel.setPixmap(pixmap)

    @Slot()
    def calculate_psnr(self, result, frame, latency):
        self.ui.infoLabel.setText(f'FPS = {1/latency:.1f} Гц')

