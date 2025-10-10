import sys

import numpy as np
from sympy.codegen.ast import continue_

sys.path.append(__file__)

from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, QImage, Qt
from pathlib import Path, PurePath
from utils import Inference
from utils.metrics import psnr, ssim, match_template, match_histograms, deconv
import cv2

import pycuda.driver as cuda
import pycuda.autoinit


class AnalyseController:
    models_dir = Path(PurePath(__file__).parents[1], 'src', 'pretrained_models')

    def __init__(self, window):
        self.ui = window.ui
        self.parent_ui = window.parent().ui
        model_text = self.parent_ui.modelComboBox.currentText()
        if len(model_text) > 0:
            self.model = self.models_dir / model_text
        else:
            self.model = None

        self.original_image = None
        self.blurred_image = None
        self.result_image = None

        self.setup_ui()
        self.connect_slots()

    def setup_ui(self):
        self.ui.comboBox.addItems(
            [self.parent_ui.modelComboBox.itemText(i) for i in range(self.parent_ui.modelComboBox.count())])
        self.ui.comboBox.setCurrentIndex(self.parent_ui.modelComboBox.currentIndex())

    def connect_slots(self):
        self.ui.originalButton.clicked.connect(self.open_original_image)
        self.ui.blurredButton.clicked.connect(self.open_blurred_image)
        self.ui.analyseButton.clicked.connect(self.analyse)
        self.ui.comboBox.activated.connect(self.update_model)
        self.ui.match_hists_checkbox.clicked.connect(lambda checked: self.ui.deconv_checkbox.setChecked(not checked)
                                                     if self.ui.deconv_checkbox.isChecked()
                                                     else True)
        self.ui.deconv_checkbox.clicked.connect(lambda checked: self.ui.match_hists_checkbox.setChecked(not checked)
                                                if self.ui.match_hists_checkbox.isChecked()
                                                else True)

    @Slot()
    def update_model(self):
        model_text = self.ui.comboBox.currentText()
        if len(model_text) > 0:
            self.model = self.models_dir / model_text
        else:
            self.model = None

    @Slot()
    def open_original_image(self):
        filters = "Изображение (*.bmp *.jpg *.jpeg *.png)"
        image_path, _ = QFileDialog.getOpenFileName(None, "Выберите оригинальное изображение", '', filters)
        if len(image_path) == 0: return
        filepath = Path(image_path)
        bytes_stream = open(filepath, 'rb')
        bytes = bytearray(bytes_stream.read())
        bytes_stream.close()
        array = np.array(bytes, dtype=np.uint8)
        self.original_image = cv2.imdecode(array, cv2.IMREAD_COLOR_RGB)
        h, w, c = self.original_image.shape
        qimage = QImage(self.original_image, w, h, w * c, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(self.ui.originalLabel.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.originalLabel.setPixmap(pixmap)

    @Slot()
    def open_blurred_image(self):
        filters = "Изображение (*.bmp *.jpg *.jpeg *.png)"
        image_path, _ = QFileDialog.getOpenFileName(None, "Выберите искаженное изображение", '', filters)
        if len(image_path) == 0: return
        filepath = Path(image_path)
        bytes_stream = open(filepath, 'rb')
        bytes = bytearray(bytes_stream.read())
        bytes_stream.close()
        array = np.array(bytes, dtype=np.uint8)
        self.blurred_image = cv2.imdecode(array, cv2.IMREAD_COLOR_RGB)
        h, w, c = self.blurred_image.shape
        qimage = QImage(self.blurred_image, w, h, w * c, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(self.ui.blurredLabel.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.blurredLabel.setPixmap(pixmap)

    @Slot()
    def analyse(self):
        if self.original_image is None or self.blurred_image is None: return

        # Восстановление изображения

        if cuda.Device.count() == 0: return
        inference = Inference()
        inference.create(self.model, self.blurred_image.shape)
        self.result_image, _ = inference(self.blurred_image)
        self.original_image = match_template(self.result_image, self.original_image)

        #--------------------------------------------------------------------------------------------------------------
        # from utils.Classical_Correction import restore_image
        # self.result_image = restore_image(self.blurred_image)
        #--------------------------------------------------------------------------------------------------------------

        inference.clear()
        # Расчет SSIM и PSNR

        original_gray = cv2.cvtColor(self.original_image, cv2.COLOR_RGB2GRAY)
        result_gray = cv2.cvtColor(self.result_image, cv2.COLOR_RGB2GRAY)

        if self.ui.match_hists_checkbox.isChecked():
            result_gray = match_histograms(result_gray, original_gray)
            self.result_image = cv2.cvtColor(result_gray, cv2.COLOR_GRAY2BGR)
        elif self.ui.deconv_checkbox.isChecked():
            blurred_gray = cv2.cvtColor(self.blurred_image, cv2.COLOR_BGR2GRAY)
            self.result_image = np.ascontiguousarray(deconv(blurred_gray, original_gray))
            result_gray = self.result_image
            self.result_image = cv2.cvtColor(self.result_image, cv2.COLOR_GRAY2BGR)

        psnr_metric = psnr(original_gray, result_gray)
        ssim_metric = ssim(original_gray, result_gray)

        self.ui.psnrLineEdit.setText(f'{psnr_metric:.2f}')
        self.ui.ssimLineEdit.setText(f'{ssim_metric:.2f}')

        h, w, c = self.blurred_image.shape
        qimage = QImage(self.result_image, w, h, w * c, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(self.ui.analyseLabel.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.analyseLabel.setPixmap(pixmap)

