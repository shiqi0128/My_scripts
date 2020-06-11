# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/27 21:57 
  @Auth : 可优
  @File : lm_09_workhome.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# *
# **
# ***
# ****
# *****

# 方式一:
# row = 1
# while row <= 5:
#     print("*" * row)
#     row += 1

# 方式二:
# row = 1
# while row <= 5:
#     column = 1
#     while column <= row:
#         # a. print函数中, end默认为\n换行符, 执行一次print打印之后, 默认会换行
#         # b. 将换行符覆盖
#         print("*", end="")
#         column += 1
#     print()
#     row += 1

# 方式三
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j, "*", i, "=", i * j, "\t", end="")
#     print()



























# *
# **
# ***
# ****
# *****
# 方式1
# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1

# 方式2
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("*", end="")
#         j += 1
#     print()
#     i += 1

# 方式三
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, "*", i, "=", i*j, "\n", end="")
    print()





