# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/10 21:53 
  @Auth : 可优
  @File : lm_08_examples.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""


# 判断用户输入的是否为整数, 如果是返回True, 否则返回False
def is_int_num(num):
    try:
        # result = int(num)
        int(num)
        # return True
    except Exception as e:
        return False
    else:
        return True


if __name__ == '__main__':
    one_num = input("请输入一个整数: ")
    print(is_int_num(one_num))
