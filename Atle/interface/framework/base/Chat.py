# ---------------------该文件为所有会话接口--------------------
import requests
from Atle.interface.framework.common.header_s import host, header  # 依赖头部文件封装的方法 host,头部和token
# from Atle.interface.framework.common.public_func import sku, goods_id, openitem_id, address_id, p_id, order_no  # 依赖公共文件返回的字段被多次调用
from Atle.interface.framework.common.color import out_format


class Chat():
    """定义一个会话相关的测试类"""
    def get_chat_list(self):
        """获取会话列表
        :param:token:用户授权的token
        """
        url = host + "/api/chat/list"
        r = requests.get(url=url, headers=header).json()
        out_format("获取会话列表:", r)
        chat_id = r["data"][0]["chat_id"]
        return chat_id

    def get_message(self):
        """获取会话消息
        :param:token:用户授权的token
        :param:chat_id:会话id
        """
        chat_id = self.get_chat_list()
        url = host + "/api/chat/get_msg_list"
        data = {"chat_id": chat_id}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("获取会话消息:", r)


# Chat().get_chat_list()
Chat().get_message()