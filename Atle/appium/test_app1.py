#-------------此文件为爱它乐app移动端接口自动化脚本--------
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {}
desired_caps['platformName'] = "Android"         # 声明是ios还是Android系统
desired_caps['platformVersion'] = '6.5.0'        # Android内核版本号，可以在夜神模拟器设置中查看
desired_caps['deviceName'] = '127.0.0.1:62001'   # 连接的设备名称
desired_caps['appPackage'] = 'com.aiitle.app'    # apk的包名
desired_caps['appActivity'] = 'io.dcloud.PandoraEntry'  # apk的launcherActivity

# appium服务监听地址
# server = 'http://localhost:4723/wd/hub'     # localhost为本机；4723为端口；/wd/hub可以看成是规定的默认地址
server = 'http://127.0.0.1:4723/wd/hub'
driver = webdriver.Remote(server, desired_caps)          # 驱动

time.sleep(10)
# ----------登录（非首次）----------
# driver.find_element_by_name("手机号码登录").click()
mbl = 'new UiSelector().text("手机号码登录")'
driver.find_element_by_android_uiautomator(mbl).click()  # 点击选择登录方式页面的手机号码登录
time.sleep(3)
driver.find_element_by_android_uiautomator('new UiSelector().text("手机密码登录")').click()   # 点击选择手机密码登录方式
time.sleep(3)
# 点击输入手机号码的文本框，输入手机号码
driver.find_element_by_android_uiautomator('new UiSelector().text("请输入手机号码")').send_keys("18717752237")
time.sleep(3)
# 点击输入手机号码的文本框，输入手机号码
driver.find_element_by_android_uiautomator('new UiSelector().text("请输入密码")').send_keys("121212")
time.sleep(3)
# 通过class定位登录按钮,需要用复数形式，因为有多个元素，返回的是列表
elements = driver.find_elements_by_class_name("android.widget.Button")[1]
elements.click()
time.sleep(5)

# -----------我的----------------
elements = driver.find_element_by_class_name("android.widget.RelativeLayout")[3] # 定位到[我的]模块
driver.find_element_by_android_uiautomator('new UiSelector().text("添加宠物")').click()   # 点击添加宠物

elements.click()
driver.quit()      # 退出 session
