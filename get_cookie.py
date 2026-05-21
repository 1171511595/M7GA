import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_live_cookie():
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

if __name__ == "__main__":
    get_live_cookie()