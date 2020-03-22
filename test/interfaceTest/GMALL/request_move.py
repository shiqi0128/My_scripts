#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""postman请求动线的代码

思路：
1、将每个顾客和该顾客“所有经过的区域”对应起来，变成一个字典
    --经过的区域应该是一个列表，例如key:[ ["区域"，"进店时间"], "区域"，"进店时间"] ]
2、由于多人多区域，串行时运行较慢，所以可以用多线程，即为每个顾客创建一个线程，所有顾客一起请求
    --将步骤1的key拿出来，一一遍历顾客名字，然后放入线程中
3、循环请求“每个顾客”下的所有动线
    --通过字典，取出key值，用key(顾客名)值得到value(该顾客所有动线)，然后再循环
注意点：由于单个人多区域时，运行过快，系统会识别成两个人，所以需要睡眠5秒
    为了加快运行，可以判断如果这个人第一次请求，睡眠5秒，如果不是第一次请求，不让其睡眠
其中图片后缀为png格式的比jpg格式请求耗时长
"""
__author__ = "wxy"
import requests
import os
import threading
import time
import re
'''
class Move(object):
    """请求动线的所有代码"""

    def __init__(self, img_path, all_customers_lines):
        self.url = "https://qa.api.gmall.gaopeng.com/api/camera/upload"  # 请求的url
        self.img_path = img_path                                 # 图片路径
        self.all_customers_lines = all_customers_lines           # 所有的顾客动线
        self.all_names_and_lines = self.customers_lines_info()   # 所有的顾客名字以及对应动线

    def customers_lines_info(self):
        """ 用于添加顾客动线的函数
        将图片和动线一一对应，变成字典
        :return: 返回顾客名称以及对应动线列表
        """
        total_customers = []                                      # 所有顾客的名字
        total_lines = []                                          # 所有顾客的动线
        for line in self.all_customers_lines:                    # 将所有动线循环，得到每个人的动线
            total_lines.append(line)                              # 将每个人的动线添加到列表中
        for img_name in os.listdir(self.img_path):               # 遍历该文件下所有的文件名
            suffix = os.path.splitext(img_name)[-1]               # 显示文件名的后缀
            if suffix == ".jpg" or suffix == ".png":            # 判断是不是图片
                total_customers.append(img_name)                  # 添加到图片名字列表中
        # print("customers_lines_info:", dict(zip(total_customers, total_lines)))
        return dict(zip(total_customers, total_lines))           # 将图片名字和动线一一对应并返回
        # {
        # '1.jpg': [('支持', '2018-09-10 10:00:10'), ('研发中心', '2018-09-10 10:00:30')],
        # '2.jpg': [('支持中心', '2018-09-10 10:00:20')]
        # }

    @staticmethod
    def region(camera_area):
        """门店区域
        通过中文来找到摄像头标识
        :param camera_area 摄像头对应的区域名称
        :return 返回摄像头标识
        """
        if camera_area == "入口":
            return "K_SP_003"
        elif camera_area == "支持":
            return "K_SP_001"
        elif camera_area == "研发":
            return "K_SP_002"

    def begin_request(self, customer_name):
        """顾客开始请求
        通过key(顾客名字),得到顾客的动线列表，然后在通过循环一一取值（就是单个区域和时间）
        :param customer_name: 顾客名字（就是图片名称）
        """
        user_log = []  # 存储动线
        user_Flag = True  # 记录顾客有没有请求过，没有请求过为True，请求过为False
        all_names_and_lines = self.all_names_and_lines               # 所有的顾客名字以及对应动线
        for customer_line in all_names_and_lines[customer_name]:    # 遍历顾客的所有动线，得到的是顾客所有想要走的动线(时间和区域)
            # customer_line = ["门店区域"，"进店时间"]
            user_log.append(customer_line)
            camera_code, date = customer_line[0], customer_line[1]    # 将门店区域和进店时间分别赋予一个新变量
            with open(self.img_path + customer_name, "rb")as f, open(self.img_path + customer_name, "rb")as f1:
                form_data = {"camera_code": (None, Move.region(camera_code)),  # 顾客被捕捉到的区域，代表门店区域
                             "image_face": (customer_name, f, "jpg/png"),    # 小图
                             "image_scene": (customer_name, f1, "jpg/png"),  # 大图
                             "date": (None, date)}             # 顾客进店时间
                response = requests.post(url=self.url, files=form_data).json()
                assert (response["code"] == 0)
            if user_Flag:
                print("%s第一次请求，开始睡眠5秒" % customer_name)
                time.sleep(5)
                user_Flag = False
            else:
                time.sleep(0.7)  # 避免请求过快，时间不对
        print("顾客【%s】：%s" % (customer_name, user_log))

    def run_thread(self):
        """多线程请求
        为每一个顾客创建一个线程
        """
        all_thread_obj = []  # 线程列表
        all_customer_name = list(self.all_names_and_lines.keys())  # 所有的顾客名字
        print("参与请求的图片名字：", all_customer_name)
        for customer_name in all_customer_name:  # 循环得到每一个顾客列表
            thread = threading.Thread(target=self.begin_request, args=(customer_name,))  # 每个顾客创建一个线程
            all_thread_obj.append(thread)  # 创建的线程对象添加到线程列表中

        for i in range(len(all_customer_name)):
            all_thread_obj[i].start()

        for i in range(len(all_customer_name)):
            all_thread_obj[i].join()
'''


class Move(object):
    """请求动线的所有代码"""

    def __init__(self, img_path, all_customers_lines):
        self.url = "https://qa.api.gmall.gaopeng.com/api/camera/upload"  # 请求的url
        self.img_path = img_path                                 # 图片路径
        self.all_customers_lines = all_customers_lines           # 所有的顾客动线
        self.all_names_and_lines = self.customers_lines_info()   # 所有的顾客名字以及对应动线

    def customers_lines_info(self):
        """ 用于添加顾客动线的函数
        将图片和动线一一对应，变成字典
        :return: 返回顾客名称以及对应动线列表
        """
        total_customers = []                                      # 所有顾客的名字
        total_lines = []                                          # 所有顾客的动线
        for line in self.all_customers_lines:                    # 将所有动线循环，得到每个人的动线
            total_lines.append(line)                              # 将每个人的动线添加到列表中
        for img_name in os.listdir(self.img_path):               # 遍历该文件下所有的文件名
            suffix = os.path.splitext(img_name)[-1]               # 显示文件名的后缀
            if suffix == ".jpg" or suffix == ".png":            # 判断是不是图片
                total_customers.append(img_name)                  # 添加到图片名字列表中
        # print("customers_lines_info:", dict(zip(total_customers, total_lines)))
        return dict(zip(total_customers, total_lines))           # 将图片名字和动线一一对应并返回
        # {
        # '1.jpg': [('支持', '2018-09-10 10:00:10'), ('研发中心', '2018-09-10 10:00:30')],
        # '2.jpg': [('支持中心', '2018-09-10 10:00:20')]
        # }

    @staticmethod
    def region(camera_area):
        """门店区域
        通过中文来找到摄像头标识
        :param camera_area 摄像头对应的区域名称
        :return 返回摄像头标识
        """
        if camera_area == "入口":
            return "K_SP_003"  # "K_SP_003"  GP_SH_003
        elif camera_area == "支持":
            return "K_SP_001"  # "K_SP_001"  GP_SH_005
        elif camera_area == "研发":
            return "K_SP_002"  # K_SP_002   GP_SH_004

    def tst(self):
        print(self.all_names_and_lines)

    def get_request_params(self, customer_name):
        """得到顾客的区域以及进店时间
        通过key(顾客名字),得到顾客的动线列表，然后在通过循环一一取值（就是单个区域和时间）
        :param customer_name: 顾客名字（就是图片名称）
        """
        user_log = []  # 存储动线
        user_Flag = True  # 记录顾客有没有请求过，没有请求过为True，请求过为False
        all_names_and_lines = self.all_names_and_lines               # 所有的顾客名字以及对应动线，是一个字典
        for customer_line in all_names_and_lines[customer_name]:    # 根据名字得到value，得到的是顾客所有想要走的动线(时间和区域)
            # customer_line = [{"2018-12-12": "研发(13:05)-入口(13:30)-研发(13:05)-支持(13:30)"}]
            for date in customer_line:  # 得到日期
                user_log.append({date: customer_line[date]})
                for str in customer_line[date].split("-"):  # 根据日期，得到具体的区域以及进店时间 [研发(13:05),入口(13:30)]
                    #  str = 研发(13:05)
                    area, into_time = (re.findall("\D{2}", str))[0], (re.findall("\d{2}:\d{2}", str))[0]
                    with open(self.img_path + customer_name, "rb")as f, open(self.img_path + customer_name, "rb")as f1:
                        form_data = {"camera_code": (None, Move.region(area)),  # 顾客被捕捉到的区域，代表门店区域
                                     "image_face": (customer_name, f, "jpg/png"),    # 小图
                                     "image_scene": (customer_name, f1, "jpg/png"),  # 大图
                                     "date": (None, date+" "+into_time+":00")}             # 顾客进店时间
                        response = requests.post(url=self.url, files=form_data).json()
                        assert (response["code"] == 0)
                    if user_Flag:
                        print("%s第一次请求，开始睡眠5秒" % customer_name)
                        time.sleep(5)
                        user_Flag = False
                    else:
                        time.sleep(1.5)  # 避免请求过快，时间不对
        print("顾客【%s】：%s" % (customer_name, user_log))

    def run_thread(self):
        """多线程请求
        为每一个顾客创建一个线程
        """
        all_thread_obj = []  # 线程列表
        all_customer_name = list(self.all_names_and_lines.keys())  # 所有的顾客名字
        print("参与请求的图片名字：", all_customer_name)
        for customer_name in all_customer_name:  # 循环得到每一个顾客列表
            thread = threading.Thread(target=self.get_request_params, args=(customer_name,))  # 每个顾客创建一个线程
            all_thread_obj.append(thread)  # 创建的线程对象添加到线程列表中

        for i in range(len(all_customer_name)):
            all_thread_obj[i].start()

        for i in range(len(all_customer_name)):
            all_thread_obj[i].join()
