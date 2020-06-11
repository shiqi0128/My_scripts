"""
-------------------------------------------------
  @Time : 2020/5/26 17:54 
  @Auth : 十七
  @File : run.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from handle_yaml import HandleYaml

do_yaml = HandleYaml()

suite = unittest.defaultTestLoader.discover(".")

with open(do_yaml.get_data("report", "filename"), "wb") as file:
    runner = HTMLTestRunner(file,
                            verbosity=do_yaml.get_data("report", "verbosity"),
                            title=do_yaml.get_data("report", "title"),
                            description=do_yaml.get_data("report", "description"),
                            tester=do_yaml.get_data("report", "tester")
                            )
    runner.run(suite)