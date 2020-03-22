#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
代码千万行，注释第一行。
编程不规范，重构两行泪。
"""
__author__ = "wxy"
"""
门店巡查：
      1、直播&回放
    √2、快拍记录
"""

import requests
from interfaceTest.GMALL.gmall_header import host, header


class StoreSnapshoot(object):
    """店铺快照接口：
        1、快照列表
        2、快照新增
        3、修改快照备注
        4、删除快照信息
    """
    def snapshoot_lst(self, shop_id=25):
        """快照列表
        :param shop_id:门店id
        """
        url = host + "/api/shops/%s/screenshots" % shop_id
        response = requests.get(url=url, headers=header).json()
        print("快照列表:", response)
        screenshots_id = response["data"]["screenshots"]["data"][0]["id"]
        return screenshots_id

    def snapshoot_new(self, camera, shop_id=25):
        """快照新增
        :param shop_id:门店id
        :param camera:摄像头编号
        """
        url = host + "/api/shops/%s/cameras/%s/screenshot" % (shop_id, camera)
        response = requests.post(url=url, headers=header).json()
        print("快照新增:", response, "\n\n")

    def put_snapshoot_remark(self, screenshot, remark="这是接口的备注", shop_id=25):
        """
        修改快照备注
        :param shop_id:门店id
        :param screenshot:?
        :param remark:备注
        :return:
        """
        url = host + "/api/shops/%s/screenshots/%s" % (shop_id, screenshot)
        response = requests.put(url=url, headers=header, data={"remark": remark}).json()
        print("修改快照备注:", response, "\n\n")
        return response

    def del_snapshoot_info(self, screenshot, shop_id=25):
        """
        删除快照信息
        :param shop_id:门店id
        :param screenshot:?
        :return:
        """
        url = host + "/api/shops/%s/screenshots/%s" % (shop_id, screenshot)
        response = requests.delete(url=url, headers=header).json()
        # print("删除快照信息:", response)
        return response



