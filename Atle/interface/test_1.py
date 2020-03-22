import requests
from Atle.interface.header_s import header
from Atle.interface.header_s import host
from Atle.interface.framework.common.color import out_format


# class alte():
#     """定义一个测试类"""
#
#     def profile(self):
#         """修改个人信息
#         :param:token:请求的token（头部）
#         :param:avatar:头像
#         :param:gender(性别)
#         :param:nickname(昵称)-----此为必传
#         :param:birthday(生日)
#         :param:city(城市)
#         :param:bio(宠物宣言)
#         如果什么都没有修改的情况，所有请求参数都要传，字段传空值
#     """
#     url = host + "/api/user/profile"
#     file_data = {"avatar": ("1.jpg", open(r"C:\Users\sz\Pictures\1.jpg", "rb").read(), "jpg/png")}  # 读取文件赋值给file
#     data = {
#         "aa": "aa",
#         "gender": "1",
#         "nickname": "小年年%s" % random.randrange(1, 1000),
#         "birthday": "2019-08-10",
#         "city": "861",
#         "bio_01": "养它爱它一辈子"
#     }
    # data = {
    #     "gender": "",
    #     "nickname": "",
    #     "birthday": "",
    #     "city": "",
    #     "bio_01": ""
    # }

    # print(type(data))
#     print(url)
#     r = requests.post(url=url, headers=header, data=data)
#     out_format("修改个人信息:", r.status_code)
#
#     def creat_address(self):
#         """
#         :param:name:收货人姓名
#         :param:phone:手机号码
#         :param:city:省市区
#         :param:address:地址
#         :param:isdefault:是否默认地址,默认值: 0
#         :return:
#         除了默认值均为必填
#         """
#         url = host + "/api/address/create"
#         data = {
#             "name": "王小二",
#             "phone": "13812151334",
#             "city": "江苏",
#             "address": "三人行",
#             "isdefault": 0
#         }
#         r = requests.post(url=url, headers=header, data=data)
#         out_format("创建收货地址:", r.status_code)
#
#
# alte().profile()
# alte().creat_address()

# abc = ["0", "1", "2", "3"]
# s = int(len(abc))
# print("s", s)
# for i in range(s):
#     print("i", i)


# def update_order():
#     """
#     更新订单
#     :param:token:用户授权token
#     :param:order_no:订单编号
#     :param:status:订单状态（0.待支付 1.待发货 2.待收货 3.待评论 4.交易关闭或已退款 5.全部完成）非必填
#     :param:deletestatus:是否删除（0.已删除 1.正常）非必填
#     :param:cancel_desc:	(订单取消原因）非必填
#     :return:
#     """
#     url = host + "/api/order/update"
#     token = "10977c52-2091-485d-88ce-6a82305aa821"
#     header = {
#             "Content-Type": "application/x-www-form-urlencoded application/json",
#             "token": "10977c52-2091-485d-88ce-6a82305aa821"
#     }
#     data = {
#
#         "order_no": 1568879012398637237
#         # "status": "",
#         # "deletestatus": "",
#         # "cancel_desc": ""
#     }
#     # print(data)
#     r = requests.post(url=url, headers=header, data=data).json()
#     out_format("更新订单:", r)
#
#
# update_order()

# ll = {1: "微信", 2: "支付宝"}
# for i in ll:
#     # print(i)
#     print("%s" % ll.values(), i)

def order_pay(self):
    """订单支付（二次支付）   # 这个接口需要先提交订单以后打印订单列表，取订单列表最新的订单编号放到参数中执行
    :param:token:用户授权token
    :param:order_no:订单编号
    :param: type:支付方式(1:微信,2:支付宝),允许值: "1", "2"
    """
    order_no_new = self.order_list()
    url = host + "/api/order/pay"
    # ll = [1, 2]
    ll = {1: "微信", 2: "支付宝"}
    for i in ll:
        data = {"order_no": order_no_new, "type": i}
        print("data", data)
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("订单支付(二次支付):", r)


# 话题相关接口
def creat_talk():
    """
    创建话题
    :param:token:用户授权的token
    :param:title:话题标题
    :param:
    :return:
    """