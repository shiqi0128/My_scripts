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

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 2、创建测试用例测试方法，一定要以test_作为前缀
    def test_1register_success(self):
        # 3、构造请求参数
        do_request = HandleRequest()
        register_url = "http://api.lemonban.com/futureloan/member/register"

        headers_dict = {
            "X-Lemonban-Media-Type": "lemonban.v2",
            "User-Agent": "Mozilla/5.0 LookSky"
        }

        do_request.add_headers(headers_dict)

        request_param = {
            "mobile_phone": "18511112247",
            "pwd": "12345678"
        }

        # 4、发起请求
        res = do_request.send("POST", register_url, json=request_param)

        # 5、提取响应数据，然后断言结果
        expected_value = 0
        real_code = res.json()["code"]

        # if expected_value == real_code:
        #     print("恭喜您，测试成功，此接口没问题！")
        # else:
        #     print("不好意思，测试失败，此接口有问题！")

        # self.assertEqual方法
        # a、是从父类中继承的方法
        # b、第一个参数，往往指定为期望值
        # c、第二参数，往往指定为实际值
        # d、第三参数，往往指定为断言失败之后的错误提示
        # e、如果期望值和实际值不匹配，那么会抛出AssertionError
        # f、可以写多个断言方法，会依次去断言，只要断言失败，同一方法中的其他断言不会执行
        self.assertEqual(expected_value, real_code, "测试注册接口的正向用例失败")
        self.assertIn("OK", res.text, "测试注册接口的正向用例失败")

    def test_2no_mobile(self):
        # 3、构造请求参数
        do_request = HandleRequest()
        register_url = "http://api.lemonban.com/futureloan/member/register"

        headers_dict = {
            "X-Lemonban-Media-Type": "lemonban.v2",
            "User-Agent": "Mozilla/5.0 LookSky"
        }

        do_request.add_headers(headers_dict)

        request_param = {
            "pwd": "12345678"
        }

        # 4、发起请求
        res = do_request.send("POST", register_url, json=request_param)

        # 5、提取响应数据，然后断言结果
        expected_value = 2
        real_code = res.json()["code"]

        self.assertEqual(expected_value, real_code, "测试手机号为空失败")

    def test_3_10_mobile(self):
        # 3、构造请求参数
        do_request = HandleRequest()
        register_url = "http://api.lemonban.com/futureloan/member/register"

        headers_dict = {
            "X-Lemonban-Media-Type": "lemonban.v2",
            "User-Agent": "Mozilla/5.0 LookSky"
        }

        do_request.add_headers(headers_dict)

        request_param = {
            "mobile_phone": "1851111224",
            "pwd": "12345678"
        }

        # 4、发起请求
        res = do_request.send("POST", register_url, json=request_param)

        # 5、提取响应数据，然后断言结果
        expected_value = 1000
        real_code = res.json()["code"]
        print("test_3_10_mobile")

        print(1/0)
        # self.assertEqual(expected_value, real_code, "测试手机号为空失败")


if __name__ == '__main__':
    unittest.main()
    # 如何执行unittest框架？
    # a、把鼠标定位到类名上，然后鼠标右击，点运行，会执行所有用例
    # b、把鼠标定位到测试用例实例方法上，然后鼠标右击，点运行，仅执行当前用例
    # c、直接在unittest.main()处，鼠标右击，点运行，会执行所有用例

    # 用例执行顺序
    # 按照测试用例实例方法名，asscii数值从小到大排序

    # 统计的用例总数：test_开头的实例方法个数
    # 统计的失败用例数：只要抛出异常，就会统计失败的实例个数（test_）
    # 统计的成功用例数：实例方法（test_）没有抛出异常的数量
