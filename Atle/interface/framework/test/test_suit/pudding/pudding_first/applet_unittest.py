import unittest
import requests
import json
from Atle.interface.framework.test.test_suit.pudding.header_n import host, header
from Atle.interface.framework.test.test_suit.pudding.pudding_first.first_base import DRP
from Atle.interface.framework.common.color import out_format

drp = DRP()

class applet(unittest.TestCase):
    """定义一个分销小程序的整体测试类"""
    def test_01_address_add(self):
        """创建收货地址"""
        r = drp.address_add()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_02_address_del(self):
        """地址删除"""
        r = drp.address_del()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_03_address_update(self):
        """地址更新"""
        r = drp.address_update()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_04_address_one(self):
        """获取单个地址"""
        r = drp.address_one()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_05_banner(self):
        """Banner图"""
        r = drp.banner()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_06_advert(self):
        """广告拉取"""
        r = drp.advert()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_07_collectList(self):
        """收藏列表"""
        r = drp.collectList()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_08_collectActivity(self):
        """单品收藏/取消"""
        r = drp.collectActivity()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_09_collectCancel(self):
        """批量取消收藏"""
        r = drp.collectCancel()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_10_goodsFind(self):
        """产品详情"""
        r = drp.goodsFind()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_11_goodsSearch(self):
        """搜索"""
        r = drp.goodsSearch()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_12_goods_check(self):
        """检查库存"""
        r = drp.goods_check()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_13_IndexMenuList(self):
        """菜单列表"""
        r = drp.IndexMenuList()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_14_moreShop(self):
        """开店申请"""
        r = drp.moreShop()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_15_moreIdea(self):
        """意见反馈"""
        r = drp.moreIdea()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_16_orderPay(self):
        """二次支付"""
        r = drp.orderPay()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_17_orderDelete(self):
        """删除订单"""
        r = drp.orderDelete()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_18_orderUpdate(self):
        """更新订单"""
        r = drp.orderUpdate()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_19_orderCreate(self):
        """订单创建/提交"""
        r = drp.orderCreate()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_20_orderFind(self):
        """订单详情"""
        r = drp.orderFind()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_21_profit_log_calculate(self):
        """交易完成--利润分配"""
        r = drp.profit_log_calculate()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_22_ProfitLogDetail(self):
        """收入明细"""
        r = drp.ProfitLogDetail()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_23_towithdrawable(self):
        """转为可提现"""
        r = drp.towithdrawable()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_24_shopActivity(self):
        """店铺商品上下架"""
        r = drp.shopActivity()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_25_shopGoods(self):
        """店铺商品列表"""
        r = drp.shopGoods()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_26_shopUpdate(self):
        """更新店铺信息"""
        r = drp.shopUpdate()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_27_shopCheck(self):
        """检查店铺状态"""
        r = drp.shopCheck()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_28_shopBind(self):
        """绑定店铺"""
        r = drp.shopBind()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_29_shopQrcode(self):
        """获取店铺/商品二维码"""
        r = drp.shopQrcode()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_30_shopFind(self):
        """获取店铺信息"""
        r = drp.shopFind()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_31_shopBindUserList(self):
        """获取绑定用户"""
        r = drp.shopBindUserList()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_32_walletIndex(self):
        """获取账户信息"""
        r = drp.walletIndex()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_33_widthdrawLog_create(self):
        """提交提现"""
        r = drp.widthdrawLog_create()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_34_withdrawlist(self):
        """提现记录"""
        r = drp.withdrawlist()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_35_consumelist(self):
        """钱包消费记录"""
        r = drp.consumelist()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_36_investGift(self):
        """礼包产品"""
        r = drp.investGift()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_37_investCreate(self):
        """订单创建/提交"""
        r = drp.investCreate()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_38_investList(self):
        """礼包购买记录"""
        r = drp.investList()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))

    def test_39_investFind(self):
        """礼包购买记录详情"""
        r = drp.investFind()
        self.assertEqual(r["code"], 1, msg="失败原因: %s != %s" % (r["code"], 1))


if __name__ == "__main__":
    unittest.main()
else:
    print("false")

