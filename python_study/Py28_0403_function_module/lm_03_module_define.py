# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/3 20:46 
  @Auth : 可优
  @File : lm_03_module_define.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# py文件名, 当作模块名
# 可以将同级目录下的模块导入
# 方式一:
# 直接忽略
import lm_02_scope
# 模块名.函数名
result = lm_02_scope.one_function(100)
print(f"result: {result}")


# 方式二:
# 不推荐
# import Py28_0403_function_module.lm_02_scope


# 模块名.函数名
# result = Py28_0403_function_module.lm_02_scope.one_function(100)
# print(f"result: {result}")
