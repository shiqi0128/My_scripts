# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/8 21:38 
  @Auth : 可优
  @File : lm_04_file_handle_read.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 1. 打开文件
# a. 如果文件路径存在, 那么返回文件对象
# b. 如果不存在, 那么会报错FileNotFoundError
# 如果不设置mode参数, 会使用默认值'r', 默认对文件进行读取操作
one_file = open("sanguo.txt", encoding="utf-8")
# one_file = open("sanguo1.txt", encoding="utf-8")

# 2. 读操作
# read()方法会将整个文件的内容全部读取出来
# 为字符串类型
# result = one_file.read()
# 可以给read传递参数, 指定读取的字节数
# result = one_file.read(1)

# readline()每次执行, 会读取一行内容
# 为字符串类型
# result = one_file.readline()

# readlines()会将每一行读取出来, 每一行作为列表的元素, 返回列表
result = one_file.readlines()

# print(one_file.readable())


# 3. 关闭文件
one_file.close()
