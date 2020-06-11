# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/13 21:54 
  @Auth : 可优
  @File : lm_04_attribute_class.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""


class People:
    # 在一个类下面定义的变量, 这个变量, 成为类属性
    head = 1

    def __init__(self, my_name, my_age, my_height):
        self.name = my_name
        self.age = my_age
        self.height = my_height

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
two_people = People("飓风", 16, 1.9)

# 如果一个属性不属于某个对象的, 而是属于类的特征, 那么把这个属性成为类属性
