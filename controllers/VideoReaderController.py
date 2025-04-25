import sys

sys.path.append(__file__)

from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import QMessageBox, QProgressDialog
from utils import Inference
import numpy as np
from pathlib import Path, PurePath
import cv2
import av
from datetime import datetime
from fractions import Fraction
import pycuda.driver as cuda
import pycuda.autoinit


class VideoWriter(QThread):
    next_frame = Signal(int, bool)
    finished = Signal(str)

    def __init__(self, filename, output_dir, controller):
        super().__init__()
        self.controller = controller
        self.input_filename = Path(filename)
        self.running = False
        self.frame = None
        self.filename = Path(f'{datetime.strftime(datetime.now(), "%Y-%m-%d_%H-%M-%S")}.mp4')
        self.container = None

        self.record_path = Path(output_dir) / self.filename

        if not self.filename.parent.exists():
            self.filename.parent.mkdir(parents=True, exist_ok=True)

    def create_container(self, fps):
        import pycuda.driver as cuda
        import pycuda.autoinit

        codec = 'h264_nvenc' if cuda.Device.count() > 0 else 'h264'

        framerate = fps
        if self.frame is not None:
            h, w, c = self.frame.shape
            self.container = av.open(self.record_path, mode='w')
            self.av_stream = self.container.add_stream(codec, rate=framerate)
            self.av_stream.width = w
            self.av_stream.height = h
            self.av_stream.pix_fmt = 'yuv420p'
            self.av_stream.codec_context.time_base = Fraction(1, framerate)

    def run(self):
        self.running = True
        self.inference = Inference()
        input_video = cv2.VideoCapture(self.input_filename)
        fps = int(input_video.get(cv2.CAP_PROP_FPS))
        total_frames = input_video.get(cv2.CAP_PROP_FRAME_COUNT)
        if not total_frames: return

        ret, self.frame = input_video.read()
        if not ret: return
        self.inference.create(self.controller.model, self.frame.shape)

        input_video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        while True:
            ret, frame = input_video.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            if self.container is None:
                self.create_container(fps)
            self.frame = self.inference(frame)
            self.frame = av.VideoFrame.from_ndarray(self.frame, 'rgb24')
            current_frame = input_video.get(cv2.CAP_PROP_POS_FRAMES)
            self.next_frame.emit(int(current_frame/total_frames * 100), self.running)

            if frame is not None:
                for packet in self.av_stream.encode(self.frame):
                    self.container.mux(packet)

        for packet in self.av_stream.encode(None):
            self.container.mux(packet)
        self.container.close()
        input_video.release()

        self.running = False
        self.inference.clear()
        self.finished.emit(str(self.record_path))


class VideoReader:
    models_dir = Path(PurePath(__file__).parents[1], 'src', 'pretrained_models')

    def __init__(self, ui, window, filename=None):
        self.filename = None
        self.ui = ui
        self.window = window
        if len(self.ui.modelComboBox.currentText()) > 0:
            self.model = self.models_dir / self.ui.modelComboBox.currentText()
        else:
            self.model = None

    def setup_ui(self):
        self.progress = QProgressDialog("Обработка видео...", "Отмена", 0, 100)
        self.progress.setWindowTitle(self.ui.modelComboBox.currentText())
        self.progress.setCancelButton(None)
        self.progress.exec()

    def open(self, filename):
        self.filename = filename
        if self.model is None:
            QMessageBox.warning(self.window, "Ошибка", "Нет доступных моделей")
            return

        output_dir = self.ui.saveEdit.text()
        self.encoder = VideoWriter(self.filename, output_dir, self)
        self.encoder.start()
        self.encoder.wait(100)
        if self.encoder.running:
            self.encoder.next_frame.connect(self.update_progress)
            self.encoder.finished.connect(self.save_finished)
            self.setup_ui()

    @Slot()
    def update_progress(self, count, running):
        self.progress.setValue(count)

    def save_finished(self, output_path):
        self.progress.close()
        QMessageBox.information(self.window, 'Обработка завершена', f'Сохранено в {output_path}')



