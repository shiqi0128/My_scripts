# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/17 20:14 
  @Auth : 可优
  @File : lm_01_enumerate.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
one_list = ["那天，微笑", "词不搭调", "tanhi"]

# i = 1
# for item in one_list:
#     print(f"{i}. {item}")
#     i += 1

# 1、可以使用enumerate函数，在遍历时，可以携带数字索引
# 2、第一个参数为可迭代对象（序列类型、字典、集合、生成器等）
# 3、默认从0开始迭代，第二个参数为起始索引
for i, item in enumerate(one_list, 1):
    print(f"{i}. {item}")

