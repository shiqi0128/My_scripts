# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/23 21:24 
  @Auth : 可优
  @File : lm_03_list_operate2.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 列表是可变类型
# testcase = [1, "登录接口正向用例", "云", "8888", "登录成功", True]
# testcase = [1, "登录接口正向用例", "云", "8888", "登录成功", True, "8888", "8888"]

# 修改列表元素
# a. 直接修改
# testcase[1] = "登录接口"
# print(f"值为: {testcase}\t类型: {type(testcase)}")

# b. insert()
# 第一个参数为索引值(待添加的位置索引)
# 第二个参数为待添加的元素
# result = testcase.insert(2, 88.8)
# testcase.insert(2, None)
# testcase.insert(2, False)
# print(result)
# print(f"值为: {testcase}\t类型: {type(testcase)}")

# c. append()
# 在列表尾部追加一个元素
# 将元素作为一个整理
# one_list = ["小妖", "520", 1314]
# testcase.append("LookSky")
# testcase.append(one_list)
# print(f"值为: {testcase}\t类型: {type(testcase)}")

# d. extend()
# 将序列类型(字符串、列表、元祖)，取出来之后, 添加到列表中
# one_list = ["小妖", "520", 1314]
# testcase.extend("LookSky")
# testcase.extend(one_list)
# print(f"值为: {testcase}\t类型: {type(testcase)}")

# 删除元素
# a. pop() 或者pop(索引)
# 删掉列表中最后一个元素, 并返回
#
# result = testcase.pop()
# result = testcase.pop(-3)
# print(f"值为: {result}\t类型: {type(result)}")
# print(f"值为: {testcase}\t类型: {type(testcase)}")

# b. remove(数据)
# 直接删掉列表中的指定元素
# result = testcase.remove("8888")
# result = testcase.remove("88881")
# print(f"值为: {result}\t类型: {type(result)}")
# print(f"值为: {testcase}\t类型: {type(testcase)}")

# 其他操作
# a. count()
# result = testcase.count("8888")
# print(f"值为: {result}\t类型: {type(result)}")
# print(f"值为: {testcase}\t类型: {type(testcase)}")

# b. index()
# c. sort() 或者 sort(reverse=True)
# testcase = [10, 20, 11, 2, 30]
# testcase.sort()
# testcase.sort(reverse=True)
# print(f"值为: {testcase}\t类型: {type(testcase)}")

# d. reverse()
testcase = [10, 20, 11, 2, 30]
# testcase.sort()
testcase.reverse()
print(f"值为: {testcase}\t类型: {type(testcase)}")
