# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/22 20:28 
  @Auth : 可优
  @File : lm_01_do_json.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
import json

# 一、json数据呈现方式
# 1、字符串形式
# 2、文件
# 3、字节类型（较少）
# 定义json对象
# json格式的数据最好使用单引号括起来
# one_str = '{"name": "日月", "age": 17, "gender": true, "hobby": null}'
# one_str = "{\"name\": \"日月\", \"age\": 17, \"gender\": true, \"hobby\": null}"

# 定义json数组
two_str = '[{"name": "日月", "age": 17, "gender": true, "hobby": null}, {"name": "船长", "age": 18, "gender": false, "hobby": ["跑步", "敲打码"]}]'

# a、使用json.loads方法，将json字符串转化为python中的字典或者列表
# b、loads将json字符串作为joads方法的第一个参数
# one_dict = json.loads(one_str)
one_dict = json.loads(two_str)
pass
