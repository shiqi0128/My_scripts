def round_up(number, ndigits=0):
    """模拟round内置函数
    :param number:输入的值
    :param ndigits：保留的位数
    """
    try:
        if ndigits == 0:
            res_3 = "%.{0}f".format(ndigits) % number
            return res_3
            # print(res_3)
        else:
            res_3 = "%.{0}f".format(ndigits + 2) % number  # 多保留两位取值 因为自带的保留值是不准确的
            res_2 = int(
                float(res_3.split(".")[-1]) / 10)  # 比如保留2位时，["1","3451"]------>>>3451/10 = 345 # 这里是想要的保留位，多一位
            res_1 = res_2 % 10  # 得到余数  345%10 = 5
            # int(res_2/10)拿到想要的保留位，pow计算乘方(10的ndigits方)，得到的结果是零点几
            last_res = int(number) + (int(res_2 / 10)) / pow(10, ndigits)  # 得到保留位数的值，然后在判断是否进“1”
            if res_1 < 5:
                # print(last_res)
                return last_res
            else:
                last_res = last_res + (1 / pow(10, ndigits))  # 保留的位数进“1”
                return last_res
                # print(last_res)
    except TypeError:
        print("输入的内容不是数字")