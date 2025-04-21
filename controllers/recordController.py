import sys

sys.path.append(__file__)

from PySide6.QtCore import QObject, Slot, QSettings, QThread
from PySide6.QtWidgets import QMessageBox, QFileDialog
from pathlib import Path, PurePath
import av
from datetime import datetime
import time

class Encoder(QThread):
    def __init__(self, ui, video_stream, filename, stream):
        """
        stream: ['camera', 'inference']
        """
        super().__init__()
        self.video_stream = video_stream
        self.ui = ui
        self.container = None
        self.stream = stream
        self.filename = filename

        path = Path(self.ui.saveEdit.text())
        assert stream in ['camera', 'inference']
        if stream == 'camera':
            self.path = path / 'Original' / filename
        elif stream == 'inference':
            self.path = path / 'Inference' / filename

        self.create_container()

    def create_container(self):
        if self.video_stream.status and self.video_stream.frame is not None:
            h, w, c = self.video_stream.frame.shape
            self.container = av.open(self.path, mode='w')
            self.av_stream = self.container.add_stream('libx264', rate=30)
            self.av_stream.width = w
            self.av_stream.height = h
            self.av_stream.pix_fmt = 'yuv420p'

    def run(self):
        start_time = time.time()
        while not self.requestInterruption():
            current_time = time.time() - start_time

            frame = None

            if self.stream == 'camera':
                frame = av.VideoFrame.from_ndarray(self.video_stream.frame, 'rgb24')
            elif self.stream == 'inference':
                frame = av.VideoFrame.from_ndarray(self.video_stream.inference_frame, 'rgb24')

            pts = int(current_time * self.container.time_base.denominator / self.container.time_base.numerator)

            frame.pts = pts

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
        record_path = Path(self.settings.value('record/path'))
        self.ui.saveEdit.setText(str(record_path))

    @Slot()
    def explore_path(self):
        video_path = QFileDialog.getExistingDirectory(self.window, "Сохранить запись в", '',
                                                      QFileDialog.Option.ShowDirsOnly)
        self.ui.saveEdit.setText(str(video_path))
        self.settings.setValue('record/path', video_path)

    @Slot()
    def start_record(self):
        if self.video_stream.frame is None:
            return

        filename = f'{datetime.strftime(datetime.now(), "%Y-%m-%d_%H-%M-%S")}.mp4'
        if  self.video_stream.frame is not None:
            self.camera_encoder = Encoder(self.ui, self.video_stream, filename, stream='camera')
            self.camera_encoder.start()
        if self.video_stream.inference_frame is not None:
            self.inference_encoder = Encoder(self.ui, self.video_stream, filename, stream='inference')
            self.inference_encoder.start()

        self.ui.startButton.setEnabled(False)
        self.ui.stopButton.setEnabled(False)
        self.ui.recordButton.setEnabled(False)
        self.ui.stopRecordButton.setEnabled(True)

    @Slot()
    def stop_record(self):
        if (self.camera_encoder and self.inference_encoder) is None:
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
