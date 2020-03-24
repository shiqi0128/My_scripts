# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/23 20:30 
  @Auth : 可优
  @File : lm_01_str_format.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# src = "我的名字是: "
# username = "孙庆庆"
# age = 18

# print(src + username + " 年龄是: " + age)
# str函数将任意的数据类型转化为字符串
# print(src + username + " 年龄是: " + str(age))

# 方式一:
# username = "孙庆庆"
# age = 18
# f字符串表达式
# a. 需要在字符串前面添加f
# b. 可以在字符串中间使用{}, 花括号的中间可以写任何表达式(或变量)
# c. python3.6+
# info = f"我的名字是: {username}\t年龄是: {age}"
# info = f"我的名字是: { username[:-1] }\t年龄是: {age + 1}"
# print(info)


# 方式二:
# 使用format方法进行格式化
# a. {}为占位符, format方法中的参数进行一一对应
# b. 往往花括号的数量与format方法中的参数个数一致
# c. {}花括号中可以填写format方法参数的索引值
# username = "孙庆庆"
# age = 18
# info = "我的名字是: {} 我的年龄是: {}\t我的分数为:{}".format(username, age, 88)
# info = "我的名字是: {2} 我的年龄是: {1}\t我的分数为:{0}".format(username, age, 88)
# print(info)


# 方式三:
# python2中推荐方式
username = "孙庆庆"
age = 18
info = "我的名字是: %s 我的年龄是: %s\t我的分数为:%s" % (username, age, 88)
print(info)
