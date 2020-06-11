"""
-------------------------------------------------
  @Time : 2020/4/26 20:12 
  @Auth : 十七
  @File : homework_042402.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
import requests
import json
import random
from homework.homework_0424 import HandleRequest

do_request = HandleRequest()


class Future_loans:
    """定义一个前程贷的测试类"""
    @staticmethod
    def default_header():
        """默认请求头"""
        headers_dict = {
            "X-Lemonban-Media-Type": "lemonban.v2",
            "User-Agent": "Mozilla/5.0 LookSky"
            ""
        }
        base_url = "http://api.lemonban.com/futureloan"
        do_request.add_headers(headers_dict)
        return headers_dict, base_url

    def sign_in(self):
        """注册
        :param:mobile_phone:手机号
        :param:pwd:密码
        :param: type:类型，0 管理员 1 普通会员， 缺省默认为 1
        """
        # sign_in_url = f"{Future_loans.default_header()[1]}/member/register"
        sign_in_url = f"{self.default_header()[1]}/member/register"
        sign_in_params = {
            "mobile_phone": "{}".format(random.randint(18111111111, 18999999999)),
            "pwd": "12345678",
            "type": 0
        }
        res = do_request.send("post", sign_in_url, json=sign_in_params)
        res_dict = res.json()
        print("注册接口返回的响应结果:", res_dict)
        mobile_phone = res_dict["data"]["mobile_phone"]
        return mobile_phone

    def login(self):
        """登录
        :param:mobile_phone:手机号
        :param:pwd:密码
        """
        # login_url = f"{Future_loans.default_header()[1]}/member/login"
        login_url = f"{self.default_header()[1]}/member/login"
        login_params = {
            # "mobile_phone": self.sign_in(),
            "mobile_phone": "18150511517",
            "pwd": "12345678",
        }
        res = do_request.send("post", login_url, json=login_params)
        response_data_dict = res.json()
        token = response_data_dict['data']['token_info']['token']  # 获取token
        user_id = response_data_dict['data']['id']  # 获取user_id
        token_dict = {
            "Authorization": f"Bearer {token}"
        }
        do_request.add_headers(token_dict)
        print("******************************华丽丽的分割线******************************")
        print(f"登录成功后响应数据：{response_data_dict},token:{token},user_id: {user_id}")
        return token, user_id

    def recharge(self):
        """充值
        :param:member_id:会员id
        :param:amount:金额
        """
        # recharge_url = f"{Future_loans.default_header()[1]}/member/recharge"
        recharge_url = f"{self.default_header()[1]}/member/recharge"
        # 构造充值请求参数
        recharge_param = {
            "member_id": self.login()[1],
            "amount": 200000
        }
        res = do_request.send("post", recharge_url, json=recharge_param)
        response_data_dict = res.json()
        print("******************************华丽丽的分割线******************************")
        print(f"充值的响应结果：{response_data_dict}")
        member_id = response_data_dict["data"]["id"]
        return member_id

    def add_project(self):
        """新增一个项目
        :param:member_id:用户id
        :param:title:标题
        :param:amount:借款金额
        :param:loan_rate:年利率
        :param:loan_term:借款期限
        :param:loan_date_type：借款期限类型
        :param:bidding_days:竞标天数
        """
        # project_url = f"{Future_loans.default_header()[1]}/loan/add"
        project_url = f"{self.default_header()[1]}/loan/add"
        project_param = {
            "member_id": self.recharge(),
            "title": "Sylvia金融投资",
            "amount": 100000,
            "loan_rate": 10.0,
            "loan_term": 6,
            "loan_date_type": 1,
            "bidding_days": 5
        }
        res = do_request.send("post", project_url, json=project_param)
        response_data_dict = res.json()
        print("******************************华丽丽的分割线******************************")
        print(f"新增项目的响应结果：{response_data_dict}")
        loan_id = response_data_dict["data"]["id"]
        member_id = response_data_dict["data"]["member_id"]
        return loan_id, member_id

    def audit(self):
        """审核项目
        :param:loan_id:项目id
        :param:approved_or_not:审核状态
        """
        # audit_url = f"{Future_loans.default_header()[1]}/loan/audit"
        audit_url = f"{self.default_header()[1]}/loan/audit"
        audit_param = {
            "loan_id": self.add_project()[0],
            "approved_or_not": True
        }
        res = do_request.send("PATCH", audit_url, json=audit_param)
        response_data_dict = res.json()
        print("******************************华丽丽的分割线******************************")
        print(f"审核项目的响应结果：{response_data_dict}")
        return response_data_dict

    def invest(self):
        """投资
        :param:member_id:用户id
        :param:loan_id:标id
        :param:amount:投资金额
        """
        # invest_url = f"{Future_loans.default_header()[1]}/member/invest"
        invest_url = f"{self.default_header()[1]}/member/invest"
        invest_param = {
            "member_id": self.add_project()[1],
            "loan_id": 87980,           # 项目新增成功后在数据库loans表的项目id=87980的项目的status改为=2为竞标状态
            "amount": "10000.00"
        }
        res = do_request.send("post", invest_url, json=invest_param)
        response_data_dict = res.json()
        print("******************************华丽丽的分割线******************************")
        print(f"投资接口的响应结果：{response_data_dict}")
        return response_data_dict


# if __name__ == '__main__':
do_loans = Future_loans()
do_loans.sign_in()                 # 注册
# do_loans.login()                 # 登录
# do_loans.recharge()              # 充值
# do_loans.add_project()           # 新增项目
# do_loans.audit()                 # 审核项目
# do_loans.invest()                # 投资
