# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/10 20:45 
  @Auth : 可优
  @File : lm_03_exception_define.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# num = int(input("请输入一个整数: "))
#
# # 如果前面抛出异常, 那么下面的程序就不会被执行, 程序会中断
# if num == 1:
#     print("Yes")
# else:
#     print("No")

try:
    # a. 如果try块语句, 没有抛出异常, 那么try的块语句会执行完(往下执行), except块语句不会执行
    # b. 如果try块语句中, 有一行抛出异常, 那么try的块语句下一行不会执行, 但except块语句会执行
    # num = int(input("请输入一个整数: "))
    num = input("请输入一个整数: ")
    num = int(num)
    print("这里会执行吗? ")
except:
    print("您输入了非整数, 请重新输入!")
    print("此处需要日志器来记录日志")

if num == 1:
    print("Yes")
else:
    print("No")
