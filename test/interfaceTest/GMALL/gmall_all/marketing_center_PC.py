import requests
import json
import os
from time import sleep
from interfaceTest.GMALL.gmall_header import header, host, token
from urllib3 import encode_multipart_formdata
from interfaceTest.GMALL.gmall_all.color import out_format

# host, header, token = get_header_pc(self, shop_id=25)


def creat_activities(shop_id=25):
    """创建活动"""
    url_04 = host + "/api/shops/%s/activities" % shop_id
    data = {"tpl_id": 1, "name": "年中大促666", "start_time": "2019-02-01 09:00:00", "end_time": "2019-02-28 20:00:00"}
    r_04 = requests.post(url=url_04, headers=header, json=data).json()
    out_format("创建活动:", r_04)
    activity_id = r_04["data"]["activity"]["id"]
    return activity_id


def import_file(shop_id=25):
    """导入活动优惠券文件"""
    url_08 = host + "/api/shops/%s/activities/%s/import-coupons" % (shop_id, activity_id)
    data = {"file": ("coupons_01.txt", open(r"F:\test\interfaceTest\coupons_01.txt", "r").read())}
    encode_data = encode_multipart_formdata(data)
    data = encode_data[0]
    header_data = {"Content-Type": encode_data[1], "Authorization": "Bearer " + token}
    r_08 = requests.post(url=url_08, headers=header_data, data=data).json()
    out_format("导入活动优惠券文件:", r_08)
    coupons_key = r_08["data"]["coupons_key"]
    return coupons_key                                          # 提取coupons_key放到优惠券的award参数传参


activity_id = creat_activities()
coupons_key = import_file()


class Activities(object):


    def activity_tpls(self, shop_id=25):
        """查看所有活动模板"""
        url_01 = host + "/api/shops/%s/activity-tpls" % shop_id
        r_01 = requests.get(url=url_01, headers=header).json()
        out_format("查看所有活动模板:", r_01)

    def index(self, shop_id=25):
        """门店活动列表"""
        url_02 = host + "/api/shops/%s/activities" % shop_id
        data = {"tpl_id": 1}
        r_02 = requests.get(url=url_02, headers=header, params=data).json()
        out_format("\033[1;32m门店活动列表:\033[0m", r_02)

    def show_details(self, shop_id=25):
        """门店活动详情"""
        url_03 = host + "/api/shops/%s/activities/%s" % (shop_id, 15)
        r_03 = requests.get(url=url_03, headers=header).json()
        out_format("门店活动详情:", r_03)

    def creat_activities(self, shop_id=25):
        """创建活动"""
        url_04 = host + "/api/shops/%s/activities" % shop_id
        data = {"tpl_id": 1, "name": "年中大促666", "start_time": "2019-02-01 09:00:00", "end_time": "2019-02-28 20:00:00"}
        r_04 = requests.post(url=url_04, headers=header, json=data).json()
        out_format("创建活动:", r_04)

    def edit(self, shop_id=25):
        """活动编辑前操作"""
        # out_format("id_01:", id_01)
        url_05 = host + "/api/shops/%s/activities/%s/edit" % (shop_id, activity_id)
        r_05 = requests.get(url=url_05, headers=header).json()
        out_format("活动前编辑操作:", r_05)

    def update(self, shop_id=25):
        """更新活动"""
        url_06 = host + "/api/shops/%s/activities/%s" % (shop_id, activity_id)
        data = {"name": "年终大促", "start_time": "2019-02-01", "end_time": "2019-02-20"}
        r_06 = requests.put(url=url_06, headers=header, json=data).json()
        out_format("更新活动:", r_06)

    def update_prize(self, shop_id=25):
        """更新活动奖品_实物"""
        url_07 = host + "/api/shops/%s/activities/%s/save-awards" % (shop_id, activity_id)
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
        out_format("更新活动奖品_实物:", r_07)

    def import_file(self, shop_id=25):
        """导入活动优惠券文件"""
        url_08 = host + "/api/shops/%s/activities/%s/import-coupons" % (shop_id, activity_id)
        data = {"file": ("coupons_01.txt", open(r"F:\test\interfaceTest\coupons_01.txt", "r").read())}
        encode_data = encode_multipart_formdata(data)
        data = encode_data[0]
        header_data = {"Content-Type": encode_data[1], "Authorization": "Bearer " + token}
        r_08 = requests.post(url=url_08, headers=header_data, data=data).json()
        out_format("导入活动优惠券文件:", r_08)
        coupons_key = r_08["data"]["coupons_key"]
        return activity_id, coupons_key                                          # 提取coupons_key放到优惠券的award参数传参

    def update_prize_coupons(self, shop_id=25):
        """更新活动奖品_优惠券"""
        url_09 = host + "/api/shops/%s/activities/%s/save-awards" % (shop_id, activity_id)
        prize_list =\
            [
                    {
                        "name": "年终大促", "price": 20, "prerequisite": "消费满500元", "started_at": "2019-02-01",
                        "ended_at": "2019-02-20", "probability": 7, "coupons_key": coupons_key
                     }
            ]
        data = {
            "award_type": 2,        # 奖品类型是优惠券
            "lottery_rule": 1,
            "awards": json.dumps(prize_list)
        }
        r_09 = requests.post(url=url_09, headers=header, json=data).json()
        out_format("更新活动奖品_优惠券:", r_09)

    def change_status(self, shop_id=25):
        """门店活动暂停/启动"""
        out_format("activity_id_06:", activity_id)
        url_10 = host + "/api/shops/%s/activities/%s/change-status" % (shop_id, activity_id)
        r_10 = requests.put(url=url_10, headers=header).json()
        out_format("门店活动暂停/启动:", r_10)

    def surplus(self, shop_id=25):
        """导出剩余优惠券"""
        url_11 = host + "/api/shops/%s/activities/%s/export-coupons" % (shop_id, activity_id)
        data = {"coupons_key": coupons_key}
        r_11 = requests.get(url=url_11, headers=header, json=data)
        out_format("导出剩余优惠券:", r_11.text)

    def delete(self, shop_id=25):
        """删除奖品优惠券"""
        url_12 = host + "/api/shops/%s/activities/%s/coupons-cache" % (shop_id, activity_id)
        r_12 = requests.delete(url=url_12, headers=header).json()
        out_format("删除奖品优惠券:", r_12)

    def qr_code(self, shop_id=25):
        """下载活动二维码"""
        url_13 = host + "/api/shops/%s/activities/%s/download-qrcode" % (shop_id, activity_id)
        data = {"size": "300"}
        r_13 = requests.get(url=url_13, headers=header, params=data)
        out_format("下载活动二维码:", r_13.text)

    def coupons_tpl(self, shop_id=25):
        """下载优惠券模板"""
        url_14 = host + "/api/shops/%s/download-coupons-tpl" % shop_id
        r_14 = requests.get(url=url_14, headers=header)
        out_format("下载优惠券模板:", r_14.text)
