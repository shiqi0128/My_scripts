# 该文件为所有地址管理的接口
import requests
from Atle.interface.framework.common.header_s import host, header  # 依赖头部文件封装的方法 host,头部和token
from Atle.interface.framework.common.public_func import address_id  # 依赖公共文件返回的字段被多次调用
from Atle.interface.framework.common.color import out_format


class address():
    """
    定义一个地址管理所有接口的测试类
    """
    def creat_address(self):
        """
        创建收货地址
        :param:token:用户授权的token
        :param:name:收货人姓名
        :param:phone:手机号码
        :param:city:省市区
        :param:address:地址
        :param:isdefault:是否默认地址,默认值: 0
        :return:
        以上参数均为必填
        """
        url = host + "/api/address/create"
        data = {
            "name": "王小二",
            "phone": "13812151334",
            "city": "江苏",
            "address": "三人行",
            "isdefault": 0
        }
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("创建收货地址:", r)
        return r

    def address_update(self):
        """
        地址更新
        :param:token:用户授权的token
        :param:id:地址id
        :param:name:姓名
        :param:phone:手机
        :param:city:省市区
        :param:address:地址
        :param:isdefault:是否默认地址,默认值0
        :return:
        """
        url = host + "/api/address/update"
        data = {
            "id": address_id,
            "name": "张晓",
            "phone": "18750511512",
            "city": "aa",
            "address": "aa",
            "isdefault": "0"
        }
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("地址更新:", r)
        return r

    def address_del(self):
        """
        地址删除
        :param:token:用户授权的token
        :param:id：地址id
        """
        url = host + "/api/address/delete"
        data = {"id": address_id}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("地址删除:", r)
        return r

    def address_one(self):
        """
        获取单个地址
        :param:token:用户授权的token
        :param:id:地址id
        :return:
        """
        url = host + "/api/address/find"
        data = {"id": address_id}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("获取单个地址:", r)
        return r
