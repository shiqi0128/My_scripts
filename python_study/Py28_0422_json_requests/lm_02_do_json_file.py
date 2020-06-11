# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/22 20:43 
  @Auth : 可优
  @File : lm_02_do_json_file.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
import json

with open("users.json", encoding="utf-8") as file:
    one_dict = json.load(file)
    pass
