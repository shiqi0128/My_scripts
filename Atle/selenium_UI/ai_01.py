from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 导入键盘事件
import time
import random
from selenium.webdriver.common.action_chains import ActionChains  # 导入鼠标事件


# def GBK2312():
#     head = random.randint(0xb0, 0xf7)
#     body = random.randint(0xa1, 0xf9)   # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
#     val = f'{head:x}{body:x}'
#     str = bytes.fromhex(val).decode('gb2312')
#     return str

driver = webdriver.Firefox()         # 重启浏览器
chain = ActionChains(driver)

# 携程旅行网
driver.get("https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index")   # 打开浏览器
driver.maximize_window()
time.sleep(1)

# 点击请登录按钮
driver.find_element_by_class_name("set-text").click()
time.sleep(1)
# 输入账号密码
driver.find_element_by_class_name("r_input").send_keys("18717752237")
driver.find_element_by_id("npwd").send_keys("119920128shiqi")
time.sleep(1)
# 定位鼠标的原位置
a = driver.find_element_by_class_name("cpt-logo cpt-img-double-right")
# driver.find_element_by_xpath("//input[@value='Log in']").click()
ActionChains(driver).drag_and_drop()

time.sleep(2)
# driver.close()
