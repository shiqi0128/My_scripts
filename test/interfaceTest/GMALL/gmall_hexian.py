import unittest
import requests
import json
import os
from time import sleep
from gmall_header import get_header_pc
from urllib3 import encode_multipart_formdata

host, header, token = get_header_pc()
# data = fenzhuang()

"""和弦图异常场景接口测试脚本"""
class Flow(unittest.TestCase):
    """定义一个测试类"""

    def test_01_camera(self):           # 出口记录，顾客循坏
        url_01 = host + "/api/camera/upload"
        scenes = [
                    # ["2.png", "GP_SH_003", "2017-12-02 09:00:00"],      # GP_SH_003=入口，场景1:是3个人不同区域同一个时间被捕捉，没有动线
                    # ["3.jpg", "GP_SH_004", "2017-12-02 09:00:00"],      # GP_SH_004=研发中心
                    # ["4.png", "GP_SH_005", "2017-12-02 09:00:00"]       # GP_SH_005=支持中心
                    # ["2.png", "GP_SH_003", "2017-12-03 09:00:00"],      # GP_SH_003=入口,场景是2个人相同的时间2个相同动线
                    # ["2.png", "GP_SH_004", "2017-12-03 09:10:00"],      # GP_SH_003=入口
                    # ["3.jpg", "GP_SH_003", "2017-12-03 09:00:00"],      # GP_SH_004=研发中心
                    # ["3.jpg", "GP_SH_004", "2017-12-03 09:10:00"],      # GP_SH_004=研发中心
                    # ["4.png", "GP_SH_005", "2017-12-02 09:00:00"]
                    # ["2.png", "Sylvia_001", "2017-12-03 09:00:00", "2.png"],  # Sylvia_001=入口,场景2:是2个人同一天2条不同动线，有1条动线重复
                    # ["2.png", "Sylvia_002", "2017-12-03 09:10:00", "2.png"],  # Sylvia_002=男装区
                    # ["2.png", "Sylvia_003", "2017-12-03 09:20:00", "2.png"],  # Sylvia_001=女装区
                    # ["3.jpg", "Sylvia_002", "2017-12-03 10:00:00", "3.jpg"],  # Sylvia_002=男装区
                    # ["3.jpg", "Sylvia_003", "2017-12-03 10:10:00", "3.jpg"],  # Sylvia_003=女装区
                    # ["2.png", "Sylvia_001", "2017-12-04 09:00:00", "2.png"],  # Sylvia_001=入口,场景3:一个人动线是1-2-3-4-1
                    # ["2.png", "Sylvia_002", "2017-12-04 09:10:00", "2.png"],  # Sylvia_002=男装区
                    # ["2.png", "Sylvia_003", "2017-12-04 09:20:00", "2.png"],  # Sylvia_003=女装区
                    # ["2.png", "Sylvia_004", "2017-12-04 10:00:00", "2.png"],  # Sylvia_004=男装区
                    # ["2.png", "Sylvia_001", "2017-12-04 10:10:00", "2.png"],  # Sylvia_001=入口
                    ["2.png", "Sylvia_001", "2017-12-05 09:00:00", "2.png"],  # Sylvia_001=入口,场景4:3个人动线分别是1-2-5;1-3-5;1-4-5
                    ["2.png", "Sylvia_002", "2017-12-05 09:10:00", "2.png"],  # Sylvia_002=男装区
                    ["2.png", "Sylvia_005", "2017-12-05 09:20:00", "2.png"],  # Sylvia_005=收银区
                    ["3.jpg", "Sylvia_001", "2017-12-05 10:00:00", "3.jpg"],  # Sylvia_001=入口
                    ["3.jpg", "Sylvia_003", "2017-12-05 10:10:00", "3.jpg"],  # Sylvia_003=女装区
                    ["3.jpg", "Sylvia_005", "2017-12-05 10:10:00", "3.jpg"],  # Sylvia_005=收银区
                    ["4.png", "Sylvia_001", "2017-12-05 10:00:00", "4.png"],  # Sylvia_001=入口
                    ["4.png", "Sylvia_004", "2017-12-05 10:10:00", "4.png"],  # Sylvia_004=童装区
                    ["4.png", "Sylvia_005", "2017-12-05 10:10:00", "4.png"],  # Sylvia_005=收银区
                ]

        for scene in scenes:
            with open(r"C:\Users\gp002\Pictures\photo/" + scene[0], "rb") as f, open(r"C:\Users\gp002\Pictures\photo/" + scene[3], "rb") as f1:        # 绝对路径拼接图片名称，for循坏到的每个列表的第一个图片名称
                files = {                                                              # 读取文件名 赋值给f
                    "image_face": (scene, f, "jpg/png"),
                    "camera_code": (None, scene[1]),        # camera_code是for循坏后取得列表的第2个值
                    "date": (None, scene[2]),               # date是for循坏后取得列表的第3个值
                    "image_scene": (scene, f1, "jpg/png")
                            }                                                      # 请求参数赋值给files
                r_01 = requests.post(url=url_01, files=files).json()               # 这个上传图片的接口不需要带头部信息，所以这边不能写headers
                print("抓拍到的人脸:", r_01, "\n")
                sleep(5)                                # 多个接口同时跑数据容易串，所以加5秒延时

    # def dailyShopStats(self):
    #     """门店客流统计（每天）客流数况"""
    #     url_09 = host + "/api/shops/%s/daily-stats/?date=" % 1
    #     data = {"date": "2017-12-01"}
    #     r_09 = requests.get(url=url_09, headers=header, params=data).json()
    #     self.assertEqual(r_09["code"], 0)
    #     print("门店客流统计（每天）客流数况:", r_09, "\n")  # 没有date日期
    #     customer_num_all = r_09["data"]["stats"]["customer_num_all"]        # 提取这个接口返回的当日进店总人数（所有摄像头）,后面需要调用
    #     print("customer_num_all:", customer_num_all, "\n")
    #     return customer_num_all

    # def hexian(self):               # 和弦图正常场景
    #     url_01 = host + "/api/shops/%s/line-chord?start_date=2018-12-09" % 1
    #     r_01 = requests.get(url=url_01, headers=header).json()
    #     print("和弦图:", r_01, "\n")

    def test_03_hexian_01(self):      # 和弦图异常场景_1个人动线是1-2-3-4-1
        # customer_num_all_01 = self.dailyShopStats()
        url_02 = host + "/api/shops/%s/line-chord?start_date=%s&end_date=%s" % (25, "2017-12-05", "2017-12-05")
        r_02 = requests.get(url=url_02, headers=header).json()
        print("r_02:", r_02, "\n")
        # print("和弦图单个区域:", r_02, "\n")
        print("和弦图3个人3条动线不重复:", r_02, "\n")
        s = len(r_02["data"]["stats"])
        print(s)
        sum = 0
        for s1 in range(s):
            value = r_02["data"]["stats"][s1]["value"]
            sum += value            # sum=sum+value
        print("关联度之和:", sum, "\n")
        self.assertEqual(sum, 9)

    # def test_04_


if __name__ == "__main__":
    unittest.main()
else:
    print("false")

