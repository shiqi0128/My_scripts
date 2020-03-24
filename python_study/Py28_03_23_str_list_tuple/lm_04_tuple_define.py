# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/23 21:50 
  @Auth : 可优
  @File : lm_04_tuple_define.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 定义元组(tuple)
# 方式一:
# a. 使用括号来创建
# one_tuple = ("小白", "橙子", 20, True, None)
# b. 创建空元素
# one_tuple = ()
# one_tuple = (10)
# c. 创建只有一个元素的元组
# one_tuple = (10, )
# print(f"值为:{one_tuple} 类型:{type(one_tuple)}")

# 方式二:
# one_tuple = "小白", "橙子", 20, True, None
# one_tuple = 10,
# print(f"值为:{one_tuple} 类型:{type(one_tuple)}")

# 方式三:
# one_tuple = tuple([10, 20, 30])
one_tuple = tuple("abc")
print(f"值为:{one_tuple} 类型:{type(one_tuple)}")
