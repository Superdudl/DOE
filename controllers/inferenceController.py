import sys
from pathlib import PurePath, Path

sys.path.append(__file__)
from utils import Inference
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage, QPixmap, Qt


class Predict(QThread):
    inference_complete = Signal()

    def __init__(self, inference, stream):
        super().__init__()
        self.inference = inference
        self.stream = stream
        self.running = False

    def run(self):
        if self.inference.model is not None and self.stream.status:
            self.running = True
            while self.running:
                result = self.inference.net(self.stream.frame)
                self.inference_complete.emit(result)


class InferenceController(Inference):
    models_dir = Path(PurePath(__file__).parents[1], 'src', 'pretrained_models')
    def __init__(self, ui, video_stream):
        super().__init__()
        self.video_stream = video_stream
        self.ui = ui
        if len(self.ui.modelComboBox.currentText()) > 0:
            self.model = self.models_dir / self.ui.modelComboBox.currentText()
            self.net = self.create(self.model)
            self.inference = Predict(self, self.video_stream)
        else:
            self.model = None

        # Slot connection
        self.ui.modelComboBox.activated.connect(self.update_model)
        self.ui.startButton.clicked.connect(self.start)
        self.ui.stopButton.clicked.connect(self.stop)

    def update_model(self):
        self.model = self.model = self.models_dir / self.ui.modelComboBox.currentText()
        self.net = self.create(self.model)

    def start(self):
        if not self.inference.running:
            self.inference.start()
            self.inference.inference_complete.connect(self.update_frame)

    def stop(self):
        if self.inference.running:
            self.inference.running = False
            self.inference.wait()
            self.inference.inference_complete.disconnect()

    def update_frame(self, img):
        self.video_stream.inference_frame = img
        h, w, c = img
        qimage = QImage(img, h, w, w * c, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(self.ui.videoCaptureLabel.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.self.ui.videoCaptureLabel.setPixmap(pixmap)
