# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/10 20:15 
  @Auth : 可优
  @File : lm_01_file_append.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 1. 打开文件
# one_file = open("one_text.txt", "w", encoding="utf-8")

# 2. 写操作
# one_file.write("允知")
# one_file.write("1")

# 3. 关闭文件
# one_file.close()

# 可以使用with上下文管理语句来简化文件的操作
# with open("one_text.txt", "w", encoding="utf-8") as one_file:
#     one_file.write("长裙")

# a. mode为a时, 为文件末尾追加内容
# b. 如果文件不存在, 那么会创建新的文件
# c. 如果文件存在, 那么会进行追加操作
# with open("one_text.txt", "a", encoding="utf-8") as one_file:
with open("one_text1.txt", "a", encoding="utf-8") as one_file:
    # one_file.write("~~~~")
    one_file.write("\n")
    one_file.write("Estelle")
