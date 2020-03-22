#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
代码千万行，注释第一行。
编程不规范，重构两行泪。
"""
__author__ = "wxy"
"""
门店巡查：
    √1、直播&回放
      2、快拍记录
"""

import requests
from interfaceTest.GMALL.gmall_header import header, host, golbal_shopid


class LivePlayback(object):
    """直播&回放：
            1、门店监控（摄像头列表）
            2、摄像头&区域列表
            3、摄像头直播地址（带有效期）
            4、摄像头萤石云 EZOpen URL
    """
    @staticmethod
    def camera_list(shop_id=golbal_shopid):
        """
        门店监控（摄像头列表）
        :param shop_id:门店id
        :return:
        """
        url = host + "/api/shops/%s/cameras" % shop_id
        response = requests.get(url=url, headers=header).json()
        print("门店监控（摄像头列表）:", response, "\n\n")
        return response

    @staticmethod
    def camera_zones_lst(shop_id=golbal_shopid):
        """
        摄像头&区域列表
        :param shop_id:门店id
        :return:
        """
        url = host + "/api/shops/%s/zones" % shop_id
        response = requests.get(url=url, headers=header).json()
        print("摄像头&区域列表:", response, "\n\n")
        return response

    @staticmethod
    def live_address(camera, shop_id=golbal_shopid):
        """
        摄像头直播地址（带有效期）
        :param shop_id:门店id
        :param camera:	摄像头编号
        :return:
        """
        url = host + "/api/shops/%s/cameras/%s/live-url" % (shop_id, camera)
        response = requests.get(url=url, headers=header).json()
        print("摄像头直播地址（带有效期）:", response, "\n\n")
        return response

    @staticmethod
    def EZOpen_URL(camera, shop_id=golbal_shopid):
        """
        摄像头萤石云 EZOpen URL
        :param shop_id:门店id
        :param camera:	摄像头编号
        :return:
        """
        url = host + "/api/shops/%s/cameras/%s/ezopen-urls" % (shop_id, camera)
        response = requests.get(url=url, headers=header).json()
        print("摄像头萤石云 EZOpen URL:", response, "\n\n")
        return response

# l = LivePlayback()
# l.camera_zones_lst()
# l.camera_list()
# l.EZOpen_URL("K_SP_001")
# l.live_address("K_SP_001")