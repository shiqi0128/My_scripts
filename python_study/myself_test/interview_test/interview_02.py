"""
-------------------------------------------------
  @Time : 2020/5/24 18:15 
  @Auth : 十七
  @File : interview_02.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
a = ["h", "e", "l", "l", "o"]
# 第一种
# b = a[0] + a[1] + a[2] + a[3] + a[4]
# print(b, type(b))
# 第二种
# b = "".join(a)
# # print(b, type(b))
# 第三种
# for i in a:
#     print(i, end="")
# 第四种
b = tuple(a)
print(b)

