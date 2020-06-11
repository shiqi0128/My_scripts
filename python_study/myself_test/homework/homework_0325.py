"""
-------------------------------------------------
  @Time : 2020/3/26 21:09 
  @Auth : 十七
  @File : homework_0325.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""

# 一、必做题
# 1.现在有一个列表 one_list = [1，2，3，4，5]
# a.请通过三行代码将上面的列表，改成这个样子 two_list  = [0，1，2，3，66，5，11，22，33]
# 第一种
one_list = [1, 2, 3, 4, 5]
one_list[3] = 66
two_list = [0] + one_list + [ 11, 22, 33]
print(two_list)
# 第二种
one_list = [1, 2, 3, 4, 5]
two_list = [11, 22, 33]
one_list[3] = 66
one_list.insert(0, 0)
print(one_list + two_list)


# b.对列表two_list进行升序排序 （从小到大）
two_list = [0, 1, 2, 3, 66, 5, 5, 11, 22, 33]
two_list.sort()
print("two_list升序排序:", two_list)

# 2.字典的增删查改操作
# 某比赛需要获取你的个人信息，编写一段代码要求如下：

# a.运行时分别提醒输入 姓名、性别、年龄、爱好 ，输入完了，请将数据通过字典存储起来；
name = input("请输入您的姓名:")
gender = input("请输入您的性别:")
age = input("请输入您的年龄:")
hobby = input("请输入您的爱好:")
info = {"name": name, "gender": gender, "age": age, "hobby": hobby}
print(f"您的个人信息为: {info}\n类型:{type(info)}")

# # # b.数据存储完了，然后输出个人介绍，格式如下：我的名字XXX，今年XXX岁，性别XX，喜欢敲代码；
print(f"我的名字{name}, 今年{age}, 性别{gender}, 喜欢{hobby}")

# # # c.有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
info["high"] = "1.68" + "cm"
info["mobile"] = 18717752237
print(f"新的个人信息:{info}")
# # # d.平台为了保护你的隐私，需要你删除你的联系方式
info.pop("mobile")
print(f"删除联系方式后的个人信息: {info}")

# # # e.你为了取得更好的成绩， 你添加了多项自己的擅长技能（例如：跑步、钢琴、吉他等）。
info["skill_1"] = "跑步"
info["skill_2"] = "钢琴"
info["skill_3"] = "吉他"
print(f"添加技能后的个人信息: {info}")



# 3.利用下划线将列表one_list = [“python”, “java”, “php”]的元素拼接成一个字符串，然后将所有字母转换为大写
one_list = ["python", "java", "php"]
res = "_".join(one_list).upper()
print(f"结果为:{res}\n类型为: {type(res)}")

# 二、选作题
# 1.求三个整数中的最大值
# 提示：

# 	a.三个整数使用input提示用户输入
a = int(input("请输入第1个整数:"))
b = int(input("请输入第2个整数:"))
c = int(input("请输入第3个整数:"))

# 	b.通过预习if条件判断语句，来完成本题
if a > b:
    if a > c:
        print(f"最大的数为:{a}")
    elif a < c:
        print(f"最大的数为: {c}")
elif b > a:
    if b > c:
        print(f"最大的数为:{b}")
    elif b < c:
        print(f"最大的数为:{c}")