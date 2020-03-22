import requests
import os
from time import sleep
from interfaceTest.GMALL.gmall_header import golbal_shopid, host, header

# host, header, token = get_header_pc()
# print(os.getcwd())


# 顾客行为——顾客行为
class gmall_customer_behavior(object):
    """

    定义一个wiki顾客行为Tab中菜单名为顾客行为的所有接口测试类

    """

    def zone_sankey_stats(self, start_date, end_date, shop_id=golbal_shopid):
        """本门店区域动线统计（用于桑基图显示）"""
        url = host + "/api/shops/%s/zone-sankey-stats" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header, params=data).json()
        print("本门店区域动线统计（用于桑基图显示）:", r, "\n\n")

    def depth_stats(self, start_date, end_date, shop_id=golbal_shopid):
        """深度分析统计（人均逛店深度/次均逛店深度)"""
        url = host + "/api/shops/%s/depth-stats" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header, params=data).json()
        print("深度分析统计（人均逛店深度/次均逛店深度):", r, "\n\n")

    def depth_stats_export(self, start_date, end_date, shop_id=golbal_shopid):
        """深度分析统计导出（人均逛店深度 / 次均逛店深度)"""
        url = host + "/api/shops/%s/depth-stats/export" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header, params=data)
        print("深度分析统计导出（人均逛店深度 / 次均逛店深度):", r.text, "\n\n")

    def line_chord(self, start_date, end_date, shop_id=golbal_shopid):
        """和弦图"""
        url = host + "/api/shops/%s/line-chord" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header, params=data).json()
        print("和弦图:", r, "\n\n")

    def line_chord_export(self, start_date, end_date, shop_id=golbal_shopid):
        """和弦图 数据导出CSV"""
        url = host + "/api/shops/%s/export/line-chord" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header, params=data)
        print("和弦图 数据导出CSV:", r.text, "\n\n")

    def stay_time(self, start_date, end_date, shop_id=golbal_shopid):
        """逛店时长（人次 均次 每天）连续多日---start_date, end_date必填项"""
        url = host + "/api/shops/%s/stay-time" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header, params=data).json()
        print("逛店时长（人次 均次 每天）连续多日:", r, "\n\n")

    def stay_time_export(self, start_date, end_date, shop_id=golbal_shopid):
        """逛店时长（人次 均次 每天）连续多日-导出CSV---start_date, end_date必填项"""
        url = host + "/api/shops/%s/stay-time/export" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header, params=data)
        print("逛店时长（人次 均次 每天）连续多日:", r.text, "\n\n")

    def enter_shop_frequency_daily(self, date, shop_id=golbal_shopid):
        """逛店频率（日）---date必填项"""
        url = host + "/api/shops/%s/enter-shop-frequency-daily" % shop_id
        data = {"date": date}
        r = requests.get(url=url, headers=header, params=data).json()
        print("逛店频率（日）:", r, "\n\n")

    def enter_shop_frequency_daily_export(self, date, shop_id=golbal_shopid):
        """逛店频率（日）导出---date必填项"""
        url = host + "/api/shops/%s/enter-shop-frequency-daily/export" % shop_id
        data = {"date": date}
        r = requests.get(url=url, headers=header, params=data)
        print("逛店频率（日）导出:", r.text, "\n")
        return r

    def enter_shop_frequency_weekly(self, start_date, end_date, shop_id=golbal_shopid):
        """逛店频率（周）---start_date, end_date必填项"""
        url = host + "/api/shops/%s/enter-shop-frequency-weekly" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header, params=data).json()
        print("逛店频率（周）:", r, "\n\n")

    def enter_shop_frequency_weekly_export(self, start_date, end_date, shop_id=golbal_shopid):
        """逛店频率（周）导出CSV---start_date, end_date必填项"""
        url = host + "/api/shops/%s/enter-shop-frequency-weekly/export/" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header, params=data)
        print("逛店频率（周）导出CSV:", r.text, "\n\n")

    def enter_shop_frequency_monthly(self, year, month, shop_id=golbal_shopid):
        """逛店频率（月）---year, month必填项"""
        url = host + "/api/shops/%s/enter-shop-frequency-monthly" % shop_id
        data = {"year": year, "month": month}
        r = requests.get(url=url, headers=header, params=data).json()
        print("逛店频率（月）:", r, "\n\n")

    def enter_shop_frequency_monthly_export(self, year, month, shop_id=golbal_shopid):
        """逛店频率（月）导出CSV---year, month必填项"""
        url = host + "/api/shops/%s/enter-shop-frequency-monthly/export/" % shop_id
        data = {"year": year, "month": month}
        r = requests.get(url=url, headers=header, params=data)
        print("逛店频率（月）导出CSV:", r.text, "\n\n")

    def zone_hourly_range_stats(self, start_date, end_date, shop_id=golbal_shopid):
        """区域统计（每小时）连续多日---start_date, end_date必填项"""
        url = host + "/api/shops/%s/zone-hourly-range-stats" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header, params=data).json()
        print("区域统计（每小时）连续多日:", r, "\n\n")

    def zone_range_average_time_stats(self, start_date, end_date, shop_id=golbal_shopid):
        """区域统计连续多日 顾客总数&平均停留时长---start_date, end_date必填项"""
        url = host + "/api/shops/%s/zone-range-average-time-stats" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header, params=data).json()
        print("区域统计连续多日 顾客总数&平均停留时长:", r, "\n\n")

    def historical_data_compare(self, date, shop_id=golbal_shopid):
        """本门店历史数据环比"""
        url = host + "/api/shops/%s/historical-data-compare" % shop_id
        data = {"date": date}
        r = requests.get(url=url, headers=header, params=data).json()
        print("本门店历史数据环比:", r, "\n\n")

    def branch_line_stats(self, start_date, end_date, shop_id=golbal_shopid):
        """动线路径"""
        url = host + "/api/shops/%s/branch-line-stats" % shop_id
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header, params=data).json()
        print("动线路径:", r, "\n\n")

    def minutely_last_stats(self, date, shop_id=golbal_shopid):
        """本门店统计（近X分钟）"""
        url = host + "/api/shops/%s/minutely-last-stats" % shop_id
        data = {"date": date}
        r = requests.get(url=url, headers=header, params=data).json()
        print("本门店统计（近X分钟）:", r, "\n\n")

