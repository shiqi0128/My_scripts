import requests
from Atle.interface.header_s import host, header  # 依赖头部文件封装的方法 host,头部和token
# from Atle.interface.public_func import sku, goods_id, openitem_id, address_id, p_id, order_no  # 依赖公共文件返回的字段被多次调用


def comment_list():
    """评论列表
    :param:token:用户授权的token
    :param:page:页数，1
    :param:size:单页数量，10
    :param:openitem_id:商品id
    :return:p_id:为评论列表提取的最新添加的第一条评论
    """
    url = host + "/api/openitem_comment/index"
    data = {"size": 10, "page": 1, "openitem_id": 224}
    r = requests.get(url=url, headers=header, params=data).json()
    # out_format("评论列表:", r)
    print(r)
    return r
    # p_id = r["data"]["list"]["latest"][0]["id"]  # 此操作为提取评论id
    # return p_id


comment_list()