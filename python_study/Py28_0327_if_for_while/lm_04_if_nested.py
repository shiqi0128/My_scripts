# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/27 20:46 
  @Auth : 可优
  @File : lm_04_if_nested.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 1. 定义布尔型变量 `has_ticket` 表示是否有车票
has_ticket = True

# 2. 定义整型变量 `knife_length` 表示刀的长度，单位：厘米
knife_length = 23.1

# 3. 首先检查是否有车票，如果有，才允许进行 **安检**
if has_ticket:
    print("您可以去安检了, 安检门在前面!")
    # 4. 安检时，需要检查刀的长度，判断是否超过 20 厘米
    #    如果超过 20 厘米，提示刀的长度，不允许上车
    #    如果不超过 20 厘米，安检通过
    if knife_length > 20:
        print("刀具没收! 请寄送!")
    else:
        print("欢迎光临!")
else:
    # 5. 如果没有车票，不允许进门
    print("购票大厅在门口!")


