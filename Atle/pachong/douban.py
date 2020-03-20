# from bs4 import BeautifulSoup
# from lxml import html
# import xml
# import requests
#
#
# def func():
#     url = "https://movie.douban.com/chart"
#     r = requests.get(url)
#     # print(r.text)
#     soup = BeautifulSoup(r.text, "lxml")
#
#     # for k in soup.find_all('div', class_='p12'):
#     # for k in soup.find_all('div', class_='p12'):
#     for k in soup.find_all('div', class_='pl2'):
#     # for k in soup.find_all('div', class_='p12'):
#         print(k)
#         # a = k.find_all('span')
#         # print(a)
#         # print(a[0].string)
#
#
# func()


# from bs4 import BeautifulSoup
# from lxml import html
# import xml
# import requests
#
# url = "https://movie.douban.com/chart"
# f = requests.get(url)
# soup = BeautifulSoup(f.text, "lxml")
#
#
# for k in soup.find_all('div', class_='pl2'):
#     a = k.find_all('span')
#     print(a)
#     print(a[0].string)

import urllib.request  # 引入urllib库

response = urllib.request.urlopen("https://tieba.baidu.com/index.html")  # 发出请求并且接收返回文本对象
html = response.read()   # 调用read()进行读取
print(html)  # 打印
