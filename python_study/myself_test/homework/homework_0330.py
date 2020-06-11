"""
-------------------------------------------------
  @Time : 2020/4/1 13:56 
  @Auth : 十七
  @File : homework_0330.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
  @Company: 江苏宠资链互联网有限公司
  @Copyright: 爱它乐
-------------------------------------------------
"""
# 一、必做题
# 1.使用for\while打印九九乘法表
# 提示：
#
# 	a.上一次作业中，已做过的同学，只需使用for循环来实现
#
# 	b.上一次作业中，未做过的同学，需要使用两种循环来实现
#
# 	c.可以思考一下，打印的行数，是否可以用一个外层循环来实现呢？打印的列数和具体计算，是否可以用一个内层循环来实现呢？
# row = 0
# line = 0
# while row < 9:
#     row += 1
#     while line < 9:
#         line += 1
#         print(row, "*", line, "=", row*line, "\t", end="")
#         if row == line:
#             line = 0
#             print("")
#             break

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j, "*", i, "=", i * j, "\t", end="")
#     print("")


# 2.请写出for循环的格式
#1）遍历列表range for i in range(list_len):
#     print(testcase[i])
# 2）遍历字典for item in one_dict.keys():
#     print(f"值为: {item}  类型为: {type(item)}")
# 3）遍历任意一个序列类型testcase = [1, "登录接口正向用例", "云", "8888", "登录成功", True]
# a. 可以遍历任意一个序列类型(str、list、tuple)、字典
# for one_var in testcase:
#     print(f"值为: {one_var}  类型为: {type(one_var)}")

# 3.while和for的异同点
# a. while循环的次数往往不明确(不明显)
# b. for循环的次数往往是明确的, 次数等于序列类型元素的个数或者range元素的个数
# c. 如果能用for, 尽量就不用while, for的性能更高

# 4.写出将列表翻转的所有方法
# 将列表[13, 20, 42, 85, 9, 45]翻转之后为[45, 9, 85, 42, 20, 13]
# 第一种 取索引拼接
# one_list = [13, 20, 42, 85, 9, 45]
# a = one_list[-1], one_list[-2], one_list[-3], one_list[-4], one_list[-5], one_list[-6]
# print(list(a))
# # 第二种 reverse()函数
# one_list = [13, 20, 42, 85, 9, 45]
# one_list.reverse()
# print(one_list)
# # 第三种 切片
# one_list = [13, 20, 42, 85, 9, 45]
# two_list = one_list[::-1]
# print(two_list)

# 5.取出列表中最大的值
# 将列表[13, 20, 42, 85, 9, 45]中的最大值为85
# 提示： 使用多种方法
# one_list = [13, 20, 42, 85, 9, 45]
# 第一种 索引取值
# print(one_list[3])
# # 第二种  函数max()
# print(max(one_list))
# # 第三种  sort排序,取最后一个
# one_list.sort()
# print(one_list[-1])
# # 第四种 for循环
# for num in one_list:
#     if num == max(one_list):
#         print(num)



# 6.编写如下程序
# 打印出1-100之间除了含7和7的倍数之外的所有数字
# 提示：
# 	a.不符合要求的部分数字为：7、14、17、21、27等等
# 第一种 列出所有不符合的数字，进行判断
# num_list = [7, 14, 17, 21, 27, 28, 35, 37, 42, 47, 49, 56, 57, 63, 67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 84, 87, 91, 97, 98]
# list_a = []
# for num in range(1, 101):
#     if num not in num_list:
#         list_a.append(num)
# print(f"结果为{list_a}\n一共有{len(list_a)}个符合要求")

# 第二种 遍历，转换为str,用find方法
# num_list = []
# for num in range(1, 101):
#     num_seven = str(num).find("7")
#     print(num_seven)
#     if num_seven == -1 and num % 7 != 0:
#         num_list.append(num)
# print(f"结果为{num_list}\n一共有{len(num_list)}个符合要求")



# 7.编写如下程序
# 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
#
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 :   65 / 1.62 ** 2 = 24.8
#
# b.根据BMI指数，给与相应提醒
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28： 过重
# 28-32： 肥胖
# 高于32： 严重肥胖
# while True:
#     high = input("请输入你的身高m:")
#     weight = input("请输入你的体重kg:")
#     BMI = float(weight) / (float(high) ** 2)   # 计算BIM
#     BMI_a = ("%.2f" % BMI)       # 计算出来的BIM保留2位小数
#     if BMI < 18.5:                 # if语句判断BIM的值属于哪个范围
#         print(f"您的BMI值为{BMI_a},低于18.5,属于过轻")
#     elif BMI >= 18.5 and BMI <= 25:
#         print(f"您的BMI值为{BMI_a},在18.5-25之内,属于正常")
#     elif BMI >= 28 and BMI <= 32:
#         print(f"您的BMI值为{BMI_a},在28-32之内,属于肥胖")
#     elif BMI > 32:
#         print(f"您的BMI值为{BMI_a},高于32，属于严重肥胖")
#         break



# 二、选作题
# 1.列表去重
# 将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
# 第一种：用成员运算符
# one_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# new_list = []
# for num in one_list:
#     if num not in new_list:
#         new_list.append(num)
# print(f"去重后为：{new_list}")



# 2.完成剪刀石头布游戏
# 提示：
#
# 	a.提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
#
# 	b.电脑随机出拳
#
# 	c.比较胜负，显示用户胜、负还是平局
#
# 电脑随机出拳实现方式
#
# 使用随机数，首先需要导入 随机数 的 模块 —— “工具包”
#
# import random
# 可以使用random.randint(a, b) ，随机生成 [a, b]之间的整数，包含 a 和 b
#
# 例如：
#
# random.randint(1, 10)  # 生成的随机数n: 1 <= n <= 10
# random.randint(4, 4)  # 结果永远是 4
# random.randint(25, 12)  # 该语句是错误的，下限必须小于上限
import random
while True:
    user = input("请输入要出的拳石头（1）／剪刀（2）／布（3）:")
    # print(f"电脑出拳:{computer}")
    if user.isdigit():    # 判断用户输入的是否为数字
        user = int(user)
        computer = random.randint(1, 3)
        # user1 = "玩家出的拳"
        # computer1 = "电脑出的拳"
        if user == 1:
            user1 = "剪刀"
        if user == 2:
            user1 = "石头"
        if user == 3:
            user1 = "布"
        if computer == 1:
            computer1 = "剪刀"
        if computer == 2:
            computer1 = "石头"
        if computer == 3:
            computer1 = "布"
        if user > 3 or user < 1:
            print("出拳有误")
        print(f"玩家出拳为: {user1}\n电脑出拳为:{computer1}")
        if (user == 1 and computer == 3) \
                or (user == 2 and computer == 1) \
                or (user == 3 and computer == 2):
            print("玩家胜利")
        if (user == 1 and computer == 2) \
                or (user == 2 and computer == 3) \
                or (user == 3 and computer == 1):
            print("电脑胜利")
        if (user == 1 and computer == 1) \
                or (user == 2 and computer == 2) \
                or (user == 3 and computer == 3):
            print("平局")
    else:
        print("出拳有误")
