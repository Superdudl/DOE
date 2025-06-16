import sys
sys.path.append(__file__)

from .videoCapture import VideoCapture
from .inference import Inference
from .videoStream import VideoStream
from . import Classical_Correction

from PySide6.QtCore import QSettings
from pathlib import Path, PurePath

class CONFIG:
    _path = Path(PurePath(__file__).parents[1]) / 'settings' / 'settings.ini'
    _settings = QSettings(str(_path), QSettings.Format.IniFormat)
    DEBUG = _settings.value('config/DEBUG', type=bool)

DEBUG = CONFIG.DEBUG