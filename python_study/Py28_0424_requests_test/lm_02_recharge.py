# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/24 20:28 
  @Auth : 可优
  @File : lm_02_recharge.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
import requests

# 一、先登录
login_url = "http://api.lemonban.com/futureloan/member/login"

headers_dict = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "User-Agent": "Mozilla/5.0 LookSky",
    # "Content-Type": "application/json"
}

login_param = {
    "mobile_phone": "18511112222",
    "pwd": "12345678"
}

res = requests.post(login_url, json=login_param, headers=headers_dict)
response_data_dict = res.json()

token = response_data_dict['data']['token_info']['token']
user_id = response_data_dict['data']['id']

# 二、再充值
recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
recharge_param = {
    "member_id": user_id,
    "amount": "100"
}

recharge_headers_dict = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "User-Agent": "Mozilla/5.0 LookSky",
    "Authorization": f"Bearer {token}"
}

recharge_res = requests.post(recharge_url, json=recharge_param, headers=recharge_headers_dict)
pass
