
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

# 启动浏览器
# driver = webdriver.Chrome()

# 指定浏览器驱动的版本和路径
# 谷歌浏览器的选项


driver = webdriver.Chrome(executable_path=r'D:\chromedriver\chromedriver_71.exe')

# 打开网页
driver.get("http://www.baidu.com")
# 最大化
driver.maximize_window()

# 元素定位先行
# 代表的就是一个网页的标签对象 WebELement
input_elem = driver.find_element_by_id('kw')
print(input_elem)

# print(input_elem.id) # 不是元素的 ID 属性，（唯一标识）
print(input_elem.tag_name)
print(input_elem.size)
# text 文本
print(input_elem.text)
# 属性 name, class_name, href
# print(input_elem.name)

# 获取属性的值
print(input_elem.get_attribute('name'))

# 对元素进行操作
input_elem.send_keys('meishiju')

