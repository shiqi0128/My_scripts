# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/17 20:41 
  @Auth : 可优
  @File : lm_03_private_attribute.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""


class People:

    def __init__(self, name, age):
        # self.name = name
        # 1. 如果在属性名前添加两个下划线， 那么定义的就是私有属性
        # 2. 正常情况下，在类外，无法直接使用 对象.私有属性
        # 3. 子类无法继承私有属性
        # self.__name = name
        self.name = name
        self.age = age

    def run(self):
        # print(f"{self.__name}在跑步")
        print(f"{self.name}在跑步")

    def eat(self, food):
        print("吃东西")


class Children(People):

    def run(self):
        print(f"{self.name}，在跑步！")


if __name__ == '__main__':
    # one_people = People("清风", 18)
    # one_people.run()
    # print(one_people.name)
    # print(one_people.__name)
    # _类名__私有属性名
    # print(one_people._People__name)

    # 面向对象中，有三大概念
    # 封装、继承、多态
    # 多态：使用父类去接收子类对象
    # int a = 10;
    # a = 10
    # People one_people = Children()

    one_people = People("清风", 18)
    one_children = Children("流沙", 17)
    two_children = Children("Cheng", 16)

    for item in [one_people, one_children, two_children]:
        print(item.run())
