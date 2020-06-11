"""
-------------------------------------------------
  @Time : 2020/5/22 21:51 
  @Auth : 十七
  @File : lm_03_unittest_report.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
import unittest
from HTMLTestRunnerNew import HTMLTestRunner

suite = unittest.defaultTestLoader.discover(".")

runner = unittest.TextTestRunner()
runner.run(suite)