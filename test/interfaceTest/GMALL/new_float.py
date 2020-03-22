def keep_decimal(num1, num2):
    """结果保留一位小数

    num1除以num2的结果为小数时，保留一位小数（四舍五入）
    %.2f会根据round方法取值，所以不可靠，必须多保留一位，例如：1.345111->1.345->345->34->4(根据余数判断是舍或入)
    :param num1: 第一个值
    :param num2: 第二个值
    :return:
    """
    result = num1 / num2
    res_3 = "%.3f" % result                       # 得到1.34511111中的1.345值
    res_2 = int(float(res_3.split(".")[1]) / 10)  # ["1","345"]------>>>345/10 = 34
    res_1 = res_2 % 10                            # 得到余数  34%10 = 4
    print("计算的初始值", result)
    if num1 % num2 == 0:
        print(result)
        # return result
    else:
        last_res = int(result) + int(res_2/10)/10   # int(res_2/10)/10 ==>>>> (34/10)/10=>>0.3
        if res_1 < 5:
            print("舍去的值", last_res)
            # return last_res
        else:
            last_res = float("%.1f" % (last_res+0.1))
            print("五入的值", last_res)
            # return last_res+0.1


keep_decimal(7, 2)