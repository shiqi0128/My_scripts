# -----------------此文件是所有需要调用多次的公共方法----------------------
import requests
import unittest
from Atle.interface.framework.common.color import out_format
from Atle.interface.framework.common.header_s import host, header


class pubilc_func(unittest.TestCase):
    """定义一个公共方法的测试类"""
    def test_get_pro_list(self):
        """获取产品列表
        :return:sku:商品规格
        """
        url = host + "/api/goods/list"
        r = requests.get(url=url).json()
        out_format("获取产品列表:", r)
        if len(r["data"]) != 0:
            sku = r["data"][-1]["sku"]
            goods_id = r["data"][-1]["id"]   # 产品的id就是data下的id,不是gid
            print("sku:", sku)
            return sku, goods_id
        else:
            print("data is NULL")

    def test_address_list(self):
        """获取地址列表
        :param:token:用户授权token
        :return:address_id:地址id
        """
        # header = get_header()
        url = host + "/api/address/list"
        r = requests.post(url=url, headers=header).json()
        out_format("获取地址列表:", r)
        if len(r["data"]) != 0:
            address_id = r["data"][0]["id"]
            print(address_id)
            return address_id
        else:
            print("data is NULL")

    def test_order_list(self):
        """订单列表
        :param:token:用户授权token
        :param:size:单页记录数
        :param:page:页码
        :param:status:订单状态（0.待支付 1.待发货 2.待收货 3.待评论）
        :return: order_no:订单编号
        """
        # header = get_header()
        url = host + "/api/order/list"
        # status = {i for i in [0, 1, 2, 3]}
        # print(status)
        for i in [0, 1, 2, 3]:
            print(i)
            data = {"size": 10, "page": 1, "status": i}
            r = requests.post(url=url, headers=header, data=data).json()
            out_format("订单列表:", r)
            # for i in range(len(r["data"])):    # 这里不能遍历i,是个问题，写完后过来复查！
            #     order_no = r["data"][i]["order_no"]    # 接上面，已解决：注：不能遍历的原因在于我return了，加return后第一遍遍历后就会结束
            if len(r["data"]) != 0:
                order_no = r["data"][0]["order_no"]
                print("order_no:", order_no)
                return order_no
            else:
                print("data is NULL")

    def test_save_categorys(self):
        """open省钱分类
        :return: items_id:子分类id
        """
        url = host + "/api/openitem/categorys"
        r = requests.get(url=url).json()
        out_format("open省钱分类:", r)
        if len(r["data"]["19"]["child"]) != 0:
            items_id = r["data"]["19"]["child"][0]["id"]     # 此操作为提取分类下第一个大分类下面的第一个子分类
            print("items_id:", items_id)
            return items_id
        else:
            print("data is NULL")

    def test_open_list(self):
        """open商品列表
        :param:page:页数，默认值1
        :param:size:单页数量，默认值10
        :param:category_id:分类id,此参数由open省钱分类返回的id
        :param:tag_id:标签id,默认值-1,即全部
        :param:platform:平台，默认值-1，允许值'jd','taobao','tmall','aiitle'
        :param:sort:价格排序，默认值0,允许值"1", "-1", "0"
        :param:recommend:这个参数为yes，就只显示后台设置推荐的，no时，不限制条件都显示
        :return:
        """
        items_id = self.test_save_categorys()
        url = host + "/api/openitem/index"
        platform = ["jd", "taobao", "tmall", "aiitle"]
        for i in platform:
            # print(i)
            data = {
                    "page": 1,
                    "size": 10,
                    "category_id": items_id,
                    "tag_id": -1,
                    "platform": i,
                    "sort": 0,        # 价格排序，默认值0
                    "recommend": "no"
                    }
            r = requests.get(url=url, params=data).json()
            if len(r["data"]["list"]) != 0:
                out_format("open商品列表--%s:" % i, r)
                if len(r["data"]["list"])  != 0:
                    openitem_id = r["data"]["list"][0]["id"]    # 提取外部的开放商品id用于后面创建评论的接口请求参数
                    print("openitem_id:", openitem_id)
                    return openitem_id
                else:
                    print(i + "没有数据")
            else:
                print("data is NULL")

    def test_comment_list(self):
        """评论列表
        :param:token:用户授权的token
        :param:page:页数，1
        :param:size:单页数量，10
        :param:openitem_id:商品id
        :return:p_id:为评论列表提取的最新添加的第一条评论
        """
        url = host + "/api/openitem_comment/index"
        data = {"size": 10, "page": 1, "openitem_id": 224}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("评论列表:", r)
        if len(r["data"]["list"]["latest"]) != 0:
            p_id = r["data"]["list"]["latest"][0]["id"]  # 此操作为提取评论id
            return p_id
        else:
            print("data is NULL")


# order_list()
# sku, goods_id = pubilc_func().test_get_pro_list()
# address_id = pubilc_func().test_address_list()
# order_no = pubilc_func().test_order_list()
# openitem_id = pubilc_func().test_open_list()
# p_id = pubilc_func().test_comment_list()
if __name__ == '__main__':
    unittest.main()
else:
    print("false")