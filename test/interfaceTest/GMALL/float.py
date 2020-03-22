"""此方法为四舍五入可以调用的方法"""

def precision(a, b):
    c = a / b
    c1 = "%.3f" % c
    print("初始值:", c1)
    c2 = int(float(c1.split(".")[1]) / 10)  # c1.split(".")=["0", "333"],取第2个是"333",333除以10=33.3,int执行后c2=33
    # print(int(c2))
    c3 = c2 % 10
    if a % b == 0:
        print(c)
    else:
        x = int(c) + int(c2 / 10) / 10  # int(c2/10)/10 ==>>>> (2/10)/10=>>0.02, 2+0.02=x=2.02
        if c3 < 5:
            print("舍去后的值", x)
            # return last_res
        else:
            x = float("%.1f" % (x + 0.1))
            print("五入的值", x)
            # return last_res+0.1


precision(35, 4)

