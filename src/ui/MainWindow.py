from PySide6.QtCore import Signal,Slot
from PySide6.QtWidgets import QMainWindow
from ui import mainwindow_ui
from modelview.blive import Blive

from ui.menu.LoginBilibili import LoginBilibili

class MainWindow(QMainWindow):

    def __init__(self,blivemodelview:Blive):
        super().__init__()
        self.ui = mainwindow_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.modelview = blivemodelview

        self.InitMember()
        self.InitConnect()

    def InitMember(self):
        # 创建B站登录态获取窗口
        self.LoginBilibliWindow = LoginBilibili()
        self.LoginBilibliWindow.hide()

        

    def InitConnect(self):
        # 连接界面菜单栏中基础设置中B站登录选项
        self.ui.actionden_login_Blibili.triggered.connect(self.on_openBilibiliLoginWindow)
        # 连接B站model发来的心跳信息
        self.modelview.signal_heart_msg.connect(self.slot_recv_heart)
        # 连接界面的PushButton
        self.ui.pushButton.clicked.connect(self.stop_bliveThread)
        # 开始线程
        self.ui.pushButton_2.clicked.connect(self.start_bliveThread)

    @Slot()
    def on_openBilibiliLoginWindow(self):
        # 打开软件中的Bilibili登录窗口
        self.LoginBilibliWindow.show()
        # 后续获取操作在窗口类中进行

    @Slot()
    def start_bliveThread(self):
        self.modelview.start_blive()

    @Slot()
    def stop_bliveThread(self):
        # print("界面按钮点击")
        self.modelview.stop_blive()

    @Slot()
    def slot_recv_heart(self,text):
        print("UI收到心跳:",text)

    