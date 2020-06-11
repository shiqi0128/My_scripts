"""
-------------------------------------------------
  @Time : 2020/4/25 19:59 
  @Auth : 十七
  @File : homework_0424.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
# 一、必做题
# 1.对requests请求库进行封装
# import requests
# session = requests.Session()
# 2.使用requests封装类，对注册、登录、充值、投资、加标接口发起请求
import requests


class HandleRequest:
    """对requests请求库进行封装"""

    def __init__(self):
        """创建一个会话对象"""
        self.session = requests.Session()

    def send(self, methods, url, **kwargs):
        """
        发送请求的方法
        :param url: 请求url
        :param methods: 请求方法
        :param headers: 请求头
        :param kwargs: headers请求头字典, data、json、files
        :return:
        """
        res = self.session.request(methods.upper(), url, **kwargs)
        return res

    def add_headers(self, one_dict):
        """添加公共的请求头"""
        self.session.headers.update(one_dict)

    def close(self):
        """关闭会话,释放资源"""
        self.session.close()


if __name__ == '__main__':
    # 1.创建HandleRequest对象
    do_request = HandleRequest()
    # # 2.创建登录的url
    # login_url = "http://api.lemonban.com/futureloan/member/login"
    # 3.构造请求头参数
    # headers_dict = {
    #     "X-Lemonban-Media-Type": "lemonban.v2",
    #     "User-Agent": "Mozilla/5.0 LookSky"
    # }
    # 4.在会话对象中添加进公共请求头
    # do_request.add_headers(headers_dict)
    #
    # base_url = "http://api.lemonban.com/futureloan"
    #
    # # 5.构造登录参数
    # login_param = {
    #     "mobile_phone": "18511112222",
    #     "pwd": "12345678"
    # }
    # do_request.send("post", login_url, headers=headers_dict, json=login_param)
    # res = do_request.send("POST", login_url, json=login_param)       # 6.先登录接口发起请求
    # response_data_dict = res.json()                                   # 7.获取登录接口响应体数据，转化为字典类型
    # token = response_data_dict['data']['token_info']['token']       # 获取token
    # user_id = response_data_dict['data']['id']                     # 获取user_id
    #
    # # 8.把token加载到请求头中
    # token_dict = {
    #     "Authorization": f"Bearer {token}"
    # }
    # do_request.add_headers(token_dict)


# 3.使用思维导图总结最近几次的内容
# 二、选做题
# 1.预习Python中unittest单元测试框架
# 六、session和token认证
# session会话机制：
# 在浏览器输入账号名密码，点击登录，服务器会拿到账号密码会以session会话形式保存在数据库当中，
# 返回一个session_id，然后服务器会把这个session_id字段保存响应报文的set-cookie字段中，
# 响应头会直接设置一个字段是set-cookie字段，值就是session_id。然后浏览器会将session_id存放到cookie里面。
# 浏览器发送带有sessionid cookie的请求，服务器根据sessionid判断是否过期，且用户信息正确，通过认证；返回响应信息
# 1）cookie保存在浏览器，session保存在服务器
# 2）sessionid如果过期了怎么办？如果过期了可能会重定向到登录页面，重新登录来获取新的sessionid
# 3）cookie和session离开谁都不行
# 4）利用session认证的缺点：
# a、因为都是存放在数据库里面的，所以会造成数据库的一个资源消耗
# b、如果项目是分布式，服务器在不同的地方，cookie认证机制就没法实现
# 1）token认证不会返回sessionid,登录成功后会以json格式返回给前端
# 4）当用户第一次登录后，服务器生成一个token并将此token返回给客户端，以后客户端只需带上这个token前来请求数据即可，
# 无需再次带上用户名和密码，判断token是否过期，并验证token正确性，返回响应信息sessionid,登录成功后会以json格式返回给前端
# 2）登录成功后获取到的token放到请求头当中
# 3）是服务端生成的一串字符串，作为客户端进行请求的一个标识。不会存放在服务器。浏览器接收到相应报文后，
# 会将token存放在local storage(本地存储（永久,除非手动删除存储内容))/session storage（会话存储（临时），关闭浏览器token就没了），
# token放在浏览器所有不会消耗服务器的存储空间
# json.loads()
# import json
# one_str = '{"name": "日月", "age": 17, "gender": true, "hobby": null}'
# one_dict = json.loads(one_str)  # 将json转化为dict
# json.load()
#
# json.dumps()
# json.dump()
