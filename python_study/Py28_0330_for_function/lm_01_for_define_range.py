# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/30 20:21 
  @Auth : 可优
  @File : lm_01_for_define.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# testcase = [1, "登录接口正向用例", "云", "8888", "登录成功", True]
# list_len = len(testcase)

# 0 1 2 3 4 5
# 如果生成连续的索引值呢?
# java中 int i=0; i <= 5 ; i++
# 1. range函数
# 返回的是一个生成器对象(不需要掌握)

# a. 有三个参数: start，stop， step
# start参数： 为记数的起始值， 默认为0
# stop参数:  为记数的结束值(只能取到前一位)
# step参数:  为记数的步长, 默认为1
# b. 如果range函数只有一个参数, 那么这个参数为stop结束值
# one_var = range(6)
# c. 把循环取的过程称为: 遍历
# d. 循环的次数等于range中元素的个数
# for i in range(3):
#     print(f"i = {i}\n类型为: {type(i)}")

# 2. 遍历列表的方式一:
# testcase = [1, "登录接口正向用例", "云", "8888", "登录成功", True]
# list_len = len(testcase)
# range(6)
# 0 1 2 3 4 5
# for i in range(list_len):
#     print(testcase[i])


# 3. 遍历列表的方式二:
# testcase = [1, "登录接口正向用例", "云", "8888", "登录成功", True]
# a. 可以遍历任意一个序列类型(str、list、tuple)、字典
# for one_var in testcase:
#     print(f"值为: {one_var}  类型为: {type(one_var)}")
# 循环的次数等于序列类型元素的个数
for one_var in "abcd":
    print(f"值为: {one_var}  类型为: {type(one_var)}")
