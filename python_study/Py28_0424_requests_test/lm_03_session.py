# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/24 20:44 
  @Auth : 可优
  @File : lm_03_session.py
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

res = requests.post(login_url, data=login_param)
pass
