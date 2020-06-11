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

import ddt
from scripts.handle_request import HandleRequest
from scripts.handle_excel import HandleExcel
from scripts.handle_yaml import do_yaml
from scripts.handle_log import do_log


@ddt.ddt
class TestLogin(unittest.TestCase):
    do_excel = HandleExcel(do_yaml.get_data("excel", "filename"), "login")
    testcases_data = do_excel.read_data()  # 嵌套字典的列表

    @classmethod
    def setUpClass(cls):
        # 3、构造请求参数
        cls.do_request = HandleRequest()

        cls.do_request.add_headers(do_yaml.get_data("api", "api_version"))
        do_log.info("开始执行用例")

    @classmethod
    def tearDownClass(cls):
        cls.do_request.close()
        do_log.info("用例执行结束")

    @ddt.data(*testcases_data)
    def test_login(self, one_testcase):

        new_url = do_yaml.get_data("api", "base_url") + one_testcase.url
        res = self.do_request.send(one_testcase.method,
                                   new_url,
                                   json=one_testcase.data)

        # real_code = res.json()["code"]
        try:
            self.assertIn(one_testcase.expected_value,
                          res.text,
                          one_testcase.name)
        except AssertionError as e:
            # my_logger.error(f"{one_testcase.name}：具体异常为{e}")
            do_log.error(f"{one_testcase.name}：具体异常为{e}")
            self.do_excel.write_data(one_testcase, res.text, "失败")
            raise e
        else:
            self.do_excel.write_data(one_testcase, res.text, "成功")


if __name__ == '__main__':
    unittest.main()
