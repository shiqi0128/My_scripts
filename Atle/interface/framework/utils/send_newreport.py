# ------------------执行所有用例发送测试报告邮件----------------
import unittest
import HTMLTestRunner
import time
from Atle.interface.framework.test.test_suit.Alte_one.All_zl import Alte    # 导入所有用例的类
from Atle.interface.framework.common.public_func import pubilc_func

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()  # 调用unittest的TestSuite(),理解为管理case的一个容器（测试套件）
    suite.addTest(Alte("test_01_get_price"))    # 添加类下的用例，用addTest方法
    suite.addTest(Alte("test_02_get_comment"))
    suite.addTest(Alte("test_03_creat_address"))
    suite.addTest(Alte("test_04_address_update"))
    suite.addTest(Alte("test_05_address_del"))
    suite.addTest(Alte("test_06_address_one"))
    suite.addTest(Alte("test_07_open_item"))
    suite.addTest(Alte("test_08_goods_one"))
    suite.addTest(Alte("test_09_goods_search"))
    suite.addTest(Alte("test_10_goods_advertise"))
    suite.addTest(Alte("test_11_home_tags"))
    suite.addTest(Alte("test_12_keywords"))
    suite.addTest(Alte("test_13_empty"))
    suite.addTest(Alte("test_14_creat_order"))
    suite.addTest(Alte("test_15_order_pay"))
    suite.addTest(Alte("test_16_update_order"))
    suite.addTest(Alte("test_17_order_detail"))
    suite.addTest(Alte("test_18_add_comment"))
    suite.addTest(Alte("test_19_comment_list"))
    suite.addTest(Alte("test_20_Ocomment"))
    suite.addTest(Alte("test_21_update_comment"))
    suite.addTest(Alte("test_22_comment_delete"))
    suite.addTest(Alte("test_23_accusation_type"))
    suite.addTest(Alte("test_24_accusation_details"))
    suite.addTest(Alte("test_25_accusation_delete"))
    suite.addTest(pubilc_func("test_address_list"))
    suite.addTest(pubilc_func("test_order_list"))
    suite.addTest(pubilc_func("test_save_categorys"))
    suite.addTest(pubilc_func("test_open_list"))
    suite.addTest(pubilc_func("test_comment_list"))

    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))

    filename = 'E:/script/Atle/interface/framework/Test_report/'+now+'-testresult.html'  # 测试报告的存放路径及文件名
    with open(filename, 'wb')as f:  # 创测试报告html文件，此时还是个空文件,二进制写入
        # 定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='爱它乐V3.0接口测试报告', description='测试结果如下: ')
        #  stream = fp  引用文件流
        #  title  测试报告标题
        #  description  报告说明与描述
        runner.run(suite)  # 运行测试用例
        f.close()


# --------定义发送邮件-----------



