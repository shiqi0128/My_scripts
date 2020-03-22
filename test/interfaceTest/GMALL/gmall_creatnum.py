import unittest
import requests
import json
import os
from time import sleep
from gmall_header import get_header_pc
from urllib3 import encode_multipart_formdata

host, header, token = get_header_pc()


def precision(a, b):
    c = a / b
    c1 = "%.3f" % c
    print("初始值:", c1)
    c2 = int(float(c1.split(".")[1]) / 10)  # c1.split(".")=["0", "333"],取第2个是"333",333除以10=33.3,int执行后c2=33
    # print(int(c2))
    c3 = c2 % 10
    if a % b == 0:
        print(c)
        return c
    else:
        x = int(c) + int(c2 / 10) / 10  # int(c2/10)/10 ==>>>> (2/10)/10=>>0.02, 2+0.02=x=2.02
        if c3 < 5:
            print("舍去后的值", x)
            return x
        else:
            x1 = float("%.1f" % (x + 0.1))
            print("五入的值", x1)
            return x1


def camera():  # 出口记录，顾客循坏
    url_01 = host + "/api/camera/upload"
    scenes = [
        # ["2.png", "Sylvia_001", "2017-12-07 09:00:00", "2.png"],  # Sylvia_001=入口,人均场景4:A动线分别是1-2-3-2-3-5
        # ["2.png", "Sylvia_002", "2017-12-07 09:10:00", "2.png"],  # Sylvia_002=男装区
        # ["2.png", "Sylvia_003", "2017-12-07 10:10:00", "2.png"],  # Sylvia_003=女装区
        # ["2.png", "Sylvia_002", "2017-12-07 10:20:00", "2.png"],  # Sylvia_002=男装区
        # ["2.png", "Sylvia_003", "2017-12-07 11:10:00", "2.png"],  # Sylvia_003=女装区
        # ["2.png", "Sylvia_005", "2017-12-07 11:20:00", "2.png"],  # Sylvia_005=收银区
        # A的运行动线
        ["2.png", "Sylvia_001", "2018-01-02 09:00:00", "2.png"],  # Sylvia_001=入口,人均场景5-A:1-2-3-5-3-3-5;
        ["2.png", "Sylvia_002", "2018-01-02 09:30:00", "2.png"],  # Sylvia_002=男装区
        ["2.png", "Sylvia_003", "2018-01-02 10:10:00", "2.png"],  # Sylvia_003=女装区
        ["2.png", "Sylvia_005", "2018-01-02 10:40:00", "2.png"],  # Sylvia_005=收银区
        ["2.png", "Sylvia_003", "2018-01-02 11:30:00", "2.png"],  # Sylvia_003=女装区
        ["2.png", "Sylvia_003", "2018-01-02 11:40:00", "2.png"],  # Sylvia_003=女装区
        ["2.png", "Sylvia_005", "2018-01-02 11:50:00", "2.png"],  # Sylvia_005=收银区
        # B的运行动线
        ["3.jpg", "Sylvia_001", "2018-01-02 10:20:00", "3.jpg"],  # Sylvia_001=入口,B:1-2-3-5
        ["3.jpg", "Sylvia_002", "2018-01-02 10:40:00", "3.jpg"],  # Sylvia_002=男装区
        ["3.jpg", "Sylvia_003", "2018-01-02 10:50:00", "3.jpg"],  # Sylvia_003=女装区
        ["3.jpg", "Sylvia_005", "2018-01-02 11:20:00", "3.jpg"],  # Sylvia_005=收银区


        # ["3.jpg", "Sylvia_001", "2017-12-05 10:00:00", "3.jpg"],  # Sylvia_001=入口
        # ["3.jpg", "Sylvia_003", "2017-12-05 10:10:00", "3.jpg"],  # Sylvia_003=女装区
        # ["3.jpg", "Sylvia_005", "2017-12-05 10:10:00", "3.jpg"],  # Sylvia_005=收银区
        # ["4.png", "Sylvia_001", "2017-12-05 10:00:00", "4.png"],  # Sylvia_001=入口
        # ["4.png", "Sylvia_004", "2017-12-05 10:10:00", "4.png"],  # Sylvia_004=店外
        # ["4.png", "Sylvia_005", "2017-12-05 10:10:00", "4.png"],  # Sylvia_005=收银区
        # {"2017-12-07": ""}
    ]
    s = len(scenes)
    b = []
    for s1 in range(s):
        rp = scenes[s1][0]
        if rp not in b:
            b.append(rp)
    else:
        w = len(b)
        print("当日进店人数:", w)

    capita = precision((s / 5), w)

    print("人均逛店深度读取:", capita)
    for index, scene in enumerate(scenes, 1):
        with open(r"C:\Users\gp002\Pictures\photo/" + scene[0], "rb") as f, open(
                r"C:\Users\gp002\Pictures\photo/" + scene[3], "rb") as f1:  # 绝对路径拼接图片名称，for循坏到的每个列表的第一个图片名称
            files = {  # 读取文件名 赋值给f
                "image_face": (scene, f, "jpg/png"),
                "camera_code": (None, scene[1]),  # camera_code是for循坏后取得列表的第2个值
                "date": (None, scene[2]),  # date是for循坏后取得列表的第3个值
                "image_scene": (scene, f1, "jpg/png")
            }  # 请求参数赋值给files
            r_01 = requests.post(url=url_01, files=files).json()  # 这个上传图片的接口不需要带头部信息，所以这边不能写headers
            print("抓拍到的人脸%s:" % index, r_01, "\n")
            sleep(5)
    return capita     # 人均逛店频次



