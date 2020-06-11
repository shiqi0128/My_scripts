# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/3 20:21 
  @Auth : 可优
  @File : lm_01_function.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""


def send_request(*args, **kwargs):
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


# one_var = ("登录接口正向用例", "GET", "http://www.lemon.com", False)
one_var = ["登录接口正向用例", "GET", "http://www.lemon.com", False]

# send_request("登录接口正向用例", "GET", "http://www.lemon.com", False)
# 装箱/装包
# send_request(one_var, 100)
# send_request("登录接口正向用例", "GET", "http://www.lemon.com", False, 100)
# 拆包
# 任意的序列类型都支持拆包
# 在函数调用时, 可以在一个序列类型变量的前面加一个*, 可以拆成多个位置参数
# send_request(*one_var, 100)

one_dict = {"method": "GET", "url": "http://www.lemon.com",
            "is_excuted": True, "title": "登录接口正向用例"}

# send_request(method="GET", url="http://www.lemon.com", is_excuted=True, title="登录接口正向用例")
# 在函数调用时, 可以在一个字典类型变量的前面加两个*, 可以拆成多个关键字参数
send_request(**one_dict)

