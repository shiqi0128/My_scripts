# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/20 20:24 
  @Auth : 可优
  @File : lm_01_define_str_slice.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
src_str = "Monty Python"

# 字符串[开始索引:结束索引:步长]
# result = src_str[0:1]
# print("result:", result)
# print("类型: ", type(result))

# a. 指定的区间属于 左闭右开型 [开始索引,  结束索引)
# 从起始位开始，到结束位的前一位结束（不包含结束位本身)
# result = src_str[0:2]
# result = src_str[3:8]
# b. 要么都是用正向索引, 要么都是用逆序索引
# result = src_str[-9:-4]
# c. 如果切片时, 索引值可以超过字符串的长度, 结束索引为字符串的长度
# result = src_str[-6:-1]
# print("result:", result)
# print("类型: ", type(result))

# d. 从头开始，开始索引的数字0可以省略，冒号不能省略
# 如果切到末尾, 那么末尾的索引也可以省略
# result = src_str[0:5]
# result = src_str[:5]
# print("result:", result)
# print("类型: ", type(result))

# 到末尾结束，结束索引的数字-1可以省略，冒号不能省略
# result = src_str[-6:]
# print("result:", result)
# print("类型: ", type(result))

# e. 步长默认为 `1`，如果连续切片，数字和冒号都可以省略
# result = src_str[0:5]
# result = src_str[0:5:1]
# result = src_str[0:12:3]
result = src_str[::3]
print("result:", result)
print("类型: ", type(result))
