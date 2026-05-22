from PySide6.QtCore import QObject, Signal, Slot
from model.blivedmmodel import BLiveModel

class Blive(QObject):
    # 定义一个信号，参数为字符串
    # 向UI发送心跳内容
    heart_msg = Signal(str)

    def __init__(self,model):
        super().__init__()
        self._model = model

    @Slot()
    def start_blive(self):
        self.thread_blivemodel = BLiveModel()
        self.thread_blivemodel.InitID(10339509,'8d936c43%2C1795006570%2Cca220%2A51')
        self.thread_blivemodel.result_heart.connect(self.on_recv_heart)
        self.thread_blivemodel.start()

    @Slot()
    def stop_blive(self):
        print("模型收到按钮的点击")
        self.thread_blivemodel.stop_asyncio()

    def on_recv_heart(self,heart_text):
        # 通过Qt信号向UI界面发送信息
        self.heart_msg.emit(heart_text)

