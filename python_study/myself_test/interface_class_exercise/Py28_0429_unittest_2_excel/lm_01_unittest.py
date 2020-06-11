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
# from test_01_register import TestRegister
# from test_02_login import TestLogin
import test_01_register
import test_02_login

# 1、创建一个TestSuite套件对象，相当于一个袋子，来装载测试用例
suite = unittest.TestSuite()

# 2、创建一个加载器对象，相当于一个工人
loader = unittest.TestLoader()

# a、使用TestSuite套件对象.addTest来加载用例
# b、使用TestLoader对象.loadTestsFromTestCase来加载测试类（Testcase的子类）
# suite.addTest(loader.loadTestsFromTestCase(TestRegister))
# suite.addTest(loader.loadTestsFromTestCase(TestLogin))

# c、使用TestLoader对象.loadTestFromodule来加载测试模块
suite.addTest(loader.loadTestsFromModule(test_01_register))
suite.addTest(loader.loadTestsFromModule(test_02_login))

# d、使用Testloader对象.loadTestFroname(模块名.类名.方法名的形式加载某一个测试用例)-----很少使用、不推荐

# 3、执行用例
runner = unittest.TextTestRunner()    # 会创建一个运行器,TextTestRunner()里面有个run方法
runner.run(suite)

#  控制台打印的结果
# .代表用例执行成功
# F代表用例执行失败