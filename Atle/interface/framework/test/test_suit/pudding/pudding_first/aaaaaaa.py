# data = []
# s = len(data)
# if s != 0:
#     print(data)
# else:
#     print("data is null")


# types = ["order", "level_commision", "sale_commision"]
# for type in types:
#     data = {"type": type, "page": 1, "size": 10}
#     print(data)

import requests
import random
import json
from Atle.interface.framework.test.test_suit.pudding.header_n import host, header
from Atle.interface.framework.test.test_suit.pudding.pudding_first.public_applet import address_id, category_id, order_no, goods_id, sku_id
from Atle.interface.framework.common.color import out_format


# def moreShop():
#     """开店申请
#     :param:openid:用户授权openid
#     :param: type: 传参类型num；开店类型id值描述:id=1:普通用户；id=2,白金用户（199元等级）；id=3,黄金用户；id=4,铂金用户；id=5,钻石用户
#     :param:fullname:姓名
#     :param:phone:联系方式
#     """
#     url = host + "/api/more/shop"
#     data = {
#         "type": 1,  # id=1
#         "fullname": "王五%s" % random.randrange(1, 1000),
#         "phone": "18750511512"
#     }
#     r = requests.post(url=url, headers=header, data=data).json()
#     out_format("开店申请:", r)
#
# moreShop()

# def shopCheck():
#     """检查店铺状态
#     :param:openid:用户授权openid
#     """
#     url = host + "/api/shop/check"
#     r = requests.post(url=url, headers=header).json()
#     out_format("检查店铺状态:", r)
#
# shopCheck()

# def WidthdrawLog_create():
#     """
#     提交提现
#     :param:openid:用户授权openid
#     :param:amount:提现金额/分
#     """
#     url = host + "/api/withdraw_log/create"
#     data = {"amount": 100}
#     r = requests.post(url=url, headers=header, data=data)
#     out_format("提交提现:", r.status_code)
#
# WidthdrawLog_create()


def investCreate():
    """订单创建/提交
    :param:openid:用户授权openid
    :param: type:(1.礼包购买 2.帐户升级，默认1)
    :param:id:礼包产品ID (type为2时，非必填)
    :param:address_id:地址ID (type为2时，非必填)
    :param:total:等级金额/元 (type为1时，非必填)
    """
    url = host + "/api/invest/create"
    data = {"type": 1, "id": 1, "address_id": 1, "total": 199}
    r = requests.post(url=url, headers=header, data=data).json()
    out_format("订单创建/提交:", r)


investCreate()
