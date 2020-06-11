"""
-------------------------------------------------
  @Time : 2020/5/19 15:19 
  @Auth : 十七
  @File : test2.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""


# 可变参数
numbers_strings = ("1", "2")


def print_str(first, second):
    print(first)
    print(second)


if __name__ == "__main__":
    print_str(*numbers_strings)