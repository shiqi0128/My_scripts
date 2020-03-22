# ---------------------该文件为举报的接口---------------------
import requests
from Atle.interface.framework.common.header_s import host, header  # 依赖头部文件封装的方法 host,头部和token
# from Atle.interface.framework.common.public_func import sku, goods_id, openitem_id, address_id, p_id, order_no  # 依赖公共文件返回的字段被多次调用
from Atle.interface.framework.common.color import out_format


def accusation_list():
    """举报列表
    :param:token:用户授权token
    :param:page:页数,默认值1
    :param:size:单页数量,默认值10
    """
    url = host + "/api/accusation/index"
    data = {"page": 2, "size": 10}
    r = requests.get(url=url, headers=header, params=data).json()
    out_format("举报列表:", r)
    len_s = len(r["data"]["list"])
    print("len_s =", len_s)
    # for i in range(len_s):
    #     print("i =", i)    # 不能遍历i，这是一个问题,与订单列表不能遍历i是一个情况,还在想办法解决中!! 191011
    # 已解决：注：不能遍历的原因在于我return了，加return后第一遍遍历后就会结束
    if len(r["data"]["list"]) != 0:
        len_s = len(r["data"]["list"])
        print("len_s =", len_s)
        report_id = r["data"]["list"][0]["id"]
        object_type = r["data"]["list"][0]["object_type"]
        object_id = r["data"]["list"][0]["object_id"]
        memo = r["data"]["list"][0]["memo"]
        reported = r["data"]["list"][0]["reported"]
        category_id = r["data"]["list"][0]["category_id"]
        return report_id, object_type, object_id, memo, reported, category_id
    else:
        print("data is None")


report_id, object_type, object_id, memo, reported, category_id = accusation_list()


class Accusation():
    """定义一个举报的测试类"""

    def accusation_add(self):
        """添加举报
        :param:token:用户授权token
        :param:object_type:对象类型
        :param:object_id:对象号
        :param:memo:备注
        :param:reported:被举报用户
        :param:category_id:举报类型
        """
        url = host + "/api/accusation/create"
        data = {
                    "object_type": object_type,
                    "object_id": object_id,
                    "memo": memo,
                    "reported": reported,
                    "category_id": category_id
                }
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("添加举报:", r)
        return r

    def accusation_type(self):
        """举报类型
        :param:token:用户授权token
        """
        url = host + "/api/accusation/types/"
        r = requests.get(url=url, headers=header).json()
        out_format("举报类型:", r)
        return r

    def accusation_details(self):
        """举报详情
        :param:token:用户授权token
        :param:id:举报号
        """
        url = host + "/api/accusation/get/:id"
        data = {"id": report_id}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("举报详情:", r)
        return r

    def accusation_delete(self):
        """删除举报
        :param:token:用户授权token
        :param:id:举报号
        """
        url = host + "/api/accusation/delete"
        data = {"id": report_id}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("删除举报:", r)
        return r


# Accusation().accusation_add()
# Accusation().accusation_type()
# Accusation().accusation_details()
# Accusation().accusation_delete()
