# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/10 21:37 
  @Auth : 可优
  @File : lm_06_exception_else.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
try:
    # 1. 如果try的块语句未抛出任何异常, 那么else块会被执行
    num = int(input("请输入一个整数: "))
    # if num == 1:
    #     print("Yes")
    # else:
    #     print("No")
    result = 10 / num
    print("这里会执行吗? ")
except (ValueError, ZeroDivisionError):
    print("可以同时处理ValueError和ZeroDivisionError异常")
# except:
except Exception as e:
    print(f"异常为: {e}\n{type(e)}")
    print("您输入了非整数, 请重新输入!")
    print("此处需要日志器来记录日志")
else:
    if num == 1:
        print("Yes")
    else:
        print("No")

print(100)
