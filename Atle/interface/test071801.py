import requests
import time
import json
import random
from Atle.interface.header_s import host, header  # 依赖头部文件封装的方法 host,头部和token
from Atle.interface.public_func import sku, goods_id, openitem_id, address_id, p_id, order_no  # 依赖公共文件返回的字段被多次调用
from Atle.interface.framework.common.color import out_format


class alte():
    """定义一个测试类"""
    def moblie_pass(self):
        """手机密码登录
        :param:mobile:手机号码
        :param:password:密码
        :return:user_id 用户id
        """
        url_01 = host + "/api/user/login"
        cookies = dict(cookies_are='working')    # 发送我的cookies到服务器
        data = {
                    "mobile": "18912763270",
                    "password": "123456789"
        }
        r_01 = requests.post(url=url_01, cookies=cookies, json=data, timeout=0.5).json()
        out_format("手机密码登录:", r_01)
        user_id = r_01["data"]["userinfo"]["id"]
        print("user_id:", user_id)
        return user_id

    # def log_out(self):
    #     """注销登录"""
    #     url_02 = host + "/api/user/logout"
    #     data = {"token": token}
    #     r_02 = requests.post(url=url_02, json=data).json()
    #     out_format("注销登录:", r_02)
# 首页接口
    def choiceness(self):
        """精选
        :param:page:页数,默认1
        :param:size:单页数量，默认10个
        :param:token:请求的token（头部）
        """
        url_03 = host + "/api/index/recommend"
        data = {"page": 1, "size": 1}
        r_03 = requests.get(url=url_03, headers=header, params=data).json()
        out_format("精选:", r_03)
        # assert (r_03["code"], 1)

    def attention(self):
        """关注
        :param:page:页数，默认1
        :param:size:单页数量，默认10个
        :param:token:请求的token（头部）
        """
        url_04 = host + "/api/index/following"
        data = {"page": 1, "size": 1}
        r_04 = requests.get(url=url_04, headers=header, params=data).json()
        out_format("关注:", r_04)
        # assert (r_04["code"], 1)

    def my_page(self):
        """我的收藏，关注，足迹数量
        :param:token:请求的token（头部）
        """
        url_05 = host + "/api/user/myPage"
        r_05 = requests.get(url=url_05, headers=header).json()
        out_format("我的收藏，关注，足迹数量:", r_05)

    def home(self):
        """个人中心
        :param:token:请求的token（头部）
        :param:user_id:目标用户ID，如果是自己传-1
        :param:page:页数，默认1
        :param:size:单页数量，默认10个
        """
        url_06 = host + "/api/user/home"
        data = {
            "user_id": "-1",
            "page": 1,
            "size": 1
        }
        r_06 = requests.get(url=url_06, headers=header, params=data).json()
        out_format("个人中心:", r_06)

    def refreshUser(self):
        """刷新用户缓存"""
        url_07 = host + "/api/user/refreshUser"
        r_07 = requests.get(url=url_07).json()
        out_format("刷新用户缓存:", r_07)

    def profile(self):
        """修改个人信息
        :param:token:请求的token（头部）
        :param:avatar:头像
        :param:gender(性别)
        :param:nickname(昵称)
        :param:birthday(生日)
        :param:city(城市)
        :param:bio(宠物宣言)
        """
        url = host + "/api/user/profile"
        file_data = {"avatar": ("1.jpg", open(r"C:\Users\sz\Pictures\1.jpg", "rb").read(), "jpg/png")}  # 读取文件赋值给file
        data = json.dumps({
                "gender": "1",
                "nickname": "小年年",
                "birthday": "2019-08-10",
                "city": "861",
                "bio_01": "养它爱它一辈子"
                })
        print(type(data))

        r = requests.post(url=url, headers=header, files=file_data, json=data).json()
        out_format("修改个人信息:", r)

    # def changemobile(self):
    #     """
    #     修改/绑定手机号
    #     :param:token:登录后返回的token
    #     :param:oldmobile:原手机号
    #     :param:mobile:新手机号
    #     :param:captcha:验证码
    #     :return:
    #     """
    #     url_09 = host + "/api/user/changemobile"
    #     data = {"oldmobile": "18717752237",
    #             "mobile": "18717752237",
    #             "captcha":

    def article_list(self):
        """文章列表
        :param:page:页数，默认1
        :param:size:单页显示数量，默认10
        :param:category_id:分类id
        :param:recommend：是否推荐，推荐yes, 默认no
        ---均为非必填
        """
        url = host + "/api/post/index"
        r = requests.get(url=url, headers=header).json()
        out_format("文章列表:", r)
        # article_id = r["data"]["list"][0]["id"]
        # return article_id

    def user_artlist(self):
        """Ta的文章列表
        :param:page:页数，默认1
        :param:size:单页显示数量，默认10
        :param:user_id:用户id
        """
        user_id = self.moblie_pass()
        url = host + "/api/post/user"
        data = {"user_id": user_id}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("Ta的文章列表:", r)

    def get_only_art(self):
        """
        获取单个文章
        :param:id:文章id
        :return:
        """
        article_id = self.article_list()
        url = host + "/api/post/get"
        data = {"id": article_id}
        r = requests.get(url=url, params=data).json()
        out_format("获取单个文章:", r)

# goods模块
    def get_goods(self):
        """
        获取单品
        :return: gid
        """
        url = host + "/api/goods/find"
        data = {"sku": sku}
        r = requests.post(url=url, json=data).json()
        out_format("获取单品:", r)
        gid = r["data"]["gid"]
        return gid

    def get_price(self):
        """
        获取单品价格和属性
        :return:
        """
        url = host + "/api/goods/line"
        data = {"sku": sku}
        r = requests.post(url=url, json=data).json()
        out_format("获取单品价格和属性:", r)
        return r

    def get_comment(self):
        """
        获取评论列表
        gid:产品id
        size:记录条数
        page:页码
        :return:
        """
        gid = self.get_goods()
        url = host + "/api/goods/comment"
        data = {"gid": gid, "size": "10", "page": "1"}
        r = requests.post(url=url, json=data).json()
        out_format("获取评论列表:", r)

# Address
    def creat_address(self):
        """
        :param:token:用户授权的token
        :param:name:收货人姓名
        :param:phone:手机号码
        :param:city:省市区
        :param:address:地址
        :param:isdefault:是否默认地址,默认值: 0
        :return:
        以上参数均为必填
        """
        url = host + "/api/address/create"
        data = {
            "name": "王小二",
            "phone": "13812151334",
            "city": "江苏",
            "address": "三人行",
            "isdefault": 0
        }
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("创建收货地址:", r)

    def address_update(self):
        """
        地址更新
        :param:token:用户授权的token
        :param:id:地址id
        :param:name:姓名
        :param:phone:手机
        :param:city:省市区
        :param:address:地址
        :param:isdefault:是否默认地址,默认值0
        :return:
        """
        url = host + "/api/address/update"
        data = {
            "id": address_id,
            "name": "张晓",
            "phone": "18750511512",
            "city": "aa",
            "address": "aa",
            "isdefault": "0"
        }
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("地址更新:", r)

    def address_del(self):
        """
        地址删除
        :param:token:用户授权的token
        :param:id：地址id
        """
        url = host + "/api/address/delete"
        data = {"id": address_id}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("地址删除:", r)

    def address_one(self):
        """
        获取单个地址
        :param:token:用户授权的token
        :param:id:地址id
        :return:
        """
        url = host + "/api/address/find"
        data = {"id": address_id}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("获取单个地址:", r)

# Openitem
    def classify_list(self):
        """
        分类列表----此接口返回的字段传给dynamic_list的category_id
        :param: type:对象类型,默认传moment（现在是只有这一种type）
        :return:category_id:分类id
        """
        url = host + "/api/category/index"
        data = {"type": "moment"}
        r = requests.get(url=url, params=data).json()
        out_format("分类列表:", r)
        category_id = r["data"][1]["id"]
        print("category_id:", category_id)
        return category_id

    def dynamic_list(self):
        """
        动态列表---此接口返回的字段传给open_item的object_id
        :param:token:用户授权的token
        :param:page:页数
        :param:size:单页数量
        :param:category_id:分类id(由分类列表返回的id)
        :param:recommend:推荐：yes,正常：no
        :return:
        """
        category_id = self.classify_list()
        url = host + "/api/Moment/index"
        data = {
                "page": 1,
                "size": 10,
                "category_id": category_id,
                "recommend": "yes"
        }
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("动态列表:", r)
        dynamic_id = r["data"]["list"][-2]["id"]   # 动态列表提取动态id,dynamic_id,传给动态相关产品的接口
        print("动态id:", dynamic_id)
        return dynamic_id

    def open_item(self):
        """
        Openitem - open动态相关商品
        :param:object_type:对象类型,默认值: moment
        :param:object_id:对象ID,目前只有1533这个id
        :param: page:页数，默认值1
        :param:size:单页数量，默认值10
        :return:
        """
        # dynamic_id = self.dynamic_list()   # 暂时用object_id=1533，暂时不调用动态列表的id
        url = host + "/api/openitem/getRelations"
        data = {
                    "object_type": "moment",
                    "object_id": 1533,
                    "page": 1,
                    "size": 10
        }
        r = requests.get(url=url, params=data).json()
        out_format("open动态相关商品:", r)

    def goods_one(self):
        """open单个商品
        :param: id:开放商品id---是商品列表返回的id
        """
        url = host + "/api/openitem/get"
        data = {"id": openitem_id}
        r = requests.get(url=url, params=data).json()
        out_format("open单个商品:", r)

    def goods_search(self):
        """open商品搜索
        :param:page:页数，默认值1
        :param:size:单页数量，默认值10
        :param: keyword:关键词
        :param:object_type:对象类型,允许值"openitem", "goods"
        均为必填
        """
        url = host + "/api/openitem/search"
        object_type = ["openitem", "goods"]
        for i in object_type:
            data = {
                "page": 1,
                "size": 10,
                "keyword": "猫",
                "object_type": i
            }
            r = requests.get(url=url, params=data).json()
            out_format("open商品搜索--%s:" % i, r)

    def goods_advertise(self):
        """
        open商品首页广告
        """
        url = host + "/api/openitem/advert"
        r = requests.get(url=url).json()
        out_format("open商品首页广告:", r)

    def home_tags(self):
        """
        open商品首页标签
        """
        url = host + "/api/openitem/hometag"
        r = requests.get(url=url).json()
        out_format("open商品首页标签:", r)

    def keywords(self):
        """
        搜索词记录
        ---此接口包含了热门和历史搜索记录
        """
        url = host + "/api/openitem/keywords"
        r = requests.get(url=url).json()
        out_format("open搜索词记录:", r)

    def empty(self):
        """
        open清空搜索记录
        ——执行此接口只会清空掉历史搜索记录，不会清空热门搜索词
        """
        url = host + "/api/openitem/keywords"
        r = requests.get(url=url).json()
        out_format("open清空搜索记录:", r)

# order订单相关接口
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
        order_no = r["data"][0]["order_no"]
        print("提交订单的新编号order_no:", order_no)
        return order_no

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

    def order_detail(self):
        """订单详情
        :param:token:用户授权token
        :param:order_no:订单号
        """
        url = host + "/api/order/find"
        data = {"order_no": order_no}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("订单详情:", r)

# 商品详情评论
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
        p_id = r["data"]["list"]["latest"][0]["id"]  # 此操作为提取评论id
        return p_id

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

    def update_comment(self):
        """
        更新评论
        :param:token:用户授权的token
        :param:id:评论id
        :param:content:修改的评论内容
        :return:
        """
        url = host + "/api/openitem_comment/update"
        data = {"id": "", "content": "我也喜欢这条狗子欧耶耶"}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("更新评论:", r)



















# alte().moblie_pass()
# alte().log_out()
# alte().choiceness()
# alte().attention()
# alte().my_page()
# alte().home()
# alte().refreshUser()
# alte().profile()
# alte().article_list()
# alte().user_artlist()
# alte().get_only_art()
# alte().get_pro_list()
# alte().get_goods()
# alte().get_price()
# alte().get_comment()
# alte().creat_address()
# alte().address_list()
# alte().address_del()
# alte().address_update()
# alte().address_one()
# alte().dynamic_list()
# alte().open_item()
# alte().save_categorys()
# alte().goods_list()
# alte().goods_one()
# alte().goods_search()
# alte().goods_advertise()
# alte().home_tags()
# alte().keywords()
# alte().empty()
# alte().creat_order()
# alte().update_order()
# alte().order_pay()
# alte().order_detail()
# alte().comment_list()
alte().add_comment()
alte().Ocomment()
alte().comment_delete()