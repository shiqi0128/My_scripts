import requests
import os
from time import sleep
from interfaceTest.GMALL.gmall_header import host, header

# host, header, token = get_header_pc()
# print(os.getcwd())


# 门店罗盘API
class gmall_stores_compass(object):
    """定义一个门店罗盘相关接口的测试类"""

    def daily_stats(self, date):
        """本门店统计（每天）"""
        url_04 = host + "/api/shops/%s/daily-stats" % 25
        data = {"date": date}
        r_04 = requests.get(url=url_04, headers=header, params=data).json()
        print("本门店统计(每天)", r_04, "\n\n")
        return r_04

    def current_stats(self):
        """本门店在线人数&最热区域"""
        url_05 = host + "/api/shops/%s/current-stats" % 25
        r_05 = requests.get(url=url_05, headers=header).json()
        print("本门店在线人数&最热区域", r_05, "\n\n")

    def minutelyShopStats(self):
        """本门店统计（每分钟）"""
        url_06 = host + "/api/shops/%s/minutely-stats" % 25
        r_06 = requests.get(url=url_06, headers=header).json()
        print("本门店统计(每分钟):", r_06, "\n\n")

    def hourlyShopStats(self):
        """本门店统计（每小时）"""
        url_07 = host + "/api/shops/%s/hourly-stats" % 25
        r_07 = requests.get(url=url_07, headers=header).json()
        print("本门店统计(每小时):", r_07, "\n\n")

    def hourly_stats_export(self, date):
        """本门店统计（每小时）导出"""
        url_08 = host + "/api/shops/%s/hourly-stats/export" % 25
        data = {"date": date}
        r_08 = requests.get(url=url_08, headers=header, params=data)
        print("本门店统计（每小时）导出", r_08.text, "\n\n")
        return r_08

    def daily_range_stats(self, start_date, end_date):
        """本门店统计（每天）连续多日"""
        url_09 = host + "/api/shops/%s/daily-range-stats" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_09 = requests.get(url=url_09, headers=header, params=data).json()
        print("本门店统计（每天）连续多日:", r_09, "\n\n")
        return r_09

    def daily_range_stats_export(self, start_date, end_date):
        """本门店统计（每小时）导出"""
        url_10 = host + "/api/shops/%s/hourly-stats/export" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_10 = requests.get(url=url_10, headers=header, params=data)
        print("本门店统计（每天）连续多日:", r_10.text, "\n\n")
        return r_10

    def store_areas(self):
        """门店区域信息"""
        url_11 = host + "/api/shops/%s" % 25
        r_11 = requests.get(url=url_11, headers=header).json()
        print("门店区域信息:", r_11, "\n\n")

    def dailyZoneStats(self, date):
        """区域客流统计（每天）"""
        url_12 = host + "/api/shops/%s/daily-zone-stats" % 25
        data = {"date": date}
        r_12 = requests.get(url=url_12, headers=header, params=data).json()
        print("区域客流统计（每天):", r_12, "\n\n")
        return r_12

    def hourlyZoneStats(self, date):
        """区域客流统计（每小时）"""
        url_13 = host + "/api/shops/%s/hourly-zone-stats" % 25
        data = {"date": date}
        r_13 = requests.get(url=url_13, headers=header, params=data).json()
        print("区域客流统计（每小时):", r_13, "\n\n")
        return r_13

    def zone_daily_range_stats(self, start_date, end_date):
        """区域客流-连续多日（每日)"""
        url_14 = host + "/api/shops/%s/zone-daily-range-stats" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_14 = requests.get(url=url_14, headers=header, params=data).json()
        print("区域客流-连续多日（每日)", r_14, "\n\n")
        return r_14

