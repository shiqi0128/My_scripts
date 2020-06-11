# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/5/13 21:46 
  @Auth : 可优
  @File : lm_01_mock_define.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 一、哪些场景下会用到mock呢？
# 1、第三方接口
# a.别人的接口
# b.在测试阶段，可能无法调用

# 2、开发未完成的接口
# a.一个业务流需要依赖未完成的接口才能测
# b.有必要使用假数据（接口）来辅助测试

from unittest import mock

import requests


def alipay():
    """
    此函数类比为支付宝的支付接口（在测试阶段不能访问）
    当前不能调用的支付宝的接口
    :return:
    """
    # url乱写的，模拟不能访问的场景
    res = requests.get("http://sddhosd.lemon/shoshsohsd")

    return res.status_code


def do_pay(card_num, password):
    """
    类比为开发写的支付流程接口，需要调用第三方支付宝接口
    :param card_num:
    :param password:
    :return:
    """
    print("1、验证账号信息成功")
    print("2、调用支付宝接口进行支付")
    return alipay()


if __name__ == '__main__':
    # do_pay("1000", "123456")
    one_dict = {
        "code": "10001",
        "msg": "支付成功"
    }

    # a.创建一个Mock对象，将第三方支付函数覆盖
    # b.do_pay函数调用alipay函数时，不会真正去调用支付宝的接口，而是直接返回我们指定的返回值（return_value）
    alipay = mock.Mock(return_value=one_dict)
    result = do_pay("1000", "123456")
    print(result)

