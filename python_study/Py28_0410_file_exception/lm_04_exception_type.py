# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/10 20:59 
  @Auth : 可优
  @File : lm_04_exception_type.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
try:
    # a. 如果try块语句, 没有抛出异常, 那么try的块语句会执行完(往下执行), except块语句不会执行
    # b. 如果try块语句中, 有一行抛出异常, 那么try的块语句下一行不会执行, 但except块语句会执行
    # c. 可以使用except 异常类, 来捕获特定的异常, 捕获了之后, 其他的异常块就不会执行
    # d. expect可以接收(捕获)所有的异常
    # num = int(input("请输入一个整数: "))
    num = input("请输入一个整数: ")
    num = int(num)
    result = 10 / num
    print("这里会执行吗? ")
except ValueError:
    print(f"您输入{num}是一个非整数, 请重新输入!")
except ZeroDivisionError:
    print(f"您输入{num}是一个0, 请重新输入!")
except:
    print("您输入了非整数, 请重新输入!")
    print("此处需要日志器来记录日志")

if num == 1:
    print("Yes")
else:
    print("No")
