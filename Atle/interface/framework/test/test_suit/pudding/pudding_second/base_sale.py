# 此文件为宠布丁小程序V2.0的商家身份登录接口脚本基础代码
import requests
import random
import json
from Atle.interface.framework.test.test_suit.pudding.header_sale import host, header_sale
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
        r = requests.post(url=url, headers=header_sale, data=data).json()
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
        r = requests.post(url=url, headers=header_sale, data=data).json()
        out_format("搜索:", r)

    def goodsCheck(self):
        """检查库存
        :param:openid:用户授权openid
        :param:shop_id:店铺ID
        :param:data:产品数据,允许值: [{"goods_id":"20", "sku_id":"1"}, {"goods_id":"17", "sku_id":"1, 1"}, {"goods_id":"17", "sku_id":"1, 2"}]
        """
        url = host + "/api/goods/check"
        data = {"shop_id": shop_id, "data": [{"goods_id": goods_id, "sku_id": sku_id}]}
        r = requests.post(url=url, headers=header_sale, data=data)
        out_format("检查库存:",r.status_code)    # 这个接口状态码返回500  日期date 03041417

    def searchIndex(self):
        """获取搜索信息
        :param:openid:用户授权openid
        """
        url = host + "/api/search/index"
        r = requests.get(url=url, headers=header_sale).json()
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
        r = requests.post(url=url, headers=header_sale, data=data).json()
        out_format("删除单个词:", r)

    def searchclean(self):
        """清空搜索历史
        :param:openid:用户授权openid
        """
        url = host + "/api/search/clean"
        r = requests.post(url=url, headers=header_sale).json()
        out_format("清空搜索历史:", r)

# DRP_N().goodsDiff()       # 今日特惠/新品推荐
# DRP_N().goodsSearch()     # 搜索
# DRP_N().goodsCheck()      # 检查库存
# DRP_N().searchIndex()     # 获取搜索信息
# DRP_N().searchDelete()    # 删除单个词
# DRP_N().searchclean()     # 清空搜索历史

