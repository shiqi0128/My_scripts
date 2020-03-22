# ------------------导购商品商品评论的相关接口----------------------
# openitemcomment商品详情评论
import requests
import time
import random
from Atle.interface.framework.common.header_s import host, header  # 依赖头部文件封装的方法 host,头部和token
from Atle.interface.framework.common.public_func import p_id  # 依赖公共文件返回的字段被多次调用
from Atle.interface.framework.common.color import out_format


class openitemcomment():
    def add_comment(self):
        """添加评论
        :param:token:用户授权的token
        :param:content:评论内容
        :param:openitem_id:开放商品id
        :param:pid:父评论id,默认值0----此处传值为0的时候意为此条评论是父评论，不是子评论
        :param:at_user:	@用户ID,默认值0----此参数非必填
        """
        url = host + "/api/openitem_comment/create"
        data = {
                "content": "我家二狗子特别喜欢吃这个东西%s" % random.randrange(1, 1000),
                "openitem_id": 224,
                "pid": 0,
                # "at_user": ""
                }
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("添加评论:", r)
        return r

    def comment_list(self):
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
        out_format("评论列表:", r)
        return r
        # p_id = r["data"]["list"]["latest"][0]["id"]  # 此操作为提取评论id
        # print("提取的评论id:", p_id)
        # return p_id

    def Ocomment(self):
        """
        一个评论
        :param:token:用户授权的token
        :param:page:页数，1
        :param:size:单页数量，10
        :param:id:评论id
        :return:
        """
        time.sleep(2)
        url = host + "/api/openitem_comment/get"
        data = {"size": 10, "page": 1, "id": p_id}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("一个评论:", r)
        return r

    def comment_delete(self):
        """
        删除评论
        :param:token:用户授权的token
        :param:id:评论id
        :return:
        """
        url = host + "/api/openitem_comment/delete"
        data = {"id": p_id}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("删除评论:", r)
        return r

    def update_comment(self):
        """
        更新评论
        :param:token:用户授权的token
        :param:id:评论id
        :param:content:修改的评论内容
        :return:
        """
        url = host + "/api/openitem_comment/update"
        data = {"id": p_id, "content": "我也喜欢这条狗子欧耶耶"}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("更新评论:", r)
        return r


# openitemcomment().add_comment()
# openitemcomment().comment_list()
# openitemcomment().Ocomment()
# openitemcomment().update_comment()
# openitemcomment().comment_delete()
