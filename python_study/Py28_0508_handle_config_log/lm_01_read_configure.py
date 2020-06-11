# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/5/8 20:41 
  @Auth : 可优
  @File : lm_01_read_configure.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 系统自带
from configparser import ConfigParser

# 1、创建ConfigParser对象
config = ConfigParser()

# 2、加载配置文件
config.read("testcases.conf", encoding="utf-8")

# 3、读取数据
# getint
# getfloat
# getboolean
result = config.get("excel", "filename")
pass
