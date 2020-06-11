# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/29 20:37 
  @Auth : 可优
  @File : lm_01_unittest.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
import unittest


# 1、使用unittest.defaultTestLoader.discover方法，会返回套件对象
# a.第一个参数为发现用例的路径（在哪里找）
# b.第二个参数为用例模块的匹配模式（test*.py）
# c.用例的自动搜索机制
suite = unittest.defaultTestLoader.discover(".")
# suite = unittest.defaultTestLoader.discover(".", "keyou*.py")

# 2、执行用例
# 创建TextTestRunner运行器
runner = unittest.TextTestRunner()
runner.run(suite)
