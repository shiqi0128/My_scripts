# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/3 21:51 
  @Auth : 可优
  @File : lm_07_module_more_time_import.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 如果同时多次导入相同的模块, 那么只有第一次导入成功
from lm_02_scope import one_function
from lm_02_scope import one_function
from lm_02_scope import one_function


print(one_function(520))
