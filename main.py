import sys
from PySide6.QtWidgets import QApplication

from src.ui.MainWindow import MainWindow as MainWindow

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
