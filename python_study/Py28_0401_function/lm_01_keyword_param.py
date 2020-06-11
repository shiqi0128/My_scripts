# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/1 20:14 
  @Auth : 可优
  @File : lm_01_keyword_param.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""


def send_request(title, method, url, is_excuted):
    """
    :param title:
    :param method:
    :param url:
    :param is_excuted:
    :return:
    """
    print(f"获取请求方法: {method}")
    print(f"获取URL: {url}")
    print("是否执行用例: ", is_excuted)
    print(f"现在对{title}发起请求...")


# 关键字参数(可以不用一一对应)
# a. 形参名=实参
# b. 不会再一一对应, 而是根据关键字参数来传参
# send_request(method="GET", url="http://www.lemon.com", is_excuted=True, title="登录接口正向用例")
# send_request("登录接口正向用例", "GET", url="http://www.lemon.com", is_excuted=True)
# send_request("登录接口正向用例", "GET", is_excuted=True, url="http://www.lemon.com")
# c. 位置参数一定要放在关键字参数前面
# 会报错
# send_request(is_excuted=True, "登录接口正向用例", "GET", url="http://www.lemon.com")
