# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/8 21:56 
  @Auth : 可优
  @File : lm_05_file_write.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 1. 打开文件
# a. 如果要对文件进行写操作, 那么需要设置mode为"w"
# b. 如果文件路径不存在, 那么会自动创建
# c. 如果文件路径存在, 如果写入内容, 会将之前的内容删除
one_file = open("one_text.txt", mode="w", encoding="utf-8")

# 2. 写操作
# write()方法, 可以将一个字符串写入到文件中
# 默认每次调用write()写入的内容不会换行
# one_file.write("1. Crystal\n")
# one_file.write("2. Twinkle")
one_file.write("3. 词不搭调")

# 3. 关闭文件
# 可以释放系统的资源
one_file.close()
