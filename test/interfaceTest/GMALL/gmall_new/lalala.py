import requests
import json
from interfaceTest.GMALL.gmall_header import host, get_header_pc
from interfaceTest.GMALL.gmall_all.color import out_format
from interfaceTest.GMALL.public_files import user_id, user_id_01
import random

header, token1 = get_header_pc("admin_sylvia", "admin1")

# def account_list():
#     """账号列表"""
#     # account_list = []
#     url = host + "/api/user?page="
#     r = requests.get(url=url, headers=header).json()
#     # s = r["data"]["users"]["data"]
#     if r["data"]["users"]["data"] is not None:
#         user_id = r["data"]["users"]["data"][-1]["id"]  # 巡查人
#         user_id_01 = r["data"]["users"]["data"][-2]["id"]   # 整改人
#         user_name = r["data"]["users"]["data"][-1]["username"]
#         # account_list.append(user_id)
#         print("获取user_id[%s]:" % user_id, "\n")
#         print("获取username[%s]:" % user_name, "\n")
#         out_format("账号列表:", r)
#         return user_id, user_id_01, user_name
#     else:
#         print("data is null")
#         out_format("账号列表:", r)
#         return None
#
#
# account_list()

# def Problem_list():
#     """问题分类--列表
#     :param:parent_id:父级id，非必填
#     """
#     url = host + "/api/company/patrol-issues"
#     r = requests.get(url=url, headers=header).json()
#     out_format("问题分类-列表:", r)
#     # problem_third_id = r["data"]["issues"][-2]["children"][0]["children"][0]["id"]
#     print("problem_third_id:", problem_third_id)
#     return problem_third_id

def Patrol_creat():
    """操作巡查记录 - 创建巡查记录
    :param:camera_id:摄像头id
    :param:issue_id:问题id，只需要填第三级问题id即可
    :param:comment:评论
    :param:corrector_uid:整改人uid
    :param:img_urls[]:图片列表，数组形式传参
    以上参数全部为必填
    """
    # problem_third_id = Problem_list()
    url = host + "/api/company/patrol-tasks"
    files = {"img_urls": ["https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1552887497680&di=532e46e352d0ef2a08854ea36cfc6e50&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F15%2F68%2F59%2F71X58PICNjx_1024.jpg"],
             "camera_id": "64",
             "issue_id": 292,
             "comment": "角落里没打扫干净",
             "corrector_uid": user_id_01,
             }

    # with open(r"F:\test\interfaceTest\baby.jpg", "rb") as f
    r_01 = requests.post(url=url, headers=header, json=files).json()
    out_format("操作巡查记录 - 创建巡查记录:", r_01)


Patrol_creat()