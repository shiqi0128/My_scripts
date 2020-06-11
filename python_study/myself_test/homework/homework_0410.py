"""
-------------------------------------------------
  @Time : 2020/4/12 15:46 
  @Auth : 十七
  @File : homework_0410.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
# 一、必做题
# 1. 打开文件的方式有哪些？
# 1)open():以mode=r、r+、w、w+、a+
# 2)使用with方法打开
# 1)第一种，直接输入f = open('your_file.txt','r')
# 2)第二种，输入f = open('your_file.txt', 'r', encoding='utf-8')
# 3)第三种，使用with方法打开
# 2.编写如下程序
# 将你喜欢的一首歌（音乐文件拓展名为mp3，比如刘德华忘情水.mp3），通过文件读写的方法将其复制并修改文件名
# with open("大壮 - 我们不一样.mp3", mode="rb") as one_file, open("十七-我们不一样.mp3", mode="wb") as two_file:
#     result = one_file.read()
#     two_file.write(result)

# 3.什么是异常？为什么要捕获异常？
# 异常就是程序执行过程中发生的错误
# （1）保证程序的健壮性,代码经得起各种情况的摧残
# （2）如果前面抛出异常, 那么下面的程序就不会被执行, 程序会中断,大部分异常不会被处理，所有需要捕获对异常进行处理
# 4.异常的完整语法格式
# try:
#  	# 尝试执行的代码
#  	pass
#  except 错误类型:
#  	#针对错误类型，对应的代码处理
#  except Except as e:   # e 是一个变量，用于记录错误类型
#  	print("未知错误", e)
#  else:
#  	# 没有异常才会执行的代码
#  	pass
#  finally:
#  	# 无论是否有异常都会执行的代码
#  	pass
# 5.在异常中，try关键字下的块语句、except下的块语句、else下的块语句、finally下的块语句执行逻辑是什么？
# try下面的块语句出现异常的时候捕获异常
# except捕获到异常根据块语句进行异常处理
# else 没有异常才会执行的语句
# finally无论是否有异常都会执行的代码
# 6.编写如下程序
# 优化去生鲜超市买橘子程序
# a.收银员输入橘子的价格，单位：元／斤
# b.收银员输入用户购买橘子的重量，单位：斤
# c.计算并且输出付款金额
# 新需求：
# d.使用捕获异常的方式，来处理用户输入无效数据的情况


def orange_total():
    """定义一个统计橘子输入单价和重量的函数"""
    while True:
        price = input("请输入橘子的价格（元）:")
        try:
            price = float(price)
            break
        except:
            print("价格输入有误，请重新输入")
    while True:
        weight = input("请输入橘子的重量（kg）:")
        try:
            weight = float(weight)
            break
        except:
            print("重量输入有误，请重新输入")
    total = price * weight
    print(f"橘子的单价为{price},橘子的重量为{weight}, 橘子的总价为{total}")


if __name__ == '__main__':
    orange_total()

# def orange_total():
#     """定义一个计算付款金额的函数"""
#     price, weight = orange_input()
#     try:
#         total = price * weight            # 总价=单价*数量
#         print(f"应付款金额为{total}")
#     except:
#         print("不能与0相乘")
#
#
# def orange_zero():
#     """定义一个输入0的函数"""
#     price, weight = orange_input()
#     if price == 0 or weight == 0:





if __name__ == '__main__':
    orange_total()

# 7.使用思维导图总结最近几次课的知识点


# 二、选做题
# 1.编写如下程序（Python测试开发入学考试题）
# 优化剪刀石头布游戏程序
#
# a.提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
#
# b.电脑随机出拳
#
# c.比较胜负，显示用户胜、负还是平局
#
# 新需求：
#
# d.使用捕获异常的方式，来处理用户输入无效数据的情况
#
# e.多次进行游戏，可以让用户选择退出游戏，退出后需要显示胜利情况，例如：用户5局胜、3局败、2局平
#
# f.当程序结束之后，要求下一次运行程序能够获取用户历史胜负情况（思考：游戏对战胜负历史记录保存在哪里呢？）

# with open("胜负的结果.txt", "w", encoding="utf-8") as f2:
#     import random
#     c = ['石头', '剪刀', '布']
#
#
#     def z(a):
#         e = 1
#         while True:
#             b = random.randint(0, 2)
#             try:
#                 d = input("请输入要出的拳：")
#                 a = int(a)
#                 d = int(d)
#             except ValueError:
#                 if type(a) != int:
#                     print(f"您输入的{a}不是数字")
#                 elif type(d) != int:
#                     print(f"您输入的{d}不是数字")
#                 else:
#                     print(f"您输入的{a}和{b}都不是数字")
#             else:
#                 if d == b:
#                     print(f"用户出{c[d]},电脑出{c[b]},平局")
#                     f2.write("1\t")
#                 elif a < b or (a == 2 and b == 0):
#                     print(f"用户出{c[d]},电脑出{c[b]},用户胜")
#                     f2.write("2\t")
#                 elif d < 0 or d > 2:
#                     print("输入有误,请重新输入")
#                     continue
#                 else:
#                     print(f"用户出{c[d]},电脑出{c[b]},用户负")
#                     f2.write("3\t")
#             if e == a:
#                 print("次数用完了,退出游戏")
#                 break
#             e += 1
#     z(a=int(input("请输入您要玩的次数：")))
# f2.close()
#
# # 下一次运行程序能够获取用户历史胜负情况:
# with open("胜负的结果.txt", "r", encoding="utf-8") as f1:
#     ai = f1.read()
#     bi = ai.strip(',').split('\t')
#     qi = 0
#     wi = 0
#     ei = 0
#     for i in bi:
#         if i == "1":
#             qi += 1
#         elif i == "2":
#             wi += 1
#         elif i == "3":
#             ei += 1
#     print(f"用户{wi}局胜、{ei}局败、{qi}局平")
# f1.close()