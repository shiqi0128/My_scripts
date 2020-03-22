# 此文件为外部商品接口
# Openitem
import requests
from Atle.interface.framework.common.header_s import host, header  # 依赖头部文件封装的方法 host,头部和token
from Atle.interface.framework.common.public_func import openitem_id  # 依赖公共文件返回的字段被多次调用
from Atle.interface.framework.common.color import out_format


class openitem():
    def classify_list(self):
        """
        分类列表----此接口返回的字段传给dynamic_list的category_id
        :param: type:对象类型,默认传moment（现在是只有这一种type）
        :return:category_id:分类id
        """
        url = host + "/api/category/index"
        data = {"type": "moment"}
        r = requests.get(url=url, params=data).json()
        out_format("分类列表:", r)
        if len(r["data"]) != 0:
            category_id = r["data"][1]["id"]
            print("category_id:", category_id)
            return category_id
        else:
            print("data is NULL")

    def dynamic_list(self):
        """
        动态列表---此接口返回的字段传给open_item的object_id
        :param:token:用户授权的token
        :param:page:页数
        :param:size:单页数量
        :param:category_id:分类id(由分类列表返回的id)
        :param:recommend:推荐：yes,正常：no
        :return:
        """
        category_id = self.classify_list()
        url = host + "/api/Moment/index"
        data = {
                "page": 1,
                "size": 10,
                "category_id": category_id,
                "recommend": "yes"
        }
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("动态列表:", r)
        if len(r["data"]["list"]) != 0:
            dynamic_id = r["data"]["list"][-2]["id"]   # 动态列表提取动态id,dynamic_id,传给动态相关产品的接口
            print("动态id:", dynamic_id)
            return dynamic_id
        else:
            print("data is NULL")

    def open_item(self):
        """
        Openitem - open动态相关商品
        :param:object_type:对象类型,默认值: moment
        :param:object_id:对象ID,目前只有1533这个id
        :param: page:页数，默认值1
        :param:size:单页数量，默认值10
        :return:
        """
        # dynamic_id = self.dynamic_list()   # 暂时用object_id=1533，暂时不调用动态列表的id
        url = host + "/api/openitem/getRelations"
        data = {
                    "object_type": "moment",
                    "object_id": 1533,
                    "page": 1,
                    "size": 10
        }
        r = requests.get(url=url, params=data).json()
        out_format("open动态相关商品:", r)
        return r

    def goods_one(self):
        """open单个商品
        :param: id:开放商品id---是商品列表返回的id
        """
        url = host + "/api/openitem/get"
        data = {"id": openitem_id}
        r = requests.get(url=url, params=data).json()
        out_format("open单个商品:", r)
        return r

    def goods_search(self):
        """open商品搜索
        :param:page:页数，默认值1
        :param:size:单页数量，默认值10
        :param: keyword:关键词
        :param:object_type:对象类型,允许值"openitem", "goods"
        均为必填
        """
        url = host + "/api/openitem/search"
        object_type = ["openitem", "goods"]
        for i in object_type:
            data = {
                "page": 1,
                "size": 10,
                "keyword": "猫",
                "object_type": i
            }
            r = requests.get(url=url, params=data).json()
            out_format("open商品搜索--%s:" % i, r)
            return r

    def goods_advertise(self):
        """
        open商品首页广告
        """
        url = host + "/api/openitem/advert"
        r = requests.get(url=url).json()
        out_format("open商品首页广告:", r)
        return r

    def home_tags(self):
        """
        open商品首页标签
        """
        url = host + "/api/openitem/hometag"
        r = requests.get(url=url).json()
        out_format("open商品首页标签:", r)
        return r

    def keywords(self):
        """
        搜索词记录
        ---此接口包含了热门和历史搜索记录
        """
        url = host + "/api/openitem/keywords"
        r = requests.get(url=url).json()
        out_format("open搜索词记录:", r)
        return r

    def empty(self):
        """
        open清空搜索记录
        ——执行此接口只会清空掉历史搜索记录，不会清空热门搜索词
        """
        url = host + "/api/openitem/keywords"
        r = requests.get(url=url).json()
        out_format("open清空搜索记录:", r)
        return r
