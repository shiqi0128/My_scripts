import json

import requests


class HandleRequest:

    def __init__(self):
        # 创建会话对象
        self.session = requests.Session()

    def send(self, method, url, **kwargs):
        """
        发送请求的方法
        :param method: 请求方法
        :param url: 请求url
        :param kwargs: headers请求头字典, data、json、files
        :return:
        """

        # if method == "POST":
        #     self.session.post()
        # elif method == "GET":
        #     self.session.get()
        # else:
        #     pass

        one_method = method.upper()

        """
        if "json" in kwargs:
            json_data = kwargs.get("json")
            if isinstance(json_data, str):
                try:
                    json_data = json.loads(json_data)
                except Exception:
                    json_data = eval(json_data)
                
                kwargs["json"] = json_data

        if "data" in kwargs:
            form_data = kwargs.get("data")
            if isinstance(form_data, str):
                try:
                    form_data = json.loads(form_data)
                except Exception:
                    form_data = eval(form_data)

                kwargs["data"] = form_data
        """
        kwargs["json"] = self.handle_param("json", kwargs)
        kwargs["data"] = self.handle_param("data", kwargs)

        return self.session.request(one_method, url, **kwargs)

    @staticmethod
    def handle_param(param_name, param_dict):

        if param_name in param_dict:
            data = param_dict.get(param_name)
            if isinstance(data, str):
                try:
                    data = json.loads(data)
                except Exception:
                    data = eval(data)

            return data
        # else:
        #     return None

    def add_headers(self, one_dict):
        """
        添加公共的请求头
        :param one_dict: 请求头参数，字典类型
        :return:
        """
        self.session.headers.update(one_dict)
        # self.session.headers = one_dict

    def close(self):
        """
        释放资源
        :return:
        """
        self.session.close()


if __name__ == '__main__':
    # 1.创建HandleRequest对象
    do_request = HandleRequest()
    # 2.创建登录url
    login_url = "http://api.lemonban.com/futureloan/member/login"

    # 3.构造请求头参数
    headers_dict = {
        "X-Lemonban-Media-Type": "lemonban.v2",
        "User-Agent": "Mozilla/5.0 LookSky"
    }
    # 4.在会话对象中添加请求头
    do_request.add_headers(headers_dict)

    # 5.构造登录参数
    # login_param = {
    #     "mobile_phone": "18511112222",
    #     "pwd": "12345678"
    # }

    login_param = '{"mobile_phone": "18522233479", "pwd": "12345678"}'

    # 6.先登录接口发起请求
    # res = do_request.send("POST", login_url, headers=headers_dict, json=login_param)
    res = do_request.send("POST", login_url, json=login_param)

    # 7.获取登录接口响应体数据，转化为字典类型
    response_data_dict = res.json()
    # 获取token
    token = response_data_dict['data']['token_info']['token']
    # 获取user_id
    user_id = response_data_dict['data']['id']
    pass
