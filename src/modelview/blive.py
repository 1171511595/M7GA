from PySide6.QtCore import QObject, Signal, Slot
import re
from model.blivedmmodel import BLiveModel

class Blive(QObject):
    # 定义一个信号，参数为字符串
    # 向UI发送心跳内容
    heart_msg = Signal(str)
    # 向UI推送处理后的普通用户信息
    normal_msg = Signal(str,str,list)
    # 向UI推送处理后的礼物消息
    gift_msg = Signal(str)
    # 向UI推送处理后的上舰等级
    captain_msg = Signal(str)
    # 向UI推送处理后的醒目留言信息
    money_msg = Signal(str)
    # 向UI推送进入直播间的用户的用户名
    come_people = Signal(str)

    def __init__(self,model):
        super().__init__()
        self._model = model
        # 将创建的模型的信号连接
        self.initConnect()
        # 今日开播总收入
        self.today_recv_money = 0
        # 今日进过直播间的人,只要是进入直播间的，名字就都记录下来
        self.today_comepeoplename:set
        # 今日直播间的所有人的普通发言信息（备查）
        self.today_allpeoplemsg:list

    def initConnect(self):
        # 连接模型的心跳信号
        self._model.result_heart.connect(self.on_recv_heart)
        # 连接模型的普通消息信号
        self._model.result_normalmsg.connect(self.on_recv_normalmsg)
        # 连接模型的礼物消息信号
        self._model.result_giftmsg.connect(self.on_recv_giftmsg)
        # 连接模型的醒目留言信息
        self._model.reslut_goldmsg.connect(self.on_recv_goldmsg)
        # 连接模型的上舰消息信号
        self._model.result_captainmsg.connect(self.on_recv_captainmsg)
        # 连接模型的醒目留言信号
        self._model.result_peoplecome.connect(self.on_recv_peoplecome)

    @Slot()
    def start_blive(self):
        # 设置使用的房间号和用户登录态SESSDATA后开始收集信息
        # print("设置房间号和登录态")
        self._model.InitID(10339509,'5291b011%2C1795093784%2C103d4%2A51')
        # print("开始线程")
        self._model.start()

    @Slot()
    def stop_blive(self):
        self._model.stop_asyncio()

    def on_recv_heart(self,heart_text):
        # 接收数据模型传来的心跳信息
        # 通过Qt信号向UI界面发送信息
        self.heart_msg.emit(heart_text)

    def on_recv_normalmsg(self,username,msg):
        # 接收数据模型传来的普通用户信息
        # 将普通用户信息存储到List列表
        self.today_allpeoplemsg.add(username+msg)
        # 对msg进行处理，找到信息中所有的表情包标识
        emojiname_list = re.findall(r'\[(.*?)\]', msg)
        # 去掉信息中的表情，留下纯文本
        left = msg.find('[')
        if left != -1:
            usermsg = msg[:left]
        else:
            print("没有找到 [")
        # 将发送人，发送信息，表情包标识全部发送到UI界面
        self.normal_msg.emit(username,usermsg,emojiname_list)



    def on_recv_giftmsg(self,username,giftname,giftnum,moneytype,money):
        # 接收数据模型传来的礼物消息
        print()

    def on_recv_captainmsg(self,username,captaingrade):
        # 接收数据模型传来的上舰等级
        print()

    def on_recv_goldmsg(self,username,msg,money):
        # 接收数据模型传来的醒目留言信息
        print()

    def on_recv_peoplecome(self,username):
        # 接收数据模型传来的进入直播间的用户的用户名
        print()

