"""
-------------------------------------------------
  @Time : 2020/4/3 10:50 
  @Auth : 十七
  @File : homework_0401.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
# 一、必做题
# 1.什么是函数？函数的有什么作用？
# 函数的定义：是将具有独立功能的代码块组织为一个小模块，在需要的时候调用
# 函数的作用：提高编写的效率、代码的重用 让程序更小、模块化
#
# 2.函数有哪几种参数类型，分别有什么特点？
# 1)位置参数：形参与实参一一对应
# 2)默认参数：为参数指定默认值, 将常见的值设置为参数的缺省值，从而简化函数的调用
# 3)关键字参数:为参数指定名称，不会再一一对应, 而是根据关键字参数来传参
# 4)可变参数:
# a.一个函数能够处理的参数个数是不确定的;
# b.参数名前增加一个 * 可以接收元组;
# c.参数名前增加两个 * 可以接收字典

# 3.在函数调用时，位置参数和关键字参数的顺序
# 位置参数在前，关键字参数在后
#
# 4.函数的可变参数是什么？有哪几种？为什么要使用可变参数？
# 一个函数能够处理的参数个数是不确定的，可变参数是指参数的个数是可变的，可变参数传入时，函数会将这些参数转化成tuple或者list来处理
# 1)一个形参前加一个 * 在函数调用时, 传递所有的位置参数被放到一个元组中, 赋值给可变参数
# 2)一个形参前加两个 * 在函数调用时, 传递所有的关键字参数会被放到一个字典中, 赋值给可变参数
#
# 5.编写如下程序
# 输入键盘数字键(0~9)，返回数字键上方字符
#
# a.定义如下字典 num_str_dic = {'1': '!', '2': '@', '3': '#', '4': '$','5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}
# num_str_dic = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}

# b.例如：键盘输入5，程序输出%
# num_list = []
# while True:
#     num = input("请输入0-9以内的数字:")
#     if num.isdigit():
#         num = int(num)
#         if num >=1 and num < 10:
#             for num_one in num_str_dic.values():
#                 num_list.append(num_one)
#             print(f"结果为:{num_list[num-1]}")
#             break
#         else:
#             print("您输入有误，请继续输入...")
#     else:
#         print("您输入有误，请继续输入...")


# c.键盘输入0~9之间的数字，程序正常输出字符之后，退出程序
#
# d.如果输入的内容不在0~9之间，则继续提示输入
#
#
#
# 6.编写如下程序
# 从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
#
# a.定义一个函数，接收用户输入的用户名和密码作为参数

# b.正确的账号，用户名为 lemon，密码为 best
# def login(username, password):
#     if username == "lemon" and password == "best":
#         print("登录系统成功")
#     else:
#         print("用户名或密码错误")
#         return username, password
#
#
# login(username=input("请输入用户名:"), password=input("请输入密码:"))
# 7.编写如下程序
# 求圆的面积
#
# a.传入一个圆的半径，将其面积返回
#
# b.函数中的Π，可以导入import math，通过math.pi来获取（也可以直接使用3.14）

# 定义一个方法来计算圆的面积,圆的面积公式为S= πr²(r为圆的半径)
# def circle_area(r):
#     pi = 3.14
#     area = pi * (r * r)    # 计算出圆的面积S= πr²(r为圆的半径)
#     return area            # 返回面积
#
#
# print("圆的面积为 %.2f" % circle_area(float(input("请输入圆的半径:"))))   # 调用方法,圆的面积保留2位小数



# 二、选作题
# 1.继续完成剪刀石头布游戏
# 提示：
#
# 	a.提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
#
# 	b.电脑随机出拳
#
# 	c.比较胜负，显示用户胜、负还是平局
#
# 	d.使用函数来封装

import random

game_list = ['石头','剪刀','布']
cpu_list = [1, 2, 3]
def player_start():
    while True:
        game = input("请用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）：")
        if game not in game_list:
            print('出拳无效！请重新输入')
        else:
            return game

def cpu_start():
    cpu = random.randint(game_list)
    return cpu

def main():
    print('欢迎来到德莱联盟！')
    round = int(input("请输入游戏回合："))
    won = 0
    tie = 0
    lose = 0
    print('游戏开始！')
    while round > 0:
        chuzhao = player_start()
        com_chuzhao = cpu_start()
        if chuzhao == com_chuzhao:
            print('电脑的出招是：%s' % com_chuzhao)
            print('平局！')
            round -= 1
            tie += 1
        elif chuzhao == chuzhaobiao[0]:
            if com_chuzhao == chuzhaobiao[1]:
                print('电脑的出招是：%s' % com_chuzhao)
                print('你赢了！')
                round -= 1
                won += 1
            elif com_chuzhao == chuzhaobiao[2]:
                print('电脑的出招是：%s' % com_chuzhao)
                print('你输了！')
                round -= 1
                lose += 1
        elif chuzhao == chuzhaobiao[1]:
            if com_chuzhao == chuzhaobiao[0]:
                print('电脑的出招是：%s' % com_chuzhao)
                print('你输了！')
                round -= 1
                lose += 1
            elif com_chuzhao == chuzhaobiao[2]:
                print('电脑的出招是：%s' % com_chuzhao)
                print('你赢了！')
                round -= 1
                won += 1
        elif chuzhao == chuzhaobiao[2]:
            if com_chuzhao == chuzhaobiao[0]:
                print('电脑的出招是：%s' % com_chuzhao)
                print('你赢了！')
                round -= 1
                won += 1
            elif com_chuzhao == chuzhaobiao[1]:
                print('电脑的出招是：%s' % com_chuzhao)
                print('你输了！')
                round -= 1
                lose += 1

    print('游戏结束！结果统计：')
    print('赢：{}, 平：{}, 输：{}'.format(won, tie, lose))

if __name__ == '__main__':
    main()