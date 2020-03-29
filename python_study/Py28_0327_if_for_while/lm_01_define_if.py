# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/27 20:17 
  @Auth : 可优
  @File : lm_01_define_if.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""

age = int(input("请输入您的年龄: "))

# 条件运算只有两种结果
if age >= 18:  # 如果if条件为True(真), 那么if下面的语句才会被执行, 如果为False, 那么不会执行
    # 缩进一致第地方, 叫做同一个块(块语句)
    # 往往缩进的是一个tab(应为4个字符)
    print("欢迎光临! 请愉快玩耍!")
    print(100)

print("继续执行!")
