import sys

sys.path.append(__file__)

from pathlib import Path, PurePath
from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMessageBox, QFileDialog
from view.MetricsDialog import MetricsDialog
from controllers import CameraController, InferenceController, RecordController, VideoReader, AnalyseController
from utils import VideoStream, open_pdf
from utils import DEBUG


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
        self.ui.analise.triggered.connect(self.open_analise_dialog)
        self.ui.action.triggered.connect(self.open_reference)

    def __del__(self):
        self.video_stream.stop_stream()
        self.inference_controller.stop()

    def open_reference(self):
        path = Path(__file__).parents[1] / 'src'
        sender = self.sender().text()
        if sender == 'Спецификация':
            path = path.joinpath('Спецификация.pdf')
        elif sender == 'Текст программы':
            path = path.joinpath('Текст программы.pdf')
        elif sender == 'Описание программы':
            path = path.joinpath('Описание программы.pdf')
        elif sender == 'Руководство оператора':
            path = path.joinpath('Руководство оператора.pdf')
        elif sender == 'Руководство системного программиста':
            path = path.joinpath('Руководство системного программиста.pdf')

        open_pdf(path)

    @Slot()
    def connect_camera(self):
        if DEBUG: source = 'DEBUG'
        else: source = 'camera'
        self.video_stream.start_stream(source)
        if not self.video_stream.status:
            QMessageBox.warning(self.window, "Ошибка", "Камера не подключена")
            return
        self.ui.exposureEdit.setEnabled(True)
        self.ui.gainEdit.setEnabled(True)
        self.ui.formatComboBox.setEnabled(True)
        self.ui.exposureAuto.setEnabled(True)
        self.ui.gainAuto.setEnabled(True)
        if not DEBUG :
            self.camera_controller = CameraController(self.video_stream.stream, self.ui)

    @Slot()
    def open_video(self):
        filters = "Видео (*.mp4 *.avi *.mkv)"
        video_path, _ = QFileDialog.getOpenFileName(self.window, "Выберите видео", '', filters)
        if len(video_path) == 0: return
        self.inference_controller.stop()
        self.video_stream.stop_stream()
        self.video_reader = VideoReader(self.ui, self.window)
        self.video_reader.open(video_path)

    @Slot()
    def open_analise_dialog(self):
        self.inference_controller.stop()
        self.video_stream.stop_stream()
        dialog_window = MetricsDialog(self.window)
        dialog_window.setWindowTitle('Анализ качества восстановления')
        dialog_window.setWindowIcon(QPixmap(':/icons/logo.png'))
        analyse_controller = AnalyseController(dialog_window)
        dialog_window.exec()



