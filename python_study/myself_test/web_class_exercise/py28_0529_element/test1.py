"""
-------------------------------------------------
  @Time : 2020/6/3 12:25 
  @Auth : 十七
  @File : test1.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://voice.baidu.com/act/newpneumonia/newpneumonia/")
driver.maximize_window()

# 元素一  百度首页
input_ele = driver.find_element("xpath", '//a[contains(text(), "百度首页")]')
input_ele.click()
# 元素二 切换地区
input_ele2 = driver.find_element("xpath", '//span[contains(text(), "切换地区")]')
input_ele2.click()
# 元素三 现有确诊
input_ele3 = driver.find_element("xpath", "//span[contains(@class, 'VirusSummarySix_1-1-265_yJu0av')]")
input_ele3.click()
# 元素四 消息通知
input_ele4 = driver.find_element("xpath", "//div[contains(@class, 'VirusSummarySix_1-1-265_szVrQM')]")
input_ele4.click()

driver.quit()