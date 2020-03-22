import unittest
import requests
import os
import random
from time import sleep
from interfaceTest.GMALL.gmall_header import host, header
from interfaceTest.GMALL.gmall_all.color import out_format


def role_list():
    """角色列表"""
    url = host + "/api/role"
    r = requests.get(url=url, headers=header).json()
    out_format("角色列表:", r)
    role_id = r["data"]["roles"][-1]["id"]
    return role_id


role_id = role_list()


# 以下接口为角色管理所有接口
class gmall_account():
    def role_creat(self):
        """角色创建"""
        url = host + "/api/role"
        data = {"display_name": "督导%s" % random.randrange(1, 1000000), "menu_ids": [1, 2, 3]}
        r = requests.post(url=url, headers=header, json=data).json()
        out_format("角色创建:", r)
        return r

    def role_read(self):
        """角色查看"""
        url = host + "/api/role/%s" % role_id
        r = requests.get(url=url, headers=header).json()
        out_format("角色查看:", r)

    def role_edit(self):
        """角色编辑"""
        url = host + "/api/role/%s" % role_id
        data = {"display_name": "小可爱%s" % random.randrange(1000000, 9999999), "menu_ids": [1, 2, 3]}
        r = requests.patch(url=url, headers=header, json=data).json()
        out_format("角色编辑:", r)

    def role_delete(self):
        """角色删除"""
        url = host + "/api/role/%s" % role_id
        r = requests.delete(url=url, headers=header).json()
        out_format("角色删除:", r)
        return role_id


gmall_account().role_creat()
gmall_account().role_read()
gmall_account().role_edit()
gmall_account().role_delete()
