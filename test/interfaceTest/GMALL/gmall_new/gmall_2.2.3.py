import unittest
import requests
import json
import os
from time import sleep
from interfaceTest.GMALL.gmall_new.invoke_fun import Passenger_flow
from urllib3 import encode_multipart_formdata
# from gmall_creatnum import camera

ss = Passenger_flow()
# capita = camera()
"""2.2.3经营分析、客流/交流测试脚本---正常场景"""


class test_passenger_flow(unittest.TestCase):
    """定义一个2.2.3的测试类"""

    def dailyRangeShopStats(self):
        """本门店统计（每天）连续多日---下面的顾客人数的接口需要调用该接口计算出日期选择范围内的顾客总人数"""
        ss.dailyRangeShopStats()            # 类名.方法名调用

    def test_01_passenger_flow(self):
        """客流模型_顾客人数"""
        a = ss.passenger_flow("2019-01-10", "customer_number")
        sum_01_new = a[1]
        r_01_new = a[0]
        self.assertEqual(r_01_new["data"]["list"][0]["f1"], str(sum_01_new))

    def test_02_Stores_length(self):
        """客流模型_逛店时长"""
        ss.Stores_length("2019-01-10")
        # self.assertEqual()

    # def test_03_indicator(self):
    #     """经营指标"""
    #     sum_new = ss.order_management(start_date="2018-12-20", end_date="2018-12-28")
    #     # sum_new = ss.order_management()
    #     r_21_new, daily_sales_new = ss.indicator(start_date="2018-12-20", end_date="2018-12-28")
    #     avg_order_amount = r_21_new["data"]["stats"]["total"]["avg_order_amount"]
    #     order_amount = r_21_new["data"]["stats"]["total"]["order_amount"]
    #     self.assertEqual(avg_order_amount, str(daily_sales_new)) # 断言日均销售额
    #     self.assertEqual(str(order_amount), sum_new)   # 断言销售额，经营指标内提取出的销售额与订单列表提取的选择日期范围的销售额相加的总销售额对比相等
    #     self.assertEqual(["code"], 0)
    #
    # # def test_order_management(self):
    # #     """订单列表"""
    # #     r_21_new_01 = self.indicator()


if __name__ == "__main__":
    unittest.main()
else:
    print("false")