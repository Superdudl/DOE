import sys

sys.path.append(__file__)

from PySide6.QtCore import QObject, Slot, QSettings, QThread
from PySide6.QtWidgets import QMessageBox, QFileDialog
from pathlib import Path, PurePath
import av
import cv2
from fractions import Fraction
from datetime import datetime
import time


class Encoder(QThread):
    def __init__(self, path, video_stream, filename):
        """
        stream: ['camera', 'inference']
        """
        super().__init__()
        self.video_stream = video_stream
        self.container = None
        self.filename = filename

        path = Path(path)
        self.path = path / filename

        if not self.path.parent.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)

        self.create_container()

    def create_container(self):
        framerate = 30
        if self.video_stream.status and self.video_stream.frame is not None:
            h, w, c = self.video_stream.frame.shape
            if self.video_stream.inference_frame is not None:
                w = w * 2
            self.container = av.open(self.path, mode='w')
            self.av_stream = self.container.add_stream('h264', rate=framerate)
            self.av_stream.width = w
            self.av_stream.height = h
            self.av_stream.pix_fmt = 'yuv420p'
            self.av_stream.codec_context.time_base = Fraction(1, framerate)

    def run(self):
        last_time = time.time()
        frame = None
        pts = 0
        while not self.isInterruptionRequested():

            current_time = time.time()
            if current_time - last_time > self.av_stream.codec_context.time_base:
                pts += self.av_stream.codec_context.time_base
                last_time = current_time
            else:
                continue

            frame = self.video_stream.frame
            if self.video_stream.inference_frame is not None:
                infer_frame = self.video_stream.inference_frame
                frame = cv2.hconcat([frame, infer_frame])

            frame = av.VideoFrame.from_ndarray(frame, 'rgb24')

            frame.pts = int(round(pts / self.av_stream.codec_context.time_base))

            if frame is not None:
                for packet in self.av_stream.encode(frame):
                    self.container.mux(packet)
        for packet in self.av_stream.encode(None):
            self.container.mux(packet)
        self.container.close()


class RecordController:
    def __init__(self, ui, window, video_stream):
        super().__init__()
        self.inference_encoder = None
        self.camera_encoder = None
        self.ui = ui
        self.window = window
        self.video_stream = video_stream
        self.setup_ui()
        self.connect_slots()

    def connect_slots(self):
        self.ui.savePath.clicked.connect(self.explore_path)
        self.ui.recordButton.clicked.connect(self.start_record)
        self.ui.stopRecordButton.clicked.connect(self.stop_record)

    def setup_ui(self):
        # Инициализация пути записи видео
        settings_path = str(Path(PurePath(__file__).parents[1], 'settings', 'settings.ini'))
        self.settings = QSettings(settings_path, QSettings.Format.IniFormat)
        self.record_path = Path(self.settings.value('record/path'))
        self.ui.saveEdit.setText(str(self.record_path))

    @Slot()
    def explore_path(self):
        video_path = QFileDialog.getExistingDirectory(self.window, "Сохранить запись в", '',
                                                      QFileDialog.Option.ShowDirsOnly)
        if len(video_path):
            self.ui.saveEdit.setText(str(video_path))
            self.settings.setValue('record/path', video_path)

    @Slot()
    def start_record(self):
        if self.video_stream.frame is None:
            return

        filename = f'{datetime.strftime(datetime.now(), "%Y-%m-%d_%H-%M-%S")}.mp4'
        if self.video_stream.frame is not None:
            self.camera_encoder = Encoder(self.record_path, self.video_stream, filename)
            self.camera_encoder.start()

        self.ui.startButton.setEnabled(False)
        self.ui.stopButton.setEnabled(False)
        self.ui.recordButton.setEnabled(False)
        self.ui.stopRecordButton.setEnabled(True)

    @Slot()
    def stop_record(self):
        if self.camera_encoder is None and self.inference_encoder is None:
            return

        if self.camera_encoder is not None:
            self.camera_encoder.requestInterruption()
            self.camera_encoder.wait()
        if self.inference_encoder is not None:
            self.inference_encoder.requestInterruption()
            self.inference_encoder.wait()

        self.ui.startButton.setEnabled(True)
        self.ui.stopButton.setEnabled(True)
        self.ui.recordButton.setEnabled(True)
        self.ui.stopRecordButton.setEnabled(False)


if __name__ == '__main__':
    pass
