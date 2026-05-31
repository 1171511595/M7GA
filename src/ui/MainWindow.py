from PySide6.QtCore import Signal,Slot,Qt
from PySide6.QtWidgets import QMainWindow,QHeaderView,QTableWidget,QTableWidgetItem
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
        self.InitUI()
        self.InitConnect()

    def InitMember(self):
        # 创建B站登录态获取窗口
        self.LoginBilibliWindow = LoginBilibili()
        self.LoginBilibliWindow.hide()

    def InitUI(self):
        # 初始化普通弹幕显示列表
        self.ui.tableWidget_normalMsg.setRowCount(999)
        self.ui.tableWidget_normalMsg.setColumnCount(3)
        self.ui.tableWidget_normalMsg.setHorizontalHeaderLabels(["来源","用户名","信息内容"])
        # 设置列表中每一列的宽度
        self.ui.tableWidget_normalMsg.setColumnWidth(0,50)
        self.ui.tableWidget_normalMsg.setColumnWidth(1,100)
        self.ui.tableWidget_normalMsg.setColumnWidth(2,280)
        # 开启自动换行
        self.ui.tableWidget_normalMsg.setWordWrap(True)
        # 设置列表的行高根据内容而变化
        self.ui.tableWidget_normalMsg.resizeRowsToContents()
        # 隐藏列序号
        self.ui.tableWidget_normalMsg.verticalHeader().setVisible(False)
        # 获取列属性对象
        normalMsgHeader = self.ui.tableWidget_normalMsg.horizontalHeader()
        # 禁止用户修改列宽
        normalMsgHeader.setSectionsMovable(False)
        normalMsgHeader.setSectionResizeMode(QHeaderView.Fixed)
        

    def InitConnect(self):
        # 连接界面菜单栏中基础设置中B站登录选项
        self.ui.actionden_login_Blibili.triggered.connect(self.on_openBilibiliLoginWindow)
        # 连接B站model发来的心跳信息
        self.modelview.signal_heart_msg.connect(self.slot_recv_heart)
        # 连接界面的PushButton
        self.ui.pushButton.clicked.connect(self.stop_bliveThread)
        # 开始线程
        self.ui.pushButton_2.clicked.connect(self.start_bliveThread)
        # 测试数据添加
        self.ui.pushButton_3.clicked.connect(self.slot_add_data)

    @Slot()
    def on_openBilibiliLoginWindow(self):
        # 打开软件中的Bilibili登录窗口
        self.LoginBilibliWindow.show()
        # 后续获取操作在窗口类中进行

    @Slot()
    def start_bliveThread(self):
        print("页面中的房间ID为："+str(self.LoginBilibliWindow.roomID))
        print("页面中的用户态为："+self.LoginBilibliWindow.sessdata)
        self.modelview.start_blive(self.LoginBilibliWindow.roomID,
                                   self.LoginBilibliWindow.sessdata)

    @Slot()
    def stop_bliveThread(self):
        # print("界面按钮点击")
        self.modelview.stop_blive()

    @Slot()
    def slot_recv_heart(self,text):
        print("UI收到心跳:",text)

    @Slot()
    def slot_add_data(self):
        data = [
            ("Item A", "这是一个非常长的描述，用于测试自动换行功能。"),
            ("Item B", "多行文本示例\n第二行\n第三行"),
            ("Item C", "短文本")
        ]

        for row, (name, desc) in enumerate(data):
            name_item = QTableWidgetItem(name)
            desc_item = QTableWidgetItem(desc)

            # 对齐方式（可选）
            desc_item.setTextAlignment(Qt.AlignTop | Qt.AlignLeft)

            self.ui.tableWidget_normalMsg.setItem(row, 0, name_item)
            self.ui.tableWidget_normalMsg.setItem(row, 1, desc_item)

        # 设置列表的行高根据内容而变化
        self.ui.tableWidget_normalMsg.resizeRowsToContents()

    