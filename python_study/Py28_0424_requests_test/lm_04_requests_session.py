# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/24 20:56 
  @Auth : 可优
  @File : lm_04_requests_session.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
import requests


login_url = "http://api.keyou.site:8000/api/login/?next=/"

login_param = {
    "username": "keyou1",
    "password": "123456"
}


# 1.创建会话对象，就相当于浏览器
# 会自动化维护cookie信息
session = requests.Session()

# 2.使用会话对象去发起请求
one_response = session.post(login_url, data=login_param)

# 3.需要关闭会话
# 仅仅只是对资源进行释放
session.close()
