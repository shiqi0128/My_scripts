# 此文件为宠布丁商家的头部文件
import requests

host = "http://cspudding.aiitle.com:99"   # 测试服务器

def get_header():
   header_sale = {
   "Content-Type": "application/x-www-form-urlencoded application/json",
   "openid": "oVkEw5eAicWfJBJVTm0Y-mlpRu2E"   # 商家的openid
     }
   print("商家的头部信息header_sales:", header_sale)
   return header_sale


header_sale = get_header()   # 商家需要调用的头部赋给变量header_sale