# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/24 21:22 
  @Auth : 可优
  @File : lm_05_do_request.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
import json

import requests


class HandleRequest:

    def __init__(self):
        # 创建会话对象
        self.session = requests.Session()

    def send(self, method, url, **kwargs):
        """
        发送请求的方法
        :param method: 请求方法
        :param url: 请求url
        :param kwargs: headers请求头字典, data、json、files
        :return:
        """

        # if method == "POST":
        #     self.session.post()
        # elif method == "GET":
        #     self.session.get()
        # else:
        #     pass
        one_method = method.upper()
        res = self.session.request(one_method, url, **kwargs)
        return res

    def add_headers(self, one_dict):
        """
        添加公共的请求头
        :param one_dict: 请求头参数，字典类型
        :return:
        """
        self.session.headers.update(one_dict)
        # self.session.headers = one_dict

    def close(self):
        """
        释放资源
        :return:
        """
        self.session.close()


if __name__ == '__main__':
    # 1.创建HandleRequest对象
    do_request = HandleRequest()
    # 2.创建登录url
    login_url = "http://api.lemonban.com/futureloan/member/login"

    # 3.构造请求头参数
    headers_dict = {
        "X-Lemonban-Media-Type": "lemonban.v2",
        "User-Agent": "Mozilla/5.0 LookSky"
    }
    # 4.在会话对象中添加请求头
    do_request.add_headers(headers_dict)

    # 5.构造登录参数
    login_param = {
        "mobile_phone": "18511112222",
        "pwd": "12345678"
    }

    # login_param = '{"mobile_phone": "18511112222", "pwd": "12345678"}'

    # 6.先登录接口发起请求
    # res = do_request.send("POST", login_url, headers=headers_dict, json=login_param)
    res = do_request.send("POST", login_url, json=login_param)

    # 7.获取登录接口响应体数据，转化为字典类型
    response_data_dict = res.json()
    # 获取token
    token = response_data_dict['data']['token_info']['token']
    # 获取user_id
    user_id = response_data_dict['data']['id']

    # 8.把token加载到请求头中
    token_dict = {
        "Authorization": f"Bearer {token}"
    }
    do_request.add_headers(token_dict)

    # 9.再充值
    # 创建充值url
    recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
    # 构造充值请求参数
    recharge_param = {
        "member_id": user_id,
        "amount": "100"
    }

    # recharge_headers_dict = {
    #     "X-Lemonban-Media-Type": "lemonban.v2",
    #     "User-Agent": "Mozilla/5.0 LookSky",
    #     "Authorization": f"Bearer {token}"
    # }

    # 10.对充值接口发起请求
    # recharge_res = do_request.send("Post", recharge_url, headers=recharge_headers_dict, json=recharge_param)
    recharge_res = do_request.send("Post", recharge_url, json=recharge_param)

    # 11.创建获取用户信息的url
    user_url = f"http://api.lemonban.com/futureloan/member/{user_id}/info"
    # 12.先用户用户信息的接口发起请求
    user_res = do_request.send("GET", user_url)
    # Response对象中，可以通过headers属性获取响应头信息， 相当于一个字典
    # Response对象中，可以通过request.headers属性获取请求头信息， 相当于一个字典
    pass
