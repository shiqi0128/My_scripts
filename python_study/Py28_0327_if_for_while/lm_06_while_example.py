# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/27 21:32 
  @Auth : 可优
  @File : lm_06_while_example.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 计算 0 ~ 100 之间所有数字的累计求和结果
# 1. 创建计数器变量
count_var = 0
total = 0

# 2. 创建循环条件
while count_var <= 100:
    # total = total + count_var
    total += count_var
    # 3. 修改循环条件
    count_var += 1

print(f"count_var = {count_var}\ntotal = {total}")
