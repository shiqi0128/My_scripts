import unittest
import requests
import os
from time import sleep
from interfaceTest.GMALL.gmall_header import golbal_shopid, host, header

# host, header, token = get_header_pc()
# print(os.getcwd())


# 顾客行为——动线&热力 API
class line_heat(object):
    """定义一个动线&热力相关接口的测试类"""
    def line_analysis(self, date, shop_id=golbal_shopid):
        """动线排行"""
        url_15 = host + "/api/shops/%s/top-lines" % shop_id
        data = {"date": date}
        r_15 = requests.get(url=url_15, headers=header, params=data).json()
        print("动线排行:", r_15, "\n\n")
        return r_15

    def heat_map(self, start_time, end_time, shop_id=golbal_shopid):
        """店面热力图(每分钟)"""
        url_16 = host + "/api/shops/%s/heat-map" % shop_id
        data = {"start_time": start_time, "end_time": end_time}
        r_16 = requests.get(url=url_16, headers=header, params=data).json()
        print("店面热力图(每分钟):", r_16, "\n\n")
        return r_16
