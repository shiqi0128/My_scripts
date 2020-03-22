import requests
from interfaceTest.GMALL.gmall_header import golbal_shopid, header, host, token
from urllib3 import encode_multipart_formdata
import random


# 门店管理——店铺管理API
class shop_manage(object):
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
                    print("导购列表:", r, "\n")
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
        url = host + "/api/shops/%s/salemans" % shop_id
        files = {"portrait": ("%s.jpg" % random.randrange(1, 5), open(r"F:\test\interfaceTest\image\%s.jpg" % random.randrange(1, 5), "rb").read(), "jpg/png"),
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
        print("导购新增:", r, "\n")

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
        print("导购更新:", r, "\n")

    def guide_delete(self, saleman, shop_id=golbal_shopid):
        """导购—删除
        :param:shop:门店id
        :param:saleman:导购id
        """
        url = host + "/api/shops/%s/salemans/%s" % (shop_id, saleman)  # saleman要填导购id,调用导购列表返回的导购id
        r = requests.delete(url=url, headers=header).json()
        print("导购-删除:", r, "\n")
