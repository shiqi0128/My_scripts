df# -*- coding: utf-8 -*-
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

    # setUp覆盖父类中的方法
    # a、测试用例实例方法有几个，那么setUp就会执行几次
    # b、先执行setUp，然后再执行测试用例实例方法
    # c、往往用于用例的初始化操作
    def setUp(self):
        # 3、构造请求参数
        print("setUp")
        self.do_request = HandleRequest()
        self.register_url = "http://api.lemonban.com/futureloan/member/register"

        headers_dict = {
            "X-Lemonban-Media-Type": "lemonban.v2",
            "User-Agent": "Mozilla/5.0 LookSky"
        }

        self.do_request.add_headers(headers_dict)

    # tearDown覆盖父类中的方法
    # a、用例实例方法有几个，那么tearDown就会执行几次
    # b、用例执行结束之后，然后再执行tearDown
    # c、往往用于资源释放操作
    def tearDown(self):
        print("tearDown")
        self.do_request.close()

    # 2、创建测试用例测试方法，一定要以test_作为前缀
    def test_1register_success(self):

        request_param = {
            "mobile_phone": "18511112239",
            "pwd": "12345678"
        }

        # 4、发起请求
        res = self.do_request.send("POST", self.register_url, json=request_param)

        # 5、提取响应数据，然后断言结果
        expected_value = 0
        real_code = res.json()["code"]
        self.assertEqual(expected_value, real_code, "测试注册接口的正向用例失败")

    def test_2no_mobile(self):

        request_param = {
            "pwd": "12345678"
        }
        # 4、发起请求
        res = self.do_request.send("POST", self.register_url, json=request_param)

        # 5、提取响应数据，然后断言结果
        expected_value = 1
        real_code = res.json()["code"]

        self.assertEqual(expected_value, real_code, "测试手机号为空失败")


if __name__ == '__main__':
    unittest.main()
