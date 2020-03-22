#——————————此文件为头部调用文件————————
import requests

# host = "http://dev.aiitle.com:10085"   # 开发服务器
host = "http://csapp.aiitle.com:88"   # 测试服务器


def login():
    url = host + '/api/user/login'
    data = {"mobile": "18717752237", "password": "121212"}
    print(url)
    r_01 = requests.post(url=url, data=data).json()
    print("r_01:", r_01)
    token = r_01["data"]["userinfo"]["token"]
    uid = r_01["data"]["userinfo"]["id"]
    print("token:", token)
    return token, uid


def get_header():
    # token = login()[0]
    # uid = login()[1]   # 3.1需要用到uid，3.0版本不需要用到
    token, uid = login()
    header = {
        "Content-Type": "application/x-www-form-urlencoded application/json",
        "token": token
        # "uid": uid
    }
    # print("\033[1;31m当前登录的账号%s\033[0m" % data["username"], r_01, "\n")
    print("header:", header)
    return header


# get_header()
# order_list()
header = get_header()
