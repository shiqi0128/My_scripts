# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/18 21:22 
  @Auth : 可优
  @File : lm_03_logical_operator.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# and 一假必假，两真才为真
# True and False
# result = (1 > 0) and (12 >= 30)
# False and True
# result = (1 <= 0) and (12 < 30)
# True and True
# result = (1 >= 0) and (12 < 30)
# print(result)

# or 一真必真，两假才为假
# True or False
# result = (1 > 0) or (12 >= 30)

# False or True
# result = (1 <= 0) or (12 < 30)

# False or False
# result = (1 < 0) or (12 >= 30)
# print(result)

# not 以假乱真，真亦假，假亦真
# not False
# result = not (1 < 0)
# result = not (1 > 0)
# print(result)


# 赋值运算
# 1. 计算等号右边的值
# 2. 然后把计算的值赋值给一个变量
# 3. 等号的左侧, 只能为变量名, 而不能为表达式
# name = "KeYou"
# name * 2 = "lucky"

one_num = 12
two_num = 2

# print(one_num + two_num)
# 1. 12 + 2 结果为 14
# 2. two_num = 14
# two_num = one_num + two_num
# print(two_num)
# print(one_num)

# two_num = one_num + two_num
two_num += one_num
print(two_num)

print(10 * 2 + 30 - 2 * 3 - 32 / 2)
print((10 * 2)+ 30 - (2 * 3) - (32 / 2))
