# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/24 20:10 
  @Auth : 可优
  @File : lm_01_post_request.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
import json

import requests

# 1、构造参数
# 可以使用url后添加？来传递查询字符串参数
# url = "http://api.lemonban.com/futureloan/loans?pageIndex=2&pageSize=2"
url = "http://api.lemonban.com/futureloan/member/register"

headers_dict = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "User-Agent": "Mozilla/5.0 LookSky",
    "Content-Type": "application/json"
}

params_dict = {
    "pageIndex": 2,
    "pageSize": 2
}

request_param = {
    "mobile_phone": "18511112222",
    "pwd": "12345678"
}

request_param_json = json.dumps(request_param)
# a、requests.post方法， 发起post请求，会返回一个Response对象，相当于一个报文
# b、第一个参数url
# c、给headers传递的是请求头参数，需要构造一个字典
# d、Response对象中的status_code属性，获取响应的状态码
# e、Response对象中的text属性，获取响应报文的字符串类型数据
# f、Response对象中的content属性，获取响应报文的字节类型数据
# g、Response对象中的json()，获取json转化为字典之后响应数据

# 给params传参，传递的是查询字符串参数，需要构造一个字典
# 给data传参，传递的是x-www-form参数，需要构造一个字典
# 给json传参，传递的是json参数，需要构造一个字典
# res = requests.post(url, data=request_param, headers=headers_dict)
# res = requests.post(url, json=request_param, headers=headers_dict, params=params_dict)
res = requests.post(url, json=request_param_json, headers=headers_dict)
pass
