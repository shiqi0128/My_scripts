import requests
import os
from time import sleep
from interfaceTest.GMALL.gmall_header import golbal_shopid, host, header
from interfaceTest.GMALL.gmall_all.color import out_format

# host, header, token = get_header_pc()
# out_format(os.getcwd())


# 顾客行为——顾客画像API
class cus_portrait(object):

    """

    定义一个wiki顾客行为Tab中菜单名为顾客画像的所有接口测试类

    """
    def get_the_whole_race(self, shop_id=golbal_shopid):
        """获取全部人种"""
        url = host + "/api/shops/%s/races" % shop_id
        r = requests.get(url=url, headers=header).json()
        out_format("获取全部人种:", r)

    def customers_list(self, shop_id=golbal_shopid):
        """顾客列表"""
        url = host + "/api/shops/%s/customers" % shop_id
        r = requests.get(url=url, headers=header).json()
        out_format("顾客列表:", r)

    def cuslist_export(self, shop_id=golbal_shopid):
        """顾客列表 导出"""
        url = host + "/api/shops/%s/customers/export" % shop_id
        r = requests.get(url=url, headers=header)
        out_format("顾客列表 导出:", r.text)

    def customer_details(self, shop_id=golbal_shopid):
        """顾客详情"""
        url = host + "/api/shops/%s/customers/%s" % (shop_id, 85)
        r = requests.get(url=url, headers=header).json()
        out_format("顾客详情:", r)

    def remove_customer(self, shop_id=golbal_shopid):
        """移除人脸"""
        url = host + "/api/shops/%s/customers/%s/remove-face" % (shop_id, 85)
        data = {"face_id": "7f63821abaeed67a32ce03e9fc212c21"}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("移出人脸:", r)

    def update_info(self, shop_id=golbal_shopid):
        """顾客详情部分信息保存"""
        url = host + "/api/shops/%s/customers/%s/update-info" % (shop_id, 1)
        r = requests.post(url=url, headers=header, json={"tag_ids": [2, 3]}).json()
        out_format("顾客详情部分信息保存:", r)

    def cus_portrait(self, start_date, end_date, shop_id=golbal_shopid):
        """客群画像"""
        url = host + "/api/shops/%s/group-stats?group_id=0" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("客群画像:", r)
        return r

    def customers_ranking(self, start_time, end_time, shop_id=golbal_shopid):
        """顾客画像Top排名"""
        url = host + "/api/shops/%s/customers-ranking" % shop_id
        data = {"start_date": start_time, "end_date": end_time}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("顾客画像Top排名:", r)
        return r

    def trend_monitoring(self, start_date, end_date, types_key, types_value, shop_id=golbal_shopid):
        """数据趋势"""
        url = host + "/api/shops/%s/distribution-stats?type=%s&age=1&gender=2" % (shop_id, types_key)
        data = {"start_date": start_date, "end_date": end_date, "group_id": 0}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("数据趋势type=%s[%s]" % (types_key, types_value), r)
        return r

    def trend_monitoring_export(self, start_date, end_date, types, shop_id=golbal_shopid):
        """数据趋势 导出"""
        url = host + "/api/shops/%s/distribution/export?type=%s&age=1&gender=2" % (shop_id, types)
        data = {"start_date": start_date, "end_date": end_date, "group_id": 0}
        r = requests.get(url=url, headers=header, params=data)
        out_format("数据趋势导出:", r.text)
        return r


cus_portrait().customer_details()
cus_portrait().remove_customer()