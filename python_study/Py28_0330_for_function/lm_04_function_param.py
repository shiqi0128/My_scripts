# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/30 21:43 
  @Auth : 可优
  @File : lm_04_function_param.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""


# def send_request():
#     print("获取请求方法: GET")
#     print("获取URL: http://www.lemon.com")
#     print("是否执行用例: ", True)
#     print("现在发起请求...")


# 1. 在函数定义时, 括号中添加的变量名:
#   形式参数(形参)
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


# 2. 在函数调用处, 括号中添加的变量值:
#   实际参数(实参)
#   往往参数是一一对应的, 实参会赋值给形参数

# 3. 一一对应的参数成为位置参数
send_request("登录接口正向用例", "GET", "http://www.lemon.com", True)
