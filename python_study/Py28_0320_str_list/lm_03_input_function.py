# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/20 21:48 
  @Auth : 可优
  @File : lm_03_input_function.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 1. 接收用户从键盘中输入的内容
# 2. input第一个参数为提示信息, 往往是字符串类型
# 3. 用户输入的任何内容，都会被当作一个字符串
username = input("请输入您的用户名: ")
# age = input("请输入您的年龄: ")

age = input("请输入您的年龄: ")

score = input("请输入您的分数: ")
score = float(score)
# 1. int()函数可以将一个数字类型的字符串("120", "520"), 转化为int类型(120, 520)
# 2. 如果字符串中有非数字, 那么会报错
age = int(age)
print(username)
print(type(username))

print("age: ", age)
print("类型: ", type(age))

print("score: ", score)
print("类型: ", type(score))

