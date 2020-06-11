# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/27 20:35 
  @Auth : 可优
  @File : lm_02_unittest_define.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
import unittest

# 0、安装ddt模块并导入
import ddt

from handle_request import HandleRequest
from handle_excel import HandleExcel

excel_filename = "testcase.xlsx"
sheet_name = "register"
do_excel = HandleExcel(excel_filename, sheet_name)
testcases_data = do_excel.read_data()   # 嵌套字典的列表


# 1、使用ddt.ddt作为类的装饰器
@ddt.ddt
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 3、构造请求参数
        cls.do_request = HandleRequest()

        headers_dict = {
            "X-Lemonban-Media-Type": "lemonban.v2"
        }

        cls.do_request.add_headers(headers_dict)

    @classmethod
    def tearDownClass(cls):
        cls.do_request.close()

    """
    def test_1register_success(self):

        request_param = {
            "mobile_phone": "18511114479",
            "pwd": "12345678"
        }

        # 4、发起请求
        res = self.do_request.send("POST", self.url, json=request_param)

        # 5、提取响应数据，然后断言结果
        expected_value = 0
        real_code = res.json()["code"]
        try:
            self.assertEqual(expected_value, real_code, "测试注册接口的正向用例失败")
        except AssertionError as e:
            print("此处需要使用日志器来记录日志！")
            print(f"具体异常为：{e}")
            # 使用raise手动抛出异常
            raise e

    def test_2no_mobile(self):

        request_param = {
            "pwd": "12345678"
        }
        # 4、发起请求
        res = self.do_request.send("POST", self.url, json=request_param)

        # 5、提取响应数据，然后断言结果
        expected_value = 1
        real_code = res.json()["code"]

        try:
            self.assertEqual(expected_value, real_code, "测试手机号为空失败")
        except AssertionError as e:
            print("此处需要使用日志器来记录日志！")
            print(f"具体异常为：{e}")
            # 使用raise手动抛出异常
            raise e
    
    """

    """
    def test_register(self):
        # 使用for循环有问题：
        # a.用例总数一直为1，无法正确统计用例总数
        # b.一旦for循环中的某一条用例执行失败，那么for循环会中断
        # c.失败的用例也无法正确统计
        for testcase_dict in testcases_data:
            res = self.do_request.send(testcase_dict["method"],
                                       testcase_dict["url"],
                                       json=testcase_dict["data"])

            real_code = res.json()["code"]
            try:
                self.assertEqual(testcase_dict["expected_value"],
                                 real_code,
                                 testcase_dict["name"])
            except AssertionError as e:
                # print("此处需要使用日志器来记录日志！")
                # print(f"具体异常为：{e}")
                raise e
    """

    # 2、使用ddt.data函数来装饰用例的实例方法
    # a.第一个参数：往往需要将序列类型（字符串、列表、元组）拆包
    # b.ddt模块，会自动（动态）创建多个实例方法，实例方法名往往为test_register_用例的索引号（序号）
    # c.每次循环会将data中的位置参数依次传给实例方法

    # 什么是数据（用例数据）驱动？
    # a.往往一个接口拥有多条用例
    # b.每一条用例执行时，仅仅只有用例的数据（参数）不同，而用例的执行逻辑几乎一致
    # c.为了减少代码量，让框架更加简洁，所以会让用例数据（excel）与用例执行逻辑进行分离，这种机制称为数据驱动
    # d.会把data拆包之后的形参依次传给test_register实例方法的第二个形参
    @ddt.data(*testcases_data)
    # @ddt.data(用例1字典, 用例2字典, 用例3字典, ...)
    # @ddt.unpack()
    def test_register(self, testcase_dict):
        res = self.do_request.send(testcase_dict["method"],
                                   testcase_dict["url"],
                                   json=testcase_dict["data"])

        real_code = res.json()["code"]
        try:
            self.assertEqual(testcase_dict["expected_value"],
                             real_code,
                             testcase_dict["name"])
        except AssertionError as e:
            # print("此处需要使用日志器来记录日志！")
            # print(f"具体异常为：{e}")
            raise e


if __name__ == '__main__':
    unittest.main()
