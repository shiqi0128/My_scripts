
# selenium

from selenium import webdriver

# Chrome 大写！！
driver = webdriver.Chrome()

# 打开某个网页
url = "http://www.baidu.com"
driver.get(url)

# 获取打开的页面 URL
print(driver.current_url)

# 获取打开的页面的标题
print(driver.title)

# 获取页面的源代码
# print(driver.page_source)

# 浏览器操作:最大化
driver.maximize_window()
# 最小化
driver.minimize_window()
# 设成指定大小
# driver.set_window_size(800, 600)

# 打开豆瓣网站
driver.get('http://www.douban.com')

# 后退
driver.back()

# 前进
driver.forward()

# 刷新
driver.refresh()

# 关闭浏览器
driver.quit()

# 关闭当前的标签页
# driver.close()

# # 元素查找
# # js ==> document.getElementById()
# input_elem = driver.find_element_by_id('kw')
#
# # 往输入框当中输入内容
# input_elem.send_keys('美食剧')
#
# # 定位百度一下
# baidu_button = driver.find_element_by_id('su')
#
# # 点击
# baidu_button.click()

#

