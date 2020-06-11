"""
-------------------------------------------------
  @Time : 2020/4/7 14:52 
  @Auth : 十七
  @File : homework_0403a.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
def curcle(r):
    """定义一个圆的周长和面积
    :param:r=面积
    """
    curcle_area = 3.14 * (r ** 2)
    curcle_area = round(curcle_area, 3)   # 四舍五入，保留3位小数
    curcle_perimeter = 2 * 3.14 * r
    curcle_perimeter = round(curcle_perimeter, 3)  # 四舍五入，保留3位小数
    print(f"半径为{r}的圆周长是{curcle_perimeter}, 圆面积是{curcle_area}")
    return curcle_area, curcle_perimeter

def rectangle(a, b):
    """定义一个长方形的周长和面积
    :param:a=长
    :param:b=宽
    """
    rectangle_area = a * b
    rectangle_perimeter = (a + b)*2
    print(f"长为{a},宽为{b}的长方形的周长为{rectangle_perimeter}, 面积为{rectangle_area}")
    return rectangle_area, rectangle_perimeter


