# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/29 21:22 
  @Auth : 可优
  @File : lm_03_unittest_report.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
import unittest

from HTMLTestRunnerNew import HTMLTestRunner

suite = unittest.defaultTestLoader.discover(".")


with open("testcase1.html", "wb") as file:
    runner = HTMLTestRunner(file,
                            verbosity=1,
                            title="py28期第一份测试报告",
                            description="非常美的报告",
                            tester="滔滔")
    runner.run(suite)
