# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/25 20:57 
  @Auth : 可优
  @File : lm_03_dict_operate.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# one_dict = {"id": 1, "title": "登录接口正向用例", "username": "云", "password": "8888",
#             "expected": "登录成功", "is_excuted": True}

# 获取字典中的某个值
# 方式一: 字典[key]
# 如果key不存在会报错
# result = one_dict["title1"]

# 方式二: 字典.get(key)
# 如果key不存在会返回None
# 如果key不存在会, 同时有添加第二个参数, 那么会返回第二个参数
# result = one_dict.get("is_excuted100", True)
# print(f"值为: {result}\n类型为: {type(result)}")

# 1. 不可变类型: int、float、str、bool、tuple、None
# 2. 可变类型： list、dict
# 3. 字典的key, 只能为不可变类型
# 4. 字典的value, 没有任何限制
# one_dict = {"id": 1, "title": "登录接口正向用例", "username": "云", "password": "8888",
#             "expected": "登录成功", "is_excuted": True, 10: 10, 10.2: None}

# 5. 字典中不可以有相同的key, 如果key重复, 那么后面的key会把前面的覆盖掉
one_dict = {"id": 1, "title": "登录接口正向用例", "username": "云", "password": "8888",
            "expected": "登录成功", "is_excuted": True, 10: 10, 10.2: None, (10, 20, "abc"): "Estelle", "id": 20}
print(f"值为: {one_dict}\n类型为: {type(one_dict)}")