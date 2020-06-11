# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/3 21:47 
  @Auth : 可优
  @File : lm_06_module_from_import.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# from lm_02_scope import one_function, two_function, username, age
# 方式三:
# 导入模块中的所有函数、类、全局变量
# from 模块 import *
# 不推荐
from lm_02_scope import *

username = "向日葵"

print(one_function(520))
print(two_function())
print(username)
print(age)
