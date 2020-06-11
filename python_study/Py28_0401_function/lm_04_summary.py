# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/1 21:24 
  @Auth : 可优
  @File : lm_04_summary.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 在函数定义时:
# a. def
# b. 参数统称为形参
# c. 位置参数
# d. 默认参数
# e. 可变参数(*args、**kwargs)
# f. 所有的可变参数, 尽量放在最后面


# 在函数调用时:
# a. 函数名()
# b. 参数统称为实参
# c. 位置参数
# d. 关键字参数


# def num_count(*args, **kwargs):
#     result = 0
#     for item in args:
#         # result = result + item
#         result += item
#
#     for value in kwargs.values():
#         result += value
#
#     print(result)
#     return None


# 用户传递的数字个数不确定
# 怎样传参也不确定
# a. 一个函数如果没有指明返回值的话, 那么默认会返回None
# one_var = num_count(10, 20, 10, 11, one=2.1, two=3, three=4)


def num_count(*args, **kwargs):
    result = 0
    # return 1
    for item in args:
        # result = result + item
        result += item

    for value in kwargs.values():
        result += value

    print(result)
    # b. 可以使用return关键字, 将一个数据返回, 会被函数调用处接收
    # return result
    # c. 如果要返回多个值, 那么多个值之间使用逗号分隔, 返回的是元组类型
    return result, item
    # d. 函数体内, return语句执行之后, 函数执行就结束, return后面的语句都不会执行
    # c = 10 + 20
    # print(c)





# one_var = num_count(10, 20, 10, 11, one=2.1, two=3, three=4)
# print(num_count(10, 20, 10, 11, one=2.1, two=3, three=4))
one_var = num_count(10, 20, 10, 11, one=2.1, two=3, three=4)
pass
