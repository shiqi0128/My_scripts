# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/13 21:30 
  @Auth : 可优
  @File : lm_03_attribute_define_2.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""


class People:

    def __init__(self, my_name, my_age, my_height):
        # 类中属性可以类比为变量
        # 在类的里面使用self.变量名 = 值
        self.name = my_name
        self.age = my_age
        self.height = my_height
        # 可以使用self.属性名来获取属性值
        # print(f"姓名为: {self.name}\n年龄为: {self.age}\n身高为: {self.height}")

    def run(self):
        # 动态创建实例属性(了解即可)
        self.fair = "飘逸秀发"
        print(f"{self.name}会跑步!")

    def eat(self, food):
        # 在类里调用实例方法
        # a. self.方法名(参数)
        self.run()
        print(f"{self.name}会吃{food}!")


one_people = People(my_name="Jack", my_age=17, my_height=1.78)
# 在类的外面
# 可以使用对象.属性名, 获取属性值 (很少这么用)
# print(f"{one_people.name}")
two_people = People("飓风", 16, 1.9)
# print(f"{two_people.name}")

# one_people.run()
# two_people.eat("饺子")
# one_people.run()
# two_people.run()
# print(f"{one_people.fair}")
# print(f"{two_people.fair}")

# 类
# 通过类可以创建对象: 实例对象
# 调用__init__()方法的过程: 成为实例化
# 通过self/对象.属性名 = 属性值: 创建的属性, 实例属性

# 动态创建实例属性(很少出现, 了解即可)
one_people.gender = "男"
print(one_people.gender)

# 如果一个属性不属于某个对象的, 而是属于类的特征, 那么把这个属性成为类属性
