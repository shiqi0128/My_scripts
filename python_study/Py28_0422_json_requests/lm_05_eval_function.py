# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/22 20:58 
  @Auth : 可优
  @File : lm_05_eval_function.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 字典类型的字符串
one_str = "{'name': '戈多', 'age': 17, 'gender': True, 'hobby': None}"

# a、eval函数可以将字符串最外层的引号拿掉（单引号或者双引号）
# b、eval函数第一个参数往往只为字符串类型
# c、可以为表达式
result = eval(one_str)
pass
