# 以下为收银防损的接口文件
import unittest
import requests
import json
import os
import random
from time import sleep
from interfaceTest.GMALL.gmall_header import golbal_shopid, host, header, token
from interfaceTest.GMALL.gmall_all.color import out_format

class Cashier_security():
    """定义一个收银防损的测试类"""
    def Cashier(self, shop_id=golbal_shopid):
        """收银防损
        :param:shop:门店id
        :param:start_date:订单支付时间范围开始
        :param:end_date:订单支付时间范围结束
        :param:cashier_number:收银员编号
        :param:pos_number:收银机编号，pos机编号
        :param:third_customer_id:顾客编号
        :param:mobile:顾客手机号
        :param:order_no:订单编号
        :param:order_amount[operator]:订单金额[表达式]
        :param:order_amount[amount]:订单金额[价格]
        :param:order_number[operator]:订单件数[表达式]
        :param:order_number[number]:订单件数[数量]
        :param:product_name:商品名称
        :param:product_amount[operator]:商品单价[表达式]
        :param:product_amount[amount]:商品单价[价格]
        """
        url = host + "/api/shops/%s/orders/cashier-loss" % shop_id
        form_data = [
            {
                "根据订单时间查询":
                    {
                        "start_date": "2019-03-10", "end_date": "2019-03-10",
                        "cashier_number": "xxx_3",
                        "pos_number": "POS_NO0002",
                        "third_customer_id": "55",
                        "third_mobile": "13250511526",
                        "order_no": "31232625163385008",
                        "order_amount[operator]": "<=", "order_amount[amount]": "6400",
                        "product_number[operator]": ">=", "product_number[number]": "8",
                        "product_name": "茅台",
                        "product_amount[operator]": "<=", "product_amount[amount]": "800"
                    }
            },
            # {"根据收银员编号查询": {"start_date": "2019-03-10", "end_date": "2019-03-10", "cashier_number": "xxx_3"}},
            # {"根据收银机编号查询": {"start_date": "2019-03-10", "end_date": "2019-03-10", "pos_number": "POS_NO0002"}},
            # {"根据顾客编号查询": {"start_date": "2019-03-10", "end_date": "2019-03-10", "third_customer_id": "55"}},
            # {"根据顾客手机号查询": {"start_date": "2019-03-10", "end_date": "2019-03-10", "third_mobile": "13250511526"}},
            # {"根据订单编号查询": {"start_date": "2019-03-10", "end_date": "2019-03-10", "order_no": "31232625163385008"}},
            # {"订单金额[表达式]&[价格]":
            #      {
            #         "start_date": "2019-03-10", "end_date": "2019-03-10",
            #         "order_amount[operator]": "<=", "order_amount[amount]": "6400"
            #       }
            # },
            # {
            #     "订单件数[表达式]&[订单件数]":
            #         {
            #             "start_date": "2019-03-10", "end_date": "2019-03-10",
            #             "product_number[operator]": ">=", "product_number[number]": "8"
            #         }
            # },
            # {"商品名称": {"start_date": "2019-03-10", "end_date": "2019-03-10", "product_name": "茅"}},
            # {
            #     "商品单价[表达式]&[价格]":
            #         {"start_date": "2019-03-10", "end_date": "2019-03-10",
            #          # "cashier_number": "xxx_3", "pos_number": "POS_NO0002",
            #          "product_amount[operator]": "<=", "product_amount[amount]": "800"
            #          }
            # },
        ]
        for data in form_data:
            for data2 in data:
                r = requests.get(url=url, headers=header, params=data[data2]).json()
                out_format("收银防损--%s:" % data2, r)


Cashier_security().Cashier()
