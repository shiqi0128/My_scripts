# 用例执行的邮件
import unittest
import os
import HTMLTestRunner
import time
from interfaceTest.GMALL.gmall_all.account import gmall_account


# class C(unittest.TestCase):
#
#     def test_b(self):
#         print("OK")


if __name__ == "__main__":
    suite = unittest.TestSuite()    # 调用unittest的TestSuite(),理解为管理case的一个容器（测试套件）
    # suite.addTest(C("test_b"))
    suite.addTest(gmall_account("test_01_users"))
    suite.addTest(gmall_account("test_02_old_password"))
    suite.addTest(gmall_account("test_03_Message_notification_list"))

    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))

    filename = 'F:/test/interfaceTest/GMALL/gmall_all/Test_report/'+now+'-testresult.html' # 测试报告的存放路径及文件名
    with open(filename, 'wb')as f:  # 创测试报告html文件，此时还是个空文件,二进制写入
        # 定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', description='测试结果如下: ')
        #  stream = fp  引用文件流
        #  title  测试报告标题
        #  description  报告说明与描述
        runner.run(suite)


