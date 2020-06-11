# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/3 21:37 
  @Auth : 可优
  @File : lm_05_module_from_import.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 方式二:
# from 模块名 import 函数或者全局变量、类
# from lm_02_scope import two_function
# from 模块名 import 函数或者全局变量、类 as 别名
from lm_02_scope import two_function as t_fun


# a. 当前程序中定义的函数与模块中导入的函数同名, 那么模块中的函数会被覆盖
def two_function():
    return "在当前py程序中"


print(two_function())
print(t_fun())
