# 此文件为产品的相关接口
# goods模块
import requests
from Atle.interface.framework.common.header_s import host  # 依赖头部文件封装的方法 host,头部和token
from Atle.interface.framework.common.public_func import sku, goods_id  # 依赖公共文件返回的字段被多次调用
from Atle.interface.framework.common.color import out_format


class goods():
    def get_goods(self):
        """
        获取单品
        :return: gid
        """
        url = host + "/api/goods/find"
        data = {"sku": sku, "gid": goods_id}
        r = requests.post(url=url, data=data).json()
        out_format("获取单品:", r)
        # gid = r["data"]["gid"]
        # return gid

    def get_price(self):
        """
        获取单品价格和属性
        :return:
        """
        url = host + "/api/goods/line"
        data = {"sku": sku, "gid": goods_id}
        r = requests.post(url=url, data=data).json()
        out_format("获取单品价格和属性:", r)
        return r

    def get_comment(self):
        """
        获取评论列表
        gid:产品id
        size:记录条数
        page:页码
        :return:
        """
        # gid = self.get_goods()
        url = host + "/api/goods/comment"
        data = {"gid": goods_id, "size": "10", "page": "1"}
        r = requests.post(url=url, json=data).json()
        out_format("获取评论列表:", r)
        return r
