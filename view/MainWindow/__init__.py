import sys
sys.path.append(__file__)

from .mainWindowUI import _MainWindowUI
from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = _MainWindowUI()
        self.ui.setupUi(self)