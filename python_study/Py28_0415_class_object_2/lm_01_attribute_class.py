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
    # 类属性是类的特征, 每一个对象都共享
    head = 1

    def __init__(self, my_name, my_age, my_height):
        self.name = my_name
        self.age = my_age
        self.height = my_height
        self.head = 1

    def run(self):
        # 动态创建实例属性(了解即可)
        self.fair = "飘逸秀发"
        print(f"{self.name}会跑步!")

    def eat(self, food):
        # 在类里调用实例方法
        # a. self.方法名(参数)
        # self.get_wether("晴朗")
        # People.get_wether("晴朗")

        # self.get_wether("晴朗")
        # self.get_wether()
        self.run()
        print(f"{self.name}会吃{food}!")

    def show_head(self):
        # 二、在类的里面
        # a. self.类属性名
        # 如果实例属性名与类属性名同名, 那么获取的是实例属性
        # self.head = 3
        print(self.head)

    # 类方法: 来操作(读取/修改/创建)类型
    # @classmethod装饰器装饰的方法, 成为类方法
    @classmethod
    def handle_head(cls, eyes):
        # b. 可以使用cls.类属性, 来获取类属性
        # print(cls.head)
        # 动态创建类属性
        cls.eyes = eyes
        pass

    # 并不需要创建实例方法
    # 跟类和对象没有直接关系, 但是有间接关系
    # @staticmethod来创建静态方法
    @staticmethod
    def get_wether(status):
        print(f"当天天气: {status}")


# def get_wether(status):
#     print(f"当天天气: {status}")


if __name__ == '__main__':
    one_people = People(my_name="Jack", my_age=17, my_height=1.78)
    two_people = People("飓风", 16, 1.9)

    # 一、在类外
    # 1. 获取类属性
    # a. 类名.类属性
    # b. 不能使用类名来访问实例属性
    # print(People.head)
    # print(People.name)
    # c. 可以使用对象.类属性
    # print(one_people.head)

    # 2. 创建类属性
    # 类名.属性名 = 值
    # People.eyes = 2
    # print(People.eyes)
    # print(one_people.eyes)

    # 不可以使用对象.属性名 = 值, 来创建类属性
    # one_people.eyes = 2
    # two_people.eyes = 1
    # print(one_people.eyes)
    # print(two_people.eyes)
    # print(People.eyes)

    # one_people.show_head()
    # two_people.show_head()

    # 在类外
    # a. 类名.类方法(参数)
    # b. 类本身传给cls
    # People.handle_head()
    # People.handle_head(2)
    # print(f"{one_people.name}, 有{one_people.eyes}只眼睛")
    # print(f"{two_people.name}, 有{two_people.eyes}只眼睛")

    # 使用对象.类方法(参数), 也能正常调用
    # 会将对象所属的类传给cls
    # one_people.handle_head(2)

    # one_people.eat("披萨")
    # two_people.eat("披萨")

    # 在类外调用静态方法
    # 可以类名.静态方法(参数)
    # 可以对象名.静态方法(参数)
    People.get_wether("晴朗")
    one_people.get_wether("小雨")

    # 为什么要创建静态方法?
    # 为了更好进行封装
    # 为了美观
