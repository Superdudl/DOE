import sys
sys.path.append(__file__)

from .mainWindowUI import Ui_mainWindow
from pathlib import Path, PurePath
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap
from .. import resources

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.setupUI()
        self.find_models()

    def setupUI(self):
        self.setWindowIcon(QPixmap(':/icons/logo.png'))
        self.ui.splitter.setSizes([100,100])
        self.ui.stopRecordButton.setEnabled(False)

        self.ui.snapshotButton.setIcon(QPixmap(':/icons/snapshot.png'))
        self.ui.recordButton.setIcon(QPixmap(':/icons/record.png'))
        self.ui.stopRecordButton.setIcon(QPixmap(':/icons/stop.png'))

        self.ui.savePath.setIcon(QPixmap(':/icons/search.png'))

    def find_models(self):
        path = Path(PurePath(__file__).parents[2], 'src', 'pretrained_models')
        for i, filename in enumerate(path.glob('*trt')):
            self.ui.modelComboBox.addItem("")
            self.ui.modelComboBox.setItemText(i, str(filename.name))

    def closeEvent(self, event, /):
        pass
