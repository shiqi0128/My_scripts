# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/13 20:27 
  @Auth : 可优
  @File : lm_01_class_define.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""


# 类的命名
# a. 大驼峰命名法
# MyName
# b. 符合标识符的命名规范
class People:

    # 把类中定义的函数叫做方法(行为动作)
    # 如果一个方法中第一个参数为self, 那么我们把这种方法叫做实例方法
    def run(self):
        print("会跑步!")

    def eat(self, food):
        # 在类里调用实例方法
        # a. self.方法名(参数)
        self.run()
        print(f"会吃{food}!")


# 创建对象
# 1. 使用类名()来创建对象
one_object = People()
print(f"one_object的id为: {id(one_object)}")

# 在类的外面调用方法
# a. 使用对象.方法(), 会自动将对象自身传给self
one_object.run()
one_object.eat("米饭")
pass
