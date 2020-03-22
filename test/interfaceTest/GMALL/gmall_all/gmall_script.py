import unittest
import requests
import os
from time import sleep
from interfaceTest.GMALL.gmall_header import host, header

# host, header, token = get_header_pc()
# print(os.getcwd())


class gmall_test(object):
    """定义Gmall测试类"""

    def users(self):
        """可创建用户角色"""
        url_01 = host + "/api/auth/user"
        r_01 = requests.get(url=url_01, headers=header).json()
        print("可创建用户角色", r_01, "\n")
        return r_01

    def old_password(self):
        """验证原密码"""
        url_02 = host + "/api/auth/check-old-password"
        data = {"old_password": "AA123456"}
        r_02 = requests.post(url=url_02, headers=header, json=data).json()
        print("验证原密码:", r_02, "\n")
        return r_02

    def Message_notification_list(self):
        """消息通知列表"""
        url_03 = host + "/api/shops/%s/notifications?date=2019-02-02&type=" % 25
        r_03 = requests.get(url=url_03, headers=header).json()
        print("消息通知列表:", r_03, "\n\n")
        return r_03


    # def change_password(self):
    #     """修改密码"""
    #     url_03 = host + "/api/auth/change-password"
    #     data_01 = {"new_password": "AA123456"}
    #     r_03 = requests.patch(url=url_03, headers=header, json=data_01).json()
    #     print("修改密码:", r_03, "\n")
    #     return r_03

    # def test_03a_admin(self):
    #     print("Hello")

    # def test_04_valid(self):
    #     """检查用户api_token是否有效"""
    #     url_04 = host + "/api/check-token"
    #     params = {"valid_token": token}
    #     r_04 = requests.get(url=url_04, headers=header, params=params).json()
    #     self.assertEqual(r_04["code"], 0)
    #     print("检查用户api_token是否有效:", r_04, "\n")
    #     # print(r_04.text, "\n")
    #     valid = r_04["data"]["valid"]           # 返回结果没有valid这个参数
    #     if valid == 1:
    #         print("token有效", "\n")
    #     else:
    #         print("token无效")

# 门店罗盘API

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


# 顾客行为——顾客行为
    def zone_sankey_stats(self, start_date, end_date):
        """本门店区域动线统计（用于桑基图显示）"""
        url_50 = host + "/api/shops/%s/zone-sankey-stats" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_50 = requests.get(url=url_50, headers=header, params=data).json()
        print("本门店区域动线统计（用于桑基图显示）:", r_50, "\n\n")

    def depth_stats(self, start_date, end_date):
        """深度分析统计（人均逛店深度/次均逛店深度)"""
        url_51 = host + "/api/shops/%s/depth-stats" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_51 = requests.get(url=url_51, headers=header, params=data).json()
        print("深度分析统计（人均逛店深度/次均逛店深度):", r_51, "\n\n")

    def depth_stats_export(self, start_date, end_date):
        """深度分析统计导出（人均逛店深度 / 次均逛店深度)"""
        url_52 = host + "/api/shops/%s/depth-stats/export" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_52 = requests.get(url=url_52, headers=header, params=data)
        print("深度分析统计导出（人均逛店深度 / 次均逛店深度):", r_52.text, "\n\n")

    def line_chord(self, start_date, end_date):
        """和弦图"""
        url_53 = host + "/api/shops/%s/line-chord" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_53 = requests.get(url=url_53, headers=header, params=data).json()
        print("和弦图:", r_53, "\n\n")

    def line_chord_export(self, start_date, end_date):
        """和弦图 数据导出CSV"""
        url_54 = host + "/api/shops/%s/export/line-chord" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_54 = requests.get(url=url_54, headers=header, params=data)
        print("和弦图 数据导出CSV:", r_54.text, "\n\n")

    def stay_time(self, start_date, end_date):
        """逛店时长（人次 均次 每天）连续多日---start_date, end_date必填项"""
        url_55 = host + "/api/shops/%s/stay-time" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_55 = requests.get(url=url_55, headers=header, params=data).json()
        print("逛店时长（人次 均次 每天）连续多日:", r_55, "\n\n")

    def stay_time_export(self, start_date, end_date):
        """逛店时长（人次 均次 每天）连续多日-导出CSV---start_date, end_date必填项"""
        url_56 = host + "/api/shops/%s/stay-time/export" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_56 = requests.get(url=url_56, headers=header, params=data)
        print("逛店时长（人次 均次 每天）连续多日:", r_56.text, "\n\n")

    def enter_shop_frequency_daily(self, date):
        """逛店频率（日）---date必填项"""
        url_57 = host + "/api/shops/%s/enter-shop-frequency-daily" % 25
        data = {"date": date}
        r_57 = requests.get(url=url_57, headers=header, params=data).json()
        print("逛店频率（日）:", r_57, "\n\n")

    def enter_shop_frequency_daily_export(self, date):
        """逛店频率（日）导出---date必填项"""
        url_58 = host + "/api/shops/%s/enter-shop-frequency-daily/export" % 25
        data = {"date": date}
        r_58 = requests.get(url=url_58, headers=header, params=data)
        print("逛店频率（日）导出:", r_58.text, "\n")
        return r_58

    def enter_shop_frequency_weekly(self, start_date, end_date):
        """逛店频率（周）---start_date, end_date必填项"""
        url_59 = host + "/api/shops/%s/enter-shop-frequency-weekly" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_59 = requests.get(url=url_59, headers=header, params=data).json()
        print("逛店频率（周）:", r_59, "\n\n")

    def enter_shop_frequency_weekly_export(self, start_date, end_date):
        """逛店频率（周）导出CSV---start_date, end_date必填项"""
        url_60 = host + "/api/shops/%s/enter-shop-frequency-weekly/export/" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_60 = requests.get(url=url_60, headers=header, params=data)
        print("逛店频率（周）导出CSV:", r_60.text, "\n\n")

    def enter_shop_frequency_monthly(self, year, month):
        """逛店频率（月）---year, month必填项"""
        url_61 = host + "/api/shops/%s/enter-shop-frequency-monthly" % 25
        data = {"year": year, "month": month}
        r_61 = requests.get(url=url_61, headers=header, params=data).json()
        print("逛店频率（月）:", r_61, "\n\n")

    def enter_shop_frequency_monthly_export(self, year, month):
        """逛店频率（月）导出CSV---year, month必填项"""
        url_62 = host + "/api/shops/%s/enter-shop-frequency-monthly/export/" % 25
        data = {"year": year, "month": month}
        r_62 = requests.get(url=url_62, headers=header, params=data)
        print("逛店频率（月）导出CSV:", r_62.text, "\n\n")

    def zone_hourly_range_stats(self, start_date, end_date):
        """区域统计（每小时）连续多日---start_date, end_date必填项"""
        url_63 = host + "/api/shops/%s/zone-hourly-range-stats" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_63 = requests.get(url=url_63, headers=header, params=data).json()
        print("区域统计（每小时）连续多日:", r_63, "\n\n")

    def zone_range_average_time_stats(self, start_date, end_date):
        """区域统计连续多日 顾客总数&平均停留时长---start_date, end_date必填项"""
        url_64 = host + "/api/shops/%s/zone-range-average-time-stats" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_64 = requests.get(url=url_64, headers=header, params=data).json()
        print("区域统计连续多日 顾客总数&平均停留时长:", r_64, "\n\n")

    def historical_data_compare(self, date):
        """本门店历史数据环比"""
        url_65 = host + "/api/shops/%s/historical-data-compare" % 25
        data = {"date": date}
        r_65 = requests.get(url=url_65, headers=header, params=data).json()
        print("本门店历史数据环比:", r_65, "\n\n")

    def branch_line_stats(self, start_date, end_date):
        """动线路径"""
        url_66 = host + "/api/shops/%s/branch-line-stats" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_66 = requests.get(url=url_66, headers=header, params=data).json()
        print("动线路径:", r_66, "\n\n")

    def minutely_last_stats(self, date):
        """本门店统计（近X分钟）"""
        url_67 = host + "/api/shops/%s/minutely-last-stats" % 25
        data = {"date": date}
        r_67 = requests.get(url=url_67, headers=header, params=data).json()
        print("本门店统计（近X分钟）:", r_67, "\n\n")


# 顾客行为——动线&热力 API
    def line_analysis(self, date):
        """动线排行"""
        url_15 = host + "/api/shops/%s/top-lines" % 25
        data = {"date": date}
        r_15 = requests.get(url=url_15, headers=header, params=data).json()
        print("动线排行:", r_15, "\n\n")
        return r_15

    def heat_map(self, start_time, end_time):
        """店面热力图(每分钟)"""
        url_16 = host + "/api/shops/%s/heat-map" % 25
        data = {"start_time": start_time, "end_time": end_time}
        r_16 = requests.get(url=url_16, headers=header, params=data).json()
        print("店面热力图(每分钟):", r_16, "\n\n")
        return r_16

# 顾客行为——顾客粘度 API
    def livenessCompare(self, date):
        """活跃度环比"""
        url_17 = host + "/api/shops/%s/liveness-compare" % 25
        data = {"date": date}
        r_17 = requests.get(url=url_17, headers=header, params=data).json()
        print("活跃度环比:", r_17, "\n")
        return r_17

    def dailyRangeLiveness(self, start_date, end_date):
        """活跃度列表"""
        url_18 = host + "/api/shops/%s/daily-range-liveness" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_18 = requests.get(url=url_18, headers=header, params=data).json()
        print("活跃度列表:", r_18, "\n")
        return r_18

    def liveness_export(self, start_date, end_date):
        """活跃度导出CSV"""
        url_19 = host + "/api/shops/%s/liveness/export" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_19 = requests.get(url=url_19, headers=header, params=data)
        print("活跃度导出CSV:", r_19.text, "\n")
        return r_19

    def weekLivenessList(self, start_date, end_date):
        """活跃天数列表（周)"""
        url_20 = host + "/api/shops/%s/liveness-week" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_20 = requests.get(url=url_20, headers=header, params=data).json()
        print("活跃天数列表(周):", r_20, "\n")
        return r_20

    def monthLivenessList(self, start_date, end_date):
        """活跃天数列表（月）"""
        url_21 = host + "/api/shops/%s/liveness-month" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_21 = requests.get(url=url_21, headers=header, params=data).json()
        print("活跃天数列表(月):", r_21, "\n")
        return r_21

    def liveness_list_export(self, start_date, end_date):
        """活跃天数导出CSV"""
        url_22 = host + "/api/shops/%s/liveness-list/export" % 25
        data = {"start_date": start_date, "end_date": end_date, "type": "week"}
        r_22 = requests.get(url=url_22, headers=header, params=data)
        print("活跃天数导出CSV:", r_22.text, "\n")
        return r_22

# 顾客行为——顾客管理
    def label_list(self, type_02):
        """获取标签/客群列表,type=1是标签，type=2是客群"""
        url_23 = host + "/api/shops/%s/tags" % 25
        data = {"type": type_02}
        r_23 = requests.get(url=url_23, headers=header, json=data).json()
        print("获取标签/客群列表_标签:", r_23, "\n")
        return r_23

    def test_24_label_details(self):
        """获取标签/客群详情,type=1是标签，type=2是客群"""
        tagID_01 = self.test_33_group_list()
        url_24 = host + "/api/shops/%s/tags/%s" % (1, tagID_01)
        r_24 = requests.get(url=url_24, headers=header).json()
        print("获取标签/客群详情:", r_24, "\n")

    def customer_funnel(self, start_date, end_date):
        """顾客漏斗"""
        url_34 = host + "/api/shops/%s/customer-buy-conversion" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_34 = requests.get(url=url_34, headers=header, params=data).json()
        print("顾客漏斗:", r_34, "\n\n")

    def customer_funnel_export(self, start_date, end_date):
        """顾客漏斗-列表导出"""
        url_35 = host + "/api/shops/%s/export/customer-buy-conversion" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_35 = requests.get(url=url_35, headers=header, params=data)
        print("顾客漏斗-列表导出:", r_35.text, "\n\n")


# 顾客行为——客群管理
    def customer_charts(self, date):
        """客群管理_门店报表"""
        url_36 = host + "/api/shops/%s/customer-charts" % 25
        data = {"date": date}
        r_36 = requests.get(url=url_36, headers=header, params=data).json()
        print("客群管理_门店报表:", r_36, "\n\n")
        return r_36

    def customer_visit_list(self):
        """顾客历史来店信息"""
        url_37 = host + "/api/shops/%s/customers/%s/visit-list" % (25, 216)
        r_37 = requests.get(url=url_37, headers=header).json()
        print("顾客历史来店信息:", r_37, "\n\n")

    def customer_entry_records(self, start_date, end_date):
        """顾客进店记录"""
        url_38 = host + "/api/shops/%s/customers/%s/entry-records" % (25, 218)
        data = {"start_date": start_date, "end_date": end_date}
        r_38 = requests.get(url=url_38, headers=header).json()
        print("顾客进店记录", r_38, "\n\n")

    def user_portrait(self):
        """用户画像"""
        url_39 = host + "/api/shops/%s/customers-minutely" % 25
        r_39 = requests.get(url=url_39, headers=header).json()
        print("用户画像:", r_39, "\n\n")

# 顾客行为——顾客画像
    def get_the_whole_race(self):
        """获取全部人种"""
        url_41 = host + "/api/shops/%s/races" % 25
        r_41 = requests.get(url=url_41, headers=header).json()
        print("获取全部人种:", r_41, "\n\n")

    def customers_list(self):
        """顾客列表"""
        url_42 = host + "/api/shops/{shop}/customers" \
                        "?search_type={}&keyword={}&gender={}&age_start={}&age_end={}&is_new_customer={}&is_bind_mobile={}last_entry_start={}&last_entry_end={} &tags={}&entry_start={}&entry_end={}&sort_field={}&sort_type={}&race={}"

    def guest_group_portrait(self, start_date, end_date):
        """客群画像"""
        url_46 = host + "/api/shops/%s/group-stats?group_id=0" % 25
        data = {"start_date": start_date, "end_date": end_date}
        r_46 = requests.get(url=url_46, headers=header, params=data).json()
        print("客群画像:", r_46, "\n\n")
        return r_46

    def customers_ranking(self, start_time, end_time):
        """顾客画像Top排名"""
        url_47 = host + "/api/shops/%s/customers-ranking" % 25
        data = {"start_date": start_time, "end_date": end_time}
        r_47 = requests.get(url=url_47, headers=header, params=data).json()
        print("顾客画像Top排名:", r_47, "\n\n")
        return r_47
    #
    # def trend_monitoring(self, start_date, end_date):
    #     """数据趋势"""
    #     url_48 = host + "/api/shops/%s/distribution-stats?type=1&age=1&gender=1"
    #
    # def trend_monitoring_export(self, start_date, end_date):







#     def hourlyShopStat(self):
#         """门店客流统计（每小时)"""
#         url_08 = host + "/api/shops/%s/hourly-stats/?date=" % 25
#         r_08 = requests.get(url=url_08, headers=header).json()
#         # self.assertEqual(r_08["code"], 0)
#         print("门店客流统计（每小时):", r_08, "\n\n")                       # 没有date日期
#
#     def dailyShopStats(self):
#         """门店客流统计（每天）客流数况"""
#         url_09 = host + "/api/shops/%s/daily-stats/?date=" % 25
#         r_09 = requests.get(url=url_09, headers=header).json()
#         # self.assertEqual(r_09["code"], 0)
#         print("门店客流统计（每天）客流数况:", r_09, "\n")                  # 没有date日期
#
#     def realTimeStats(self):
#         """实时数据轮询"""
#         url_10 = host + "/api/shops/%s/real-time-stats?ago=" % 25
#         r_10 = requests.get(url=url_10, headers=header).json()
#         # self.assertEqual(r_10["code"], 0)
#         print("实时数据轮询:", r_10, "\n")
#
#     def cameras(self):
#         """门店监控（摄像头列表)"""
#         url_13 = host + "/api/shops/%s/cameras" % 25
#         r_13 = requests.get(url=url_13, headers=header).json()
#         # self.assertEqual(r_13["code"], 0)
#         print("门店监控（摄像头列表):", r_13, "\n")
#
#     def dailyRangeStayTime(self):
#         """逛店时长（人次 均次 每天）连续多日"""
#         url_17 = host + "/api/shops/%s/stay-time" % 25
#         data = {"start_date": "2018-11-01", "end_date": "2018-11-20"}
#         r_17 = requests.get(url=url_17, headers=header, json=data).json()
#         self.assertEqual(r_17["code"], 0)
#         print("逛店时长（人次 均次 每天）连续多日:", r_17, "\n")
#
#     def enterShopFrequencyDaily(self):
#         """逛店频率（日）"""
#         url_18 = host + "/api/shops/%s/enter-shop-frequency-daily" % 25
#         data = {"date": "2018-11-20"}
#         r_18 = requests.get(url=url_18, headers=header, params=data).json()
#         self.assertEqual(r_18["code"], 0)
#         print("逛店频率（日）:", r_18, "\n")
#
#     def enterShopFrequencyWeekly(self):
#         """逛店频率（周）"""
#         url_19 = host + "/api/shops/%s/enter-shop-frequency-weekly" % 25
#         data = {"start_date": "2018-11-01", "end_date": "2018-11-20"}
#         r_19 = requests.get(url=url_19, headers=header, params=data).json()
#         self.assertEqual(r_19["code"], 0)
#         print("逛店频率（周）:", r_19, "\n")
#
#     def zoneRangeAverageTimeStats(self):
#         """区域统计连续多日 顾客总数&平均停留时长"""
#         url_20 = host + "/api/shops/%s/zone-range-average-time-stats" % 25
#         data = {"start_date": "2018-11-01", "end_date": "2018-11-20"}
#         r_20 = requests.get(url=url_20, headers=header, params=data).json()
#         self.assertEqual(r_20["code"], 0)
#         print("区域统计连续多日 顾客总数&平均停留时长:", r_20, "\n")
#
#     def historicalDataCompare(self):
#         """本门店历史数据环比"""
#         url_21 = host + "/api/shops/%s/historical-data-compare" % 25
#         data = {"date": "2018-11-28"}
#         r_21 = requests.get(url=url_21, headers=header, params=data).json()
#         self.assertEqual(r_21['code'], 0)
#         print("本门店历史数据环比:", r_21, "\n")
#
#     def branchLineStats(self):
#         """动线路径"""
#         url_22 = host + "/api/shops/%s/branch-line-stats" % 25
#         data = {"start_date": "2018-11-01", "end_date": "2018-11-20"}
#         r_22 = requests.get(url=url_22, headers=header, params=data).json()
#         self.assertEqual(r_22['code'], 0)
#         print("本门店历史数据环比:", r_22, "\n")
#
#     # def test_23_shopInfoUpdate(self):
#     #     """门店信息修改"""
#     #     url_23 = host + "/api/shops/%s/shop-info-update" % 1
#
#     def test_24_minutelyShopLastStats(self):
#         """本门店统计（近X分钟）"""
#         url_24 = host + "/api/shops/%s/minutely-last-stats" % 25
#         r_24 = requests.get(url=url_24, headers=header).json()
#         self.assertEqual(r_24["code"], 0)
#         print("本门店统计（近X分钟）:", r_24, "\n")
#
# # 客群管理API
#     def test_25_report(self):
#         """门店报表"""
#         url_25 = host + "/api/shops/%s/customer-charts/?date=%s" % (1, "2018-11-28")
#         r_25 = requests.get(url=url_25, headers=header).json()
#         self.assertEqual(r_25["code"], 0)
#         print("门店报表:", r_25, "\n")
#
#     def test_26_visitList(self):
#         """顾客历史来店信息"""
#         url_26 = host + "/api/shops/%s/customers/%s/visit-list" % (1, 134)
#         r_26 = requests.get(url=url_26, headers=header).json()
#         # self.assertEqual(r_26["code"], 0)
#         print("顾客历史来店信息:", r_26, "\n")
#
#     def test_27_user_portrait(self):
#         """顾客信息"""
#         url_27 = host + "/api/shops/%s/customers/%s" % (1, 134)
#         r_27 = requests.get(url=url_27, headers=header).json()
#         # self.assertEqual(r_27["code"], 0)
#         print("顾客信息:", r_27, "\n")
#

#

#
#
#     def test_35_creat_label(self):
#         """创建标签"""
#         url_35 = host + "/api/shops/%s/tags" % 1
#         data = {"type": 1, "name": "80后女性消费者", }          # type=1,标签
