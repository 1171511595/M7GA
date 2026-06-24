from PySide6.QtCore import Signal,Slot
from PySide6.QtWidgets import QWidget
import json
import time
# 谷歌浏览器支持相关引入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
from ui.menu.LoginBilibili_ui import Ui_WidgetLoginBilibili

class LoginBilibili(QWidget):

    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = Ui_WidgetLoginBilibili()
        self.ui.setupUi(self)
        self.InitMember()
        self.InitConnect()
        

    def InitMember(self):
        self.str_Login_SESSDATA:str = ''
        # chrome驱动
        self.driver = None
        # 页面cookies
        self.cookies = None
        self.roomID:int = 0
        # B站用户登录态
        self.sessdata:str = ''

    def InitConnect(self):
        # 将打开登录窗口的按钮和对应的槽函数相关联
        self.ui.pushButton_openBilibiliLogin.clicked.connect(self.on_OpenBilibiliLogin)
        # 将获取用户登录态的按钮和对应的槽函数相关联
        self.ui.pushButton_getBilibiliSESSDATA.clicked.connect(self.on_GetBilibiliSESSDATA)
        # 将从缓存中获取用户登录态的按钮和对应的槽函数相关联
        self.ui.pushButton_fileGetBilibiliSESSDATA.clicked.connect(self.on_FileGetBilibiliSESSDATA)
        # 将获取房间ID号的按钮和对应的槽函数相关联
        self.ui.pushButton_inputRoomID.clicked.connect(self.slot_getRoomID)
        # 将关闭登录窗口的按钮和对应的槽函数相关联
        self.ui.pushButton_closeBilibiliWinodw.clicked.connect(self.on_CloseBilibiliLogin)

    @Slot()
    def on_OpenBilibiliLogin(self):
        # 打开Bilibili登录页面
        # 等待用户扫码登录

        # 1. 配置 Chrome 选项，重点：加入反自动化检测参数
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        
        # 2. 自动获取并配置 ChromeDriver
        try:
            service = Service(ChromeDriverManager().install())
        
            # 3. 启动浏览器
            self.driver = webdriver.Chrome(service=service, options=options)
            
            # 进一步隐藏自动化特征
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            # 4. 直接打开 B站的直播页（这里用一个默认的直播大播间作为跳板，或者直接打开登录页）
            # 策略：先访问直播主页，再跳转登录，更符合真人行为
            print("🚀 正在打开 B站直播页面...")
            self.driver.get("https://live.bilibili.com/")
            time.sleep(2) # 稍微等待页面加载
        except TimeoutException:
            print("[Erro]页面加载超时，当前电脑未联网或应用程序联网权限被防火墙拦截")
        except WebDriverException as e :
            print("[Erro]浏览器驱动或电脑网络连接异常:{e}")
        except Exception as e:
            print("[Erro]其他错误：{e}")


    @Slot()
    def on_GetBilibiliSESSDATA(self):
        # 未打开页面就点击获取SESSDATA时不进入逻辑
        if self.driver == None:
            return
        # 5. 获取所有 Cookie
        print("🔍 正在提取 Cookie...")
        self.cookies = self.driver.get_cookies()
        
        # 6. 从中筛选出 SESSDATA
        self.sessdata = None
        for cookie in self.cookies:
            if cookie['name'] == 'SESSDATA':
                self.sessdata = cookie['value']
                break
                
        if self.sessdata != '':
            print(f"✅ 获取成功！你的 SESSDATA 是：{self.sessdata}")
            # 保存为 JSON 文件，方便后续 blivedm 读取
            with open("Bilibilicookies.json", "w", encoding="utf-8") as f:
                json.dump(self.cookies, f, indent=4, ensure_ascii=False)
            print("💾 Cookie 已保存为 Bilibilicookies.json")
        else:
            print("❌ 未能获取 SESSDATA，请确认是否登录成功。")


    @Slot()
    def on_FileGetBilibiliSESSDATA(self):
        import json
        data = None
        # 读取根目录下的缓存文件
        with open ('Bilibilicookies.json', 'r',encoding='utf-8') as f :
            data = json.load(f)
        # 读取缓存文件中的SESSDATA值字段
        if data == None:
            print('从缓存文件中未获取到内容')
            return
        for item in data:
            if item['name'] == 'SESSDATA':
                print('于缓存文件中获取到SESSDATA')
                print('SESSDATA的内容为：')
                print(item['value'])
                self.sessdata = item['value']
                break
                
        if self.sessdata != '':
            print(f"✅ 获取成功！你的 SESSDATA 是：{self.sessdata}")
        else:
            print("❌ 未能获取 SESSDATA，请确认是否登录成功。")

    @Slot()
    def on_CloseBilibiliLogin(self):
        # 未打开页面就点击退出页面时不进入逻辑
        if self.driver == None:
            self.hide()
            return
        # 退出浏览器页面
        self.driver.quit()
        # 隐藏当前窗口
        self.hide()

    @Slot()
    def slot_getRoomID(self):
        # 获取用户输入的RoomID
        self.roomID = int(self.ui.lineEdit_inputRoomID.text())
        return