import sys
sys.path.append(__file__)
import subprocess

def open_pdf(filepath):
    path = Path(filepath)
    if path.exists():
        QDesktopServices.openUrl(QUrl.fromLocalFile(path))
    else:
        QMessageBox.warning(None, 'Ошибка', 'Файл не найден')

def cuda_is_available():
    try:
        result = subprocess.run(['nvcc', '--version'], capture_output=True, text=True)
        if result.returncode == 0: return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

from .videoCapture import VideoCapture
from .inference import Inference
from .videoStream import VideoStream

from PySide6.QtCore import QSettings, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QMessageBox
from pathlib import Path, PurePath

class CONFIG:
    _path = Path(PurePath(__file__).parents[1]) / 'settings' / 'settings.ini'
    _settings = QSettings(str(_path), QSettings.Format.IniFormat)
    DEBUG = _settings.value('config/DEBUG', type=bool)

DEBUG = CONFIG.DEBUG
