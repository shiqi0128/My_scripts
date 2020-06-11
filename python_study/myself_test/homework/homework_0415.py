"""
-------------------------------------------------
  @Time : 2020/4/16 21:43 
  @Auth : 十七
  @File : homework_0415.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
# 一、必做题
# 1.实例方法、类方法、静态方法分别是什么？有作用？如何定义？如何调用？
# 实例方法--定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）
# 调用：只能由实例对象调用
# 类方法--定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；
# 调用：实例对象和类对象都可以调用
# 静态方法--定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；
# 调用：实例对象和类对象都可以调用。

# 2.实例属性、类属性分别是什么？如何创建？如何调用？
# 实例属性：__init__内定义的属性。
# 类属性：在类方法外定义的属性。
# 实例属性创建：在__init__内定义的属性，实例属性每个实例各自拥有，相互独立
# 类属性创建：在类里面定义的属性，只有1份，创建的实例都会继承自唯一的类属性
# 类属性调用：类.类属性
# 实例属性调用：实例对象.类属性
#
# 3.什么是继承？有什么特性？
# 定义：继承指的是类与类之间的关系
# 特性：子类会继承父类的所有的属性和方法,子类也可以覆盖父类同名的变量和方法。
# 4.编写如下程序
# 创建一个名为 Restaurant类，要求至少拥有饭店名和美食种类这两个特征。
#
# a.需要创建一个方法来描述饭店名和美食种类相关信息
#
# b.同时能够显示饭店营业状态（例如：正在营业）


# class Restaurant():
#     def __init__(self, res_name, food_type):
#         """初始化属性restaurant_name和cuisine_type"""
#         self.res_name = res_name
#         self.food_type = food_type
#
#     def describe_restaurant(self):
#         print("The restarurant name is " + self.res_name.title() + ".")
#         print("The restarurant's food type is " + self.food_type.title() + ".")
#
#     def open_restaurant(self):
#         print("The " + self.res_name.title() + " is openning!")
#
#
# my_restaurant=Restaurant('germy', 'chinese food')
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# 5.编写如下程序
# 编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算。
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        sum_a = self.a + self.b
        return sum_a

    def sub(self):
        sub_a = self.a - self.b
        return sub_a

    def mul(self):
        mul_a = self.a * self.b
        return mul_a

    def div(self):
        try:
            return round(self.a / self.b, 2)  # 相乘之后四舍五入保留2位小数
        except ZeroDivisionError:
            # print("出现除0错误！")
            return "除数不能为0"


if __name__ == '__main__':
    nums = (10, 0)  # 传入两个参数
    math_1 = Math(*nums)  # *拆包
    print("{} + {} = {}".format(*nums, math_1.add()))
    print("{} - {} = {}".format(*nums, math_1.sub()))
    print("{} * {} = {}".format(*nums, math_1.mul()))
    print("{} / {} = {}".format(*nums, math_1.div()))


# 二、选作题
# 1.编写如下程序
# 编写一个工具类和工具箱类，工具需要有的名称、功能描述、价格，工具箱能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。

# def f(str1, *args, **kwargs):
#     print(str1, args, kwargs)
#
#
# l = [1, 2, 3]
# t = [4, 5, 6]
# d = {"a": 7, "b": 8, "c": 9}
#
# f(1, 2)
# f(1, 2, 3, "python")
# f("python", l, d)
# f("python", *t)
# f("python", *l, **d)
# f("python", q="winning", **d)


# 等长的两个列表合并到一个字典,要求：合并成{'A': 1, 'B': 2, 'C': 3},请用一行代码实现
# list_a = ["A", "B", "C"]
# list_b = [1, 2, 3]
# print(dict(zip(list_a, list_b)))

#
# 合并两个列表并消除重复值
# list_1 = ["a", "b", "c", "1", "A", "winning"]
# list_2 = ["a", "python", "string"]
# print(set(list_1 + list_2))

# 31、已知一个列表，根据字典中的x ,由大到小排序这个列表
# a = [{"x": 1, "y": 2}, {"x": 2, "y": 3}, {"x": 3, "y": 4}]
# # print(a[1]["x"])
# print(sorted(a[1]["x"], reverse=True))

# 写出语句打印" let's go", she said
# print("\" let's go\", she said")

# 请写一段代码,随机生成10个数并写入文件
# import random
#
# with open("lemon.txt", "a") as file:
#     list1 = []
#     for item in range(0, 10):
#         num = random.randint(0, 10)
#         list1.append(str(num))
#
#     print(list1)
#     file.write(",".join(list1))

# def f(x, l=[]):
#     for i in range(x):
#         l.append(i * i)
#         print(l)
#
# f(2)   # [0] [0, 1]
# f(3, [3, 2, 1])  # [0][0, 1][0,1,4][3, 2, 1]
# f(3)   # 3 [0, 1, 4, 9] [0][0, 1][0,1,4]

# 用python写一段代码，计算1-1000以内能被7整除，除以5余3的整数，并按行打印
# for i in range(1, 1001):
#     if i % 7 == 0 and i % 5 == 3:
#         print(i)

# 50、小明有一百元，他想买一百本书，英语书5元一本，数学书3元一本，语文书0.5元一本，请问他有多少种买法。请编程解决这个问题，可以使用任何编程语言，包括伪语言。
# egl = 5
# math = 3
# chinese = 0.5
#
# if egl*a + math*b + chinese*c == 100:

# print('%.2f' % (20/3))
# a = '小简女神'
# b = a*2
# print(",".join(a))


# a = '1'
# b = '2'
# print('{1}{0}'.format(a,b))