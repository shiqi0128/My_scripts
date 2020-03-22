# ------------------此页面文件为执行3.1所有用例生成html测试报告----------------
import unittest
import HTMLTestRunner
import time
from Atle.interface.framework.test.test_suit.Alte_one.run import Activity
from Atle.interface.framework.common.pubilc_act import double_elev
# from Atle.interface.framework.common.public_func import pubilc_func

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()  # 调用unittest的TestSuite(),理解为管理case的一个容器（测试套件）
    suite.addTest(Activity("test_03_who_list"))
    suite.addTest(Activity("test_04_who_list_find"))
    suite.addTest(Activity("test_05_ranking"))
    suite.addTest(Activity("test_06_begin"))
    suite.addTest(Activity("test_07_already"))
    suite.addTest(Activity("test_08_progress"))
    suite.addTest(Activity("test_09_details"))
    suite.addTest(double_elev("test_mart_list"))
    suite.addTest(double_elev("test_past"))

    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))

    filename = 'E:/script/Atle/interface/framework/Test_report/'+now+'-testresult.html'  # 测试报告的存放路径及文件名
    with open(filename, 'wb')as f:  # 创测试报告html文件，此时还是个空文件,二进制写入
        # 定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='爱它乐V3.1接口测试报告', description='测试结果如下: ')
        #  stream = fp  引用文件流
        #  title  测试报告标题
        #  description  报告说明与描述
        runner.run(suite)  # 运行测试用例
        f.close()


# --------定义发送邮件-----------



