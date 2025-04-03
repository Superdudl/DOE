import sys
sys.path.append(__file__)

from PySide6.QtWidgets import QApplication
from view.MainWindow import MainWindow
from controllers import MainController

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.showMaximized()
    _ = MainController(window.ui)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()