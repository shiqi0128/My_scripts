import requests
# import os
# from time import sleep
from interfaceTest.GMALL.gmall_header import golbal_shopid, header, host, token
from interfaceTest.GMALL.gmall_all.color import out_format
from urllib3 import encode_multipart_formdata
import random


# 门店管理——店铺管理API
class Shop_manage(object):
    """
    定义一个wiki门店管理Tab中菜单名为店铺管理的所有接口测试类
    """
    def guide_list(self, shop_id=golbal_shopid):
        """导购-列表
        :param:shop:门店id
        :param:page_size 分页条数（非必填）
        :param:page 页码（默认1）（非必填）
        """
        guide_id_list = []
        url = host + "/api/shops/%s/salemans" % shop_id
        r = requests.get(url=url, headers=header).json()
        if r["data"]["salemans"]["data"] is not None:
            s = len(r["data"]["salemans"]["data"])
            print("长度:", s)
            for i in range(s):
                guide_id_list.append(r["data"]["salemans"]["data"][i]["id"])
                for index, guide_id in enumerate(guide_id_list, 1):
                    print("获取导购id[%s]:" % index, r["data"]["salemans"]["data"][i]["id"], "\n")
                    out_format("导购列表:", r)
                    return guide_id
        else:
            print("data is null")
            print("导购列表", r, "\n")
        return None

    def guide_add(self, name, gender, mobile, age=None, career=None, shop_id=golbal_shopid):
        """导购-新增
        :param:shop:门店id
        :param:portrait:导购头像
        :param:name:导购姓名
        :param:gender:导购性别
        :param:mobile:导购电话
        :param:age:导购年龄---非必填
        :param:career:工龄---非必填
        """
        rand = random.randrange(1, 5)
        print("_____", rand)
        url = host + "/api/shops/%s/salemans" % shop_id
        files = {"portrait": ("%s.jpg" % rand, open(r"F:\test\interfaceTest\image\%s.jpg" % rand, "rb").read(),
                              "jpg/png"),
                 "name": name+str(random.randrange(0, 100)),
                 "gender": gender,
                 "mobile": mobile
                 }
        encode_data = encode_multipart_formdata(files)  # encode_multipart_formdata是导入的一个方法,这个方法下面的文件赋值给encode_data
        data = encode_data[0]  # encode的返回结果第一个值是上传的文件
        header_data = \
                {
                    "Content-Type": encode_data[1],  # 指要上传文件的方式，输出encode_data的结果，头部变更为第2个值才能上传
                    "Authorization": "Bearer "+token,
                                 }
        r = requests.post(url=url, headers=header_data, data=data).json()
        out_format("导购新增:", r)

    def guide_update(self, saleman, name, gender, mobile, age=None, career=None, shop_id=golbal_shopid):
        """导购-更新
        :param:shop:门店id
        :param:saleman:导购id
        :param:portrait:导购头像
        :param:name:导购姓名
        :param:gender:导购性别
        :param:mobile:导购电话
        :param:age:导购年龄---非必填
        :param:career:工龄---非必填
        """
        url = host + "/api/shops/%s/salemans" % shop_id
        files = {"portrait": ("%s.jpg" % random.randrange(5, 10), open(r"F:\test\interfaceTest\image\%s.jpg" % random.randrange(5, 10), "rb").read(), "jpg/png"),
                 "saleman": saleman,
                 "name": name + str(random.randrange(0, 100)),
                 "gender": gender,
                 "mobile": mobile
                 }
        encode_data = encode_multipart_formdata(files)  # encode_multipart_formdata是导入的一个方法,这个方法下面的文件赋值给encode_data
        data = encode_data[0]  # encode的返回结果第一个值是上传的文件
        header_data = \
            {
                "Content-Type": encode_data[1],  # 指要上传文件的方式，输出encode_data的结果，头部变更为第2个值才能上传
                "Authorization": "Bearer " + token,
            }
        r = requests.post(url=url, headers=header_data, data=data).json()
        out_format("导购更新:", r)

    def guide_delete(self, saleman, shop_id=golbal_shopid):
        """导购—删除
        :param:shop:门店id
        :param:saleman:导购id
        """
        url = host + "/api/shops/%s/salemans/%s" % (shop_id, saleman)
        r = requests.delete(url=url, headers=header).json()
        out_format("导购-删除:", r)

    # 黑名单相关接口
    def blacklist(self, identity= None, customer_id= None, shop_id=golbal_shopid):
        """黑名单列表"""
        blacklist_id_all = []
        url = host + "/api/shops/%s/blacklist" % shop_id
        r = requests.get(url=url, headers=header).json()
        s = r["data"]["blacklists"]["data"]
        if r["data"]["blacklists"]["data"] is not None:
            for i in range(len(s)):
                blacklist_id = r["data"]["blacklists"]["data"][i]["id"]
                blacklist_id_all.append(blacklist_id)
                print("获取黑名单id[%s]:" % blacklist_id, "\n")
                out_format("黑名单列表", r)
                return blacklist_id     # r["data"]["blacklists"]["data"]不为空则返回blacklist_id，为空则返回None
        else:
            print("data is null")
            out_format("黑名单列表", r)
        return None

    # 该接口暂时有问题
    def blacklist_add(self, identity, gender, remark, shop_id=golbal_shopid):
        """黑名单--新增
        :param identity:身份
        :param gender:性别
        :param remark:备注
        :param avatar:黑名单头像
        """
        url = host + "/api/shops/%s/blacklist" % shop_id
        files = {"avatar": ("%s.jpg" % random.randrange(10, 18), open(r"F:\test\interfaceTest\image\%s.jpg" % random.randrange(10, 18), "rb").read(), "jpg/png"),
                 "identity": identity,
                 "gender": gender,
                 "remark": remark
                 }
        encode_data = encode_multipart_formdata(files)  # encode_multipart_formdata是导入的一个方法,这个方法下面的文件赋值给encode_data
        data = encode_data[0]  # encode的返回结果第一个值是上传的文件
        header_data = \
            {
                "Content-Type": encode_data[1],  # 指要上传文件的方式，输出encode_data的结果，头部变更为第2个值才能上传
                "Authorization": "Bearer "+token,
            }
        r = requests.post(url=url, headers=header_data, data=data).json()
        out_format("黑名单--新增:", r)

    def blacklist_detail(self, blacklist_id, shop_id=golbal_shopid):
        """黑名单--详情"""
        url = host + "/api/shops/%s/blacklist/%s" % (shop_id, blacklist_id)
        r = requests.get(url=url, headers=header).json()
        out_format("黑名单--详情:", r)

    def blacklist_update(self, blacklist_id, identity, gender, remark=None, shop_id=golbal_shopid):
        """黑名单--更新
        :param identity:身份
        :param gender:性别
        :param remark:备注
        :param avatar:黑名单头像
        """
        url = host + "/api/shops/%s/blacklist/%s" % (shop_id, blacklist_id)
        data = {
                "identity": identity,
                "gender": gender,
                "remark": remark,
                "_method": "PUT"
        }
        r = requests.post(url=url, headers=header, json=data).json()
        out_format("黑名单--更新:", r)

    def blacklist_delete(self, blacklist_id, shop_id=golbal_shopid):
        """黑名单--删除"""
        url = host + "/api/shops/%s/blacklist/%s" % (shop_id, blacklist_id)
        r = requests.delete(url=url, headers=header).json()
        out_format("黑名单--删除:", r)

    def blacklist_batch(self, identity, remark=None, shop_id=golbal_shopid):
        """黑名单-批量添加
        :param:customer_ids:顾客id 集合
        :param:identity:身份
        :param:remark:备注
        """
        url = host + "/api/shops/%s/blacklist/batch-blacklist-store" % shop_id
        data = {"identity": identity, "customer_ids": ["212", "213", "214"]}
        r = requests.post(url=url, headers=header, json=data).json()
        out_format("黑名单--批量添加:", r)

    def reception_detail(self, shop_id=golbal_shopid):
        """接待统计详情
        :param:shop_id:门店id
        :param:date:日期
        """
        url = host + "/api/shops/%s/reception" % shop_id
        r = requests.get(url=url, headers=header).json()
        out_format("接待统计详情:", r)

    def guide_info(self, guide_id, date, shop_id=golbal_shopid):
        """导购信息"""
        url = host + "/api/shops/%s/salemans/%s/detail" % (shop_id, guide_id)
        r = requests.get(url=url, headers=header).json()
        out_format("导购信息", r)

    def guide_recept(self, guide_id, date, shop_id=golbal_shopid):
        """导购接待详情
        :param:saleman:导购id
        :param:date:日期
        :param:gender:性别1男2女---非必填
        :param:page_size：分页条数（默认10)---非必填
        :param:page:页码（默认1）---非必填
        """
        url = host + "/api/shops/%s/salemans/%s/guide-list" % (shop_id, guide_id)
        data = {"date": date}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("导购接待详情:", r)

    def update_message(self, shop_id=golbal_shopid):
        """修改门店消息
        :param:name:门店名称
        :param:address:门店地址
        :param:province:省
        :param:city:市
        :param:region:区
        :param:contact:商场联系人
        :param:contact_phone:联系电话
        :param:area:门店面积
        :param:scale:平面图缩放比例---json
        :param:openning_hours:营业时间
        :param:ips:ip白名单
        :param:shop_threshold:门店预警值
        :param:zone_threshold:区域预警值
        ----以上均为非必填
        """
        url = host + "/api/shops/%s/shop-info-update" % shop_id
        r = requests.get(url=url, headers=header).json()
        out_format("修改门店消息", r)

    def notice_show(self, shop_id=golbal_shopid):
        """门店提醒规则查看"""
        url = host + "/api/shops/%s/arrival-notice-show" % shop_id
        r = requests.get(url=url, headers=header).json()
        out_format("门店提醒规则查看:", r)

    def notice_update(self, is_vip, is_consume, is_new_customer, last_entry_interval, shop_id=golbal_shopid):
        """门店提醒规则更新
        :param:is_vip:VIP
        :param:is_consume:消费记录
        :param:is_new_customer:新老客
        :param:last_entry_interval:上次进店
        """
        url = host + "/api/shops/%s/arrival-notice-update" % shop_id
        data = {"is_vip":is_vip, "is_consume":is_consume, "is_new_customer":is_new_customer, "last_entry_interval":last_entry_interval}
        r = requests.put(url=url, headers=header, json=data).json()
        out_format("门店提醒规则更新", r)

    def notice_list(self, shop_id=golbal_shopid):
        """门店提醒规则列表"""
        url = host + "/api/shops/%s/arrival-customer-list" % shop_id
        r = requests.get(url=url, headers=header).json()
        out_format("门店提醒规则列表", r)




# shop_manage().guide_list()
# shop_manage().guide_add("小叮当", 1, "18772727272")
# blacklist_id = shop_manage().blacklist
# shop_manage().blacklist_add("小偷偷", 1, "这个小偷偷了几次顾客的东西")
# shop_manage().blacklist_update("小偷偷", 1, "这个小偷偷了几次顾客的东西")
# shop_manage().blacklist_delete()
# shop_manage().blacklist_batch("骗子")
# Shop_manage().reception_detail()
# Shop_manage().guide_info()
# Shop_manage().guide_recept()
# Shop_manage().update_message()
Shop_manage().notice_show()
# Shop_manage().notice_update()
# Shop_manage().notice_list()
