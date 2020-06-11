# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/15 21:34 
  @Auth : 可优
  @File : lm_03_class_inherit.py
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


class Dog:

    def __init__(self, name, age):
        self.name, self.age = name, age

    def eat(self):
        print(f"{self.name}需要吃东西")

    def drink(self):
        print(f"{self.name}需要喝水")

    def run(self):
        print(f"{self.name}能跑")

    def sleep(self):
        print(f"{self.name}需要睡觉")

    def bark(self):
        print(f"{self.name}会汪汪叫")


class Cat:

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

    def catch(self):
        print(f"{self.name}能抓老鼠")


animal = Animal("xxx动物")
siberian_husky = Dog("哈士奇", 3)
tom = Cat("tom猫")


animal.eat()
siberian_husky.bark()
tom.catch()
