# 此文件为宠布丁小程序V1.0的接口脚本基础代码
import requests
import random
import json
from Atle.interface.framework.test.test_suit.pudding.header_n import host, header
from Atle.interface.framework.test.test_suit.pudding.pudding_first.public_applet import address_id, category_id, shop_id, order_no, goods_id, sku_id
from Atle.interface.framework.common.color import out_format



class DRP():
    """创建一个爱它乐小程序的测试类"""
    def address_add(self):
        """创建收货地址
        :param:openid--头部header
        :param:name:姓名
        :param:phone:手机号
        :param:city:省市区
        :param:address:地址
        """
        url = host + "/api/address/create"
        data = {
            "name": "张三%s" % random.randrange(1, 1000),
            "phone": "15850511512",
            "city": "苏州",
            "address": "保利居上",
            "isdefault": 0
      }
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("创建地址:", r)
        return r

    def address_del(self):
        """地址删除
        :param:openid--头部header
        """
        url = host + "/api/address/delete"
        data = {"id": address_id}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("删除地址:", r)
        return r

    def address_update(self):
        """地址更新
        :param:openid--头部header
        :param:id:地址id
        :param:name:姓名
        :param:phone:手机
        :param:city:省市区
        :param:address:地址
        :param:isdefault:是否默认地址，默认值0
        """
        url = host + "/api/address/update"
        data = {
            "id": address_id,
            "name": "李四%s" % random.randrange(1, 1000),
            "phone": "15850511512",
            "city": "苏州",
            "address": "保利居上%s"% random.randrange(1, 1000),
            "isdefault": 0
        }
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("地址更新:", r)
        return r

    def address_one(self):
        """
        获取单个地址
        :param:openid:用户授权的openid
        :param:id:地址id
        """
        url = host + "/api/address/find"
        data = {"id": address_id}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("获取单个地址:", r)
        return r

    # Banner
    def banner(self):
        """Banner图"""
        url = host + "/api/banner/list"
        r = requests.post(url=url).json()
        out_format("Banner图:", r)
        return r

    def advert(self):
        """广告拉取"""
        url = host + "/api/banner/advert"
        r = requests.get(url=url).json()
        out_format("广告拉取:", r)
        return r

    # Collect
    def collectList(self):
        """收藏列表
        :param:openid:用户授权openid
        :param:size:单页记录数 (不传默认：10)
        :param:page:页码 (不传默认：1)
        """
        url = host + "/api/collect/list"
        data = {"size": 10, "page": 1}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("收藏列表:", r)
        if len(r["data"]) != 0:
            goods_id = r["data"][0]["goods_id"]
            sku_id = r["data"][0]["sku_id"]
            return goods_id, sku_id
        else:
            print("data is null")


    def collectActivity(self):
        """单品收藏/取消
        :param:openid:用户授权openid
        :param:goods_id:产品id----由收藏列表返回
        :param:sku_id:规格id----由收藏列表返回
        """
        goods_id, sku_id = self.collectList()
        url = host + "/api/collect/activity"
        data = {
            "goods_id": goods_id,
            "sku_id": sku_id
        }
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("单品收藏/取消:", r)
        return r

    def collectCancel(self):
        """批量取消收藏
        :param:openid:用户授权openid
        :param:ids:	收藏记录ID（多个用英文,号隔开，如：1,2,3...）
        """
        url = host + "/api/collect/cancel"
        data = {"ids": ""}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("批量取消收藏:", r)
        return r

# Goods
    def goodsFind(self):
        """产品详情
        :param:openid:用户授权openid
        :param:goods_id:产品id-----由产品列表的接口返回
        :param:sku_id:规格ID------由为你推荐的接口返回
        """
        # sku_id = self.goodsRecommend()
        # goods_id = self.goodsList()
        url = host + "/api/goods/find"
        data = {"goods_id": goods_id, "sku_id": sku_id}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("产品详情:", r)
        return r

    def goodsSearch(self):
        """搜索
        :param:openid:用户授权openid
        :param:shop_id:店铺ID
        :param: keyword:搜索关键字-----经测试，传的产品列表或者详情返回的name字段为搜索关键词
        :param:size:单页记录数 (不传默认：10)
        :param:page:页码 (不传默认：1)
        """
        url = host + "/api/goods/search"
        data = {
            "shop_id": shop_id,
            "keyword": "小",
            "size": 10,
            "page": 1
        }
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("搜索:", r)
        return r

    def goods_check(self):
        """检查库存
        :param:openid:用户授权openid
        :param:shop_id:当前店铺ID-----取哪个接口返回值？？
        :param:data:产品数据,允许值: [{"goods_id":"20", "sku_id":"1"}, {"goods_id":"17", "sku_id":"1, 1"}, {"goods_id":"17", "sku_id":"1, 2"}]
        """
        url = host + "/api/goods/check"
        data = json.dumps({"shop_id": shop_id, "data": [{"goods_id": goods_id, "sku_id": sku_id}]})
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("检查库存:", r)
        return r

    # Index
    def IndexMenuList(self):
        """菜单列表"""
        url = host + "/api/index/menu_list"
        r = requests.post(url=url).json()
        out_format("菜单列表:", r)
        return r

    # More开店
    def moreShop(self):
        """开店申请
        :param:openid:用户授权openid
        :param: type: 传参类型num；开店类型id值描述:id=1:普通用户；id=2,白金用户（199元等级）；id=3,黄金用户；id=4,铂金用户；id=5,钻石用户
        :param:fullname:姓名
        :param:phone:联系方式
        """
        url = host + "/api/more/shop"
        data = {
            "type": 1,   # id=1
            "fullname": "王五%s" % random.randrange(1, 1000),
            "phone": "18750511512"
        }
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("开店申请:", r)
        return r

    def moreIdea(self):
        """意见反馈
        :param:openid:用户授权openid
        :param:content:意见内容
        """
        url = host + "/api/more/idea"
        data = {"content": "信息填写错误%s" % random.randrange(1, 1000)}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("意见反馈:", r)
        return r

    # Order  订单
    def orderPay(self):
        """二次支付
        :param:openid:用户授权openid
        :param: order_no:订单号
        """
        url = host + "/api/order/pay"
        data = {"order_no": order_no}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("二次支付:", r)
        return r

    def orderDelete(self):
        """删除订单
        :param:openid:用户授权openid
        :param:order_no:订单号
        """
        url = host + "/api/order/delete"
        data = {"order_no": order_no}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("删除订单:", r)
        return r

    def orderUpdate(self):
        """更新订单
        :param:openid:用户授权openid
        :param:order_no:订单号
        :param:status:订单状态（确认收货传：3，取消订单传：4）
        """
        url = host + "/api/order/update"
        data = {
            "order_no": order_no,
            "status": 3
        }
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("更新订单:", r)
        return r

    def orderCreate(self):
        """订单创建/提交
        :param:openid:用户授权openid
        :param:address_id:地址id
        :param:shop_id:店铺ID
        :param: type:支付方式（1.微信支付 2.钱包支付）
        :param:order:产品 如格式：[{"goods_id":1,"sku_id": "1,1","count":1}]----上传的时候转换成json格式上传
        :param:id:产品id
        :param:count:数量
        """
        url = host + "/api/order/create"
        data = {
            "address_id": address_id,
            "shop_id": shop_id,
            "type": 1,
            "order": json.dumps([{"goods_id": goods_id, "sku_id": sku_id, "count": 1}])
        }
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("订单创建/提交:", r)
        return r

    def orderFind(self):
        """订单详情
        :param:openid:用户授权openid
        :param:order_no:订单号
        """
        url = host + "/api/order/find"
        data = {"order_no": order_no}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("订单详情:", r)
        return r

    # ProfitLog
    def profit_log_calculate(self):
        """交易完成--利润分配
        :param:openid:用户授权openid
        :param:order_no:订单号
        """
        url = host + "/api/profit_log/calculate"
        data = {"order_no": order_no}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("利润分配:", r)
        return r

    def ProfitLogDetail(self):
        """收入明细
        :param:openid:用户授权openid
        :param: type:类型,允许值: "order订单收益", "level_commision佣金收益", "sale_commision提成收益"
        :param:page:页数,默认值: 1
        :param:size:单页数量，默认值:10
        """
        url = host + "/api/profit_log/detail"
        types = ["order","level_commision", "sale_commision"]
        for type in types:
            data = {"type": type, "page": 1, "size": 10}
            r = requests.get(url=url, headers=header, params=data).json()
            out_format("收入明细:", r)
            return r

    def towithdrawable(self):
        """转为可提现
        :param:openid:用户授权openid
        :param:order_no:订单号
        """
        url = host + "/api/profit_log/to_withdrawable"
        data = {"order_no": order_no}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("转为可提现:", r)
        return r

    # Shop
    def shopActivity(self):
        """店铺商品上下架
        :param:openid:用户授权openid
        :param:category_id:品类ID（品类ID从C端品类接口获取）
        :param:shop_id:店铺ID
        :param:goods_id:产品ID
        """
        url = host + "/api/shop/activity"
        data = {"category_id": category_id, "shop_id": shop_id, "goods_id": goods_id}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("店铺商品上下架:", r)
        return r

    def shopGoods(self):
        """店铺商品列表
        :param:openid:用户授权openid
        :param:category_id:品类ID（品类ID从C端品类接口获取）
        :param:shop_id:店铺ID
        :param:page:页数,默认值: 1
        :param:size:单页数量，默认值:10
        """
        url = host + "/api/shop/goods"
        data = {"category_id": category_id, "shop_id": shop_id, "page": 1, "size": 10}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("店铺商品列表:", r)
        return r

    def shopUpdate(self):
        """更新店铺信息
        :param:openid:用户授权openid
        :param:title:店铺名称
        :param:contacter:联系人
        :param:mobile:联系电话
        :param:inviter:邀请人
        """
        url = host + "/api/shop/update"
        data = {"title": "十七的宠猫舍", "contacter": "十七", "mobile": "15850511512"}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("更新店铺信息:", r)
        return r

    def shopCheck(self):
        """检查店铺状态
        :param:openid:用户授权openid
        """
        url = host + "/api/shop/check"
        r = requests.post(url=url, headers=header).json()
        out_format("检查店铺状态:", r)
        return r

    def shopBind(self):
        """绑定店铺
        :param:openid:用户授权openid
        :param:shop_id:店铺ID----从开店信息的接口获取
        """
        url = host + "/api/shop/bind"
        data = {"shop_id": shop_id}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("绑定店铺:", r)
        return r

    def shopQrcode(self):
        """获取店铺/商品二维码
        :param:openid:用户授权openid
        :param:scene:分享参数(固定格式：0_店铺ID_(Goods_id)_(sku_id))_____字符串格式传参
        """
        url = host + "/api/shop/qrcode"
        data = {"scene": "0_%s_%s_%s" % (shop_id, goods_id, sku_id)}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("获取店铺/商品二维码:", r)
        return r

    def shopFind(self):
        """获取店铺信息
        :param:openid:用户授权openid
        :param:shop_id:店铺ID----不知道从哪里获取??-----在检测店铺状态的接口返回结果获取
        """
        url = host + "/api/shop/find"
        data = {"shop_id": shop_id}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("获取店铺信息:", r)
        return r

    # ShopBindUser
    def shopBindUserList(self):
        """获取绑定用户
        :param:openid:用户授权openid
        :param:page:页数,默认值: 1
        :param:size:单页数量，默认值:10
        """
        url = host + "/api/Shopbinduser/list"
        data = {"page": 1, "size": 10}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("获取绑定用户:", r)
        return r

    # Wallet
    def walletIndex(self):
        """获取账户信息
        :param:openid:用户授权openid
        """
        url = host + "/api/wallet/index"
        r = requests.post(url=url, headers=header).json()
        out_format("获取账户信息:", r)
        return r

    # WidthdrawLog
    def widthdrawLog_create(self):
        """
        提交提现
        :param:openid:用户授权openid
        :param:amount:提现金额/分____注意:这边的金额单位是分
        """
        url = host + "/api/withdraw_log/create"
        data = {"amount": 10}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("提交提现:", r)
        return r

    def withdrawlist(self):
        """提现记录
        :param:openid:用户授权openid
        :param:page:页数,默认值: 1
        :param:size:单页数量，默认值:10
        """
        url = host + "/api/withdraw_log/withdraw_list"
        data = {"page": 1, "size": 10}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("提现记录:", r)
        return r

    def consumelist(self):
        """
        钱包消费记录
        :param:openid:用户授权openid
        :param:page:页数,默认值: 1
        :param:size:单页数量，默认值:10
        """
        url = host + "/api/withdraw_log/consume_list"
        data = {"page": 1, "size": 10}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("钱包消费记录:", r)
        return r

    # invest
    def investGift(self):
        """礼包产品
        :param:openid:用户授权openid
        """
        url = host + "/api/invest/gift"
        r = requests.post(url=url, headers=header).json()
        out_format("礼包产品:", r)
        return r

    def investCreate(self):
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
        return r

    def investList(self):
        """礼包购买记录
        :param:openid:用户授权openid
        """
        url = host + "/api/invest/list"
        r = requests.post(url=url, headers=header).json()
        out_format("礼包购买记录:", r)
        return r

    def investFind(self):
        """礼包购买记录详情
        :param:openid:用户授权openid
        :param:order_no:订单号
        """
        url = host + "/api/invest/find"
        data = {"order_no": order_no}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("礼包购买记录详情:", r)
        return r


# DRP().address_add()     # 创建收货地址
# DRP().address_del()     # 删除收货地址
# DRP().address_update()     # 地址更新
# DRP().address_one()         # 获取单个地址
# DRP().banner()              # Banner图
# DRP().advert()     # 广告拉取
# DRP().collectList()     # 收藏列表
# # DRP().collectActivity()    # ------此接口运行前提需要直接怎么+收藏，不然此接口只能运行2遍，现在只有2个产品，运行后收藏列表会没有数据
# # DRP().collectCancel()      # --------同上
# DRP().goodsFind()      # 产品详情
# DRP().goodsSearch()    # 搜索
# DRP().goods_check()    # 检查库存
# DRP().IndexMenuList()  # 菜单列表
# DRP().moreShop()       # 开店申请
# DRP().moreIdea()        # 意见反馈
# DRP().orderPay()          # 二次支付
# DRP().orderDelete()      # 删除订单
# DRP().orderUpdate()     # 更新订单
# DRP().orderCreate()             # 订单创建/提交
# DRP().orderFind()               # 订单详情
# DRP().profit_log_calculate()    # 交易完成--利润分配
# DRP().ProfitLogDetail()         # 收入明细
# DRP().towithdrawable()          # 转为可提现
# DRP().shopActivity()  # 店铺商品上下架
# DRP().shopGoods()     # 店铺商品列表
# DRP().shopUpdate()    # 更新店铺信息
# DRP().shopBind()      # 绑定店铺
# DRP().shopQrcode()    # 获取店铺/商品二维码
# DRP().shopFind()      # 获取店铺信息
# DRP().ShopBindUserList()   # 获取绑定用户
# DRP().WalletIndex()    # 获取账户信息
# # DRP().WidthdrawLog_create()   # 提交提现    ------此接口会报错，原因是因为微信提现功能没有审核通过，暂时不能使用提现功能，所以会报500
# DRP().withdrawlist()    # 提现记录
# DRP().consumelist()       # 钱包消费记录
# DRP().investGift()        # 礼包产品
# DRP().investCreate()      # 订单创建/提交   -------此接口参数不传值也不会报错，接口没有细化，暂时先这样
# DRP().investList()        # 礼包购买记录
# DRP().investFind()        # 礼包购买记录详情





