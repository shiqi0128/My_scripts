# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/15 21:42 
  @Auth : 可优
  @File : lm_04_class_inherit_2.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}需要吃东西")

    def drink(self):
        print(f"{self.name}需要喝水")

    def run(self):
        print(f"{self.name}能跑")

    def sleep(self):
        print(f"{self.name}需要睡觉")


# a. 称为继承
# b. 在定义一个类时, 在括号中添加父类名
# c. 自动获取父类的属性(实例属性/类属性)和方法(实例方法/类方法/静态方法)
# d. 私有属性和方法除外
# 把Dog称为子类(派生类), Animal称为父类(基类)
class Dog(Animal):

    # a. 如果父类中的某个方法不满足要求, 那么可以重写/覆盖
    # b. 定义与父类同名的方法, 那么会将父类中的方法覆盖
    def __init__(self, name, age):
        # 如果父类中的方法, 不完全满足我们的要求, 我们需要添加其他逻辑
        # 那么可以对父类进行拓展
        # self.name = name
        # self.age = age
        # super().父类中方法(参数)
        super().__init__(name)
        self.age = age

    def bark(self):
        print(f"{self.name}会汪汪叫")


class Cat(Animal):

    def catch(self):
        print(f"{self.name}能抓老鼠")

    def eat(self):
        super().eat()
        print("吃得好开心")


animal = Animal("xxx动物")
# siberian_husky = Dog("哈士奇")
siberian_husky = Dog("哈士奇", 3)
tom = Cat("tom猫")


# animal.eat()
# siberian_husky.sleep()
# tom.run()
siberian_husky.bark()
tom.catch()
tom.eat()
