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
# python中的内置模块（框架）
# 0、导入unittest模块
import unittest

from Py28_0427_unittest.handle_request import HandleRequest


# 1、需要继承unittest.TestCase父类
class TestRegister(unittest.TestCase):

    # setUpClass覆盖父类中的方法
    # a、不管用例有多少条，只会执行一次
    # b、先执行setUpClass，然后把所有测试用例实例方法执行完毕，之后再执行tearDownClass
    # c、往往用于所有用例的公共初始化操作
    @classmethod
    def setUpClass(cls):
        # 3、构造请求参数
        print("setUpClass\n")
        cls.do_request = HandleRequest()
        cls.register_url = "http://api.lemonban.com/futureloan/member/register"

        headers_dict = {
            "X-Lemonban-Media-Type": "lemonban.v2",
            "User-Agent": "Mozilla/5.0 LookSky"
        }

        cls.do_request.add_headers(headers_dict)

    # tearDownClass覆盖父类中的方法
    # a、不管用例有多少条，只会执行一次
    # b、先执行setUpClass，然后把所有测试用例实例方法执行完毕，之后再执行tearDownClass
    # c、往往用于所有用例的公共资源释放
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        cls.do_request.close()

    # 2、创建测试用例测试方法，一定要以test_作为前缀
    def test_1register_success(self):

        request_param = {
            "mobile_phone": "18511113459",
            "pwd": "12345678"
        }

        # 4、发起请求
        res = TestRegister.do_request.send("POST", TestRegister.register_url, json=request_param)

        # 5、提取响应数据，然后断言结果
        expected_value = 0
        real_code = res.json()["code"]
        self.assertEqual(expected_value, real_code, "测试注册接口的正向用例失败")

    def test_2no_mobile(self):

        request_param = {
            "pwd": "12345678"
        }
        # 4、发起请求
        res = TestRegister.do_request.send("POST", TestRegister.register_url, json=request_param)

        # 5、提取响应数据，然后断言结果
        expected_value = 1
        real_code = res.json()["code"]

        self.assertEqual(expected_value, real_code, "测试手机号为空失败")


if __name__ == '__main__':
    unittest.main()
