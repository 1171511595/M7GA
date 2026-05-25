from PySide6.QtCore import Signal,Slot
from PySide6.QtWidgets import QWidget
from menu import LoginBilibili_ui

class LoginBilibili(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = LoginBilibili_ui.Ui_WidgetLoginBilibili()
        self.ui.setupUi()
        
        