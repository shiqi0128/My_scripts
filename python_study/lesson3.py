# best_language = " PHP is the best programming language in the world! "
# a = best_language.strip()
# b = a.replace("PHP", "Python")
# print(b)

# print(best_language.strip().replace("PHP", "Python"))

my_hobby = "Never stop learning!"
# a.	截取从 位置 2 ~ 位置6 的字符串
# result = my_hobby[1:6]
# print("截取从 位置 2 ~ 位置6 的字符串--结果为:", result)
# b.截取从位置2 ~ 末尾位置 的字符串
# result = my_hobby[1:]
# print("截取从位置 2 ~ 末尾位置的字符串--结果为:", result)
# c.截取从 开始位置 ~ 6位置 的字符串
# result = my_hobby[:]
# print("截取完整的字符串--结果为:", result)
# d.截取完整的字符串
# e.从开始位置，每隔一个字符截取字符串
# result = my_hobby[::2]
# print("从开始位置，每隔一个字符截取字符串--结果为:", result)
# f.从 索引3 开始，每2个字符中取一个字符
# result = my_hobby[3::2]
# print("从 索引3 开始，每2个字符中取一个字符--结果为:", result)
# g.截取从 索引2 ~ 末尾-1 的字符串
# result = my_hobby[2:]
# print("截取从 索引2 ~ 末尾-1 的字符串--结果为:", result)
# h.截取字符串末尾两个字符
# result = my_hobby[-2:]
# print("截取字符串末尾两个字符--结果为:", result)
# i.字符串的逆序（拓展）
# result = my_hobby[::-1]
# # print("字符串的逆序（拓展）--结果为:", result)

# 4.去生鲜超市买橘子
# a.收银员输入橘子的价格，单位：元／斤
# b.收银员输入用户购买橘子的重量，单位：斤
# c.计算并且 输出 付款金额
# 思考：如果输入的不是一个数字，执行程序会怎样？如何解决呢？
5
# 输入橘子单价
# price = input("请输入橘子的价格:")
# # print(type(price))
# # 输入橘子重量
# weight = input("请输入用户购买橘子的重量:")
# # 计算所付款金额
# total = float(price) * float(weight)
# print("需付款:", total)
# try:
#     price = float(price)
#     weight = float(weight)
#     print('付款金额: {}'.format(price * weight))
# except:
#     print("请输入数字!")
#     print("橘子所付金额为:", total)
# # print("橘子每斤{:.1f}元，您购买了{:.1f}斤，需要支付{:.1f} 元！".format(float(price) , float(weight) , total))

# 输入橘子单价
# price = input("请输入橘子的价格:").strip()
# while True:
#     price = input("请输入橘子的价格:").strip()    # 输入橘子单价
#     if price.isdigit():                  # if输入的橘子单价包含数字继续往下执行，不包含数字则执行else语句，重新输入
#         weight = input("请输入用户购买橘子的重量:").strip()    # 输入橘子单价正确则执行这条语句，属于橘子的重量
#         if weight.isdigit():                          # if输入的橘子重量包含数字继续往下执行，不包含数字则执行else语句，重新输入
#             total = float(price) * float(weight)        # 得出橘子的金额，输入的为str型，转换为浮点型计算
#             print("橘子每斤{:.1f}元，您购买了{:.1f}斤，需要支付{:.1f} 元！".format(float(price), float(weight), total))  # 输入结果
#             break                                      # 执行正确后退出循环
#         else:
#             print("您输入的不是数字。请重新输入！")         # 输入的不是数字则重新输入
#     else:
#         print("您输入的不是数字。请重新输入！")            # 输入的不是数字则重新输入



# 1.个人信息展示
# a.在控制台依次提示用户输入：姓名、网名、年龄、性别、爱好、座右铭
# b.照以下格式输出：
# **************************************************
# 个人信息展示
#
# 姓名（网名）
#
# 年龄：年龄
# 性别：性别
# 爱好：爱好
# 座右铭：座右铭
# **************************************************


# name = input("请输入您的姓名:").strip()
# web_name = input("请输入您的网名:").strip()
# age = input("请输入您的年龄:").strip()
# gender = input("请输入您的性别:").strip()
# hobby= input("请输入您的爱好:").strip()
# motto = input("请输入您的座右铭:").strip()
# print("**************************************************", "\n")
# print("个人信息展示", "\n\n")
# print("姓名(网名):", name, web_name, "\n\n")
# print("年龄:", age, "\n")
# print("性别:", gender, "\n")
# print("爱好:", hobby, "\n")
# print("座右铭:", motto, "\n")
# print("**************************************************", "\n")
#
message = input("请输入:姓名、网名、年龄、性别、爱好、座右铭:").strip()
message_list = message.split("、")      # 按、切割后存为列表，按列表索引取值
print("**************************************************", "\n")
print("个人信息展示", "\n\n")
print("姓名(网名):", message_list[0], (message_list[1]), "\n\n")
print("年龄:", message[1], "\n")
print("性别:", message_list[2], "\n")
print("爱好:", message_list[3], "\n")
print("座右铭:", message_list[4], "\n")
print("**************************************************", "\n")





