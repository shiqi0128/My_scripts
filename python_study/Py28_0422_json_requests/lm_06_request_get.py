# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/22 21:25 
  @Auth : 可优
  @File : lm_06_request_get.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# requests第三方模块，来发起请求
# 0、导入requests
import requests


# 1、构造参数
# 可以使用url后添加？来传递查询字符串参数
# url = "http://api.lemonban.com/futureloan/loans?pageIndex=2&pageSize=2"
url = "http://api.lemonban.com/futureloan/loans"

headers_dict = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "User-Agent": "Mozilla/5.0 LookSky"
}

params_dict = {
    "pageIndex": 2,
    "pageSize": 2
}

# a、requests.get方法， 发起get请求，会返回一个Response对象，相当于一个报文
# b、第一个参数url
# c、给headers传递的是请求头参数，需要构造一个字典
# d、Response对象中的status_code属性，获取响应的状态码
# e、Response对象中的text属性，获取响应报文的字符串类型数据
# f、Response对象中的content属性，获取响应报文的字节类型数据
# g、Response对象中的json()，获取json转化为字典之后响应数据

# 给params传参，传递的是查询字符串参数，需要构造一个字典
res = requests.get(url, headers=headers_dict, params=params_dict)
pass

