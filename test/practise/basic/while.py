# current_number = 1
# while current_number <= 6:
#    print(current_number)
#    current_number += 1

# a = "Tell me something,and I will repeat it back to you: "
# a += "\nEnter 'quit' to end the program. "

# a = True
# while a:
#     message = input(a)

#     if message == 'quit':
#         a = False
#     else:
#         print(message)

# i = 1
# sum = 0
# while i <= 100:
#     if i % 2 == 0:
#         sum += i
#     else:
#         pass
#     i += 1
# print("从1到100的和为：%s" % sum)

# 打印矩形
# x = 1
# y = 1

# while y <= 10:       # 为了输出10行
#     x = 1
#     while x <= 10:     # 为了在一行中输出10个*
#         print("*", end="")  # 函数默认在输出之后就换行，如果不换行，输出help(print)
#         x += 1
#     print("")
#     y += 1
# print("已经完成")

# help(print)

# 打印99乘法表
# x = 1  # 代表行数

# while x <= 9:  # 一共要循坏9次还能打印9行，每行打印的列数和行号一样
#     y = 1 # 代表列数
#     while y <= x:
#         print("%d*%d=%d\t" % (y, x, x*y), end="")
#         y += 1
#     print("")
#     x += 1
# print("结束")

# 打印一个倒三角形，要求倒三角形是等边三角形，并且行数由用户输入
# x = int(input("打印等边三角形，请输入行数："))

# while x <= 6:


x = 1
while x <= 9:
    y = 1
    while x