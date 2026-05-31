from PySide6.QtCore import QObject, Signal, Slot
import re
from model.blivedmmodel import BLiveModel

class Blive(QObject):
    # 定义一个信号，参数为字符串
    # 向UI发送心跳内容
    signal_heart_msg = Signal(str)
    # 向UI推送处理后的普通用户信息
    # 用户名，勋章名，勋章等级，信息内容
    signal_normal_msg = Signal(str,str,str,str)
    # 向UI推送处理后的礼物消息
    signal_gift_msg = Signal(str)
    # 向UI推送处理后的上舰等级
    signal_captain_msg = Signal(str)
    # 向UI推送处理后的醒目留言信息
    signal_money_msg = Signal(str)
    # 向UI推送进入直播间的用户的用户名
    signal_come_people = Signal(str)

    def __init__(self,model):
        super().__init__()
        self._model = model
        # 将创建的模型的信号连接
        self.initConnect()
        # 今日开播总收入
        self.today_recv_money = 0
        # 今日进过直播间的人,只要是进入直播间的，名字就都记录下来
        self.today_comepeoplename:set = set()
        # 今日直播间的所有人的普通发言信息（备查）
        self.today_allpeoplemsg:list = []
        # 今日直播间的所有礼物记录列表
        self.today_allgiftmsg:list = []
        # 今日直播间的所有上舰记录列表
        self.today_allcaptain:list = []
        # 今日直播间的所有付费留言
        self.today_gold_message:list = []
        # 用户登录信息中的SESSDATA
        self.today_USER_SESSDATA = ''

    def initConnect(self):
        # 连接模型的心跳信号
        self._model.signal_result_heart.connect(self.slot_recv_heart)
        # 连接模型的普通消息信号
        self._model.signal_result_normalmsg.connect(self.slot_recv_normalmsg)
        # 连接模型的礼物消息信号
        self._model.signal_result_giftmsg.connect(self.slot_recv_giftmsg)
        # 连接模型的醒目留言信息
        self._model.signal_result_captainmsg.connect(self.slot_recv_goldmsg)
        # 连接模型的上舰消息信号
        self._model.signal_reslut_goldmsg.connect(self.slot_recv_captainmsg)
        # 连接模型的醒目留言信号
        self._model.signal_result_peoplecome.connect(self.slot_recv_peoplecome)

    @Slot()
    def start_blive(self,roomID:int,SESSDATA:str):
        # 设置使用的房间号和用户登录态SESSDATA后开始收集信息
        # 重开一个线程
        if (self._model == None):
            self._model = BLiveModel()
            # 因为新建了数据对象，所以需要重新链接槽函数
            self.initConnect()
        # print("设置房间号和登录态")
        self._model.InitID(roomID,SESSDATA)
        # print("开始线程")
        self._model.start()


    @Slot()
    def stop_blive(self):
        if (self._model == None):
            return
        self._model.stop_asyncio()
        self._model = None

    @Slot()
    def slot_recv_heart(self,heart_text):
        # 接收数据模型传来的心跳信息
        # 通过Qt信号向UI界面发送信息
        self.signal_heart_msg.emit(heart_text)

    @Slot()
    def slot_recv_normalmsg(self,username,medal_name,medal_level,msg):
        # 接收数据模型传来的普通用户信息
        # 将普通用户信息存储到List列表
        self.today_allpeoplemsg.append(username+medal_name+medal_level+msg)
        # msg处理部分移到UI界面绘制中
        # # 对msg进行处理，找到信息中所有的表情包标识
        # emojiname_list = re.findall(r'\[(.*?)\]', msg)
        # # 去掉信息中的表情，留下纯文本
        # usermsg = ''
        # left = msg.find('[')
        # if left != -1:
        #     usermsg = msg[:left]
        # else:
        #     # 没有找到'['，直接把信息复制到usermsg中
        #     usermsg = msg

        # 将发送人，发送信息，表情包标识全部发送到UI界面
        self.signal_normal_msg.emit(username,medal_name,medal_level,msg)


    @Slot()
    def slot_recv_giftmsg(self,username,giftname,giftnum,moneytype,money):
        # 接收数据模型传来的礼物消息
        # 将礼物消息添加到记录列表中
        self.today_allgiftmsg.append(username+giftname+'x'+giftnum+moneytype+'x'+money)
        # 计算收入
        if(moneytype == 'gold'):
            # 1元==1000金瓜子
            self.today_recv_money += float(money)/1000
            print('今日已收入'+str(int(self.today_recv_money))+'元')
        # 将送礼人，礼物名字，礼物数量，收入，全部发送到UI界面
        self.signal_gift_msg.emit(username+giftname+'x'+giftnum+moneytype+'x'+money)

    @Slot()
    def slot_recv_goldmsg(self,username,msg,money):
        # 接收数据模型传来的醒目留言信息
        # 将付费留言添加到记录列表中
        self.today_gold_message.append(username+msg+money)
        # 计算收入
        self.today_recv_money += int(money)

        print('今日已收入'+str(int(self.today_recv_money))+'元')
        # 将付费留言发送到UI界面
        self.signal_money_msg.emit(username+msg+money)

    @Slot()
    def slot_recv_captainmsg(self,username,captaingrade):
        # 接收数据模型传来的上舰等级
        # 将上舰记录添加到记录列表中
        self.today_allcaptain.append(username+captaingrade)
        # 计算收入
        if (captaingrade == '总督'):
            self.today_recv_money += 10000
        if (captaingrade == '提督'):
            self.today_recv_money += 1000
        if (captaingrade == '舰长'):
            self.today_recv_money += 100

        print('今日已收入'+str(int(self.today_recv_money))+'元')
        # 将上舰消息发送到UI界面
        self.signal_captain_msg.emit(username+captaingrade)

    @Slot()
    def slot_recv_peoplecome(self,username):
        # 接收数据模型传来的进入直播间的用户的用户名
        # 将进入直播间的用户名记录到集合中
        self.today_comepeoplename.add(str(username))
        # 将观众进入信息发送到UI界面
        self.signal_come_people.emit(username)
