def out_format(res, args):
    """正常接口返回的颜色显示

    改变颜色后的输出结果
    """
    print("\033[1;32m{0}\033[0m".format(res), args, "\n\n")
