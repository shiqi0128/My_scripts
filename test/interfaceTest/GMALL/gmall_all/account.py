import unittest
import requests
import os
import random
import HtmlTestRunner
import time
from time import sleep
from interfaceTest.GMALL.gmall_header import golbal_shopid, host, header
from interfaceTest.GMALL.gmall_all.color import out_format

# host, header, token = get_header_pc()
# out_format(os.getcwd())


# 此方法返回值 role_id 为角色管理的公共调用的参数
# def role_list():
#     """角色列表"""
#     url = host + "/api/role"
#     r = requests.get(url=url, headers=header).json()
#     out_format("角色列表:", r)
#     role_id = r["data"]["roles"][-1]["id"]
#     return role_id
#
#
# role_id = role_list()


class gmall_account(unittest.TestCase):
    """定义一个账号相关接口的测试类"""

    def test_01_users(self):
        """可创建用户角色"""
        url_01 = host + "/api/auth/user"
        r_01 = requests.get(url=url_01, headers=header).json()
        out_format("可创建用户角色", r_01)
        # return r_01

    def test_02_old_password(self):
        """验证原密码"""
        url_02 = host + "/api/auth/check-old-password"
        data = {"old_password": "AA123456"}
        r_02 = requests.post(url=url_02, headers=header, json=data).json()
        out_format("验证原密码:", r_02)
        # return r_02

    def test_03_Message_notification_list(self, shop_id=golbal_shopid):
        """消息通知列表"""
        url_03 = host + "/api/shops/%s/notifications?date=2019-02-02&type=" % shop_id
        r_03 = requests.get(url=url_03, headers=header).json()
        out_format("消息通知列表:", r_03)
        # return r_03

    # def change_password(self):
    #     """修改密码"""
    #     url_03 = host + "/api/auth/change-password"
    #     data_01 = {"new_password": "AA123456"}
    #     r_03 = requests.patch(url=url_03, headers=header, json=data_01).json()
    #     out_format("修改密码:", r_03)
    #     return r_03

    # def test_03a_admin(self):
    #     out_format("Hello")

    # def test_04_valid(self):
    #     """检查用户api_token是否有效"""
    #     url_04 = host + "/api/check-token"
    #     params = {"valid_token": token}
    #     r_04 = requests.get(url=url_04, headers=header, params=params).json()
    #     self.assertEqual(r_04["code"], 0)
    #     out_format("检查用户api_token是否有效:", r_04)
    #     # out_format(r_04.text)
    #     valid = r_04["data"]["valid"]           # 返回结果没有valid这个参数
    #     if valid == 1:
    #         out_format("token有效")
    #     else:
    #         out_format("token无效")

    # 以下接口为角色管理所有接口
    # def role_creat(self):
    #     """角色创建"""
    #     url = host + "/api/role"
    #     data = {"display_name": "督导%s" % random.randrange(1, 1000000), "menu_ids": [1, 2, 3]}
    #     r = requests.post(url=url, headers=header, json=data).json()
    #     out_format("角色创建:", r)
    #     return r
    #
    # def role_read(self):
    #     """角色查看"""
    #     url = host + "/api/role/%s" % role_id
    #     r = requests.get(url=url, headers=header).json()
    #     out_format("角色查看:", r)
    #
    # def role_edit(self):
    #     """角色编辑"""
    #     url = host + "/api/role/%s" % role_id
    #     data = {"display_name": "小可爱%s" % random.randrange(1000000, 9999999), "menu_ids": [1, 2, 3]}
    #     r = requests.patch(url=url, headers=header, json=data).json()
    #     out_format("角色编辑:", r)
    #
    # def role_delete(self):
    #     """角色删除"""
    #     url = host + "/api/role/%s" % role_id
    #     r = requests.delete(url=url, headers=header).json()
    #     out_format("角色删除:", r)
    #     return role_id


# gmall_account().users()
# gmall_account().old_password()
# gmall_account().Message_notification_list()
# gmall_account().role_list()
# gmall_account().role_creat()
# gmall_account().role_read()
# gmall_account().role_edit()
# gmall_account().role_delete()

