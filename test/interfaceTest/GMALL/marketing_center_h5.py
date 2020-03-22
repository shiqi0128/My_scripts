import unittest
import requests
import json
import os
from time import sleep
from gmall_header import get_header_h5
from urllib3 import encode_multipart_formdata

host, header = get_header_h5()

class ActivitiesH5(object):

    def user(self):
        """获取用户信息"""
        url_01 = host + "/activity/user"
        r_01 = requests.get(url=url_01, headers=header).json()
        print("获取用户信息:", r_01, "\n")

    def show(self):
        """获取活动详情"""
        url_02 = host + "/activity/activity-detail"
        data = {"activity_id": "vZ7PARoXEM"}
        r_02 = requests.get(url=url_02, headers=header, json=data).json()
        print("获取活动详情:", r_02, "\n")

    def user_awards(self):
        """获取指定奖品详情"""
        url_03 = host + "/activity/user-awards/%s" % "vZ7PARoXEM"
        r_03 = requests.get(url=url_03, headers=header).json()
        print("获取指定奖品详情:", r_03, "\n")

    def use(self):
        """奖品核销"""
        url_04 = host + "/activity/user-awards/%s/use" % "vZ7PARoXEM"
        r_04 = requests.post(url=url_04, headers=header).json()
        print("奖品核销:", r_04, "\n")

    def get_prize_object(self):
        """获取我的奖品列表_实物"""
        url_05 = host + "/activity/user-awards"
        data = {"activity_id": "vZ7PARoXEM", "type": 1}             # 获取奖品为实物的奖品列表，type=1是实物
        r_05 = requests.get(url=url_05, headers=header, json=data).json()
        print("获取我的奖品列表_实物:", r_05, "\n")

    def get_prize_coupons(self):
        """获取我的奖品列表_优惠券"""
        url_06 = host + "/activity/user-awards"
        data = {"activity_id": "vZ7PARoXEM", "type": 2}             # 获取奖品为优惠券的奖品列表，type=2是优惠券
        r_06 = requests.get(url=url_06, headers=header, json=data).json()
        print("获取我的奖品列表_优惠券:", r_06, "\n")

    def get_prize_num(self):
        """获取我的奖品数量"""
        url_07 = host + "/activity/user-awards-stats"
        data = {"activity_id": "vZ7PARoXEM"}
        r_07 = requests.get(url=url_07, headers=header, json=data).json()
        print("获取我的奖品数量:", r_07, "\n")

    def upload(self):
        """上传图片"""
        url_08 = host + "/activity/upload-image"
        files = {"image": ("baby.jpg", open(r"F:\test\interfaceTest\baby.jpg", "rb").read(), "jpg/png")}   # 读取文件赋值给file
        encode_data = encode_multipart_formdata(files)   # encode_multipart_formdata是导入的一个方法,这个方法下面的文件赋值给encode_data
        data = encode_data[0]                       # encode的返回结果第一个值是上传的文件
        header_data = \
            {
                "Content-Type": encode_data[1],          # 指要上传文件的方式，输出encode_data的结果，头部变更为第2个值才能上传
                # "Authorization": "Bearer df6ffc7f56271c3b079e3d79381b02704e2d50d4"
            }
        r_08 = requests.post(url=url_08, headers=header_data, data=data).json()
        print("上传图片:", r_08, "\n")
        img_key = r_08["data"]["img_key"]
        img_url = r_08["data"]["img_url"]
        return img_key, img_url

    def identify(self):
        """测试颜值"""
        img_key_01, img_url_01 = self.upload()
        url_09 = host + "/activity/face-beauty/identify"
        data = \
            {
                "activity_id": "vZ7PARoXEM",
                "img_key": img_key_01,
                "img_url": img_url_01
            }
        r_09 = requests.post(url=url_09, headers=header, json=data).json()
        print("测试颜值:", r_09, "\n")


# ActivitiesH5().user()
# ActivitiesH5().show()
# ActivitiesH5().user_awards()
# ActivitiesH5().use()
# ActivitiesH5().get_prize_object()
# ActivitiesH5().get_prize_coupons()
# ActivitiesH5().get_prize_num()
# ActivitiesH5().identify()

