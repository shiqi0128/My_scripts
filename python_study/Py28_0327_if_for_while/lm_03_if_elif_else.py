# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/27 20:36 
  @Auth : 可优
  @File : lm_03_if_elif_else.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
age = int(input("请输入您的年龄: "))

# 条件运算只有两种结果
# 1. 如果if条件成立, 那么会执行if下面的块语句, 而不会执行else下面的块语句
# 2. 如果if条件不成立, 那么不会执行if下面的块语句, 而会执行else下面的块语句
# 3. 如果elif条件成立, 那么只会执行elif下面的块语句
# 4. 如果if和elif条件都都不成立, 那么会执行else块语句
if age >= 70:  # 如果if条件为True(真), 那么if下面的语句才会被执行, 如果为False, 那么不会执行
    print("请回家锻炼身体再来!")
    print(300)
elif age >= 18:
    print("欢迎光临! 请愉快玩耍!")
    print(100)
else:
    print("您未成年, 请回家做作业吧!")
    print(200)

print("继续执行!")
