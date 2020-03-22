# 此文件为所有订单相关接口
# order订单相关接口
import requests
import time
import json
from Atle.interface.framework.common.header_s import host, header  # 依赖头部文件封装的方法 host,头部和token
from Atle.interface.framework.common.public_func import goods_id, address_id, order_no  # 依赖公共文件返回的字段被多次调用
from Atle.interface.framework.common.color import out_format


class order():
    """定义一个订单相关的测试类"""
    def creat_order(self):
        """
        提交订单
        :param:token:用户授权token
        :param: address_id:地址id
        :param:order:产品---下面2个参数id和count输入order参数的主从关系
        :param:id:单品id
        :param:count:数量
        :param: type:支付方式(1:微信,2:支付宝),允许值: "1", "2"
        以上均为必填
        """
        url = host + "/api/order/create"
        order = [{"id": goods_id, "count": 1}]  # 参数为列表格式
        data = {
            "address_id": address_id,
            "order": json.dumps(order),   # 需要转成str格式再上传
            "type": 1
        }
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("提交订单:", r)
        time.sleep(3)
        return r

    def order_list(self):
        """
        订单列表
        :param:token:用户授权token
        :param:size:单页记录数
        :param:page:页码
        :param:status:订单状态（0.待支付 1.待发货 2.待收货 3.待评论）
        :return: order_no:订单编号
        """
        # header = get_header()
        url = host + "/api/order/list"
        # status = {i for i in [0, 1, 2, 3]}
        # print(status)
        # for i in [0, 1, 2, 3]:
        #     print(i)
        data = {"size": 10, "page": 1, "status": 0}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("订单列表:", r)
        # for i in range(len(r["data"])):    # 这里不能遍历i,是个问题，写完后过来复查！
        #     order_no = r["data"][i]["order_no"]
        if len(r["data"]) != 0:
            order_no = r["data"][0]["order_no"]
            print("提交订单的新编号order_no:", order_no)
            return order_no
        else:
            print("data is NULL")

    def order_pay(self):
        """订单支付（二次支付）   # 这个接口需要先提交订单以后打印订单列表，取订单列表最新的订单编号放到参数中执行
        :param:token:用户授权token
        :param:order_no:订单编号
        :param: type:支付方式(1:微信,2:支付宝),允许值: "1", "2"
        """
        order_no_new = self.order_list()
        url = host + "/api/order/pay"
        ll = [1, 2]
        for i in ll:
            data = {"order_no": order_no_new, "type": i}
            print("data", data)
            r = requests.post(url=url, headers=header, data=data).json()
            out_format("订单支付(二次支付):", r)
            return r

    def update_order(self):
        """
        更新订单
        :param:token:用户授权token
        :param:order_no:订单编号
        :param:status:订单状态（0.待支付 1.待发货 2.待收货 3.待评论 4.交易关闭或已退款 5.全部完成）非必填
        :param:deletestatus:是否删除（0.已删除 1.正常）非必填
        :param:cancel_desc:	(订单取消原因）非必填
        :return:
        """
        url = host + "/api/order/update"
        data = {
            "order_no": order_no,
            "status": "",
            "deletestatus": ""
        }
        # print(data)
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("更新订单:", r)
        return r

    def order_detail(self):
        """订单详情
        :param:token:用户授权token
        :param:order_no:订单号
        """
        url = host + "/api/order/find"
        data = {"order_no": order_no}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("订单详情:", r)
        return r
