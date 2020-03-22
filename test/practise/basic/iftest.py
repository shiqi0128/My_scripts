# h = float(input("请输入身高： "))
# w = float(input("请输入体重： "))



# BIM = w / (h ** 2)

# if BIM < 18.5:
#     print("过轻")
# elif BIM >= 18.5 and BIM < 25:
#     print("正常")
# elif BIM >= 25 and BIM < 30:
#     print("过重")
# elif BIM >= 28 and BIM < 32:
#     print("肥胖")
# else:
#     print("严重肥胖")

# print("小明的身高为:%.2f, 体重为: %.2f, BIM为: %.2f" % (h, w, BIM))

# k = float(input("请输入刀子的长度: "))

# if k < 10:
#     print("可以上火车")
# else:
#     print("不允许上火车")

balance = float(input("请输入公交车当前余额："))

if balance > 2:
    print("可以上公交车")
    seat = int(input("请输入当前座位："))
    if seat > 0:
        print("可以坐下")
    else:
        print("只能站着")
else:
    print("不可以上公交车")