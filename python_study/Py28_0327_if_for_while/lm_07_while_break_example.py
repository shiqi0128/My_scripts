# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/27 21:37 
  @Auth : 可优
  @File : lm_07_while_break_example.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 计算1~100以内，前23个数字之和
# 计算1~100以内，从第24个开始, 就结束循环
# 1. 创建计数器变量
count_var = 1
total = 0

# 2. 创建循环条件
# a. 一旦程序执行到break处, 那么循环会中断
# b. break后面的语句都不会被执行
while count_var <= 100:
    if count_var == 24:
        break
        print("100")
    total += count_var
    count_var += 1

print(f"count_var = {count_var}\ntotal = {total}")
