import sys

sys.path.append(__file__)

from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, QImage, Qt
from pathlib import Path, PurePath
from utils import Inference
from utils.metrics import psnr, ssim
import cv2

import pycuda.driver as cuda
import pycuda.autoinit


class AnalyseController:
    models_dir = Path(PurePath(__file__).parents[1], 'src', 'pretrained_models')

    def __init__(self, window):
        self.ui = window.ui
        model_text = window.parent().ui.modelComboBox.currentText()
        if len(model_text) > 0:
            self.model = self.models_dir / model_text
        else:
            self.model = None

        self.original_image = None
        self.blurred_image = None
        self.result_image = None
        self.connect_slots()

    def connect_slots(self):
        self.ui.originalButton.clicked.connect(self.open_original_image)
        self.ui.blurredButton.clicked.connect(self.open_blurred_image)
        self.ui.analyseButton.clicked.connect(self.analyse)

    @Slot()
    def open_original_image(self):
        filters = "Изображение (*.bmp *.jpg *.jpeg *.png)"
        image_path, _ = QFileDialog.getOpenFileName(None, "Выберите видео", '', filters)
        if len(image_path) == 0: return
        self.original_image = cv2.imread(Path(image_path), cv2.IMREAD_COLOR_RGB)
        h, w, c = self.original_image.shape
        qimage = QImage(self.original_image, w, h, w * c, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(self.ui.originalLabel.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.originalLabel.setPixmap(pixmap)

    @Slot()
    def open_blurred_image(self):
        filters = "Изображение (*.bmp *.jpg *.jpeg *.png)"
        image_path, _ = QFileDialog.getOpenFileName(None, "Выберите видео", '', filters)
        if len(image_path) == 0: return
        self.blurred_image = cv2.imread(Path(image_path), cv2.IMREAD_COLOR_RGB)
        h, w, c = self.blurred_image.shape
        qimage = QImage(self.blurred_image, w, h, w * c, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(self.ui.blurredLabel.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.blurredLabel.setPixmap(pixmap)

    @Slot()
    def analyse(self):

        # Восстановление изображения

        if cuda.Device.count() == 0: return
        inference = Inference()
        inference.create(self.model, self.blurred_image.shape)
        self.result_image, _ = inference(self.blurred_image)
        inference.clear()
        h, w, c = self.blurred_image.shape
        qimage = QImage(self.result_image, w, h, w * c, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(self.ui.analyseLabel.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.analyseLabel.setPixmap(pixmap)

        # Расчет SSIM и PSNR

        original_gray = cv2.cvtColor(self.original_image, cv2.COLOR_RGB2GRAY)
        result_gray = cv2.cvtColor(self.result_image, cv2.COLOR_RGB2GRAY)

        psnr_metric = psnr(original_gray, result_gray)
        ssim_metric = ssim(original_gray, result_gray)

        self.ui.psnrLineEdit.setText(f'{psnr_metric:.2f}')
        self.ui.ssimLineEdit.setText(f'{ssim_metric:.2f}')
