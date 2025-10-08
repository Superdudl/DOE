import sys

sys.path.append(__file__)

from .metricsDialogUI import Ui_Dialog
from PySide6.QtWidgets import QDialog, QButtonGroup


class MetricsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def closeEvent(self, event, /):
        pass
