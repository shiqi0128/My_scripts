# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/30 20:46 
  @Auth : 可优
  @File : lm_02_for_dict.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
one_dict = {"id": 1, "title": "登录接口正向用例", "username": "云", "password": "8888",
            "expected": "登录成功", "is_excuted": True}

# 1. 如果直接遍历字典, 那么遍历的是key
# for item in one_dict:
# for item in one_dict.keys():
#     print(f"值为: {item}  类型为: {type(item)}")
#
# for item in one_dict.values():
#     print(f"值为: {item}  类型为: {type(item)}")

# 2. 拆包
# a. 可以对任意一个序列类型进行拆包(解包)
# b. 将序列类型中的每一个元素取出来, 然后一一赋值
# one_list = [10, 20, "abc"]
# one_var, two_var, three_var = one_list

# 3. one_dict.items() 相当于一个嵌套元组的列表
# for key, value in one_dict.items():
#     print(key, "->", value)

# 4. for 和 while循环的区别?
# a. while循环的次数往往不明确(不明显)
# b. for循环的次数往往是明确的, 次数等于序列类型元素的个数或者range元素的个数
# c. 如果能用for, 尽量就不用while, for的性能更高
