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

# from test_01_register import TestRegister
# from test_02_login import TestLogin

# import test_01_register
# import test_02_login


# 1、创建一个TestSuite套件对象
# 相当于一个袋子，来装载测试用例
suite = unittest.TestSuite()

# 2、创建一个TestLoader加载器对象
# 相当于工人
loader = unittest.TestLoader()

# a.使用TestSuite套件对象.addTest来加载用例
# b.使用TestLoader对象.loadTestsFromTestCase来加载测试类（TestCase的子类）
# suite.addTest(loader.loadTestsFromTestCase(TestRegister))
# suite.addTest(loader.loadTestsFromTestCase(TestLogin))

# c.使用TestLoader对象.loadTestsFromModule来加载测试模块
# suite.addTest(loader.loadTestsFromModule(test_01_register))
# suite.addTest(loader.loadTestsFromModule(test_02_login))

# 很少使用，不推荐
# suite.addTest(loader.loadTestsFromName("test_01_register.TestRegister.test_2no_mobile"))


# 3、执行用例
# 创建TextTestRunner运行器
runner = unittest.TextTestRunner()
runner.run(suite)

# 控制台中打印的结果
# .代表用例执行成功
# F代表用例执行失败
