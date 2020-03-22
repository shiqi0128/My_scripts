import requests

def golbal_shopid():
    """定义shop_id"""
    shop_id = 25
    return shop_id

golbal_shopid = golbal_shopid()

host = "https://qa-api-gmall.wetax.com.cn"


def get_header_pc():
    url = host + '/api/auth/login'
    data = {"username": "admin_sylvia", "password": "admin1"}
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


header, token = get_header_pc()
#
#
# def get_header_h5():
#     host = "https://qa.api.gmall.gaopeng.com"
#     # url = host + '/api/auth/login'
#     # data = {"username": "admin666", "password": "AA123456"}
#     header = {
#         "X - APP - ID": "1",
#         "Authorization": "Bearer 45ebc94ce335f3747135b65665e001b12a4500ee",
#         "Content-Type": "application/x-www-form-urlencoded application/json"
#     }
#     return host, header


# get_header_pc()

# def get_header():
#     token = get_token()
#     header = {
#         "X - APP - ID": "1",
#         "Authorization": "Bearer " + token,
#         "Content-Type": "application/json"
#     }
#     print(token)
#     return header
#
#
# get_header()