# import urllib

# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
from lxml import html

# f = urllib.request
# files = {"files": ("1.jpg", open(r"C:\Users\sz\Pictures\1.jpg"), "rb")}
# print(files)

# if __name__ == "__main__":
#     target = "https://www.biqukan.com/1_1094/5403177.html"
#     req = requests.get(url=target)
#     req.encoding = "gbk"
#     html = req.text
#     bh = BeautifulSoup(html)
#     texts = bh.find_all('div', class_='showtxt')
#     print(texts)


# if __name__ == '__main__':
#      target = 'https://unsplash.com/'
#      req = requests.get(url=target)
#      print(req.text)
url = 'https://www.baidu.com/'
data = requests.get(url)
data.encoding = 'utf-8'
# print(data.content)
bs = BeautifulSoup(data.content, "lxml")  # 将网页源码构造成BeautifulSoup对象，方便操作
a_list = bs.find_all("a")  # 获取网页中所有a标签对象
for a in a_list:
    print(a.get("href"))  # 打印a标签对象的href属性，即这个对象指向的链接地址
# print(bs)