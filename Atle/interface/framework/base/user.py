# 该文件为app3.2更改登录方式和新增优惠券入口的接口
import requests
import json
from Atle.interface.framework.common.header_s import host, header  # 依赖头部文件封装的方法 host,头部和token
from Atle.interface.framework.common.color import out_format

class Discount():
    """定义app3.2主要功能为登录和优惠券的功能"""
    # def event_login(self):
    #     """第三方登录
    #     :param:platform:平台 wx|qq|sina
    #     :param:captcha:验证码
    #     :param:nickname:昵称
    #     :param:avatar:头像地址
    #     :param:secret:验证参数
    #     """
    #     url = host + "/api/user/event_login"

    def getprofile(self):
        """获取个人资料"""
        url = host + "/api/user/getprofile"
        r = requests.post(url=url, headers=header).json()
        out_format("获取个人资料:", r)
        return r

    def user_label(self):
        """设置用户标签
        :param:token:用户授权token
        :param:avatar:头像
        :param:nickname:昵称
        :param:gender:性别,允许值: "0:女", "1:男"
        :param:age_group:年龄段,允许值: "1970:80前", "1980:80后", "1990:90后", "2000:00后"
        :param:pet_type:宠物种类,允许值: "none:没有", "dog:狗", "cat:猫", "aquatic:水族", "reptile:爬行", "birds:飞禽"
        """
        url = host + "/api/user/taged"
        files = {"avatar": ("3.jpg", open(r"C:\Users\sz\Desktop\aiitle\3.0\photos\3.jpg", "rb").read(), "jpg/png")}
        # print("类型:", type(str(files)))
        data = {
            "avatar": files,
            "nickname": "冬瓜",
            "gender": "0",
            "age_group": "2000",
            "pet_type": "none"
        }
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("设置用户标签:", r)
        return r

    def center(self):
        """个人中心
        :param:token:用户授权token
        :param:user_id:目标用户id，如果是自己-1
        :param:page:页数
        :param:size:单页数量
        """
        url = host + "/api/user/home"
        data = {"user_id": -1, "page": 1, "size": 10}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("个人中心:", r)
        return r

    def Brand_Story(self):
        """达人推荐"""
        url = host + "/api/user/hot"
        r = requests.get(url=url, headers=header).json()
        out_format("达人推荐:", r)
        return r

    # def resetpwd(self):
    #     """重置密码
    #     :param:token:用户授权的token
    #     """
    #     url = host + "/api/user/resetpwd"
    #     r = requests.post(url=url, headers=header).json()
    #     out_format("重置密码:", r)

    def check_mobile(self):
        """检测手机号
        :param:token:用户授权token
        """
        url = host + "/api/validate/check_mobile_exist"
        r = requests.post(url=url, headers=header).json()
        out_format("检测手机号:", r)
        return r




# Discount().getprofile()
# Discount().user_label()
# Discount().center()
# Discount().Brand_Story()
Discount().check_mobile()

