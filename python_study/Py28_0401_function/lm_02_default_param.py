# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/1 20:28 
  @Auth : 可优
  @File : lm_02_default_param.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""


# 默认参数
# a. 函数定义时, 形参=值, 添加的是默认参数
# b. 如果函数调用时, 不传参数, 那么当前默认参数会使用默认值
# c. 如果函数调用时, 传参数, 那么当前默认参数不会使用默认值, 会使用当前的实参
def send_request(title, method, url, is_excuted=True):
    # d. 非默认参数(位置参数)要放在默认参数的前面
    # 会报错
    # def send_request(title, is_excuted=True, method, url):
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


# send_request("登录接口正向用例", "GET", "http://www.lemon.com")
# send_request("登录接口正向用例", "GET", "http://www.lemon.com", False)
# 不会报错
# send_request("登录接口正向用例", "GET", "http://www.lemon.com", is_excuted=False)
# 会报错
# send_request("登录接口正向用例", method="GET", "http://www.lemon.com", is_excuted=False)
# 不会报错
send_request("登录接口正向用例", method="GET", url="http://www.lemon.com", is_excuted=False)
