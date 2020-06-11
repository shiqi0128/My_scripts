# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/3 21:21 
  @Auth : 可优
  @File : lm_04_module_import.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# - 标示符可以由 **字母**、**下划线** 和 **数字** 组成
# from Py28_0403_function_module.1test

# - 不能以数字开头
# - 不能与关键字重名
# - 不能与系统内置的模块、函数、类重名
# - 建议不要以下划线开头
# - 建议不要使用中文

# 变量 = "皮卡丘"
# print(变量)

# 方式一:
# import 模块名
# import lm_01_function, lm_02_scope, lm_03_module_define
#
# import lm_01_function
# import lm_02_scope
# import lm_03_module_define
# 在导入一个模块时, 会执行模块中没有缩进的语句
import lm_02_scope

print(lm_02_scope.one_function(520))
print(lm_02_scope.two_function())

