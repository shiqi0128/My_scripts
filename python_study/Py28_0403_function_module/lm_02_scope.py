# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/1 21:48 
  @Auth : 可优
  @File : lm_05_scope.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""

username = "词不搭调"
age = 18


# 案例二:
def one_function(one_var):
    # 可以使用global关键字来声明, 全局变量
    global username
    username = "新世纪"
    print(f"函数内部: username为{username}")
    return one_var


def two_function():
    print("乌托邦")
    return age


# result = one_function(100)
# print(f"函数外部: username为{username}")
print("lm_02_scopy.py模块执行结束")
