# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/22 20:53 
  @Auth : 可优
  @File : lm_04_dict_list_to_json_file.py
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

# a、使用json.dump方法， 将python中的数据类型（字典、列表）转化为json文件
# b、dump方法，第一个参数为待写入的对象，第二个参数为文件对象
with open("users_write.json", "w", encoding="utf-8") as file:
    json.dump(one_dict, file, ensure_ascii=False, indent=2)
