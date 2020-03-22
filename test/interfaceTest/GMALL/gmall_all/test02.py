import requests
import unittest
import os
from time import sleep
import random
from interfaceTest.GMALL.public_files import user_id, user_id_01
from interfaceTest.GMALL.gmall_header import host, get_header_pc
from interfaceTest.GMALL.gmall_all.color import out_format

header, token1 = get_header_pc("admin_sylvia", "admin1")
header_xun, token2 = get_header_pc("admin80473", "admin@123")
header_zheng, token3 = get_header_pc("admin38796", "admin@123")


# def get_tags_list(self, tag_type, tag, shop_id=golbal_shopid, keyword=None, search_type=None):
#     """
#     获取 标签/客群 列表
#     :param tag_type: 类型 ---1：标签 2：客群(int)
#     :param tag: 客群/标签
#     :param keyword: 模糊搜索关键字(string)
#     :param search_type:当有keyword时为必填,1：搜索标签名 2：搜索标签id 3：搜索备注(int)
#     :param shop_id:门店id
#     :return: 返回标签/客群id列表
#     """
#     tags_id_list = []  # 标签/客群的id集合
#     url = host + "/api/shops/%s/tags" % shop_id
#     tag_data = {"type": tag_type}  # tag_type = 标签类型（1/2）
#     response = requests.get(url=url, headers=header, params=tag_data).json()
#     if response["data"]["tags"] is not None:  # 表示没有客群或标签id
#         tag_len = len(response["data"]["tags"])  # 统计有多少个标签
#         for tag_id in range(tag_len):
#             tags_id_list.append(response["data"]["tags"][tag_id]["id"])  # 拿到每一个标签id，并放到标签列表中
#     print("获取【%s,type=%s】列表:" % (tag, tag_type), response)
#     print("获取%s的id：" % tag, tags_id_list)
#     return tags_id_list
#
#
# def get_tags_particulars(self, tag_type, tag,  tag_id, shop_id=golbal_shopid):
#     """
#     获取 标签/客群 详情
#     :param tag_type: 类型 1：标签 2：客群(int)
#     :param tag: 标签/客群
#     :param tag_id: 标签id
#     :param shop_id:门店id
#     :return:
#     """
#     url = host + "/api/shops/%s/tags/%s" % (shop_id, tag_id)
#     response = requests.get(url=url, headers=header).json()
#     print("获取【{0}[id={1}],type={2}】详情:" .format(tag, tag_id, tag_type), response)
#     return response


# def Merch_sales(start_date, end_date, shop_id=golbal_shopid):
#     """商品销售经营分析
#     :param:shop:门店id
#     :param:start_date:开始日期
#     :param:end_date:结束日期
#     :param:page_size:分页条数（默认10）---非必填
#     :param:product_id:商品id---非必填
#     :param:product_name:商品名--非必填
#     :param:category_id:品类ID--非必填
#     """
#     url = host + "/api/shops/%s/manage/product-analyze" % shop_id
#     data = {"start_date": start_date, "end_date": end_date}
#     r = requests.get(url=url, headers=header, params=data).json()
#     print("r:", r)
#     # if r["data"]["stats"]["data"] is not None:
#     #     s = len(r["data"]["stats"]["data"])
#     #     for i in range(s):
#     #         product_id = r["data"]["stats"]["data"][i]["product_id"]
#     #         out_format("商品销售经营分析:", r)
#     #         return product_id
#     # else:
#     #     print("data is null")
#     #     return None
#
#
# product_id = Merch_sales("2019-01-13", "2019-01-14")
#


h = {
    "code": 0,
    "message": "createSchedule",
    "data": {
        "schedule": {
            "uid": 8204,
            "company_id": 44,
            "name": "测试",
            "snapshot_ats": [
                "03:00"
            ],
            "start_date": "2018-02-01",
            "end_date": "2019-05-01",
            "cycle": [
                "1"
            ],
            "patroller_uid": "75",
            "camera_ids": [
                "131"
            ],
            "status": 1,
            "updated_at": "2019-03-19 11:25:16",
            "created_at": "2019-03-19 11:25:16",
            "id": 17
        }
    },
    "elapsed": 0.547
}

# scheduleId = h["data"]["schedule"]["id"]
# print("id", scheduleId)

# i = 1
# while i<=5:
#
#     try:
#         print("i:", i)
#         break
#     except:
#         pass
#     i+=1


# class test(unittest.TestCase):
# def Patrol_detail():
#     """巡查计划--详情
#     :param:scheduleId:巡查计划id
#     """
#     # scheduleId_01 = self.Patrol_add("2019-03-01", "2019-03-10")
#     i = 1
#     while i <= 5:
#         try:
#             url = host + "/api/company/patrol-schedules/%s" % 44
#             r = requests.get(url=url, headers=header).json()
#             print(r)
#             assert(r["code"] == 0)
#             out_format("巡查计划--详情:", r)
#             break
#         except:
#             url_01 = host + "/api/company/patrol-schedules/%s" % 44
#             r = requests.patch(url=url_01, headers=header).json()
#             out_format("巡查计划 - 修改状态:", r)
#         i += 1
#
#
# Patrol_detail()
# if __name__ == "__main__":
#     unittest.main()
# else:
#     print("false")

class test():
    # def Patrol_add(self, start_date, end_date):
    #     """巡查计划--新增
    #     :param:start_date:任务开始时间
    #     :param:end_date:任务结束时间
    #     :param:name:任务名称
    #     :param:snapshot_ats:抓拍时间段,传数组形式
    #     :param:camera_ids:摄像头id 集合,传数组形式----注意，这里填的是camera的id不是code
    #     :param:patroller_uid:巡查人id
    #     :param:cycle:周期 0、1、2、3、4、5、6分别对应周日至周六, 传数组形式
    #     """
    #     url = host + "/api/company/patrol-schedules"
    #     data = {
    #         "start_date": start_date, "end_date": end_date,
    #         "name": "检查垃圾桶%s" % random.randrange(1, 10000),
    #         "snapshot_ats":
    #             ["18:09"],
    #         "camera_ids": ["64"],
    #         "patroller_uid": user_id,
    #         "cycle": ["0", "1", "2", "3", "4", "5", "6"]
    #     }
    #     print("data", data)
    #     r = requests.post(url=url, headers=header, json=data).json()
    #     out_format("巡查计划--新增:", r)
    #     scheduleId = r["data"]["schedule"]["id"]  # 巡查任务id， 下面的巡查详情需要调用
    #     print("scheduleId:", scheduleId)
    #     return scheduleId

    # def comment_list(self):
    #     """巡查记录-评论列表
    #     :param:page:页码
    #     :param:target_type:目标类型 1：巡检记录
    #     :param:target_id:目标id
    #     :param:page_size:每页条数
    #     以上均为必填
    #     """
    #     # scheduleId_04 = self.Patrol_add("2019-03-28", "2019-03-28")
    #     # sleep(60)
    #     url = host + "/api/comments"
    #     data = {"target_type": 1, "target_id": 90}
    #     r = requests.get(url=url, headers=header_xun, params=data).json()
    #     out_format("巡查记录--评论列表:", r)
    #     return scheduleId_04

    def comment_add(self):
        """巡查记录-添加评论
        :param:content:评论内容
        :param:replied_id:回复的评论id-----非必填
        :param:target_type:评论对象类型 1：巡查记录
        :param:target_id:评论对象id，对应[巡查记录列表]返回的字段的【id】
        """
        # scheduleId_05 = self.comment_list()
        url = host + "/api/comments"
        data = {"content": "尽快整改，领导要来检查", "target_type": 1, "target_id": 321}
        r = requests.post(url=url, headers=header_xun, json=data).json()
        out_format("巡查记录--添加评论:", r)


# test().comment_list()
# test().comment_add()

import time,datetime
from datetime import datetime,timedelta

ti = datetime.now()+timedelta(minutes=1)
print(ti.strftime("%Y-%m-%d %H:%M"))



# print(datetime.datetime.today())
