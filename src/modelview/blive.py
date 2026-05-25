from PySide6.QtCore import QObject, Signal, Slot
import re
from model.blivedmmodel import BLiveModel

class Blive(QObject):
    # 定义一个信号，参数为字符串
    # 向UI发送心跳内容
    heart_msg = Signal(str)
    # 向UI推送处理后的普通用户信息
    # 用户名，勋章名，勋章等级，信息内容
    normal_msg = Signal(str,str,str,str)
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
        # 重开一个线程
        if (self._model == None):
            self._model = BLiveModel()
            # 因为新建了数据对象，所以需要重新链接槽函数
            self.initConnect()
        # print("设置房间号和登录态")
        self._model.InitID(46197,'801ee64e%2C1795149443%2C936bf%2A51')
        # print("开始线程")
        self._model.start()


    @Slot()
    def stop_blive(self):
        if (self._model == None):
            return
        self._model.stop_asyncio()
        self._model = None

    @Slot()
    def on_recv_heart(self,heart_text):
        # 接收数据模型传来的心跳信息
        # 通过Qt信号向UI界面发送信息
        self.heart_msg.emit(heart_text)

    @Slot()
    def on_recv_normalmsg(self,username,medal_name,medal_level,msg):
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
        self.normal_msg.emit(username,medal_name,medal_level,msg)


    @Slot()
    def on_recv_giftmsg(self,username,giftname,giftnum,moneytype,money):
        # 接收数据模型传来的礼物消息
        # 将礼物消息添加到记录列表中
        self.today_allgiftmsg.append(username+giftname+'x'+giftnum+moneytype+'x'+money)
        # 计算收入
        if(moneytype == 'gold'):
            # 1元==1000金瓜子
            self.today_recv_money += float(money)/1000
            print('今日已收入'+str(int(self.today_recv_money))+'元')
        # 将送礼人，礼物名字，礼物数量，收入，全部发送到UI界面
        self.gift_msg.emit(username+giftname+'x'+giftnum+moneytype+'x'+money)

    @Slot()
    def on_recv_captainmsg(self,username,captaingrade):
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
        self.captain_msg.emit(username+captaingrade)

    @Slot()
    def on_recv_goldmsg(self,username,msg,money):
        # 接收数据模型传来的醒目留言信息
        # 将付费留言添加到记录列表中
        self.today_gold_message.append(username+msg+money)
        # 计算收入
        self.today_recv_money += int(money)

        print('今日已收入'+str(int(self.today_recv_money))+'元')
        # 将付费留言发送到UI界面
        self.on_recv_goldmsg.emit(username+msg+money)

    @Slot()
    def on_recv_peoplecome(self,username):
        # 接收数据模型传来的进入直播间的用户的用户名
        # 将进入直播间的用户名记录到集合中
        self.today_comepeoplename.add(str(username))
        # 将观众进入信息发送到UI界面
        self.come_people.emit(username)

    @Slot()
    def on_get_login_cookies(self):
        # 获取cookies并提取SESSDATA
        import json
        import time
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        from webdriver_manager.chrome import ChromeDriverManager
        # 1. 配置 Chrome 选项，重点：加入反自动化检测参数
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        
        # 2. 自动获取并配置 ChromeDriver
        service = Service(ChromeDriverManager().install())
        
        # 3. 启动浏览器
        driver = webdriver.Chrome(service=service, options=options)
        
        # 进一步隐藏自动化特征
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # 4. 直接打开 B站的直播页（这里用一个默认的直播大播间作为跳板，或者直接打开登录页）
        # 策略：先访问直播主页，再跳转登录，更符合真人行为
        print("🚀 正在打开 B站直播页面...")
        driver.get("https://live.bilibili.com/")
        time.sleep(2) # 稍微等待页面加载
        
        # 5. 触发登录弹窗（通过 JS 点击右上角的登录按钮）
        try:
            print("🖱️ 正在尝试点击登录按钮...")
            login_btn = driver.find_element("xpath", "//a[contains(@class,'header-login-entry')]")
            login_btn.click()
            print("✅ 已成功触发登录弹窗！")
        except Exception as e:
            print(f"⚠️ 未找到登录按钮，可能页面结构已变化或已登录。错误：{e}")

        # 6. 暂停，等待你手动扫码登录
        print("⏸️ 请在弹出的浏览器中扫码登录，登录完成后回到控制台按 Enter 键继续...")
        input() # 阻塞在这里，直到你按 Enter
        
        # 7. 获取所有 Cookie
        print("🔍 正在提取 Cookie...")
        cookies = driver.get_cookies()
        
        # 8. 从中筛选出 SESSDATA
        sessdata = None
        for cookie in cookies:
            if cookie['name'] == 'SESSDATA':
                sessdata = cookie['value']
                self.today_USER_SESSDATA = cookie['value']
                break
                
        if sessdata:
            print(f"✅ 获取成功！你的 SESSDATA 是：{sessdata}")
            # 保存为 JSON 文件，方便后续 blivedm 读取
            with open("cookies.json", "w", encoding="utf-8") as f:
                json.dump(cookies, f, indent=4, ensure_ascii=False)
            print("💾 Cookie 已保存为 cookies.json")
        else:
            print("❌ 未能获取 SESSDATA，请确认是否登录成功。")
            
        driver.quit()