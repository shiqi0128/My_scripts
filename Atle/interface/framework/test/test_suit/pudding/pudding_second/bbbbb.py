# 此文件专为调试用

# import time
# print("当前时间为:", time.strftime("%Y-%m-%d %X", time.localtime()))
# # print(time.strptime("2020-03-04 14:56:58", "%Y-%m-%d %X"))
#
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# import requests
# import random
# import json
# from Atle.interface.framework.test.test_suit.Applet.header_user import host, header_user     # 调用用户的头部文件
# from Atle.interface.framework.test.test_suit.Applet.applet_one.public_applet import address_id, category_id, shop_id, order_no, goods_id, sku_id
# from Atle.interface.framework.common.color import out_format


# 第一个接口要返回已使用和未使用
# def discountHome(self):
#     """我的优惠券
#     :param:openid:用户授权openid
#     :param:issue:状态（0.未使用 1.已使用）
#     """
#     url = host + "/api/discount/home"
#     data = {"issue": 0}
#     r = requests.post(url=url, headers=header_user, data=data).json()
#     out_format("我的优惠券:", r)
#
# def discountGain(self):
#     """领取优惠券
#     :param:openid:用户授权openid
#     :param:id:优惠券ID
#     """
#     url = host + "/api/discount/gain"
#     data = {"id": ""}
#     r = requests.post(url=url, headers=header_user, data=data).json()
#     out_format("领取优惠券:", r)

# import keyword
# print(keyword.kwlist)
# ipython = 13
# print(ipython)


# third = []
# for i in range(1, 101):
#     if i % 3 == 0:
#         third.append(i)
#         print(third)
#         print("被3整除的", len(third))
#         if i % 5 == 0:
#             third.append(i)
#             print("被5整除的", len(third))
#             if i % 8 == 0:
#                 third.append(i)
#                 print("被8整除的", len(third))
#     else:
#         print("hahahahaha")


# a = [1, 2, 3]
# print(len(a))


url= "http://www.python.org"
# str = url[11:17]
# print(str)
str = url[-10:-4]
print(str)
