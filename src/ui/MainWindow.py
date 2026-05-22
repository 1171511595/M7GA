from PySide6.QtWidgets import QMainWindow
from src.ui import mainwindow_ui
from src.model.blivedmmodel import BLiveModel

class MainWindow(QMainWindow):

    def __init__(self,blivemodelview:BLiveModel):
        super().__init__()
        self.modelview = blivemodelview
        self.ui = mainwindow_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.modelview.heart_msg.connect(self.on_recv_heart)

    # def start_blive(self):
    #     self.thread_blivemodel = BLiveModel()
    #     self.thread_blivemodel.InitID(24056350,'8d936c43%2C1795006570%2Cca220%2A51')
    #     self.thread_blivemodel.result_heart.connect(self.on_recv_heart)
    #     self.thread_blivemodel.start()


    def on_recv_heart(self,text):
        print("UI收到心跳:",text)

    