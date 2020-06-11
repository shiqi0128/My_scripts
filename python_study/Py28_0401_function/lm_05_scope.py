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
# a. 在函数体外部称为全局作用域
# b. 在函数体外部定义的变量称为全局变量
# c. 在函数内部定义的变量称为局部变量
# d. 在函数内部称为局部作用域
username = "词不搭调"
age = 18


# 案例一:
# def one_funtion(one_var):
#     print(username)
#     return one_var
#
#
# result = one_funtion(100)


# 案例二:
def one_funtion(one_var):
    # a. 在函数体内部, 定义的变量为局部变量
    # b. 只要在函数体内部, 有赋值(看到等号), 哪怕与全局变量同名, 定义的变量为局部变量
    # c. 局部变量往往跟全局变量没关联
    # username = "just you"
    # age = one_var
    # print(f"函数内部: username为{username}")
    # return one_var

    # 获取变量的值, 是有优秀级的
    # 1. 首先在函数内部找, 有没有定义此变量
    # 2. 如果有, 那么优先使用
    # 3. 如果没有, 会去全局查找

    # 想要在函数体内部, 修改全局变量?
    print(f"函数内部: username为{username}")
    # username = "just you"
    age = one_var
    return one_var


result = one_funtion(100)
print(f"函数外部: username为{username}")
