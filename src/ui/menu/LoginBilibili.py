from PySide6.QtCore import Signal,Slot
from PySide6.QtWidgets import QWidget
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
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
        self.cookie = None
        # B站用户登录态
        self.sessdata = None

    def InitConnect(self):
        # 将打开登录窗口的按钮和对应的槽函数相关联
        self.ui.pushButton_openBilibiliLogin.clicked.connect(self.on_OpenBilibiliLogin)
        # 将获取用户登录态的按钮和对应的槽函数相关联
        self.ui.pushButton_getBilibiliSESSDATA.clicked.connect(self.on_GetBilibiliSESSDATA)
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

    @Slot()
    def on_GetBilibiliSESSDATA(self):
        # 5. 获取所有 Cookie
        print("🔍 正在提取 Cookie...")
        cookies = self.driver.get_cookies()
        
        # 6. 从中筛选出 SESSDATA
        sessdata = None
        for cookie in cookies:
            if cookie['name'] == 'SESSDATA':
                sessdata = cookie['value']
                self.today_USER_SESSDATA = cookie['value']
                break
                
        if sessdata:
            print(f"✅ 获取成功！你的 SESSDATA 是：{sessdata}")
            # 保存为 JSON 文件，方便后续 blivedm 读取
            with open("Bilibilicookies.json", "w", encoding="utf-8") as f:
                json.dump(cookies, f, indent=4, ensure_ascii=False)
            print("💾 Cookie 已保存为 Bilibilicookies.json")
        else:
            print("❌ 未能获取 SESSDATA，请确认是否登录成功。")
            
        self.driver.quit()

    @Slot()
    def on_CloseBilibiliLogin(self):
        # 退出浏览器页面
        self.driver.quit()
        # 隐藏当前窗口
        self.hide()
