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


# 如果在定义类时，没有显式继承父类（没有括号），那么会默认继承object父类（任何类的父类）
class People(object):
# class People:

    def run(self):
        print(f"{self.name}跑步")

    def eat(self, food):
        print("吃东西")


if __name__ == '__main__':
    one_people = People()
    two_people = People()
    # 1、方式一
    # 在类外面动态创建类属性（不推荐）
    one_people.name = "半夏"

    # 2、方式二
    # setattr(对象/类, 属性名, 属性值)
    # setattr(x, 'y', v) is equivalent to x.y = v
    setattr(one_people, "name", "半夏")
    setattr(People, "head", 1)
    # print(one_people.name)
    # print(two_people.head)

    # a. 可以使用getattr函数来获取一个对象或者类的属性
    # b. getattr(对象/类, 属性名)
    # c. 如果属性名不存在， 会报错
    # print(getattr(one_people, "name1"))
    # d.如果添加第三个参数，那么属性不存在的话，会返回默认值
    print(getattr(one_people, "name1", "婷婷"))
