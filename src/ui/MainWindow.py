from PySide6.QtWidgets import QMainWindow
from src.ui import mainwindow_ui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainwindow_ui.Ui_MainWindow()
        self.ui.setupUi(self)