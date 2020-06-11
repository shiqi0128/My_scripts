# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/8 21:19 
  @Auth : 可优
  @File : one_module.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""


def one_function(*args):
    result = 0
    for i in args:
        result += i

    return result


# __name__是系统变量, 无需定义
# a. 如果运行当前模块, 那么__name__ 等于 __main__
# b. 如果当前模块是被其他py文件导入的, 那么__name__ 等于 模块名
if __name__ == '__main__':
    # 下面的代码为: 模块设计者的测试代码
    res = one_function(10, 20, 12)
    print(res)
    pass
