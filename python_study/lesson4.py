"""
-------------------------------------------------
  @Time : 2020/3/22 21:42 
  @Auth : 十七
  @File : lesson4.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
  @Company: 江苏宠资链互联网有限公司
  @Copyright: 爱它乐
-------------------------------------------------
"""
# 100以内所有奇数之和
# count_var = 1
# total = 0
# while count_var <= 100:
#     if count_var % 2 == 1:
#         total += count_var
#     count_var += 1
#
# print(f"100以内的奇数之和为：{total}")

# 100以内前23位数字之和
count_var = 1
total = 0
while count_var <= 100:
    total += count_var
    count_var += 1
    if count_var == 24:
        break

print(f"100以内的前23位数字之和为：{total}")

