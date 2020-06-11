# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/10 20:28 
  @Auth : 可优
  @File : lm_02_hande_binary_file.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 1. 处理二进制文件, mode需要添加b
# 如何复制粘贴一个文件?
# 复制: 读取
# with open("pic.jpg", mode="rb") as one_file:
#     result = one_file.read()
#     pass

# 粘贴: 写入
# with open("pic_bk.jpg", mode="wb") as two_file:
#     two_file.write(result)

# 使用with语句同时对多个文件进行操作
# with open("pic.jpg", mode="rb") as one_file, open("pic_bk1.jpg", mode="wb") as two_file:
#     result = one_file.read()
#     two_file.write(result)

# 如果图片文件有10G, 怎么办?
with open("pic.jpg", mode="rb") as one_file, open("pic_bk1.jpg", mode="wb") as two_file:
    while True:
        result = one_file.read(1024)
        # 如果读到文件末尾, 那么result将为空, 相当于False
        if not bool(result):
            break
        two_file.write(result)
