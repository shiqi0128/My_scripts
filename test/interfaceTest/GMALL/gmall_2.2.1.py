import unittest
import requests
import json
import os
from time import sleep
from gmall_header import get_header_pc
from urllib3 import encode_multipart_formdata
from gmall_creatnum import camera

host, header, token = get_header_pc()
capita = camera()

"""2.2.1接口测试脚本---正常场景"""
class test01(unittest.TestCase):
    """定义一个测试类"""
    # def customer_list(self):
    #     """顾客列表"""
    #     url_01 = host + "/api/shops/%s/customers" % 25
    #     # "/api/shops/%s/customers" \
    #     # "?search_type=%s&keyword=%s&gender=%s&age_start=%s&age_end=%s" \
    #     # "&is_new_customer=%s&is_bind_mobile={}%s&last_entry_start=%s&last_entry_end=%s" \
    #     # "&tags=%s&entry_start=%s&entry_end=%s&sort_field=%s&sort_type=%s" % (25, str(71), str(71),)
    #     r_01 = requests.get(url=url_01, headers=header).json()
    #     print("顾客列表所有数据:", r_01, "\n")
    #     s = len(r_01["data"]["list"]["data"])
    #     for s1 in range(s):
    #         customer_id = r_01["data"]["list"]["data"][s1]["customer_id"]
    #         return customer_id
    #
    # def test_02_customer_details(self):
    #     """顾客详情"""
    #     customer_id_01 = self.customer_list()
    #     url_03 = host + "/api/shops/%s/customers/%s" % (25, customer_id_01)
    #     r_03 = requests.get(url=url_03, headers=header).json()
    #     print("顾客详情:", r_03, "\n")
    #
    # def test_03_export(self):
    #     """顾客列表导出"""
    #     url_02 = host + "/api/shops/%s/customers/export" % 25
    #     data = {"entry_start": "2017-12-05", "entry_end": "2017-12-05"}
    #     r_02 = requests.get(url=url_02, headers=header, params=data)
    #     print("顾客列表导出:", r_02.text, "\n")
    #
    # def test_04_portrait(self):
    #     """客群画像"""
    #     url_04 = host + "/api/shops/%s/group-stats?start_date=%s&end_date=%s&group_id=%s" % (25, "2017-12-05", "2017-12-05", 0)
    #     r_04 = requests.get(url=url_04, headers=header).json()
    #     print("客群画像:", r_04, "\n")

    def test_06_deep_analysis(self):
        """深度分析统计（人均逛店深度/次均逛店深度）"""
        url_06 = host + "/api/shops/%s/depth-stats" % 25
        date = {"start_date": "2018-01-02", "end_date": "2018-01-02"}
        r_06 = requests.get(url=url_06, headers=header, params=date).json()
        print("深度分析统计（人均逛店深度/次均逛店深度):", r_06, "\n")
        list_01 = []
        for l1 in range(len(r_06["data"]["stats"])):
            stat_dates = r_06["data"]["stats"][l1]["stats_date"]
            list_01.append(stat_dates)
        print("List:", list_01, "\n")
        for index, list_tt in enumerate(list_01, 0):
            if list_tt == "2018-01-02":
                person_depth = r_06["data"]["stats"][index]["person_depth"]
                print("index：", index, list_tt)
                print("人均逛店深度:", person_depth, "\n")
                self.assertEqual(person_depth, capita)
        else:
            print("未找到你要的日期")

    # def test_06_deep_export(self):
    #     """深度分析统计导出（人均逛店深度/次均逛店深度"""
    #     url_06 = host + "/api/shops/%s/depth-stats/export" % 25
    #     date = {"start_date": "2017-12-01", "end_date": "2017-12-30"}
    #     r_06 = requests.get(url=url_06, headers=header, params=date)
    #     print("深度分析统计导出（人均逛店深度/次均逛店深度):", r_06.text, "\n")


if __name__ == "__main__":
    unittest.main()
else:
    print("false")