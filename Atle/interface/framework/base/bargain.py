# 此文件为砍价列表接口
import requests
import json
from Atle.interface.framework.common.header_s import host, header  # 依赖头部文件封装的方法 host,头部和token
from Atle.interface.framework.common.pubilc_act import kp_id # 依赖砍价列表的产品id和抽奖的产品id
from Atle.interface.framework.common.color import out_format


class Bargain():
    """定义一个砍价的测试类"""
    def mart_details(self):
        """砍价详情"""
        url = host + "/api/mart/find"
        data = {"id": kp_id}
        r = requests.get(url=url, data=data).json()
        out_format("砍价详情:", r)
        return r

    def join(self):
        """参与此砍价活动
        :param:id:产品id
        :param:uid:当前用户id(已封装到头部header_s文件的header中)
        """
        # p_id = self.mart_list()
        url = host + "/api/mart/join"
        data = {"id": kp_id}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("参与此砍价活动:", r)
        return r

    # def help(self):
    #     """帮砍
    #     :param:id:产品ID
    #     :param:uid:发起人用户ID
    #     :param:userid:帮砍用户ID
    #     :param:nickname:帮砍用户昵称
    #     :param:avatar:帮砍用户头像
    #     ————此接口帮砍用户的数据前端存在本地，而不是后端返回的，故不能做接口自动化
    #     """

    def who_list(self):
        """我的砍价列表
        :param:uid:当前用户ID，（此处直接传UID即可，暂不用TOKEN，没有重要数据，无关紧要）
        :param:size:单页记录数
        :param:page:页码
        """
        url = host + "/api/mart/who_list"
        data = {"size": 10, "page": 1}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("我的砍价列表:", r)
        return r

    def who_list_find(self):
        """我的砍价列表详情
        :param:uid:	当前用户ID，（此处直接传UID即可，暂不用TOKEN，没有重要数据，无关紧要）
        :param:userid:帮砍用户ID，默认可不传
        :param:id:产品id
        """
        url = host + "/api/mart/who_list_find"
        data = {"id": kp_id}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("我的砍价列表详情:", r)
        return r

    def ranking(self):
        """砍价榜单
        :param:uid:当前用户ID，（此处直接传UID即可，暂不用TOKEN，没有重要数据，无关紧要）
        :param:size:单页记录数
        :param:page:页码
        """
        url = host + "/api/mart/ranking"
        data = {"size": 10, "page": 1}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("砍价榜单:", r)
        return r




# Bargain().mart_list()
# Bargain().mart_details()   ------这两个接口返回的都是产品已下架或库存不足
# Bargain().join()           ------同上
# Bargain().who_list()  ——————data列表内是空的
# Bargain().who_list_find()
# Bargain().ranking()
