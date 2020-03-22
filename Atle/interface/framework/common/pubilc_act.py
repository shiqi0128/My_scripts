# -----------------此文件是3.1需要调用多次的公共方法,包含砍价和抽奖的接口----------------------
import requests
import unittest
from Atle.interface.framework.common.color import out_format
from Atle.interface.framework.common.header_s import host, header

class double_elev(unittest.TestCase):
    """定义一个双十一活动的公共测试类"""
    def test_mart_list(self):
        """砍价列表"""
        url = host + "/api/mart/list"
        data = {"size": 10, "page": 1}
        r = requests.post(url=url, data=data).json()
        out_format("砍价列表:", r)
        s = len(r["data"])
        if s == 0:
            print("data is null")
        else:
            p_id = r["data"][5]["id"]
            return p_id

    def test_past(self):
        """往期开奖
        :param:size:单页记录数
        :param:page:页码
        """
        url = host + "/api/trophy/list"
        data = {"size": 10, "page": 1}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("往期开奖:", r)
        print("长度:", len(r["data"]))
        if len(r["data"]) == 0:
            print("data is null")
        else:
            p_id = r["data"][0]["id"]
            return p_id


kp_id = double_elev().test_mart_list()
cp_id = double_elev().test_past()
