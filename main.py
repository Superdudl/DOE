import sys
sys.path.append(__file__)

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSettings
from view.MainWindow import MainWindow
from pathlib import Path, PurePath

DEBUG = False

def main():
    path = Path(PurePath(__file__).parent) / 'settings' / 'settings.ini'
    settings = QSettings(str(path), QSettings.Format.IniFormat)
    settings.setValue('config/DEBUG', DEBUG)

    app = QApplication(sys.argv)
    from controllers import MainController

    window = MainWindow()
    window.showMaximized()
    _ = MainController(window)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()