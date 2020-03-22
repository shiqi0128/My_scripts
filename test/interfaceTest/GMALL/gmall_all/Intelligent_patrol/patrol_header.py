import requests

host = "https://qa.api.gmall.gaopeng.com"


def get_header_pc(username, password):
    url = host + '/api/auth/login'
    data = {"username": username, "password": password}
    # {"username": "admin80473", "password": "admin@123"}  # 巡查人
    # {"username": "admin_sylvia", "password": "admin1"}  # 主体账号
    # {"username": "admin38796", "password": "admin@123"}    # 整改人
    r_01 = requests.post(url=url, json=data).json()
    token = r_01["data"]["token"]
    print("token", token)
    header = {
    "X - APP - ID": "1",
    "Authorization": "Bearer " + token,
    "Content-Type": "application/x-www-form-urlencoded application/json"
    }
    print("\033[1;31m当前登录的账号%s\033[0m" % data["username"], r_01, "\n")
    return header, token