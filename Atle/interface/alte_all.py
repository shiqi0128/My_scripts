import unittest
import requests
import random
import time
from Atle.interface.test071801 import alte

alte = alte()


class aiitle_test(unittest.TestCase):
    """

    定义一个爱它乐的测试类

    """
    # def test_01_moblie_pass(self):
    #     r = alte.moblie_pass()
    #     self.assertEqual(r["msg"], "登录成功")

    def test_02_get_goods(self):
        """
        获取单品
        :return:
        """
        r = alte.get_goods()
        self.assertEqual(r["code"], 1)

    def test_03_comment_list(self):
        """
        评论列表
        :return:
        """
        r = alte.comment_list()
        self.assertEqual(r["code"], 1)


if __name__ == "__main__":
    unittest.main()
else:
    print("false")