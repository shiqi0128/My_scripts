# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/13 20:50 
  @Auth : 可优
  @File : lm_02_attribute_define.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""


class People:

    # __init__(self)
    # 1. 名称固定
    # 2. 往往把此方法此为构造方法或者构造器(创建对象的方法)
    # 3. 作用为创建对象时来定义属性
    def __init__(self):
        # 类中属性可以类比为变量
        # 在类的里面使用self.变量名 = 值
        self.name = "皮卡丘"
        self.age = 18
        self.height = 1.85
        # 可以使用self.属性名来获取属性值
        print(f"姓名为: {self.name}\n年龄为: {self.age}\n身高为: {self.height}")

    def run(self):
        print("会跑步!")

    def eat(self, food):
        # 在类里调用实例方法
        # a. self.方法名(参数)
        self.run()
        print(f"会吃{food}!")


# 类名()
# a. 自动调用__init__()方法
# b. 如果没有定义__init__()方法, 那么会调用父类的__init__()方法
# c. 如果有定义__init__()方法, 那么会自动调用
# d. 创建一个对象, 也称为实例化一个对象
one_people = People()
two_people = People()
one_people.run()

# one_people_id = id(one_people)
# two_people_id = id(two_people)
#
# if one_people_id == two_people:
#     print("这个两个对象是同一个对象")
# else:
#     print("这个两个对象不是同一个对象")

# 变量1 is 变量2
# 1. 判断变量1和变量2是否是同一个变量
# 2. 如果一致, 返回True
# 否则返回False
# is not 或者 is
# not in 或者 in
if one_people is not two_people:
    print("这个两个对象是同一个对象")
else:
    print("这个两个对象不是同一个对象")
