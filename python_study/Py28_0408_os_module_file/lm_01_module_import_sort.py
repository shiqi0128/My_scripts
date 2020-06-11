# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/3 21:54 
  @Auth : 可优
  @File : lm_01_module_import_sort.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 1. 先导入系统模块
# a. 搜索当前目录指定模块名的文件，如果有就直接导入
# b. 如果没有，再搜索系统目录
# 在python安装目录lib下, 是系统提供模块
# c. 如果系统目录下也没有的话, 那么会报错ModuleNotFoundError
# from random import randint
# from random100 import randint

# print(randint(1, 10))
# print(520)

import sys

# 可以使用sys.path获取模块搜索路径, 值为列表
one_var = sys.path
print(one_var)
pass
