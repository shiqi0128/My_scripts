# ---------------------此文件专为调试使用-------------------
# import time
# local_time = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime(time.time()))
# print(local_time)

# for i in range(8):
#     print(i)

# for i in [0, 1, 2, 3]:
#     print(i)

# import requests
# import time
# import json
# import random
# import HTMLTestRunner
# from Atle.interface.header_s import host, header  # 依赖头部文件封装的方法 host,头部和token
# # from Atle.interface.public_func import sku, goods_id, openitem_id, address_id, p_id, order_no  # 依赖公共文件返回的字段被多次调用
# from Atle.interface.color import out_format
# from urllib3 import encode_multipart_formdata


# def accusation_list():
#     """举报列表
#     :param:token:用户授权token
#     :param:page:页数,默认值1
#     :param:size:单页数量,默认值10
#     """
#     report_id_list = []
#     object_id_list = []
#     object_type_list = []
#     memo_list = []
#     reported_id_list = []
#     category_id_list = []
#     url = host + "/api/accusation/index"
#     data = {"page": 1, "size": 10}
#     r = requests.get(url=url, headers=header, params=data).json()
#     out_format("举报列表:", r)
#     if r["data"]["list"] is not None:
#         len_s = len(r["data"]["list"])
#         print("len_s =", len_s)
#         for i in range(len_s):
#             print("i =", i)    # 不能遍历i，这是一个问题,与订单列表不能遍历i是一个情况,还在想办法解决中!! 191011
#             report_id_list.append(r["data"]["list"][i]["id"])
#             print(report_id_list)
#             object_type_list.append(r["data"]["list"][i]["object_type"])
#             object_id_list.append(r["data"]["list"][i]["object_id"])
#             memo_list.append(r["data"]["list"][i]["memo"])
#             reported_id_list.append(r["data"]["list"][i]["reported"])
#             category_id_list.append(r["data"]["list"][i]["category_id"])
#             for index, report_id in enumerate(report_id_list, 1):
#                 for index, object_type in enumerate(object_type_list, 1):
#                     for index, object_id in enumerate(object_id_list, 1):
#                         for index, memo in enumerate(memo_list, 1):
#                             for index, reported in enumerate(reported_id_list, 1):
#                                 for index, category_id in enumerate(category_id_list, 1):
#                                     print(report_id, object_type, object_id, memo, reported, category_id)
#                                     return report_id, object_type, object_id, memo, reported, category_id
#     else:
#         print("data is null")
#         print("导购列表", r, "\n")
#     return None




            # return report_id, object_type, object_id, memo, reported, category_id


# accusation_list()

# a = {'code': 1, 'msg': 'ok', 'data': [], 'next': 2}
# print(len(a["data"]))

# a = {'code': 1, 'msg': 'ok', 'data': {'id': 172, 'cid': 0, 'gid': '3795933991573098332', 'title': '暹罗猫母猫', 'brief': '产品简介',
#                                   'thumb': [
#                                       'http://csapp.aiitle.com:88/uploads/20191107/thumb_fcc6df3168671a61b73d991985a7dbd8___500x333.jpg'],
#                                   'productprice': '500.00', 'marketprice': 100000, 'stock': 100, 'sales': 0, 'isdef': 0,
#                                   'type': 3, 'mart_total': '100.00', 'content': '<p>产品详情</p>', 'sku': '2',
#                                   'sku_item': '母猫', 'status': 1, 'hit_count': 5, 'collect_count': 0, 'share_count': 0,
#                                   'price': '400.00', 'total': 0}}
#
# r = a["code"]
# print(r)
import requests
import unittest
from Atle.interface.framework.common.color import out_format
from Atle.interface.framework.common.header_s import host, header


def test_address_list():
    """获取地址列表
    :param:token:用户授权token
    :return:address_id:地址id
    """
    # header = get_header()
    url = host + "/api/address/list"
    r = requests.post(url=url, headers=header).json()
    out_format("获取地址列表:", r)
    if len(r["data"]) != 0:
        address_id = r["data"][0]["id"]
        print(address_id)
        return address_id
    else:
        print("data is NULL")


def test_order_list():
    """订单列表
    :param:token:用户授权token
    :param:size:单页记录数
    :param:page:页码
    :param:status:订单状态（0.待支付 1.待发货 2.待收货 3.待评论）
    :return: order_no:订单编号
    """
    # header = get_header()
    url = host + "/api/order/list"
    # status = {i for i in [0, 1, 2, 3]}
    # print(status)
    for i in [0, 1, 2, 3]:
        print(i)
        data = {"size": 10, "page": 1, "status": i}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("订单列表:", r)
        # for i in range(len(r["data"])):    # 这里不能遍历i,是个问题，写完后过来复查！
        #     order_no = r["data"][i]["order_no"]    # 接上面，已解决：注：不能遍历的原因在于我return了，加return后第一遍遍历后就会结束
        if len(r["data"]) != 0:
            order_no = r["data"][0]["order_no"]
            print("order_no:", order_no)
            return order_no
        else:
            print("data is NULL")

test_address_list()
test_order_list()