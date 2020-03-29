# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/27 21:19 
  @Auth : 可优
  @File : lm_04_while_define.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 计数器变量
count_var = 1

# 1. while循环, 如果条件为True, 那么会执行while下面的块语句
# 2. 当块语句执行完, 会回到条件判断处, 继续判断
# 3. 如果条件一直为True, 那么循环将会一直执行(死循环)
# 4. 如果while条件为False之后, 循环会退出
while count_var <= 5:
    print("Hello, Python!")
    print(100)
    # 需要修改循环条件, 不然的话, 会成为死循环
    # count_var = count_var + 1
    count_var += 1

print("继续往下执行")
