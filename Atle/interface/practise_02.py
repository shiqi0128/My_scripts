import unittest
import requests
import random
import time
from Atle.interface.practise_01 import comment_list

# alte = comment_list()


class aiitle_test(unittest.TestCase):
    """

    定义一个所有的测试类

    """
    def test_comment_list(self):
        """
        评论列表
        :return:
        """
        r_01 = comment_list()
        # b = r_01["msg"]
        # print(r_01)
        self.assertEqual(r_01["code"], 1)


# comment_list()
if __name__ == "__main__":
    unittest.main()
else:
    print("false")
