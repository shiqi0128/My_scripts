import requests
import os
import random
from time import sleep
from interfaceTest.GMALL.gmall_header import golbal_shopid, header, host, token
from interfaceTest.GMALL.gmall_all.color import out_format
from urllib3 import encode_multipart_formdata


def report_creat(email, type_ids, shop_id=golbal_shopid):
    """订阅者创建
    :param:email:邮箱
    :param:shop_ids:门店id--数组形式传参
    :param:type_ids:订阅类型 id--数组形式传参
    """
    url = host + "/api/report-subscribers"
    data = {"email": email, "type_ids": [type_ids], "shop_ids": [str(shop_id)]}
    r = requests.post(url=url, headers=header, json=data).json()
    out_format("订阅者创建:", r)
    report_id = r["data"]["subscriber"]["id"]
    print("获取订阅者id[%s]:" % report_id, "\n")
    return report_id


report_id = report_creat("%s@163.com" % random.randrange(3, 30000), "娱乐")
# 此操作为设置全局变量，订阅者创建这个接口的方法赋值给return出来的report_id，供主调文件调用

# 门店管理--[设置]相关接口(Golcer v2.3.0)
class settings():
    def shop_list(self):
        """门店列表
        :param:shop_id:门店id
        :param:page_size:每页数量（默认值：20）
        """
        url = host + "/api/corp-shops?keyword={}&page_size={}"
        r = requests.get(url=url, headers=header).json()
        out_format("门店列表:", r)

    def set_default(self, shop_id=golbal_shopid):
        """设置默认门店
        :param:shop_id:门店id
        """
        url = host + "/api/shops/%s/set-default" % shop_id
        r = requests.put(url=url, headers=header).json()
        out_format("设置默认门店:", r)

    def account_creat(self, user_pass):
        """账号创建
        :param:user_name:账号
        :param:user_pass:密码
        :param:phone:联系方式
        :param:staff_name:员工姓名
        :param:role_ids:角色ids : 1,2,3,4  传参方式以数组形式传参
        :param:shop_ids:门店ids : 1,2,3,4  传参方式以数组形式传参
        """
        url = host + "/api/user"
        data = {
                "user_name": "admin%s" % random.randrange(200, 100000),
                "user_pass": user_pass,
                "phone": random.randrange(13100000000, 13199999999),
                "staff_name": "刘欢%s" % random.randrange(1, 10000),
                "role_ids": ["1"],
                "shop_ids": ["25"]
        }
        r = requests.post(url=url, headers=header, json=data).json()
        out_format("账号创建:", r)

    def account_delete(self, user_id):
        """账号删除
        :param:userid:账号id
        """
        url = host + "/api/user/%s" % user_id
        r = requests.delete(url=url, headers=header).json()
        out_format("账号删除", r)

    def account_read(self, user_id):
        """账号查看
        :param:userid:账号id
        """
        url = host + "/api/user/%s" % user_id
        r = requests.get(url=url, headers=header).json()
        out_format("账号查看", r)

    def account_edit(self, user_id):
        """账号编辑
        :param:phone:联系方式
        :param:staff_name:员工姓名
        :param:role_ids:角色ids : 1,2,3,4  传参方式以数组形式传参，string类型
        :param:shop_ids:门店ids : 1,2,3,4  传参方式以数组形式传参,string类型
        """
        url = host + "/api/user/%s" % user_id
        data = {
            "phone": random.randrange(13100000000, 13199999999),
            "staff_name": "张亮%s" % random.randrange(1, 10000),
            "role_ids": ["52"],
            "shop_ids": ["25"]
        }
        r = requests.patch(url=url, headers=header, json=data).json()
        out_format("账号编辑", r)

    def account_update_info(self, user_id, status, password):
        """账号更新部分信息
        :param:status:0 禁用; 1 启用
        :param:password:0 不重置; 1 重置
        """
        url = host + "/api/user-update-info/%s?" % user_id
        data = {"status": status, "password": password}
        r = requests.put(url=url, headers=header, json=data).json()
        out_format("账号更新部分信息", r)

    def account_chect(self, user_name):
        """账号唯一检查
        :param:user_name:账号
        """
        url = host + "/api/user-check"
        data = {"user_name": user_name}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("账号唯一检查:", r)

    def report_list(self):
        """报表订阅列表"""
        url = host + "/api/report-subscribers"
        r = requests.get(url=url, headers=header).json()
        out_format("报表订阅列表:", r)

    # def report_creat(self, type_ids, shop_id=golbal_shopid):
    #     """订阅者创建
    #     :param:email:邮箱
    #     :param:shop_ids:门店id--数组形式传参
    #     :param:type_ids:订阅类型 id--数组形式传参
    #     """
    #     url = host + "/api/report-subscribers"
    #     data = {
    #         "email": "19%s@163.com" % random.randrange(1, 9000),
    #         "type_ids": [type_ids],
    #         "shop_ids": [str(shop_id)]
    #     }
    #     r = requests.post(url=url, headers=header, json=data).json()
    #     out_format("订阅者创建:", r)
    #     report_id = r["data"]["subscriber"]["id"]
    #     return report_id
    #     # if r["data"]["subscriber"] is not None:
    #     #     for s in range(len(r["data"]["subscriber"])):
    #     #         report_id = r["data"]["subscriber"][s]["id"]
    #     #         print("获取订阅者id[%s]:" % report_id, "\n")
    #     #         out_format("订阅者创建:", r)
    #     #         return report_id
    #     # else:
    #     #     print("无数据")
    #     #     out_format("订阅者创建", r)
    #     # return None

    def report_read(self):
        """订阅者查看
        :param:id:订阅者id
        """
        url = host + "/api/report-subscribers/%s" % report_id
        print("url:", url)
        r = requests.get(url=url, headers=header).json()
        out_format("订阅者查看:", r)
        return r

    def report_edit(self, type_ids, shop_id=golbal_shopid):
        """订阅者编辑
        :param:email:邮箱
        :param:shop_ids:门店id
        :param:categories:订阅品类
        """
        url = host + "/api/report-subscribers/%s" % report_id
        print("url:", url)
        data = {
            "email": "19%s@163.com" % random.randrange(1, 9000),
            "type_ids": [str(type_ids)],
            "shop_ids": [str(shop_id)]
        }
        r = requests.put(url=url, headers=header, json=data).json()
        out_format("订阅者编辑:", r)
        return r

    def report_delete(self):
        """订阅者删除
        :param:id:订阅者id
        """
        url = host + "/api/report-subscribers/%s" % report_id
        r = requests.delete(url=url, headers=header).json()
        out_format("订阅者删除:", r)
        return r






# settings().account_list()
# settings().account_creat("admin1")
# settings().account_delete()
# settings().account_read()
# settings().account_edit()
# settings().account_update_info("1", "1")
# settings().account_chect()
# settings().report_list()
# settings().report_creat("1@163.com", "娱乐")
# settings().report_read()

