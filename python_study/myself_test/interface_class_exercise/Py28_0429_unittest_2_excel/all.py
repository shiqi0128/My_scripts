"""
-------------------------------------------------
  @Time : 2020/5/26 13:17 
  @Auth : 十七
  @File : all.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
# 生成html测试报告
import unittest
from HTMLTestRunnerNew import HTMLTestRunner

suite = unittest.defaultTestLoader.discover(".")

with open("testcase2.html", "wb") as file:
    runner = HTMLTestRunner(
        title="py28测试报告05261320",
        description="很美丽",
        tester = "小十七"
    )
    runner.run(suite)