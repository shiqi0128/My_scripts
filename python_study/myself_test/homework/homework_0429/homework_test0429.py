"""
-------------------------------------------------
  @Time : 2020/5/6 14:30 
  @Auth : 十七
  @File : homework_test0429.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
import unittest
from test_01_register import TestRegister
from test_02_login import  TestLogin

# 1、创建一个TestSuite套件对象
# 相当于一个袋子，用来装载测试用例
suite = unittest.TestSuite()

# 创建一个TestLoader加载器对象
# 相当于一个工人
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestRegister))