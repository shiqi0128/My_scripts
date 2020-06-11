"""
-------------------------------------------------
  @Time : 2020/5/22 18:12 
  @Auth : 十七
  @File : interview_01.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""

# 1、print(sum(range(1, 101)))

# a = 5
#
#
# 2、def func():
#     global a
#     a = 4
#
# func()
# print(a)

# 3、python的5个标准库
# 1）os,提供了不少与操作系统相关联的函数
# 2）sys,通常用于命令行参数
# 3）re,正则匹配
# 4）math,数学运算
# 5）datetime,处理日期时间

# 4、字典如何删除键和合并两个字典
one_dict = {"name": "lily", "age": "18"}
# two_dict = one_dict.keys()
# del one_dict["name"]
# print(one_dict)
two_dict = {"hobby": "dancing"}
one_dict.update(two_dict)
print(one_dict)