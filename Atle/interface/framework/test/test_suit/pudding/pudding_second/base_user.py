# 此文件为宠布丁小程序V2.0的用户身份登录接口脚本基础代码
import requests
import random
import json
from Atle.interface.framework.test.test_suit.pudding.header_user import host, header_user     # 调用用户的头部文件
from Atle.interface.framework.test.test_suit.pudding.pudding_first.public_applet import address_id, category_id, shop_id, order_no, goods_id, sku_id
from Atle.interface.framework.common.color import out_format


class DRP_N():
    """创建一个爱它乐小程序的测试类"""
    def goodsDiff(self):
        """今日特惠/新品推荐
        :param:openid:用户授权openid
        :param:shop_id:店铺ID
        :param:size:单页记录数 (不传默认：10)
        :param:page:页码 (不传默认：1)
        :param: type:类别（2.今日特惠，3.新品推荐）
        :param:field:排序字段（价格：productprice，收藏：collect_num，销量：sales_num）
        :param:sort:排序方向（正序：asc，倒序：desc）
        """
        url = host + "/api/goods/diff"
        data = {"shop_id": shop_id, "size":10, "page": 1, "type": 2}
        r = requests.post(url=url, headers=header_user, data=data).json()
        out_format("今日特惠/新品推荐:", r)

    def goodsSearch(self):
        """搜索
        :param:openid:用户授权openid
        :param:shop_id:店铺ID
        :param: keyword:搜索关键字
        :param:size:单页记录数 (不传默认：10)
        :param:page:页码 (不传默认：1)
        """
        url = host + "/api/goods/search"
        data = {"shop_id": shop_id, "keyword": "狗粮", "size": 10, "page": 1}
        r = requests.post(url=url, headers=header_user, data=data).json()
        out_format("搜索:", r)

    def goodsCheck(self):
        """检查库存
        :param:openid:用户授权openid
        :param:shop_id:店铺ID
        :param:data:产品数据,允许值: [{"goods_id":"20", "sku_id":"1"}, {"goods_id":"17", "sku_id":"1, 1"}, {"goods_id":"17", "sku_id":"1, 2"}]
        """
        url = host + "/api/goods/check"
        data = {"shop_id": shop_id, "data": [{"goods_id": goods_id, "sku_id": sku_id}]}
        r = requests.post(url=url, headers=header_user, data=data)
        out_format("检查库存:",r.status_code)    # 这个接口状态码返回500  日期date 03041417

    def searchIndex(self):
        """获取搜索信息
        :param:openid:用户授权openid
        """
        url = host + "/api/search/index"
        r = requests.get(url=url, headers=header_user).json()
        out_format("获取搜索信息:", r)
        if len(r["data"]["user"] ) != 0:
            word = r["data"]["user"][0]["id"]
            return word
        else:
            print("搜索信息是空的")

    def searchDelete(self):
        """删除单个词
        :param:openid:用户授权openid
        :param:id:单词id
        """
        word = self.searchIndex()
        url = host + "/api/search/delete"
        data = {"id": word}
        r = requests.post(url=url, headers=header_user, data=data).json()
        out_format("删除单个词:", r)

    def searchclean(self):
        """清空搜索历史
        :param:openid:用户授权openid
        """
        url = host + "/api/search/clean"
        r = requests.post(url=url, headers=header_user).json()
        out_format("清空搜索历史:", r)

    def discount_list(self):
        """优惠券/礼包列表
        :param:openid:用户授权openid
        :param:tag:标题（传 0.新人礼包 1.优惠券 2.所有，包括新人礼包和优惠券）
        """
        url = host + "/api/discount/list"
        data = {"tag": 2}
        r = requests.post(url=url, headers=header_user, data=data).json()
        out_format("优惠券/礼包列表:", r)

    # def discountHome(self):
    #     """我的优惠券
    #     :param:openid:用户授权openid
    #     :param:issue:状态（0.未使用 1.已使用）
    #     """
    #     url = host + "/api/discount/home"
    #     issue = [0, 1]
    #     for i in range(len(issue)):
    #         data = {"issue": i}
    #         r = requests.post(url=url, headers=header_user, data=data).json()
    #         out_format("我的优惠券:", r)
    def discountHome(self):
        """我的优惠券
        :param:openid:用户授权openid
        :param:issue:状态（0.未使用 1.已使用）
        """
        url = host + "/api/discount/home"
        data = {"issue": 0}
        r = requests.post(url=url, headers=header_user, data=data).json()
        out_format("我的优惠券:", r)
        if len(r["data"]) != 0:
            discount_id = r["data"][0]["id"]
            return discount_id     # 返回优惠券id
        else:
            print("当前用户没有未领取的优惠券!")

    def discountInvalid(self):
        """我的优惠券--已失效
        :param:openid:用户授权openid
        """
        url = host + "/api/discount/invalid"
        r = requests.post(url=url, headers=header_user).json()
        out_format("我的优惠券--已失效:", r)

    def discountOpen_gift(self):
        """打开新人礼包
        :param:openid:用户授权openid
        """
        url = host + "/api/discount/open_gift"
        r = requests.post(url=url, headers=header_user).json()
        out_format("打开新人礼包:", r)

    def discountGain(self):
        """领取优惠券
        :param:openid:用户授权openid
        :param:id:优惠券ID
        """
        discount_id = self.discountHome()
        url = host + "/api/discount/gain"
        data = {"id": discount_id}
        r = requests.post(url=url, headers=header_user, data=data).json()
        out_format("领取优惠券:", r)

    def investGift(self):
        """礼包产品
        :param:openid:用户授权openid
        """
        url = host + "/api/invest/gift"
        r = requests.post(url=url, headers=header_user).json()
        out_format("礼包产品:", r)

    def investList(self):
        """礼包购买记录
        :param:openid:用户授权openid
        """
        url = host + "/api/invest/list"
        r = requests.post(url=url, headers=header_user).json()
        if len(r["data"]) != 0:
            out_format("礼包购买记录:", r)
        else:
            print("\033[1;36;45m{0}\033[0m".format("礼包购买记录:"), "当前用户没有礼包购买记录")
            # print("礼包购买记录: 当前用户没有礼包购买记录")

    def investFind(self):
        """礼包购买记录详情
        :param:openid:用户授权openid
        :param:order_no:订单号
        """
        url = host + "/api/invest/find"
        data = {"order_no": ""}
        r = requests.post(url=url, headers=header_user, data=data).json()
        out_format("礼包购买记录详情:", r)

# DRP_N().goodsDiff()       # 今日特惠/新品推荐
# DRP_N().goodsSearch()     # 搜索
# DRP_N().goodsCheck()      # 检查库存
# DRP_N().searchIndex()     # 获取搜索信息
# DRP_N().searchDelete()    # 删除单个词
# DRP_N().searchclean()     # 清空搜索历史
DRP_N().discount_list()     # 优惠券/礼包列表
# DRP_N().discountHome()      # 我的优惠券
DRP_N().discountInvalid()     # 我的优惠券--已失效
DRP_N().discountGain()      # 领取优惠券
DRP_N().investGift()        # 礼包产品
DRP_N().investList()        # 礼包购买记录
# DRP_N().investFind()        # 礼包购买记录详情

