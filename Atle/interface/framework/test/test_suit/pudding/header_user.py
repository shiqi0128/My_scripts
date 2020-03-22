# 此文件为宠布丁商家的头部文件
import requests

host = "http://cspudding.aiitle.com:99"   # 测试服务器

def get_header():
   header_user = {
   "Content-Type": "application/x-www-form-urlencoded application/json",
   "openid": "oVkEw5TfRFfkGgijhmuuFpyVNN_Y"   # 用户的openid
     }
   print("header_user:", header_user)
   return header_user


header_user = get_header()   # 商家需要调用的头部赋给变量header_user