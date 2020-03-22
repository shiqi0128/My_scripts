#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
主运行动线的代码
如果目录下的图片有多个，但是动线只有2个人的，那就只会有2个人的动线
"""
__author__ = "wxy"


import time
import os
from request_move import Move
from move_data import all_move_data  # 所有顾客动线


if __name__ == "__main__":
    img_path = r"C:\Users\html_\Pictures\Saved Pictures/"  # 图片目录
    # img_path = r"C:\Users\html_\Pictures\test/"  # 图片目录

    def run():
        """主运行程序"""
        start_time = time.time()
        # Move(img_path, all_move_data).run_thread()
        Move(img_path, all_move_data).run_thread()
        end_time = time.time()
        print("\033[0;36m总耗时%.3f秒\033[0m" % (end_time-start_time))
    run()


# from multiprocessing import Event,Process
#
# def light():
#     while True:
#         print("\033[31m 红灯亮了\033[0m")
#         time.sleep(1)
#         print("\033[32m 绿灯亮了\033[0m")
#
# if __name__ == "__main__":
#     light()

# import re
# use = [
#     [{"2018-12-12": "入口(13:05)-支持(13:30)-入口(13:05)-支持(13:30)"},
#      {"2018-12-13": "入口(13:05)-支持(13:30)-入口(13:05)-支持(13:30)"}]
# ]
# for use_info in use:   # 去掉最外面的列表
#     print(use_info)
#     for key_1 in use_info:  # 得到每一个key
#         for key_2 in key_1:
#             # print(key_1[key_2])
#             value = key_1[key_2]
#             for qy in value.split("-"):
#                 print(re.findall("\D{2}", qy), re.findall("(\d{2}:\d{2})", qy))



