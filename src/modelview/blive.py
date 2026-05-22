from PySide6.QtCore import QObject, Signal

class Blive(QObject):
    # 定义一个信号，参数为字符串
    message_signal = Signal(str)
    # 定义一个信号，参数为整数
    count_changed = Signal(int)

    def __init__(self,model):
        super().__init__()
        self._model = model

    def send_message(self, message):
        # 发送信号，传递消息
        self.message_signal.emit(message)

        
    def increment(self):
        self._model.increment()
        self.count_changed.emit(self._model.count)

    def decrement(self):
        self._model.decrement()
        self.count_changed.emit(self._model.count)

    @property
    def count(self):
        return self._model.count