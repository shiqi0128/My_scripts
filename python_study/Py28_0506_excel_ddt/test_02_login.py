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

from Py28_0427_unittest.handle_request import HandleRequest


# 1、需要继承unittest.TestCase父类
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 3、构造请求参数
        cls.do_request = HandleRequest()
        cls.url = "http://api.lemonban.com/futureloan/member/login"

        headers_dict = {
            "X-Lemonban-Media-Type": "lemonban.v2",
            "User-Agent": "Mozilla/5.0 LookSky"
        }

        cls.do_request.add_headers(headers_dict)

    @classmethod
    def tearDownClass(cls):
        cls.do_request.close()

    # 2、创建测试用例测试方法，一定要以test_作为前缀
    def test_01_login_success(self):

        request_param = {
            "mobile_phone": "18511113469",
            "pwd": "12345678"
        }

        # 4、发起请求
        res = self.do_request.send("POST", self.url, json=request_param)

        # 5、提取响应数据，然后断言结果
        expected_value = "token_info"
        # real_code = res.json()["code"]
        try:
            self.assertIn(expected_value, res.text, "测试登录接口的正向用例失败")
        except AssertionError as e:
            print("此处需要使用日志器来记录日志！")
            print(f"具体异常为：{e}")
            raise e

    def test_02_no_password(self):

        request_param = {
            "mobile_phone": "18511113459",
            "pwd": ""
        }
        # 4、发起请求
        res = self.do_request.send("POST", self.url, json=request_param)

        # 5、提取响应数据，然后断言结果
        expected_value = 1
        real_code = res.json()["code"]

        try:
            self.assertEqual(expected_value, real_code, "测试密码为空失败")
        except AssertionError as e:
            print("此处需要使用日志器来记录日志！")
            print(f"具体异常为：{e}")
            raise e


if __name__ == '__main__':
    unittest.main()
