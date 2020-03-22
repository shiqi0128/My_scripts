import unittest
import requests
import os
from time import sleep
from gmall_header import get_header
import json
from urllib3 import encode_multipart_formdata

host, header, token = get_header()


# def update_prize_object():
#     """更新活动奖品_实物"""
#     url_07 = host + "/api/shops/%s/activities/%s/save-awards" % (1, 148)
#     prize_list = [{"name": "年终大促", "price": 20, "prerequisite": "消费满500元", "started_at": "2018-12-15", "ended_at": "2018-12-31", "probability": 7}]
#     data = {
#                 "award_type": 1,
#                 "lottery_rule": 1,
#                 "awards": json.dumps(prize_list)
#     }
#     r_07 = requests.post(url=url_07, headers=header, json=data).json()
#     print("更新活动奖品:", r_07, "\n")

# def update_prize_coupons():
#     """导入活动优惠券文件"""
#     url_08 = host + "/api/shops/%s/activities/%s/import-coupons" % (1, 148)
#     files_01 = open("F:/test/interfaceTest/coupons_01.txt", "r")
#     files = {"file": files_01}
#     print(files_01.read())
#     try:
#         r_08 = requests.post(url=url_08, headers=header, files=files).json()
#         print("导入活动优惠券文件:", r_08, "\n")
#     except:
#         print("file 为空")


# def update_prize_coupons():
#     """导入活动优惠券文件"""
#     url_08 = host + "/api/shops/%s/activities/%s/import-coupons" % (1, 148)
#     data = {"file": ("coupons_01.txt", open(r"F:\test\interfaceTest\coupons_01.txt", "r").read())}
#     encode_data = encode_multipart_formdata(data)
#     print(encode_data)
#     data = encode_data[0]
#     header_data = {"Content-Type": encode_data[1], "Authorization": "Bearer " + token}
#     r_08 = requests.post(url=url_08, headers=header_data, data=data).json()
#     print("导入活动优惠券文件:", r_08)


# def update_prize_coupons():
#     """更新活动奖品_优惠券"""
#     url_09 = host + "/api/shops/%s/activities/%s/save-awards" % (1, 148)
#     prize_list = [{"name": "年终大促", "price": 20, "prerequisite": "消费满500元", "started_at": "2018-12-15",
#                    "ended_at": "2018-12-31", "probability": 7, "coupons_key": "QcCk7CG9TnoFP7vtrRRs4BabAGFZ9IfUqvPJ"}]
#     data = {
#         "award_type": 2,
#         "lottery_rule": 1,
#         "awards": json.dumps(prize_list)
#     }
#     r_09 = requests.post(url=url_09, headers=header, json=data).json()
#     print("更新活动奖品:", r_09, "\n")
#
#
# update_prize_coupons()

# def update_prize_coupons():
#     """导入活动优惠券文件"""
#     url_08 = host + "/api/shops/%s/activities/%s/import-coupons" % (1, 148)
#     with open("cunpons.txt", "r") as file:
#         file = {"file": r"F:\test\interfaceTest\cunpons.txt"}
#         r_08 = requests.post(url=url_08, headers=header, files=file).json()
#         print("导入活动优惠券文件:", r_08, "\n")
#
# def update_prize_coupons(self):
#     """更新活动奖品_优惠券"""

# update_prize_object()
# update_prize_coupons()

# with open("cunpons.txt") as file:
# prize_list = [{"name": "年终大促", "price": 20, "prerequisite": "消费满500元", "started_at": "2018-12-15", "ended_at": "2018-12-31", "probability": 7}]
#
# datas = {"award_type": 2, "lottery_rule": 1, "awards": json.dumps(prize_list)}

def surplus():
    """导出剩余优惠券"""
    activity_id_07 = change_status()
    print("activity_id_07:", activity_id_07)
    # coupons_key_02 = self.update_prize_coupons()
    # url_11 = host + "/api/shops/%s/activities/%s/export-coupons" % (1, activity_id_07)
    # data = {"coupons_key": coupons_key_02}
    # r_11 = requests.get(url=url_11, headers=header, data=data).json()
    # print("导出剩余优惠券:", r_11, "\n")
    # return activity_id_07


surplus()