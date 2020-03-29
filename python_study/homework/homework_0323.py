# """
# -------------------------------------------------
#   @Time : 2020/3/24 20:33
#   @Auth : 十七
#   @File : homework_0323.py
#   @IDE  : PyCharm
#   @Motto: ABC(Always Be Coding)
#   @Email: 1941816343@qq.com
# -------------------------------------------------
# """
# # 一、必做题
# # 1.列表中append和extend方法的区别，请举例说明
# # append 是指在列表尾部增加一个元素
# name_list = ["Bob", "Lily", "Lucy"]
# name_list.append("Amy")
# print(f"append输出结果为:{name_list}")
# # extend 是指将序列类型(字符串、列表、元祖)，取出来之后, 添加到列表中
name_list = ["Bob", "Lily", "Lucy"]
name_list.extend("Star")
print(f"expend输出结果为:{name_list}")
# # 2.编写代码，用户输入1-7七个数字，分别代表周一到周日，如果输入的数字是6或7，打印输出“周末”
# # 提示：
#
# # 	可以使用已学知识来完成，例如：列表（["周一", "周二", ...]）
# weekend = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
# while True:
#     day = int(input("请输入1-7中的任意数字,输入0退出:"))
#     if day == 6 or day == 7:
#         print("周末")
#     elif day in range(1, 6):
#         print("工作日")
#     elif day == 0:
#         break
#
#
# # 3.删除如下列表中的"矮穷丑"，写出能想到的所有方法
# # 第一种，使用pop指定下标
# keyou_info = ["可优", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]
# keyou_info.pop(3)
# print("使用pop指定下标删除:", keyou_info)
# # 第二种，使用remove指定下标
# keyou_info = ["可优", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]
# keyou_info.pop(3)
# print("使用remove指定下标删除:", keyou_info)
# # 第三种，使用del，del还能删除指定范围
# keyou_info = ["可优", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]
# del keyou_info[3]
# print("使用del删除:", keyou_info)
#
# # 4.元组和列表有什么区别？
# # list是一种有序的集合，可以随时添加、修改和删除其中的元素；列表使用方括号[]
# # tuple一旦初始化就不能修改,可以获取元素但不能删除,而且没有append() insert()pop()这些方法;元组使用小括号()
#
# # 5.请使用思维导图总结上次课和本次课的学习内容
# # 百度脑图的地址：
# "https://naotu.baidu.com/file/621cfa4ee243579da2fe347467b93679"
