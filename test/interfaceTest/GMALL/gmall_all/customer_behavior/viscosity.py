import requests
import os
from time import sleep
from interfaceTest.GMALL.gmall_header import golbal_shopid, host, header

# host, header, token = get_header_pc()
# print(os.getcwd())


# 顾客行为——顾客粘度 API
class viscosity(object):
    """

    定义一个wiki顾客行为Tab中菜单名为顾客粘度的所有接口测试类

    """
    def livenessCompare(self, date, shop_id=golbal_shopid):
        """活跃度环比"""
        url_17 = host + "/api/shops/%s/liveness-compare" % shop_id
        data = {"date": date}
        r_17 = requests.get(url=url_17, headers=header, params=data).json()
        print("活跃度环比:", r_17, "\n")
        return r_17

    def dailyRangeLiveness(self, start_date, end_date, shop_id=golbal_shopid):
        """活跃度列表"""
        url_18 = host + "/api/shops/%s/daily-range-liveness" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r_18 = requests.get(url=url_18, headers=header, params=data).json()
        print("活跃度列表:", r_18, "\n")
        return r_18

    def liveness_export(self, start_date, end_date, shop_id=golbal_shopid):
        """活跃度导出CSV"""
        url_19 = host + "/api/shops/%s/liveness/export" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r_19 = requests.get(url=url_19, headers=header, params=data)
        print("活跃度导出CSV:", r_19.text, "\n")
        return r_19

    def weekLivenessList(self, start_date, end_date, shop_id=golbal_shopid):
        """活跃天数列表（周)"""
        url_20 = host + "/api/shops/%s/liveness-week" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r_20 = requests.get(url=url_20, headers=header, params=data).json()
        print("活跃天数列表(周):", r_20, "\n")
        return r_20

    def monthLivenessList(self, start_date, end_date, shop_id=golbal_shopid):
        """活跃天数列表（月）"""
        url_21 = host + "/api/shops/%s/liveness-month" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r_21 = requests.get(url=url_21, headers=header, params=data).json()
        print("活跃天数列表(月):", r_21, "\n")
        return r_21

    def liveness_list_export(self, start_date, end_date, shop_id=golbal_shopid):
        """活跃天数导出CSV"""
        url_22 = host + "/api/shops/%s/liveness-list/export" % shop_id
        data = {"start_date": start_date, "end_date": end_date, "type": "week"}
        r_22 = requests.get(url=url_22, headers=header, params=data)
        print("活跃天数导出CSV:", r_22.text, "\n")
        return r_22
