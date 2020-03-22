# 此文件为宠布丁小程序V3.0的商家身份登录接口脚本基础代码
import requests
import random
import json
from Atle.interface.framework.test.test_suit.pudding.header_n import host, header
# from Atle.interface.framework.test.test_suit.pudding.pudding_first.public_applet import address_id, category_id, shop_id, order_no, goods_id, sku_id
from Atle.interface.framework.common.color import out_format

class Third_pudding():
    """定义一个宠布丁3.0的测试类"""
    def accountlevel(self):
        """等级列表"""
        url = host + "/api/account/level"
        r = requests.post(url=url).json()
        out_format("等级列表:", r)

    def goodsThursday(self, shop_id=1005):
        """超级星期四
        :param:openid:用户授权openid
        :param:shop_id:店铺id
        :param:size:单页记录数 (不传默认：10)
        :param:page:页码 (不传默认：1)
        """
        # 此接口 参数传空 不报错，不传data也可以运行成功
        url = host + "/api/goods/thursday"
        # data = {"shop_id": "", "size": "", "page": ""}
        r = requests.post(url=url, headers=header).json()
        out_format("超级星期四:", r)

    def IndexEventsetting(self):
        """活动页面设置
        :param:code:活动拼音小写,允许值: chaojixingqisi或dahuopin
        """
        url = host + "/api/index/event_setting"
        data = {"code": "chaojixingqisi"}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("活动页面设置:", r)

    def postIndex(self):
        """文章列表
        :param:size:单页记录数 (不传默认：10)
        :param:page:页码 (不传默认：1)
        """
        url = host + "/api/post/index"
        r = requests.get(url=url).json()
        out_format("文章列表:", r)

    def postGet(self):
        """文章详情
        :param:id:文章ID
        """
        url = host + "/api/post/get"
        data = {"id": 7}       # 不传参数提示参数不合法，开发设计如此
        r = requests.get(url=url,params=data).json()
        out_format("文章详情:", r)

    def shopModifyTitle(self):
        """修改标题
        :param:openid:用户授权openid
        :param:title:新店铺名称
        """
        url = host + "/api/shop/modify_title"
        data = {"title": "萌宠乐园%s" % random.randrange(1, 1000)}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("修改标题:", r)

    def ShopBindUserIndex(self):
        """获取绑定用户
        :param:openid:用户授权openid
        :param:page:页数,默认值: 1 (不传默认1)
        :param:size:单页数量，默认值10 （不传默认10）
        """
        url = host + "/api/Shopbinduser/index"
        r = requests.get(url=url, headers=header).json()
        out_format("获取绑定用户:", r)

    def spellList(self):
        """拼单商品列表
        :param:openid:用户授权openid
        :param:page:页数,默认值: 1       ---非必填(不填的情况是上传默认值)
        :param:size:单页数量，默认值10   ---非必填（不填的情况是上传默认值）
        """
        url = host + "/api/spell/list"
        r = requests.post(url=url, headers=header).json()
        out_format("拼单商品列表:", r)

    def taskSpec(self):
        """任务规格
        :param:openid:用户授权openid
        """
        url = host + "/api/task/spec"
        r = requests.post(url=url, headers=header).json()
        out_format("任务规格:", r)

    def taskInvite(self):
        """好友邀请返回
        :param:openid:用户授权openid
        :param:openid:发起人openid
        :param:in_openid:被邀请者openid
        """
        url = host + "/api/task/invite"
        data = {"openid": "oVkEw5YCc-IYvCPekF8xm64aZ7aw", "in_openid": "oVkEw5YCc-IYvCPekF8xm64aZ7aw"}
        r = requests.post(url=url, headers=header, data=data).json()
        out_format("好友申请返回:", r)

    def taskToast(self):
        """我的通知
        :param:openid:用户授权openid
        """
        url = host + "/api/task/toast"
        r = requests.post(url=url, headers=header).json()
        out_format("我的通知:", r)

    def taskUsers(self):
        """我邀请的好友列表
        :param:openid:用户授权openid
        """
        url = host + "/api/task/users"
        r = requests.post(url=url, headers=header).json()
        out_format("我邀请的好友列表:", r)

    def taskDelete_toast(self):
        """收下/删除通知
        :param:openid:用户授权openid
        """
        url = host + "/api/task/delete_toast"
        r = requests.post(url=url, headers=header).json()
        out_format("收下/删除通知:", r)

    def discountOpen_gift(self):
        """打开新人礼包
        :param:openid:用户授权openid
        """
        url = host + "/api/discount/open_gift"
        r = requests.post(url=url, headers=header).json()
        out_format("打开新人礼包:", r)
        return r

    def discountHasReceiveNewUserCoupon(self):
        """是否领取了新人券
        :param:openid:用户授权openid
        """
        url = host + "/api/discount/has_receive_new_user_coupon"
        r = requests.post(url=url, headers=header).json()
        out_format("是否领取了新人券:", r)
        if r["code"] == 0:
            self.discountOpen_gift()
        else:
            print("\033[1;34m没有领取新人券\033[0m")


# Third_pudding().accountlevel()          # 等级列表
# Third_pudding().goodsThursday()         # 超级星期四
# Third_pudding().IndexEventsetting()     # 活动页面设置
# Third_pudding().postIndex()             # 文章列表
# Third_pudding().postGet()               # 文章详情
# Third_pudding().shopModifyTitle()       # 修改标题
# Third_pudding().ShopBindUserIndex()       # 获取绑定用户
# Third_pudding().spellList()                  # 拼单商品列表
# Third_pudding().taskSpec()                    # 任务规格
# Third_pudding().taskInvite()                  # 好友邀请返回
# Third_pudding().taskToast()                            # 我的通知
# Third_pudding().taskUsers()                            # 我邀请的好友列表
# Third_pudding().taskDelete_toast()                     # 收下/删除通知
# Third_pudding().discountOpen_gift()                      # 打开新人礼包
# Third_pudding().discountHasReceiveNewUserCoupon()        # 是否领取了新人券
