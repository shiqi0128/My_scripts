# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/22 20:48 
  @Auth : 可优
  @File : lm_03_dict_list_to_json.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
import json

one_dict = {
    'name': "小明",
    "age": 18,
    17: True,
    None: 1.3
}

# 使用json.dumps方法，将python中的数据类型（字典、列表）转化为json字符串
# 宕机
# dj
json_str = json.dumps(one_dict, ensure_ascii=False)
pass
