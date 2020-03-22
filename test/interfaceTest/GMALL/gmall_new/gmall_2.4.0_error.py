"""此文件包含gmall2,4.0所有异常场景测试脚本"""
import unittest
import requests
import random
from time import sleep
from interfaceTest.GMALL.gmall_header import golbal_shopid, host, header
from interfaceTest.GMALL.gmall_all.color import out_format
# from interfaceTest.GMALL.gmall_new.gmall_business_model import Merch_sales


class business_model():
    """定义一个gmall2.4.0的异常场景测试类"""
    # def category_stats(self, shop_id=golbal_shopid):
    #     """品类占比
    #     :param:start_date:开始日期
    #     :param:end_date:结束日期
    #     """
    #     url = host + "/api/shops/%s/product/categories-stats" % shop_id
    #     # data = {"start_date": start_date, "end_date": end_date}
    #     r = requests.get(url=url, headers=header).json()
    #     out_format("品类占比:", r)

    # def category_export(self, start_date, end_date, shop_id=golbal_shopid):
    #     """品类占比--导出
    #     :param:start_date:开始日期
    #     :param:end_date:结束日期
    #     """
    #     url = host + "/api/shops/%s/export/categories-stats" % golbal_shopid
    #     data = {"start_date": start_date, "end_date": end_date}
    #     r = requests.get(url=url, headers=header, params=data)
    #     out_format("品类占比--导出:", r.text)
    #
    # def Sales_cycle(self, start_date=None, end_date=None, shop_id=golbal_shopid):
    #     """销量周期
    #     :param:start_date:开始日期
    #     :param:end_date:结束日期
    #     :param:category_id:指定类别统计
    #     以上均为非必填
    #     """
    #     url = host + "/api/shops/%s/product/sale-period" % shop_id
    #     r = requests.get(url=url, headers=header).json()
    #     out_format("销量周期:", r)
    #
    # def Sales_export(self, start_date=None, end_date=None, shop_id=golbal_shopid):
    #     """销量周期--导出
    #     :param:start_date:开始日期
    #     :param:end_date:结束日期
    #     :param:category_id:指定类别统计
    #     以上均为非必填
    #     """
    #     url = host + "/api/shops/%s/export/sale-period" % shop_id
    #     r = requests.get(url=url, headers=header)
    #     out_format("销量周期--导出:", r.text)

    def Merch_sales(self, shop_id=golbal_shopid):
        """商品销售经营分析--异常场景，此接口不填必填项start_date，end_date
        :param:shop:门店id
        :param:start_date:开始日期
        :param:end_date:结束日期
        :param:page_size:分页条数（默认10）---非必填
        :param:product_id:商品id---非必填
        :param:product_name:商品名--非必填
        :param:category_id:品类ID--非必填
        :param:sort_field:order_num : 订单量; cusomer_num ：下单人数;sales_num ：商品销量; sales_amount：商品金额 unit_price：销售单价
        :param:sort_type:排序值 (asc:升序，desc:倒序)
        """
        url = host + "/api/shops/%s/manage/product-analyze" % shop_id
        form_data = [
            {"全部为空": {"start_date": "", "end_date": ""}},
            {"start_date为空": {"start_date": "", "end_date": "2019-03-01"}},
            {"end_date为空": {"start_date": "2019-03-01", "end_date": ""}},
            {"start_date大于end_date": {"start_date": "2019-03-05", "end_date": "2019-03-01"}},
            {"start_date小于end_date": {"start_date": "2019-03-01", "end_date": "2019-03-05"}}
        ]
        for data in form_data:     # 循坏列表，得到的值是列表下的每一长条的字典
            for da in data:         # 循坏上面的循坏得到的每一长条的字典，得到字典里面的key,即"全部为空"这些key,循坏结果显示key的value值
                print("da", da)
                r = requests.get(url=url, headers=header, params=data[da]).json()    # 循坏da得到的value值就是需要上传的请求参数
                out_format("商品销售经营分析%s:" % da, r)

    # def Merch_sales_export(self, start_date, end_date, shop_id=golbal_shopid):
    #     """商品销售经营分析--导出
    #     :param:shop:门店id
    #     :param:start_date:开始日期
    #     :param:end_date:结束日期
    #     :param:page_size:分页条数（默认10）---非必填
    #     :param:product_id:商品id---非必填
    #     :param:product_name:商品名--非必填
    #     :param:category_id:品类ID--非必填
    #     """
    #     url = host + "/api/shops/%s/export/product-analyze" % shop_id
    #     data = {"start_date": start_date, "end_date": end_date}
    #     r = requests.get(url=url, headers=header, params=data)
    #     out_format("商品销售经营分析--导出:", r.text)
    #
    # def sales_trend(self, start_date, end_date, shop_id=golbal_shopid):
    #     """商品销售--趋势
    #     :param:shop:门店id
    #     :param:start_date:开始日期
    #     :param:end_date:结束日期
    #     :param:product_id:商品id
    #     """
    #     url = host + "/api/shops/%s/manage/product-trend/%s" % (shop_id, product_id)
    #     data = {"start_date": start_date, "end_date": end_date}
    #     r = requests.get(url=url, headers=header, params=data).json()
    #     out_format("商品销售--趋势:", r)
    #
    # def sales_trend_export(self, start_date, end_date, shop_id=golbal_shopid):
    #     """商品销售--趋势导出
    #     :param:shop:门店id
    #     :param:start_date:开始日期
    #     :param:end_date:结束日期
    #     :param:product_id:商品id
    #     """
    #     url = host + "/api/shops/%s/manage/product-trend/%s" % (shop_id, product_id)
    #     data = {"start_date": start_date, "end_date": end_date}
    #     r = requests.get(url=url, headers=header, params=data)
    #     out_format("商品销售趋势--导出:", r.text)
    #
    # def sales_relates(self, start_date, end_date, shop_id=golbal_shopid):
    #     """商品销售--关联
    #     :param:shop:门店id
    #     :param:start_date:开始日期
    #     :param:end_date:结束日期
    #     :param:product_id:商品id
    #     """
    #     url = host + "/api/shops/%s/manage/product-trend/%s" % (shop_id, product_id)
    #     data = {"start_date": start_date, "end_date": end_date}
    #     r = requests.get(url=url, headers=header, params=data).json()
    #     out_format("商品销售趋势--导出:", r)
    #
    # def sales_relates_export(self, start_date, end_date, shop_id=golbal_shopid):
    #     """商品销售--关联导出
    #     :param:shop:门店id
    #     :param:start_date:开始日期
    #     :param:end_date:结束日期
    #     :param:product_id:商品id
    #     """
    #     url = host + "/api/shops/%s/manage/product-trend/%s" % (shop_id, product_id)
    #     data = {"start_date": start_date, "end_date": end_date}
    #     r = requests.get(url=url, headers=header, params=data)
    #     out_format("商品销售--关联导出:", r.text)
    #
    # def shop_list(self):
    #     """门店列表"""
    #     url = host + "/api/company/stats-shops-list"
    #     r = requests.get(url=url, headers=header).json()
    #     out_format("门店列表:", r)
    #
    # def shop_trend(self, start_date, end_date):
    #     """门店趋势
    #     :param:shop:门店id--数组格式
    #     :param:start_date:开始日期
    #     :param:end_date:结束日期
    #     """
    #     url = host + "/api/company/trend-shops"
    #     data = {"shop_ids": [25], "start_date": start_date, "end_date": end_date}
    #     r = requests.post(url=url, headers=header, json=data).json()
    #     out_format("门店趋势:", r)


# business_model().category_stats()
# business_model().category_export("2019-03-01", "2019-03-01")
# business_model().Sales_cycle()
# business_model().Sales_export()
business_model().Merch_sales()
# business_model().Merch_sales_export("2019-03-01", "2019-03-01")
# business_model().sales_trend("2019-03-01", "2019-03-01")
# business_model().sales_relates_export("2019-03-01", "2019-03-01")
# business_model().sales_relates("2019-03-01", "2019-03-01")
# business_model().sales_relates_export("2019-03-01", "2019-03-01")
# business_model().shop_list()
# business_model().shop_trend("2019-03-01", "2019-03-01")
# business_model().shop_trend_export("2019-03-01", "2019-03-01")



# [
#     {"为空": {"riqi":"","jieshu":""}},
#
#
#
#
#
# ]