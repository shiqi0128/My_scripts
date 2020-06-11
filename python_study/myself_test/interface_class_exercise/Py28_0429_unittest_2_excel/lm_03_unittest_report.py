"""
-------------------------------------------------
  @Time : 2020/5/22 2:11 
  @Auth : 十七
  @File : lm_03_unittest_report.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
# import unittest
# from HTMLTestRunnerNew import HTMLTestRunner
#
# suite = unittest.defaultTestLoader.discover(".")
#
# with open("testcase.html", "wb") as file:
#     runner = HTMLTestRunner(file, title="py28第一个接口测试报告", description="非常漂亮的报告", tester="十七")
#     runner.run(suite)





































import unittest
from HTMLTestRunnerNew import HTMLTestRunner


unittest.defaultTestLoader.discover(".")
with open("testcase.html", "wb") as file:
     runner = HTMLTestRunner(file, verbosity=1, description="很美的接口自动化报告", tester="十七")









