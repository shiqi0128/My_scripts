import requests
from interfaceTest.GMALL.gmall_header import host, golbal_shopid, get_header_pc
from interfaceTest.GMALL.gmall_all.color import out_format
import random


header, token1 = get_header_pc()
# 此文件为公共调用的文件

# def guide_list(shop_id=golbal_shopid):
#     """导购-列表
#     :param:shop:门店id
#     :param:page_size 分页条数（非必填）
#     :param:page 页码（默认1）（非必填）
#     """
#     guide_id_list = []
#     url = host + "/api/shops/%s/salemans" % shop_id
#     r = requests.get(url=url, headers=header).json()
#     if r["data"]["salemans"]["data"] is not None:
#         s = len(r["data"]["salemans"]["data"])
#         print("长度:", s)
#         for i in range(s):
#             guide_id_list.append(r["data"]["salemans"]["data"][i]["id"])
#             for index, guide_id in enumerate(guide_id_list, 1):
#                 print("获取导购id[%s]:" % index, r["data"]["salemans"]["data"][i]["id"], "\n")
#                 out_format("导购列表:", r)
#                 return guide_id
#     else:
#         print("data is null")
#         print("导购列表", r, "\n")
#     return None
#
#
# guide_id = guide_list()     # 此接口返回值guide_id为导购id可供 导购新增、更新、删除接口调用，参数名为saleman
#
#
# def blacklist(identity= None, customer_id= None, shop_id=golbal_shopid):
#         """黑名单列表"""
#         blacklist_id_all = []
#         url = host + "/api/shops/%s/blacklist" % shop_id
#         r = requests.get(url=url, headers=header).json()
#         s = r["data"]["blacklists"]["data"]
#         if r["data"]["blacklists"]["data"] is not None:
#             for i in range(len(s)):
#                 blacklist_id = r["data"]["blacklists"]["data"][i]["id"]
#                 blacklist_id_all.append(blacklist_id)
#                 print("获取黑名单id[%s]:" % blacklist_id, "\n")
#                 out_format("黑名单列表", r)
#                 return blacklist_id     # r["data"]["blacklists"]["data"]不为空则返回blacklist_id，为空则返回None
#         else:
#             print("data is null")
#             out_format("黑名单列表", r)
#         return None
#
#
# blacklist_id = blacklist()              # 此接口返回值blacklist_id为导购id可供 导购新增、更新、删除接口调用，参数名为blacklist


def account_list():
    """账号列表"""
    # account_list = []
    url = host + "/api/user?page="
    r = requests.get(url=url, headers=header).json()
    # s = r["data"]["users"]["data"]
    if r["data"]["users"]["data"] is not None:
        user_id = r["data"]["users"]["data"][-1]["id"]  # 巡查人
        user_name = r["data"]["users"]["data"][-1]["username"]  # 巡查人账号
        user_id_01 = r["data"]["users"]["data"][-2]["id"]   # 整改人
        user_name_01 = r["data"]["users"]["data"][-2]["username"]
        # account_list.append(user_id)
        print("获取巡查人user_id[%s]username\033[1;31m[%s]:\033[0m" % (user_id, user_name), "\n")
        print("获取整改人user_id_01[%s]username_01\033[1;31m[%s]:\033[0m:" % (user_id_01, user_name_01), "\n")
        out_format("账号列表:", r)
        return user_id, user_id_01, user_name
    else:
        print("data is null")
        out_format("账号列表:", r)
        return None


user_id, user_id_01, user_name = account_list()    # 此操作为设置全局变量，账号列表的方法赋值给return出的结果值，即user_id, user_name
# user_id 是巡查人，user_id_01是整改人


def report_creat(email, type_ids, shop_id=golbal_shopid):
    """订阅者创建
    :param:email:邮箱
    :param:shop_ids:门店id--数组形式传参
    :param:type_ids:订阅类型 id--数组形式传参
    """
    url = host + "/api/report-subscribers"
    data = {"email": email, "type_ids": [type_ids], "shop_ids": [str(shop_id)]}
    r = requests.post(url=url, headers=header, json=data).json()
    out_format("订阅者创建:", r)
    report_id = r["data"]["subscriber"]["id"]
    print("获取订阅者id[%s]:" % report_id, "\n")
    # print(r)
    # if r["data"]["subscriber"]is not None:
    #     report_id = r["data"]["subscriber"]["id"]
    #     print("获取订阅者id[%s]:" % report_id, "\n")
    #     out_format("订阅者创建:", r)
    #     return report_id
    # else:
    #     print("无数据")
    #     out_format("订阅者创建", r)
    # return None


report_id = report_creat("%s@163.com" % random.randrange(3, 30000), "娱乐")
# 此操作为设置全局变量，订阅者创建这个接口的方法赋值给return出来的report_id，供主调文件调用
#
#
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
#     if r["data"]["stats"]["data"] is not None:
#         s = len(r["data"]["stats"]["data"])
#         for i in range(s):
#             product_id = r["data"]["stats"]["data"][i]["product_id"]
#             out_format("商品销售经营分析:", r)
#             return product_id
#     else:
#         print("data is null")
#         return None
#
#
# product_id = Merch_sales("2019-01-13", "2019-01-14")
