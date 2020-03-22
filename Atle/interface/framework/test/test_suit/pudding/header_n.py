# 此文件为小程序的头部文件
import requests

host = "http://cspudding.aiitle.com:99"   # 测试服务器
openids = "oVkEw5eAicWfJBJVTm0Y-mlpRu2E"

def get_header():
   header = {
   "Content-Type": "application/x-www-form-urlencoded application/json",
   "openid": openids   # 商家的openid
     }
   print("header:", header)
   return header


header = get_header()   # 需要调用的头部
