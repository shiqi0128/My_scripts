# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/25 20:19 
  @Auth : 可优
  @File : lm_01_tuple_operate.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 元组: 是一个不可修改的列表
# testcase = [1, "登录接口正向用例", "云", "8888", "登录成功", True]
# testcase_tuple = (1, "登录接口正向用例", "云", "8888", "登录成功", True)
# 1. 通过数字索引取值
# print(testcase_tuple[3])
# 2. 切片
# 3. len()函数获取长度
# 4. in 成员运算符
# print(1 in testcase_tuple)

# 5. 不可以修改元组中元素
# a. 相比list列表, 元组性能更高(取值操作)
# b. 可以作为字典的key
# testcase_tuple[3] = "9999"
# print(testcase_tuple)

# c. 元组中尽量不要存放可变类型的数据
# testcase_tuple = (1, "登录接口正向用例", "云", "8888", "登录成功", True, [10, 20, True])
# print(testcase_tuple)

# index
# testcase_tuple = (1, "登录接口正向用例", "云", "8888", "登录成功", True, 1, 20, "8888", 1)
# print(testcase_tuple.index(1))
# print(testcase_tuple.index("8888"))

# count
# True: 1
# False: 0
# testcase_tuple = (1, "登录接口正向用例", "云", "8888", "登录成功", True, 1, 20, "8888", 1)
# print(testcase_tuple.count("8888"))

# 使用list()函数将元组转化为列表
# 使用tuple()函数将列表转化为元组
testcase_tuple = (1, "登录接口正向用例", "云", "8888", "登录成功", True, 1, 20, "8888", 1)
# testcase_list = [1, "登录接口正向用例", "云", "8888", "登录成功", True, 1, 20, "8888", 1]
# result = tuple(testcase_list)
# print(f"值为: {tuple(testcase_list)}\n类型为: {type(tuple(testcase_list))}")
# print(f"值为: {result}\n类型为: {type(result)}")


# str、list、tuple
# 序列类型: 一串数据合并在一起
one_list = [10, 20, "LookSky", True]
two_list = [30, False, "NK", True]

# 两个序列类型相加, 相当于是合并操作
# extend
result = one_list + two_list
print(f"值为: {result}\n类型为: {type(result)}")
