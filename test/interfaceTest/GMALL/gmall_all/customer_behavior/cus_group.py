import requests
import os
from time import sleep
from interfaceTest.GMALL.gmall_header import golbal_shopid, host, header

# host, header, token = get_header_pc()
# print(os.getcwd())


# 顾客行为——客群管理API
class cus_group(object):

    """

    定义一个wiki顾客行为Tab中菜单名为客群管理的所有接口测试类

    """
    def customer_charts(self, date, shop_id=golbal_shopid):
        """客群管理_门店报表"""
        url = host + "/api/shops/%s/customer-charts" % shop_id
        data = {"date": date}
        r = requests.get(url=url, headers=header, params=data).json()
        print("客群管理_门店报表:", r, "\n\n")
        return r

    def customer_visit_list(self, shop_id=golbal_shopid):
        """顾客历史来店信息"""
        url = host + "/api/shops/%s/customers/%s/visit-list" % (shop_id, 216)
        r = requests.get(url=url, headers=header).json()
        print("顾客历史来店信息:", r, "\n\n")

    def customer_entry_records(self, start_date, end_date, shop_id=golbal_shopid):
        """顾客进店记录"""
        url = host + "/api/shops/%s/customers/%s/entry-records" % (shop_id, 218)
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header).json()
        print("顾客进店记录", r, "\n\n")

    # def user_portrait(self, shop_id=golbal_shopid):
    #     """用户画像"""
    #     url = host + "/api/shops/%s/customers-minutely" % shop_id
    #     r = requests.get(url=url, headers=header).json()
    #     print("用户画像:", r, "\n\n")
    #
    # def Customer_informa(self, shop_id=golbal_shopid):
    #     """顾客信息"""
    #     url = host + "/api/shops/%s/customers/%s/lines/%s" % (shop_id, 219, 2)