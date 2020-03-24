# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/20 20:51 
  @Auth : 可优
  @File : lm_02_str_methods.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# one_user = "KeYou520"
# one_user = "KeYou"

# 字符串.isalpha() 判断该字符串是全部由字母字母
# result = one_user.isalpha()
# print("result:", result)
# print("类型:", type(result))

# isdigit()
# 判断字符串是否全部由数字组成
# one_user = "KeYou520"
# one_user = "520"
# result = one_user.isdigit()
# print("result:", result)
# print("类型:", type(result))

# islower() 判断该字符串是否全为小写
# 这工具(方法/函数)
# one_user = "KeYou"
# one_user = "keyou"
# result = one_user.islower()
# print("result:", result)
# print("类型:", type(result))

# isupper() 判断该字符串是否全为大写
# one_user = "keyou"
# one_user = "KEYOU"
# result = one_user.isupper()
# print("result:", result)
# print("类型:", type(result))


# startswith()
# 是否以给定的字符串开头, 如果是返回True, 否则返回False
# username = "Estelle"
# result = username.startswith("Es")
# print("result: ", result)

# endswith()
# username = "Estelle"
# 是否以给定的字符串结尾, 如果是返回True, 否则返回False
# result = username.endswith("le")
# print("result: ", result)
# print("result: ", username.endswith("le"))

# find()
# a. 获取子字符串在原始字符串中的位置(索引值)
# b. 原始字符串中不包含子字符串, 那么-1
# username = "Python is very best program language!"
# print(username.find("th"))
# print(username.find("it"))

# index()
# a. 获取子字符串在原始字符串中的位置(索引值)
# b. 原始字符串中不包含子字符串, 那么会报错
# username = "Python is very best program language! th th dhoad th"
# print(username.index("th"))
# print(username.index("it"))

# replace()
# username = "Python is very best program language!"
# result = username.replace("Python", "Java")
# print(result)

# lower() 将原始字符串全部改为小写
# info = "Python is very best program language!"
# result = info.lower()

# result = "Python is very best program language!".lower()
# print(result)
# upper()

# strip()
# 清空字符串左右两侧的空格
# info = "     Python is very best program language!       1         "
# result = info.strip()
# print(result)

# 字符串.split("切割符")
# 以给定的分隔符, 来切割原始字符串
# info = "Python is very best program language"
# result = info.split(" ")
# info = "Python-is-very best-program-language"
# result = info.split("-")
# print("result: ", result)
# print("类型: ", type(result))

# 拼接符字符串.join(列表)
# 返回拼接之后的字符串
# one_list = ["KeYou", "is", "very", "handsome!"]
# result = "$".join(one_list)
# print("result: ", result)
# print("类型: ", type(result))

# 判断是否含有某一个子字符串?
# 含有/不含有
# True/False
info = "Python is very best program language"
# result = "Python" in info
# 成员运算符 in 和 not in
# 子字符串 in 原始字符串(判断子字符串是否在原始字符串中)
# result = "Py520" in info
result = "Py520" not in info
print("result: ", result)
print("类型: ", type(result))
