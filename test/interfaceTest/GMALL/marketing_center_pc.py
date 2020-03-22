import unittest
import requests
import json
import os
from time import sleep
from gmall_header import get_header_pc
from urllib3 import encode_multipart_formdata

host, header, token = get_header_pc()


class Activities(object):

    def activity_tpls(self):
        """查看所有活动模板"""
        url_01 = host + "/api/shops/%s/activity-tpls" % 25
        r_01 = requests.get(url=url_01, headers=header).json()
        print("查看所有活动模板:", r_01, "\n")

    def index(self):
        """门店活动列表"""
        url_02 = host + "/api/shops/%s/activities" % 25
        data = {"tpl_id": 1}
        r_02 = requests.get(url=url_02, headers=header, params=data).json()
        print("门店活动列表:", r_02, "\n")

    def show_details(self):
        """门店活动详情"""
        url_03 = host + "/api/shops/%s/activities/%s" % (25, 15)
        r_03 = requests.get(url=url_03, headers=header).json()
        print("门店活动详情:", r_03, "\n")

    def creat_activities(self):
        """创建活动"""
        url_04 = host + "/api/shops/%s/activities" % 25
        data = {"tpl_id": 1, "name": "年中大促666", "start_time": "2019-02-01 09:00:00", "end_time": "2019-02-28 20:00:00"}
        r_04 = requests.post(url=url_04, headers=header, json=data).json()
        print("创建活动:", r_04, "\n")
        activity_id = r_04["data"]["activity"]["id"]
        return activity_id

    def edit(self):
        """活动编辑前操作"""
        activity_id_01 = self.creat_activities()
        # print("id_01:", id_01)
        url_05 = host + "/api/shops/%s/activities/%s/edit" % (25, activity_id_01)
        r_05 = requests.get(url=url_05, headers=header).json()
        print("活动前编辑操作:", r_05, "\n")
        return activity_id_01

    def update(self):
        """更新活动"""
        activity_id_02 = self.edit()
        url_06 = host + "/api/shops/%s/activities/%s" % (25, activity_id_02)
        data = {"name": "年终大促", "start_time": "2019-02-01", "end_time": "2019-02-20"}
        r_06 = requests.put(url=url_06, headers=header, json=data).json()
        print("更新活动:", r_06, "\n")
        return activity_id_02

    def update_prize(self):
        """更新活动奖品_实物"""
        activity_id_03 = self.update()
        url_07 = host + "/api/shops/%s/activities/%s/save-awards" % (25, activity_id_03)
        prize_list = \
            [
                {
                    "name": "年终大促",
                    "price": 20,
                    "prerequisite": "消费满500元",
                    "started_at": "2019-02-01",
                    "ended_at": "2019-02-20",
                    "probability": 7
                }
            ]
        data = {
            "award_type": 1,            # 奖品类型是实物
            "lottery_rule": 1,
            "awards": json.dumps(prize_list)
        }
        r_07 = requests.post(url=url_07, headers=header, json=data).json()
        print("更新活动奖品_实物:", r_07, "\n")
        return activity_id_03

    def import_file(self):
        """导入活动优惠券文件"""
        activity_id_04 = self.update_prize()
        url_08 = host + "/api/shops/%s/activities/%s/import-coupons" % (25, activity_id_04)
        data = {"file": ("coupons_01.txt", open(r"F:\test\interfaceTest\coupons_01.txt", "r").read())}
        encode_data = encode_multipart_formdata(data)
        print(encode_data)
        data = encode_data[0]
        header_data = {"Content-Type": encode_data[1], "Authorization": "Bearer " + token}
        r_08 = requests.post(url=url_08, headers=header_data, data=data).json()
        print("导入活动优惠券文件:", r_08, "\n")
        coupons_key = r_08["data"]["coupons_key"]
        return activity_id_04, coupons_key                                          # 提取coupons_key放到优惠券的award参数传参

    def update_prize_coupons(self):
        """更新活动奖品_优惠券"""
        activity_id_05, coupons_key_01 = self.import_file()
        url_09 = host + "/api/shops/%s/activities/%s/save-awards" % (25, activity_id_05)
        prize_list =\
            [
                    {
                        "name": "年终大促", "price": 20, "prerequisite": "消费满500元", "started_at": "2019-02-01",
                        "ended_at": "2019-02-20", "probability": 7, "coupons_key": coupons_key_01
                     }
            ]
        data = {
            "award_type": 2,        # 奖品类型是优惠券
            "lottery_rule": 1,
            "awards": json.dumps(prize_list)
        }
        r_09 = requests.post(url=url_09, headers=header, json=data).json()
        print("更新活动奖品_优惠券:", r_09, "\n")
        return activity_id_05, coupons_key_01

    def change_status(self):
        """门店活动暂停/启动"""
        activity_id_06 = self.update_prize_coupons()[0]
        print("activity_id_06:", activity_id_06)
        url_10 = host + "/api/shops/%s/activities/%s/change-status" % (25, activity_id_06)
        r_10 = requests.put(url=url_10, headers=header).json()
        print("门店活动暂停/启动:", r_10, "\n")
        return activity_id_06

    def surplus(self):
        """导出剩余优惠券"""
        activity_id_07 = self.change_status()
        coupons_key_02 = self.update_prize_coupons()[1]
        url_11 = host + "/api/shops/%s/activities/%s/export-coupons" % (25, activity_id_07)
        data = {"coupons_key": coupons_key_02}
        r_11 = requests.get(url=url_11, headers=header, data=data)
        print("导出剩余优惠券:", r_11.text, "\n")
        return activity_id_07

    def delete(self):
        """删除奖品优惠券"""
        activity_id_08 = self.surplus()
        url_12 = host + "/api/shops/%s/activities/%s/coupons-cache" % (25, activity_id_08)
        r_12 = requests.delete(url=url_12, headers=header).json()
        print("删除奖品优惠券:", r_12, "\n")
        return activity_id_08

    def qr_code(self):
        """下载活动二维码"""
        activity_id_09 = self.delete()
        url_13 = host + "/api/shops/%s/activities/%s/download-qrcode" % (25, activity_id_09)
        data = {"size": "300"}
        r_13 = requests.get(url=url_13, headers=header, params=data)
        print("下载活动二维码:", r_13.text, "\n")

    def coupons_tpl(self):
        """下载优惠券模板"""
        url_14 = host + "/api/shops/%s/download-coupons-tpl" % 25
        r_14 = requests.get(url=url_14, headers=header)
        print("下载优惠券模板:", r_14.text, "\n")


# Activities().activity_tpls()
# Activities().index()
# Activities().show_details()
# Activities().qr_code()
# Activities().coupons_tpl()
