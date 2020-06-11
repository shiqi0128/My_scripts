# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/15 20:54 
  @Auth : 可优
  @File : py_test.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# from lm_01_attribute_class import People, get_wether
from lm_01_attribute_class import People


one_people = People(my_name="Jack", my_age=17, my_height=1.78)
two_people = People("飓风", 16, 1.9)
People.get_wether("大雨")
