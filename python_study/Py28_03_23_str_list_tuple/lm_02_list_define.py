# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/23 20:53 
  @Auth : 可优
  @File : lm_02_list_define.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 1. 定义
# 方式一:
# 用例编号、用例名称、用户名、密码、期望值、是否要执行
# a. 使用[]来定义, 每一个元素之间使用逗号分隔, 这种类型的数据, 就叫做列表
# b. 往往元素与元素之间, 逗号后面加一个空格
testcase = [1, "登录接口正向用例", "云", "8888", "登录成功", True]
# \t 为制表符
# \n 为换行符
print(f"testcase: {testcase}\n类型: {type(testcase)}")

# 方式二:
# list()
