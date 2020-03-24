# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/18 21:42 
  @Auth : 可优
  @File : lm_04_str.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# - 可以使用 **一对双引号** `"` 或者 **一对单引号** `'` 定义一个字符串
username = "Young Boy"
username1 = """
Young Boy
dhsdodhos
hsoshod
"""
# user_name = 'Young Boy'
# user_name1 = '''Young Boy'''
# print(username)
# print(type(username))
# print(user_name)
# print(type(user_name))

# - 如果字符串中含有单引号或者双引号呢？
# a. 可以使用\来转义
# user_name = 'I\'am Young Boy'
# user_name = "I'am Young Boy"
# print(user_name)
# print(type(user_name))

# 获取指定位置的字符
# a. 支持索引取值
language = "Python"
# b. 通过索引取值: 字符串[索引值]
# result = language[0]
# result = language[2]
# result = language[5]
# print(result)
# print(type(result))

# c. 获取字符串的长度
# len函数来获取字符串的长度
# d. 最大的索引值为长度 - 1
# index = len(language)
# result = language[index - 1]
# print(result)
# print(type(result))

# e. 负值索引
# result = language[-1]
result = language[-6]
print(result)
print(type(result))
print(len(result))
