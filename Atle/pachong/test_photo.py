# coding=utf-8

import requests
from bs4 import BeautifulSoup

url = 'http://www.mzitu.com'

# 设置headers，网站会根据这个判断你的浏览器及操作系统，很多网站没有此信息将拒绝你访问
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

# 用get方法打开url并发送headers
html = requests.get(url, headers=header)

soup = BeautifulSoup(html.text, 'html.parser')

# 最大页数在span标签中的第10个
pic_max = soup.find_all('span')[10].text
print(pic_max)

# 输出每个图片页面的地址
for i in range(1, int(pic_max) + 1):
    href = url + '/' + str(i)
    print(href)

