import requests
import os
from time import sleep
from interfaceTest.GMALL.gmall_header import golbal_shopid, header, host

# host, header, token = get_header_pc()


# print(os.getcwd())


# 顾客行为——顾客管理API
class cus_manage(object):
    """

    定义一个wiki顾客行为Tab中菜单名为顾客管理的所有接口测试类

    """

    def label_list(self, tag_type, tag, shop_id=golbal_shopid, keyword=None, search_type=None):
        """获取标签/客群列表,type=1是标签，type=2是客群
    :param tag_type: 类型 ---1：标签 2：客群(int)
    :param tag: 客群/标签
    :param keyword: 模糊搜索关键字(string)
    :param search_type:当有keyword时为必填,1：搜索标签名 2：搜索标签id 3：搜索备注(int)
    :param shop_id:门店id
    :return: tag_list,返回标签/客群id列表
    """
        url = host + "/api/shops/%s/tags" % shop_id
        data = {"type": tag_type}
        r = requests.get(url=url, headers=header, params=data).json()
        print("获取标签/客群列表type=%s[%s]:" % (tag_type, tag), r, "\n")
        tag_list = []
        if r["data"]["tags"] is not None:
            s = len(r["data"]["tags"])
            for i in range(s):
                tag_list.append(r["data"]["tags"][i]["id"])
                print(tag_list)
                print("获取【%s,type=%s】列表:" % (tag, tag_type), r)
        else:
            print("tags is null")
        return tag_list

    # def label_details(self, types_int, types_value, tag_id_01, shop_id=golbal_shopid):
    #     """获取标签/客群详情,type=1是标签，type=2是客群"""
    #     url = host + "/api/shops/%s/tags/%s" % (shop_id, tag_id_01)
    #     r = requests.get(url=url, headers=header).json()
    #     print("获取标签/客群详情type=%s[%s]:" % (types_int, types_value), r, "\n")
    #
    # def creat_label(self, shop_id=golbal_shopid):
    #     """创建标签/客群，type=1是标签，type=2是客群"""
    #     url = host + "/api/shops/%s/tags" % shop_id
    #     r = requests.post(url=url, headers=header)
    #     print("创建标签/客群:", r, "\n\n")
    #
    # def update_label(self, shop_id=golbal_shopid):
    #     """更新标签/客群"""
    #     url = host + "/api/shops/%s/tags/%s" % (shop_id, tags_id)
    #     r = requests.put(url=url, headers=header).json()
    #     print("更新标签/客群:", r, "\n\n")
    #
    # def delete_label(self, shop_id=golbal_shopid):
    #     """删除标签/客群"""
    #     url = host + "/api/shops/%s/tags/%s" % (shop_id, tags_id)
    #     r = requests.delete(url=url, headers=header).json()
    #     print("删除标签/客群:", r, "\n\n")
    #
    # def order_list(self, shop_id=golbal_shopid):
    #     """订单管理--列表"""
    #     url = host + "/api/shops/%s/orders" % shop_id
    #     r = requests.get(url=url, headers=header).json()
    #     print("订单管理--列表:", r, "\n\n")
    #
    # def order_sort(self, shop_id=golbal_shopid):
    #     """订单管理--品类"""
    #     url = host + "/api/shops/%s/order-categories" % shop_id
    #     r = requests.get(url=url, headers=header).json()
    #     print("订单管理--品类:", r, "\n\n")
    #
    # def order_details(self, order_id, shop_id=golbal_shopid):
    #     """订单管理--详情"""
    #     url = host + "/api/shops/%s/orders/%s/detail" % (shop_id, order_id)
    #     r = requests.get(url=url, headers=header).json()
    #     print("订单管理--详情:", r, "\n\n")
    #
    # def order_export(self, shop_id=golbal_shopid):
    #     """订单管理--列表导出"""
    #     url = host + "/api/shops/%s/orders/export" % shop_id
    #     r = requests.get(url=url, headers=header).json()
    #     print("订单管理--列表导出:", r, "\n\n")
    #
    # def customer_funnel(self, start_date, end_date, shop_id=golbal_shopid):
    #     """顾客漏斗"""
    #     url = host + "/api/shops/%s/customer-buy-conversion" % shop_id
    #     data = {"start_date": start_date, "end_date": end_date}
    #     r = requests.get(url=url, headers=header, params=data).json()
    #     print("顾客漏斗:", r, "\n\n")
    #
    # def customer_funnel_export(self, start_date, end_date, shop_id=golbal_shopid):
    #     """顾客漏斗-列表导出"""
    #     url = host + "/api/shops/%s/export/customer-buy-conversion" % shop_id
    #     data = {"start_date": start_date, "end_date": end_date}
    #     r = requests.get(url=url, headers=header, params=data)
    #     print("顾客漏斗-列表导出:", r.text, "\n\n")


cus_manage().label_list(1, "标签")
