# 此文件为抽奖所有接口
import requests
import json
from Atle.interface.framework.common.header_s import host, header  # 依赖头部文件封装的方法 host,头部和token
from Atle.interface.framework.common.pubilc_act import cp_id # 依赖砍价列表的产品id和抽奖的产品id
from Atle.interface.framework.common.color import out_format


class Trophy():
    """定义一个抽奖的测试类"""
    def begin(self):
        """即将开始"""
        url = host + "/api/trophy/begin"
        r = requests.post(url=url).json()
        out_format("即将开始:", r)
        return r

    def already(self):
        """已开奖
        :param:uid:当前登录id
        """
        url = host + "/api/trophy/already"
        r = requests.post(url=url, headers=header).json()
        out_format("已开奖:", r)
        return r

    def progress(self):
        """进行中
        :param:uid:用户id"""
        url = host + "/api/trophy/progress"
        r = requests.post(url=url, headers=header).json()
        out_format("进行中:", r)
        return r

    def details(self):
        """抽奖详情
        :param:id:ID
        :param:uid:发起人用户id
        :param:userid:帮抽用户ID（此参数可不传，为方便在帮抽页判断当前是否帮抽过）
        """
        # p_id = self.past()
        url = host + "/api/trophy/find"
        data = {"id": cp_id}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("抽奖详情:", r)
        return r

    # def help(self):
    #     """帮好友抽奖
    #     :param:id:产品id
    #     :param:uid:发起人用户id
    #     :param:userid:帮抽奖用户id
    #     :param:nickname:帮抽奖砍用户昵称
    #     :param:avatar:帮抽奖用户头像
    #     -------此接口由于是前端存在本地的，不是后台返回的，故无法实现自动化------
    #     """
    #     url = host + "/api/trophy/help"
    #     data = {"id": p_id}





# Trophy().begin()
# Trophy().already()
# Trophy().past()
# Trophy().progress()
Trophy().details()