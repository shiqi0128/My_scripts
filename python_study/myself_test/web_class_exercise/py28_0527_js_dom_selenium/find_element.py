"""
-------------------------------------------------
  @Time : 2020/5/29 19:26 
  @Auth : 十七
  @File : find_element.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
from selenium import webdriver

driver = webdriver.Chrome()         # 谷歌驱动
driver.get("https://www.baidu.com/")   # 打开百度网页
print(driver.current_url)     # 获取打开网页的url
print(driver.title)           # 获取打开页面的标题
print(driver.page_source)     # 获取页面的源代码
driver.maximize_window()      # 页面最大化
driver.minimize_window()      # 页面最小化
driver.set_window_size(800, 600)    # 设成指定大小
driver.back()           # 后退
driver.forward()        # 前进
driver.refresh()        # 刷新

# driver.close()          # 关闭当前标签
input_ele = driver.find_element_by_id("kw")
input_ele.send_keys("美食")
baidu_botton = driver.find_element_by_id("su").click()   # 点击百度一下按钮。
driver.quit()           # 关闭浏览器（所有的）
