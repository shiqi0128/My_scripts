# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/8 20:30 
  @Auth : 可优
  @File : lm_02_os_module.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
import os


# 查看一个路径下的目录结构
# 绝对路径
# 从系统根路径开始(C、D、/usr/)
# C:\Users\KeYou\PycharmProjects\Python_Automated_Testing_Class_28\Py28_0408_os_module_file
# 相对路径
# 相对于项目根路径
# Py28_0408_os_module_file
# 在字符串的前面加r, 让\t、\n这些特殊字符不起作用
# result = os.listdir(r"C:\Users\KeYou\PycharmProjects\Python_Automated_Testing_Class_28\Py28_0408_os_module_file")
# result = os.listdir("./")

# 创建目录
# os.mkdir("one_dir")

# 删除目录
# os.rmdir("one_dir")

# 获取当前py文件所处的绝对路径
# result = os.getcwd()

# 使用os.path.isfile来判断一个路径是否为文件, 如果是返回True, 否则返回False
# result = os.path.isfile("./")
# result = os.path.isfile("random1.py")

# 判断是否为目录
# result = os.path.isdir("./")

# 获取当前py文件所处的目录路径
# 可以使用__file__系统变量, 来获取
print(__file__)
# 获取上一级目录的路径
# result = os.path.dirname(__file__)
result = os.path.dirname(os.path.abspath(__file__))
res1 = os.path.dirname(result)

res2 = os.path.join(res1, "reports", "abc")
pass
