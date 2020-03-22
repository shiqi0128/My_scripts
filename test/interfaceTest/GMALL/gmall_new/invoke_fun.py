import unittest
import requests
import json
import os
from time import sleep
import datetime
from interfaceTest.GMALL.gmall_header import get_header_pc
from interfaceTest.GMALL.rounding_off import round_up
from urllib3 import encode_multipart_formdata
# from gmall_creatnum import camera

host, header, token = get_header_pc()

# capita = camera()

"""2.2.3经营分析、客流/交流测试脚本---正常场景"""


class Passenger_flow(object):

    def dailyRangeShopStats(self):
        """本门店统计（每天）连续多日---下面的顾客人数的接口需要调用该接口计算出日期选择范围内的顾客总人数"""
        url_00 = host + "/api/shops/%s/daily-range-stats" % 25
        data = {"start_date": "2019-01-18", "end_date": "2019-01-20"}
        r_00 = requests.get(url=url_00, headers=header, params=data).json()
        # self.assertEqual(r_00["code"], 0)
        print("本门店统计（每天）连续多日:", r_00, "\n")
        s = len(r_00["data"]["stats"])
        print(s)
        sum = 0  # 先把sum赋值=0
        for i in range(s):
            customer_num = r_00["data"]["stats"][i]["customer_num"]
            # print(customer_num)
            sum += customer_num
        print("顾客总人数customer_num =", sum)
        return sum

    def passenger_flow(self, date, type):
        """客流模型_顾客人数"""
        sum_01 = self.dailyRangeShopStats()
        url_01 = host + "/api/shops/25/customer-rf"
        data = {"date": date, "type": type}
        r_01 = requests.get(url=url_01, headers=header, params=data).json()
        print("RF模型_顾客人数:", r_01, "\n\n")
        return r_01, sum_01
        # assert(r_01["data"]["list"][0]["f1"] == str(sum_01))     # f1=1，这个1是字符串，所以需要在变量前加str把数值型转成字符型

    def Stores_length(self, date):
        """客流模型_逛店时长"""
        url_02 = host + "/api/shops/25/customer-rf"
        data = {"date": date, "type": "customer_seconds"}
        r_02 = requests.get(url=url_02, headers=header, params=data).json()
        print("RF模型_逛店时长:", r_02, "\n\n")

    # def indicator(self, start_date, end_date):
    #     """经营指标_日均销售额"""
    #     m1 = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    #     m2 = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    #     dates = (m2-m1).days     # 计算出选择时间段的总天数
    #     print("相减的天数:", dates)
    #     url_21 = host + "/api/shops/25/manage/indicator"
    #     data = {"start_date": start_date, "end_date": end_date}
    #     r_21 = requests.get(url=url_21, headers=header, params=data).json()
    #     print("经营指标:", r_21, "\n\n")
    #     order_amount = r_21["data"]["stats"]["total"]["order_amount"]  # 返回结果取出销售额的值为了后面根据公式计算出日均销售额的结果
    #     print("order_amount:", order_amount)
    #     daily_sales = float(order_amount) / (dates+1)                               # 销售额/选择的天数=日均销售额
    #     # w = r_21["data"]["stats"]["total"]["avg_order_amount"]    # 返回的结果取出日均销售额的值与上面计算的结果对比正确则一致
    #     # daily_sales = daily_sales_rq    # 需要验证这2个结果是不是一致
    #     new_order_amount = r_21["data"]["stats"]["total"]["new_order_amount"]  # 返回结果取出的新客销售额
    #     return r_21, round_up(daily_sales, 2)

    # def order_management(self, start_date, end_date):
    #     """订单列表"""
    #     url_03 = host + "/api/shops/25/orders"
    #     data = {"start_date": start_date, "end_date": end_date}
    #     r_03 = requests.get(url=url_03, headers=header, params=data).json()
    #     print("订单列表:", r_03, "\n")
    #     amount_path = r_03["data"]["orderList"]["data"]
    #     s = len(amount_path)
    #     print(s)
    #     sum = 0
    #     for i in range(s):
    #         order_amount = amount_path[i]["order_amount"]
    #         sum += float(order_amount)
    #     sum1 = "%.2f" % sum
    #     print("销售额总和:", sum1)
    #     return sum1


# Passenger_flow().dailyRangeShopStats()
# Passenger_flow().passenger_flow()
# Passenger_flow().Stores_length()
# Passenger_flow().indicator()
# Passenger_flow().order_management("2018-12-20", "2018-12-28")



