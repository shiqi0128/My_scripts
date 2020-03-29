# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/27 21:45 
  @Auth : 可优
  @File : lm_08_while_continue_example.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 计算1~100以内，所有奇数之和
# 1. 创建计数器变量
count_var = 1
total = 0

# 2. 创建循环条件
# a. 一旦程序执行到break处, 那么循环会中断
# while count_var <= 100:
#     # 方式一:
#     if count_var % 2 == 1:
#         total += count_var
#         # count_var += 1
#     count_var += 1

while count_var <= 100:
    # a. 如果程序执行到continue处, 那么本次循环会结束, 整个循环不会结束
    # b. 相当于点刹
    # c. 本次循环, continue后面的语句不会被执行
    # 方式二:
    if count_var % 2 == 0:
        count_var += 1
        continue
        print(100)
    total += count_var
    count_var += 1

print(f"count_var = {count_var}\ntotal = {total}")
