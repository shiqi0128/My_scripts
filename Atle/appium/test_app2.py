# ------此文件为测试的小明计算器的app代码--------
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {}
desired_caps['platformName'] = "Android"         # 声明是ios还是Android系统
desired_caps['platformVersion'] = '6.3.0'        # Android内核版本号，可以在夜神模拟器设置中查看
desired_caps['deviceName'] = '127.0.0.1:62001'   # 连接的设备名称
desired_caps['appPackage'] = 'com.differ.xiaoming_45'    # apk的包名
desired_caps['appActivity'] = 'com.differ.xiaoming.activity.CalcActivity'  # apk的launcherActivity

# appium服务监听地址
server = 'http://localhost:4723/wd/hub'     # localhost为本机；4723为端口；/wd/hub可以看成是规定的默认地址

driver = webdriver.Remote(server, desired_caps)          # 驱动

time.sleep(5)

driver.find_element_by_id("com.differ.xiaoming:id/btn_clear").click()
driver.find_element_by_id("com.differ.xiaoming:id/btn_one").click()
driver.find_element_by_id("com.differ.xiaoming:id/btn_zero").click()
driver.find_element_by_id("com.differ.xiaoming:id/btn_divide").click()
driver.find_element_by_id("com.differ.xiaoming:id/btn_two").click()
driver.find_element_by_id("com.differ.xiaoming:id/btn_equal").click()

driver.quit()      # 退出 session
