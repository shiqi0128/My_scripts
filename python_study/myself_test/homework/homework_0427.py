"""
-------------------------------------------------
  @Time : 2020/4/27 20:41 
  @Auth : 十七
  @File : homework_0427.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
# 20200427_unittest单元测试
# 一、必做题
# 1.使用unittest框架来测试登录接口
import unittest
import requests
from homework.homework_0424 import HandleRequest


class TestRegister(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            """构造请求参数"""
            print("setUpClass\n")
            cls.do_request = HandleRequest()
            cls.register_url = "http://api.lemonban.com/futureloan/member/login"
            headers_dict = {
                "X-Lemonban-Media-Type": "lemonban.v2",
                "User-Agent": "Mozilla/5.0 LookSky"
            }

            cls.do_request.add_headers(headers_dict)

        @classmethod
        def tearDownClass(cls):
            print("tearDownClass")
            cls.do_request.close()
            
        def test_1register_success(self):
            """登录
            :param:mobile_phone:手机号
            :param:pwd:密码
            """
            requests_params = {
                "mobile_phone": "18150511512",
                "pwd": "12345678",
            }
            # 4、发起请求
            res = TestRegister.do_request.send("POST", TestRegister.register_url, json=requests_params)

            # 5、提取响应数据，然后断言结果
            expected_value = 0
            real_code = res.json()["code"]
            self.assertEqual(expected_value, real_code, "测试登录接口的正向用例失败")

        def test_2no_mobile(self):
            request_param = {
                "pwd": "12345678"
            }
            # 4、发起请求
            res = TestRegister.do_request.send("POST", TestRegister.register_url, json=request_param)

            # 5、提取响应数据，然后断言结果
            expected_value = 2
            real_code = res.json()["code"]

            self.assertEqual(expected_value, real_code, "测试手机号为空失败")
            print("测试手机号为")

        def test_3no_pwd(self):
            request_param = {
                "mobile_phone": "18150511517"
            }
            # 4、发起请求
            res = TestRegister.do_request.send("POST", TestRegister.register_url, json=request_param)

            # 5、提取响应数据，然后断言结果
            expected_value = 2
            real_code = res.json()["code"]

            self.assertEqual(expected_value, real_code, "测试密码为空失败")

        def test_4no_mobile_no_pwd(self):
            request_param = {}
            # 4、发起请求
            res = TestRegister.do_request.send("POST", TestRegister.register_url, json=request_param)

            # 5、提取响应数据，然后断言结果
            expected_value = 2
            real_code = res.json()["code"]

            self.assertEqual(expected_value, real_code, "测试账号密码为空失败")

        def test_5unregistered_mobile(self):
            request_param = {
                "mobile_phone": "18150511520",
                "pwd": "12345678"
            }
            # 4、发起请求
            res = TestRegister.do_request.send("POST", TestRegister.register_url, json=request_param)

            # 5、提取响应数据，然后断言结果
            expected_value = 1001
            real_code = res.json()["code"]

            self.assertEqual(expected_value, real_code, "测试未注册的账号登录失败")

        def test_6error_mobile(self):
            request_param = {
                "mobile_phone": "181505115zx",
                "pwd": "12345678"
            }
            # 4、发起请求
            res = TestRegister.do_request.send("POST", TestRegister.register_url, json=request_param)

            # 5、提取响应数据，然后断言结果
            expected_value = 2
            real_code = res.json()["code"]

            self.assertEqual(expected_value, real_code, "测试手机号输入格式错误失败")

        def test_7long_mobile(self):
            request_param = {
                "mobile_phone": "181505115zx",
                "pwd": "12345678"
            }
            # 4、发起请求
            res = TestRegister.do_request.send("POST", TestRegister.register_url, json=request_param)

            # 5、提取响应数据，然后断言结果
            expected_value = 2
            real_code = res.json()["code"]

            self.assertEqual(expected_value, real_code, "测试手机号超过11位失败")


if __name__ == '__main__':
    unittest.main()

# 2.当前使用unittest框架对接口进行测试，有哪些痛点（改进的地方）？
# 二、选做题
# 1.对课堂上学的HandleRequest类，进一步封装，需要实现，不管传字典还是json字符串参数都能成功处理
# 提示：可以判断传递的是否为字符串类型，使用json.loads()转化

