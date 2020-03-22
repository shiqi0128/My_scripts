# ------------------此文件为主调文件--------------------
import unittest
from Atle.interface.framework.base.aGoods import goods
from Atle.interface.framework.base.aAddress import address
from Atle.interface.framework.base.aOpenitem import openitem
from Atle.interface.framework.base.aOrder import order
from Atle.interface.framework.base.aOpenitemComment import openitemcomment
# from Atle.interface.framework.Accusation import Accusation

goods = goods()
adr = address()
open = openitem()
ord = order()
openic = openitemcomment()
# acc = Accusation()


class Alte(unittest.TestCase):
    """定义一个爱它乐相关的整体测试类"""
# goods
    def test_01_get_price(self):
        """获取单品价格和属性"""
        r = goods.get_price()
        self.assertEqual(r["code"], 1)

    def test_02_get_comment(self):
        """获取评论列表"""       # 此方法在主要文件Goods内调用了获取单品的接口
        r = goods.get_comment()
        self.assertEqual(r["code"], 1)

# Address
    def test_03_creat_address(self):
        """创建收货地址"""
        r = adr.creat_address()
        self.assertEqual(r["code"], 1)

    def test_04_address_update(self):
        """地址更新"""
        r = adr.address_update()
        self.assertEqual(r["code"], 1)

    def test_05_address_del(self):
        """地址删除"""
        r = adr.address_del()
        self.assertEqual(r["code"], 1)

    def test_06_address_one(self):
        """获取单个地址"""
        r = adr.address_one()
        self.assertEqual(r["code"], 1)

# Openitem
    def test_07_open_item(self):
        """open动态相关商品----此接口返回的字段传给dynamic_list的category_id"""
        r = open.open_item()
        self.assertEqual(r["code"], 1)

    def test_08_goods_one(self):
        """open单个商品"""
        r = open.goods_one()
        self.assertEqual(r["code"], 1)

    def test_09_goods_search(self):
        """open商品搜索"""
        r = open.goods_search()
        self.assertEqual(r["code"], 1)

    def test_10_goods_advertise(self):
        """open商品首页广告"""
        r = open.goods_advertise()
        self.assertEqual(r["code"], 1)

    def test_11_home_tags(self):
        """open商品首页标签"""
        r = open.home_tags()
        self.assertEqual(r["code"], 1)

    def test_12_keywords(self):
        """搜索词记录"""
        r = open.keywords()
        self.assertEqual(r["code"], 1)

    def test_13_empty(self):
        """open清空搜索记录"""
        r = open.empty()
        self.assertEqual(r["code"], 1)

    def test_14_creat_order(self):
        """提交订单"""
        r = ord.creat_order()
        self.assertEqual(r["code"], 1)

    def test_15_order_pay(self):
        """订单支付（二次支付）"""
        r = ord.order_pay()
        self.assertEqual(r["code"], 1)

    def test_16_update_order(self):
        """更新订单"""
        r = ord.update_order()
        self.assertEqual(r["code"], 1)

    def test_17_order_detail(self):
        """订单详情"""
        r = ord.order_detail()
        self.assertEqual(r["code"], 1)

# openitemcomment
    def test_18_add_comment(self):
        """添加评论"""
        r = openic.add_comment()
        self.assertEqual(r["code"], 1)

    def test_19_comment_list(self):
        """评论列表"""
        r = openic.comment_list()
        self.assertEqual(r["code"], 1)

    def test_20_Ocomment(self):
        """一个评论"""
        r = openic.Ocomment()
        self.assertEqual(r["code"], 1)

    def test_21_update_comment(self):
        """更新评论"""
        r = openic.update_comment()
        self.assertEqual(r["code"], 1)

    def test_22_comment_delete(self):
        """删除评论"""
        r = openic.comment_delete()
        self.assertEqual(r["code"], 1)

# accusation 举报
#     def test_23_accusation_type(self):
#         """举报类型"""
#         r = acc.accusation_type()
#         self.assertEqual(r["code"], 1)
#
#     def test_24_accusation_details(self):
#         """举报详情"""
#         r = acc.accusation_details()
#         self.assertEqual(r["code"], 1)
#
#     def test_25_accusation_delete(self):
#         """删除举报"""
#         r = acc.accusation_delete()
#         self.assertEqual(r["code"], 1)


if __name__ == "__main__":
    unittest.main()
else:
    print("false")
