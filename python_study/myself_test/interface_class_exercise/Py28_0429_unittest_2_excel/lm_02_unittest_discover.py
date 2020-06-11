"""
-------------------------------------------------
  @Time : 2020/5/21 20:28 
  @Auth : 十七
  @File : lm_01_unittest.py.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
import unittest

# defaultTestLoader=TestLoader(),是一个加载器
# discover = suite.TestSuite，一个测试套件
# a、第一个参数为发现用例的路径（在哪里找这个用例）
# b、第二个参数为用例模块的匹配模式（test*.py）
# c、用例的自动搜索机制
suite = unittest.defaultTestLoader.discover(".")

# 3、执行用例
runner = unittest.TextTestRunner()    # 会创建一个运行器,TextTestRunner()里面有个run方法
runner.run(suite)

#  控制台打印的结果
# .代表用例执行成功
# F代表用例执行失败