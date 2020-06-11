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
# from handle_yaml import HandleYaml
from handle_yaml import do_yaml
from handle_log import do_log

# do_yaml = HandleYaml()


# 1、使用ddt.ddt作为类的装饰器
@ddt.ddt
class TestRegister(unittest.TestCase):
    # excel_filename = "testcase.xlsx"
    do_excel = HandleExcel(do_yaml.get_data("excel", "filename"), "register")
    testcases_data = do_excel.read_data()  # 嵌套字典的列表

    @classmethod
    def setUpClass(cls):
        # 3、构造请求参数
        cls.do_request = HandleRequest()

        # headers_dict = {
        #     "X-Lemonban-Media-Type": "lemonban.v2"
        # }
        cls.do_request.add_headers(do_yaml.get_data("api", "api_version"))
        do_log.info("开始执行用例")

    @classmethod
    def tearDownClass(cls):
        cls.do_request.close()
        do_log.info("用例执行结束")

    """
    @ddt.data(*testcases_data)
    def test_register(self, testcase_dict):
        # testcase_dict.method
        
        res = self.do_request.send(testcase_dict["method"],
                                   testcase_dict["url"],
                                   json=testcase_dict["data"])

        real_code = res.json()["code"]
        row = testcase_dict["id"] + 1
        self.do_excel.write_data(row, 7, res.text)
        name = testcase_dict["name"]
        try:
            self.assertEqual(testcase_dict["expected_value"],
                             real_code,
                             testcase_dict["name"])
        except AssertionError as e:
            # print("此处需要使用日志器来记录日志！")
            my_logger.error(f"{name}：具体异常为{e}")
            # print(f"具体异常为：{e}")
            self.do_excel.write_data(row, 8, "失败")
            raise e
        else:
            self.do_excel.write_data(row, 8, "成功")
    """

    @ddt.data(*testcases_data)
    def test_register(self, one_testcase):

        new_url = do_yaml.get_data("api", "base_url") + one_testcase.url
        res = self.do_request.send(one_testcase.method,
                                   new_url,
                                   json=one_testcase.data)

        real_code = res.json()["code"]
        # row = testcase_dict["id"] + 1
        # self.do_excel.write_data(row, 7, res.text)
        # name = testcase_dict["name"]
        try:
            self.assertEqual(one_testcase.expected_value,
                             real_code,
                             one_testcase.name)
        except AssertionError as e:
            # print("此处需要使用日志器来记录日志！")
            # my_logger.error(f"{one_testcase.name}：具体异常为{e}")
            do_log.error(f"{one_testcase.name}：具体异常为{e}")
            # print(f"具体异常为：{e}")
            # self.do_excel.write_data(row, 8, "失败")
            self.do_excel.write_data(one_testcase, res.text, "失败")
            raise e
        else:
            # self.do_excel.write_data(row, 8, "成功")
            # do_log.debug(res.text)
            self.do_excel.write_data(one_testcase, res.text, "成功")


if __name__ == '__main__':
    unittest.main()
