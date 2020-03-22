import unittest
import requests
import json
import os
from time import sleep
from gmall_header import get_header_pc
from urllib3 import encode_multipart_formdata
# from gmall_creatnum import camera

host, header, token = get_header_pc()
# capita = camera()

"""2.2.2监控中心视频接口测试脚本---正常场景"""
class test_video(unittest.TestCase):
    """定义一个测试类"""
    def test_01_snapshot_new(self):
        """快照新增"""
        url_01 = host + "/api/shops/25/screenshots"
        data = {"code": "Sylvia_002", "sort_type": "desc"}
        r_01 = requests.get(url=url_01, headers=header, json=data).json()
        print("快照新增:", r_01, "\n")

    def snapshot_list(self):
        """快照列表"""
        r_02_list = []        # 定义一个空列表
        url_02 = host + "/api/shops/25/screenshots"
        data = [{"sort_type": "asc"}, {"sort_type": "desc"}]  # asc 升序 desc 降序,用列表包字典，可以提取相同的字段，不同的值
        for i in data:
            r_02 = requests.get(url=url_02, headers=header, params=i).json()
            print("快照列表:", r_02, "\n")
            r_02_list.append(r_02)   # 把循坏输出的r_02保存到空列表内
        screenshots_id = r_02_list[0]["data"]["screenshots"]["data"][0]["id"]  # 提取截图id
        print("截图id:", screenshots_id)
        return screenshots_id
        # a = []
        # b = r_01["data"][0]["created_at"]

    def update_remark(self):
        """修改快照备注"""
        screenshots_id_01 = self.snapshot_list()
        url_03 = host + "/api/shops/25/screenshots/%s" % screenshots_id_01
        data = {"remark": "角落区域没有打扫干净，垃圾没有倒掉，地面上有积水"}
        r_03 = requests.put(url=url_03, headers=header, json=data).json()
        print("修改快照备注:", r_03, "\n")
        return screenshots_id_01

    def test_02_delete_remark(self):
        """删除快照信息"""
        screenshots_id_02 = self.update_remark()
        url_04 = host + "/api/shops/25/screenshots/%s" % screenshots_id_02
        r_04 = requests.delete(url=url_04, headers=header).json()
        print("删除快照信息:", r_04, "\n")


if __name__ == "__main__":
    unittest.main()
else:
    print("false")

