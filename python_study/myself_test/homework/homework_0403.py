"""
-------------------------------------------------
  @Time : 2020/4/5 13:17 
  @Auth : 十七
  @File : homework_0403.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
# *
# **
# ***
# ****
# *****
# 方式一：
# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1
# for i in range(1, 6):
#     print("*" * i)
#     i += 1

# 方式二while：
# i = 1    # i是行数
# while i <= 5:
#     j = 1  # j是列数
#     while j <= i:
#         print("*", end="")
#         j += 1
#     print()
#     i += 1

# 方式三for：
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(j, "*", i, "=", i*j, "\t", end="")
#     print()

# 一、必做题
# 1.函数默认返回什么值? 返回值有哪些形式? 在函数体中, return会中断循环吗?
# 1）默认返回None
# 2）返回值有4种形式：
# a)def test1():
#     print("in the test1")#无返回值
# b)def test2():
#     print("in the test2")#返回0
#     return 0
# c)def test3():
#     print("in the test3")#返回参数
#     return 'test3'
# d)def test4():
#     print("in the test4")#返回函数
#     return test2()
# 3）在函数体中, return会中断循环，循坏体内return后面的语句不会再执行

# 2.局部变量和全局变量是什么? 如何在函数内部修改全局变量?
# 局部变量：就是在函数内部定义的变量
# 全局变量：顶着头开始写，没有任何缩进，在py文件的任何位置都能调用,全局作用域是全局
# 可以在函数内部使用global关键字来声明, 全局变量
# 3.局部变量的搜索顺序?
# 变量调用的顺序是先找局部作用域，如果找不到，再往外层找，然后在找全局作用域
#
# 4.什么是模块？有什么作用？
# 模块的定义：python中，模块是后缀名为.py的文件，包含Python定义和语句的文件
# 模块的作用：
# 1）模块可以被其他程序调用，让你能够有逻辑地组织你的 Python 代码段。
# 2）把相关的代码分配到一个模块里能让你的代码更好用，更易懂。
# 3）模块能定义函数，类和变量，模块里也能包含可执行的代码
# 5.模块中的哪些资源可以被调用处使用？
# 函数、类
#
# 6.模块的命名规范
# - 不能以数字开头
# - 不能与关键字重名
# - 不能与系统内置的模块、函数、类重名
# - 建议不要以下划线开头
# - 建议不要使用中文
#
# 7.模块的导入方式有哪几种？
# 1)import 模块名1， 模块名2
# 2)from 模块名1 import 函数、全局变量或者类
# 3)from 模块 import *  导入模块中的所有函数、类、全局变量
# 8.编写如下程序
# 从键盘获取一个数字，然后计算它的阶乘，例如输入的是3，那么即计算3!的结果，并输出
#
# 提示：
#
# 	a. 1!等于 1        1*1=1
#
# 	b. 2!等于 1*2      1*2=2
#
# 	c. 3!等于 1*2*3     2*3=6
#                      6*4=24
#                      24*5=120
#                      120*6=720
#                      720*7=5040
# 	d. n!等于 1*2*3*...*n
# while True:
#     factorial = 1
#     num = input("请输入一个不是负数的数字:")
#     # if num.isdigit():
#     num = int(num)
#     if num < 0:
#         print(f"{num}！没有阶乘")
#     elif num == 0:
#         print(f"{num}！= 1")
#     else:
#         for n in range(1, num+1):
#             factorial = factorial * n
#         print(f"{num}! = {factorial}")
#     else:
#         print("您输入的不是一个数字!")


# 9.编写如下程序
# a.在一个模块中，定义求圆的面积和周长、长方形的面积和周长的函数，然后分别在另一个程序中调用
# 1) import 模块名
# import homework_0403a
#
# homework_0403a.curcle(5)
# homework_0403a.rectangle(1, 2)
# # b.使用多种方式导入模块
# # 2) from 模块名 import 函数或者全局变量、类
# from homework_0403a import curcle, rectangle
# curcle(5)
# rectangle(1, 2)
# # 3) from 模块 import *
# from homework_0403a import *
# curcle(5)
# rectangle(1, 2)

# 10.将两个变量的值进行交换（a = 100, b = 200）
# a.交换之后，a = 200， b = 100
#
# b.使用你能想到的所有方法来实现
# 第一种,字典索引取值
# num = {"a": 100, "b": 200}
# num["a"] = 200
# num["b"] = 100
# print(f"第一种交换后：a={num['a']}, b={num['b']}")
# # 第二种,默认函数，调用函数重新赋值
# def num(a=100, b=200):
#     print(f"第二种交换后：a={a}, b={b}")
#
#
# num(a=200, b=100)
# # 第三种
# a, b = 100, 200
# a, b = b, a
# print(f"第三种交换后：a={a}, b={b}")
# # 第四种
# a = 100
# b = 200
# t = a
# a = b
# b = t
# print(f"第四种交换后：a={a}, b={b}")
# # 第五种
# a = 100
# b = 200
# a = a + b
# b = a - b
# a = a - b
# print(f"第五种交换后：a={a}, b={b}")
# 11.编写如下程序
# 将用户输入的所有数字相乘之后对20取余数
#
# a.用户输入的数字个数不确定
#
# b.用户输入的每个数字之间以逗号分隔（可以使用字符串的split方法），例如：10,1,2,13,20
#
# c.请使用函数来实现
#
# d.分割为列表之后，将列表拆包传给函数
def num(*args):
    num = 1
    for item in args:
        num *= item
    print(f"计算结果:{num % 20}")    # 将用户输入的所有数字相乘之后对20取余数


new_list = []
nat_num = input("请输入一个数字,以逗号分隔:")
if nat_num != 0:
    n_list = nat_num.split(",")   # 将用户输入的所有数字使用逗号进行分割后存入列表
    print(f"n_list:{n_list}")
    for i in n_list:
        new_list.append(int(i))
else:
    print("0与任何数相乘都为0")

num(*new_list)     # 调用函数，将列表拆包


# def num_count(*args):
#     """
#     将用户输入的所有数字相乘之后对20取余数
#     :param args:
#     :return:
#     """
#     num = 1
#     for value in args:
#         num *= value
#     print("计算结果为：{}".format(num % 20))
#
# # 方法一：
# num = input("请输入需要计算的数字（以逗号分隔）: ")
# list_num = num.split(",")        # 将用户输入的所有数字使用逗号进行分割
# new_list_num = []
# for item in list_num:
#     new_list_num.append(int(item))
# num_count(*new_list_num)



# def mutil_num(*args):
#     """
#     接收传入的参数是打包的元组：意思就是调用函数mutil_num(1,2,3,4) 就是装包(1,2,3,4)
#     利用for循环进行迭代乘积*=
#     最后对乘积进行%20取余处理
#     :param args:
#     :return:
#     """
#     count = 1
#     for i in args:
#         count *= i
#     print("用户输入数字的乘积：{}".format(count))
#     rem_num = count % 20
#     print("数字的乘积取余数为：{}".format(rem_num))
#
#
# def split_num(nat_num):
#     """
#     这个是对用户input录入的数据进行拆分
#     拆分的list再次迭代将0元素剔除后再组成new_list
#     因为再return返回new_list，因为mutil_num函数是*args接收参数，实质是一个元组类型
#     不在return中转换，而在调用的时候转换,考虑其他程序的调用
#     tips:list(str)可以将字符串的单个元素拆分转换成list
#     :param nat_num:
#     :return:
#     """
#     list_num = nat_num.split(',')
#     new_list = []
#     for item in list_num:
#         if item == '0':
#             list_num.remove(item)
#         else:
#             new_list.append(int(item))
#     return new_list
#
#
# # 自定义用户录入数据
# nat_num = input("请用户输入任意数字用逗号隔开，进行乘积之后对20取余数(0除外)：")
#
# # 调用函数把return回来的数据转换成tuple类型，*args可接收的类型
# tuple_result = tuple(split_num(nat_num))
#
# # 调用的mutil_num函数*args动态参数接收的类型是一个打包好的元组类型的数据
# # 实参会被打包成一个元组给*args接收，那就是传入的元组再会被打包成元组((1,2,3,4),)，这样程序内部处理逻辑会报错，tuple不能直接做算术运算
# # 因此在函数调用时传入一个元组时，需要解包，在元组类型的变量前加一个*星号与函数对应：解包，
# mutil_num(tuple_result)
# # print(*tuple_result) # 解包元组打印出各个元素



# 12.使用思维导图总结前面几次课的内容


# 二、选作题
# 1.编写如下程序
# 裴伯拉切数列，从第三个元素开始，每个元素为前两个元素之和，用户输入某个大于0的正整数，求出小于等于这个正整数的所有裴伯拉切元素
#
# a.裴伯拉切数列为：0  1  1  2  3  5  8  13  21  34  55  89  144  ...
#
# b.例如，用户输入50，那么小于等于50的裴伯拉切元素为：0  1  1  2  3  5  8  13  21  34
#
# c.要求在一个模块中定义，在另一个程序中调用

