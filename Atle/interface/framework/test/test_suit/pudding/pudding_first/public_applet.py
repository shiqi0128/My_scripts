import requests
import random
import json
from Atle.interface.framework.test.test_suit.pudding.header_sale import host, header_sale
from Atle.interface.framework.common.color import out_format


def address_list():
    """获取地址列表
    :param:token:用户授权openid
    :return:address_id:地址id
    """
    # header = get_header()
    url = host + "/api/address/list"
    r = requests.post(url=url, headers=header_sale).json()
    out_format("获取地址列表:", r)
    if len(r["data"]) != 0:
        address_id = r["data"][0]["id"]
        print(address_id)
        return address_id
    else:
        print("data is NULL")


# Category
def categoryList():
    """分类列表"""
    url = host + "/api/category/list"
    r = requests.post(url=url).json()
    out_format("分类列表:", r)
    if len(r["data"]) != 0:
        category_id = r["data"][2]["id"]    # 获取分类id,现在只有猫粮的分类下面有数据，猫粮下标是2，id=1
        print("category_id:", category_id)
        return category_id
    else:
        print("data is null")


def orderList():
    """订单列表
    :param:openid:用户授权openid
    :param:status:订单状态 (不传默认：-1， -1.全部 0.待付款 1.待发货 2.待收货 3.交易完成 4.交易关闭)
    :param:size:单页记录数 (不传默认：10)
    :param:page:页码 (不传默认：1)
    """
    url = host + "/api/order/list"
    data = {"status": -1, "size": 10, "page": 1}
    r = requests.post(url=url, headers=header_sale, data=data).json()
    out_format("订单列表:", r)
    if len(r["data"]) != 0:
        order_no = r["data"][0]["order_no"]
        print("order_no:", order_no)
        return order_no
    else:
        print("data is null")


def goodsList():
    """产品列表
    :param:openid:用户授权openid
    :param:category_id:分类ID
    :param:shop_id:店铺ID------调试时先默认传1
    :param: type:排序类型 (不传默认：ID， 收藏：collect_num，销量：sales_num，价格：productprice)
    :param:sort:排序方式 (不传默认：desc， 倒序(最新的)：desc，正序：asc)
    :param:size:单页记录数 (不传默认：10)
    :param:page:页码 (不传默认：1)
    """
    url = host + "/api/goods/list"
    data = {
        "category_id": category_id,  # 现在只有猫粮的分类下面有数据，id=1
        "shop_id": shop_id,
        "type": "id",
        "sort": "desc",
        "size": 10,
        "page": 1
    }
    r = requests.post(url=url, headers=header_sale, data=data).json()
    out_format("产品列表:", r)
    if len(r["data"]) != 0:
        goods_id = r["data"][0]["goods_id"]
        print("goods_id:", goods_id)
        return goods_id
    else:
        print("data is null")


# Goods
def goodsRecommend():
    """为你推荐
    :param:openid:用户授权openid
    :param:size:单页记录数 (不传默认：10)
    :param:page:页码 (不传默认：1)
    """
    url = host + "/api/goods/recommend"
    data = {"size": 10, "page": 1}
    r = requests.post(url=url, headers=header_sale, data=data).json()
    out_format("为你推荐:", r)
    if len(r["data"]) != 0:
        sku_id = r["data"][-1]["sku_id"]
        return sku_id
    else:
        print("data is null")

# def shopCreate():
#     """开店信息
#     :param:openid:用户授权openid
#     :param:title:店铺名称
#     :param:contacter:联系人
#     :param:mobile:联系人电话
#     """
#     url = host + "/api/shop/create"
#     data = {
#         "title": "爱他美%s" % random.randrange(1, 1000),
#         "contacter": "张晓彤%s" % random.randrange(1, 1000),
#         "mobile": "15250511512"
#     }
#     r = requests.post(url=url, headers=header, data=data).json()
#     out_format("开店信息:", r)
#     shop_id = r["data"]["id"]
#     print("shop_id:", shop_id)
#     return shop_id

def shopCheck():
    """检查店铺状态
    :param:openid:用户授权openid
    """
    url = host + "/api/shop/check"
    r = requests.post(url=url, headers=header_sale).json()
    out_format("检查店铺状态:", r)
    shop_id = r["data"]["id"]
    print("shop_id:", shop_id)
    return shop_id


address_id = address_list()
category_id = categoryList()
shop_id = shopCheck()

order_no = orderList()
goods_id = goodsList()
sku_id = goodsRecommend()
# shop_id = shopCreate()

