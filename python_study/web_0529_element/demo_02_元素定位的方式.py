from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'D:\chromedriver\chromedriver_71.exe')
driver.get("http://www.baidu.com")

# 第一种：ID


# find_elements 找到符合要求的所有的运算，存到列表当中。
# 如果找不到元素, find_elements 得到的是空列表

# es = driver.find_elements_by_name('wdjfofsof')
# print(es)
#
# # 第二种：name
# # find_element... 只会找符合属性的第一个元素
# # 找不到元素，会报错：NoSuchElementException
# e = driver.find_element_by_name('wdjfofsof')
# print(e)


# 第三种：class_name
# e = driver.find_element_by_class_name('s_ipt')

# TODO: 坑：当 class_name 出现空格的时候, 需要把空格去掉，只能用其中的一个 class
e = driver.find_element_by_class_name('s_ipt_wr')

# 第四种：tag_name 有，但是在自动化测试很少使用。

# 第五种：通过 link_text， 主要用来定位超链接<a>， 通过连接的文本, 其他的标签不支持
# 第六种：通过 partial_link_text， 一部分文本定位， 输入的参数被包含在 text 文本当中
# e = driver.find_element_by_link_text('新')

# 这个叫做通用的元素定位方式
e = driver.find_element("id", "kw")
e = driver.find_element("name", "wd")
e = driver.find_element("class name", "s_ipt")

# 类属性的表示方式
e = driver.find_element(By.ID, "kw")


# 第七种：xpath
e = driver.find_element('xpath', '//a[contains(text(), "频")]')
# 第八种：css_selector