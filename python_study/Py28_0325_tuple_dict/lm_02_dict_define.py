# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/25 20:50 
  @Auth : 可优
  @File : lm_02_dict_define.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# testcase = [1, "登录接口正向用例", "云", "8888", "登录成功", True]
# 创建字典类型
# 方式一: {}
# one_dict = {"id": 1, "title": "登录接口正向用例", "username": "云", "password": "8888",
#             "expected": "登录成功", "is_excuted": True}

# 方式二: dict()
# one_dict = dict(id=1, title="登录接口正向用例")

# 创建空字典
one_dict = {}
print(f"值为: {one_dict}\n类型为: {type(one_dict)}")
