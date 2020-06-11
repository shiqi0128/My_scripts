# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/1 20:41 
  @Auth : 可优
  @File : lm_03_variable_param.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""


# 可变参数
# a. 在一个形参前面添加一个*
# b. 在函数调用时, 传递所有的位置参数被放到一个元组中, 赋值给可变参数
# def send_request(*param):
# def send_request(*param, time, count):
#
# 在一个形参前面添加两个*
# a. 在函数调用时, 传递所有的关键字参数会被放到一个字典中, 赋值给可变参数
# def send_request(*param, **kwparam):
# b. *args, **kwargs, 这样定义会更加规范
def send_request(*args, **kwargs):
    # 两个*的可变参数要放在一个*可变参数的后面
    # def send_request(**kwparam, *param):
    """
    :param title:
    :param method:
    :param url:
    :param is_excuted:
    :return:
    """
    # print(f"获取请求方法: {param[1]}")
    # print(f"获取URL: {param[2]}")
    # print("是否执行用例: ", param[-1])
    # print(f"现在对{param[0]}发起请求...")
    print(f"值为: {args}\n类型: {type(args)}")


# send_request("登录接口正向用例", "GET", "http://www.lemon.com", False)
# send_request("登录接口正向用例", "GET")
# send_request()
# send_request("登录接口正向用例", "GET", "http://www.lemon.com", False, 100, 200, [10, 20])

# send_request("登录接口正向用例", "GET", "http://www.lemon.com", False, 100, 200, [10, 20], time="now", count=5)
# send_request("登录接口正向用例", "GET", "http://www.lemon.com", False, 100, 200, [10, 20], time="now")  # 会报错
# send_request("登录接口正向用例", "GET", "http://www.lemon.com", False, 100, 200, [10, 20], "now", 5)  # 会报错
# send_request("登录接口正向用例", "GET", "http://www.lemon.com", False, 100, 200, [10, 20], time="now", count=5, weight=10)
# send_request("登录接口正向用例", "GET", "http://www.lemon.com", False, 100, 200, [10, 20], time="now")  # 不会报错
# send_request("登录接口正向用例", "GET", "http://www.lemon.com", False, 100, 200, [10, 20])
send_request()
