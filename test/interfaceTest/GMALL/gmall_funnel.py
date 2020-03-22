import unittest
import requests
import json
import os
from time import sleep
from gmall_header import get_header_pc
from urllib3 import encode_multipart_formdata

host, header, token = get_header_pc()
# data = fenzhuang()

"""顾客漏斗接口测试脚本"""
class funnel(unittest.TestCase):
    """定义一个测试类"""
    def test_01_order_list(self):
        url_01 = host + "/api/shops/%s/orders" % 25
        r_01 = requests.get(url=url_01, headers=header).json()
        print("订单列表:", r_01, "\n\n")
    # def test_01_funnel_list(self):
    #     url_01=host + "/api/shops/%s/customer-buy-conversion" % 25
    #     data = {"start_date": "2017-12-01", "end_date": "2017-12-01"}
    #     r_01 = requests.get(url=url_01, headers=header, params=data).json()
    #     print("顾客漏斗列表:", r_01, "\n\n")
    #     self.assertEqual(r_01["code"], 0)
    #
    # def test_02_f


if __name__ == "__main__":
    unittest.main()
