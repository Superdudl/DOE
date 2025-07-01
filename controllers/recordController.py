import sys

import numpy as np

sys.path.append(__file__)

from PySide6.QtCore import Slot, QSettings, QThread
from PySide6.QtWidgets import QFileDialog
from pathlib import Path, PurePath
import av
from PIL import Image
import cv2
from fractions import Fraction
from datetime import datetime
import time


class Encoder(QThread):
    def __init__(self, path, video_stream, filename):
        super().__init__()
        self.video_stream = video_stream
        self.container = None
        self.filename = filename
        settings_path = str(Path(PurePath(__file__).parents[1], 'settings', 'settings.ini'))
        self.settings = QSettings(settings_path, QSettings.Format.IniFormat)

        path = Path(path)
        self.path = path / filename

        if not self.path.parent.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)

        self.create_container()

    def create_container(self):
        import pycuda.driver as cuda
        import pycuda.autoinit

        codec = self.settings.value('record/codec', type=str)

        if codec == 'H.264':
            if cuda.Device.count() > 0:
                codec = 'h264_nvenc'
            else:
                codec = 'h264'
            pix_fmt = 'yuv420p'
            self.path = self.path.with_suffix('.mp4')

        elif codec == 'H.265':
            if cuda.Device.count() > 0:
                codec = 'hevc_nvenc'
            else:
                codec = 'hevc'
            pix_fmt = 'yuv420p'
            self.path = self.path.with_suffix('.mp4')

        elif codec == 'MJPEG':
            codec = 'mjpeg'
            pix_fmt = 'yuvj420p'
            self.path = self.path.with_suffix('.avi')

        elif codec == 'MPEG-4':
            codec = 'mpeg4'
            pix_fmt = 'yuv420p'
            self.path = self.path.with_suffix('.mp4')

        if self.video_stream.inference_frame is not None: codec = 'libopenh264'

        framerate = 30
        if self.video_stream.status and self.video_stream.frame is not None:
            h, w, c = self.video_stream.frame.shape
            if self.video_stream.inference_frame is not None:
                w = w + self.video_stream.inference_frame.shape[1]
                _h = self.video_stream.inference_frame.shape[0]
                h = _h if (_h > h) else h
            self.container = av.open(self.path, mode='w')
            self.av_stream = self.container.add_stream(codec, rate=framerate)
            self.av_stream.width = w
            self.av_stream.height = h
            self.av_stream.pix_fmt = pix_fmt
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
                _h = frame.shape[0]
                h = infer_frame.shape[0]
                if _h > h:
                    pad = _h - h
                    infer_frame = cv2.copyMakeBorder(infer_frame,
                                                     top=int(pad / 2) if pad % 2 == 0 else 0,
                                                     bottom=int(pad / 2) if pad % 2 == 0 else pad,
                                                     left=0,
                                                     right=0,
                                                     borderType=cv2.BORDER_CONSTANT,
                                                     value=[0, 0, 0]
                                                     )
                elif _h < h:
                    pad = h - _h
                    frame = cv2.copyMakeBorder(frame,
                                               top=int(pad / 2) if pad % 2 == 0 else 0,
                                               bottom=int(pad / 2) if pad % 2 == 0 else pad,
                                               left=0,
                                               right=0,
                                               borderType=cv2.BORDER_CONSTANT,
                                               value=[0, 0, 0]
                                               )
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
        self.ui.snapshotButton.clicked.connect(self.snapshot)
        self.ui.codecGroupBox.activated.connect(self.update_codec)

    def setup_ui(self):
        # Инициализация пути записи видео
        settings_path = str(Path(PurePath(__file__).parents[1], 'settings', 'settings.ini'))
        self.settings = QSettings(settings_path, QSettings.Format.IniFormat)
        self.record_path = Path(self.settings.value('record/path'))
        self.ui.saveEdit.setText(str(self.record_path))

    @Slot()
    def update_codec(self):
        codec = self.ui.codecGroupBox.currentText()
        self.settings.setValue('record/codec', codec)

    @Slot()
    def explore_path(self):
        video_path = QFileDialog.getExistingDirectory(self.window, "Сохранить запись в", '',
                                                      QFileDialog.Option.ShowDirsOnly)
        if len(video_path):
            self.ui.saveEdit.setText(str(video_path))
            self.record_path = Path(video_path)
            self.settings.setValue('record/path', video_path)

    @Slot()
    def start_record(self):
        if self.video_stream.frame is None:
            return

        filename = f'{datetime.strftime(datetime.now(), "%Y-%m-%d_%H-%M-%S")}'
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

    def snapshot(self):
        if self.video_stream.frame is None:
            return
        frame = np.copy(self.video_stream.frame)
        if self.video_stream.inference_frame is not None:
            infer_frame = np.copy(self.video_stream.inference_frame)
        else:
            infer_frame = None
        filters = " BMP (*.bmp);;JPEG (*.jpeg);;PNG (*.png)"
        image_path, extension = QFileDialog.getSaveFileName(None, 'Сохранить как', '', filter=filters)
        if len(image_path) < 1: return
        frame = frame if infer_frame is None else cv2.hconcat([frame, infer_frame])
        Image.fromarray(frame).save(Path(image_path))


if __name__ == '__main__':
    pass
