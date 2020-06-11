"""
-------------------------------------------------
  @Time : 2020/4/23 17:49 
  @Auth : 十七
  @File : homework_0422.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
# 一、必做题
# 1.json格式的数据有哪几种类型？
# 1)字符串形式
# 2)文件
# 3)字节类型（较少）
# 2.json与python中的字典和列表有什么区别？
# 1)json的格式要求必须且只能使用双引号作为key或者值的边界符号，不能使用单引号;
#   字典使用单引号
# 2)python字典里可以嵌套tuple,list;
#   json里只有array数组
# 3）json: true false null
#   python:True False None
# 4）Python中字典的键可以是字符串，元组，数字，但是不能是列表；
#   json的key必须是字符串,value 可以是合法的JSON数据类型（字符串, 数字, 对象, 数组, 布尔值或 null）
# 5）可以互相转换
# json.dumps()转换成json格式字符串；json.loads()把json字符串转换成字典



# 3.使用Python来处理json格式的数据（loads和load区别、dumps和dump区别）
# 提示：
# 	a.需提交案例演练代码
# import json
# one_str = '{"name": "日月", "age": 17, "gender": true, "hobby": null}'
# one_dict = json.loads(one_str)  # 将json转化为dict
# two_str = '[{"name": "日月", "age": 17, "gender": true, "hobby": null}, {"name": "船长", "age": 18, "gender": false, "hobby": ["跑步", "敲打码"]}]'
# # 转化为字典、列表
# one_dict = json.loads(one_str)
# two_list = json.loads(two_str)
# print(f"转化后的one_str类型为{type(one_dict)}\n转化后的two_str类型为{type(two_list)}")

# load
# import json
# with open("user.json", encoding="utf-8") as file:
#     one_dict = json.load(file)
#     pass

# import json
#
# one_dict = {
#     'name': "小明",
#     "age": 18,
#     17: True,
#     None: 1.3
# }
#
# with open("users_write.json", mode="w",encoding="utf-8") as file:
#     json_str = json.dump(one_dict, file, ensure_ascii=False, indent=2)

# 二、选做题
# 1.预习Python中的requests请求库的相关操作
# a.尝试发起post请求
# 英文文档：https://2.python-requests.org/en/master/
# 中文文档：https://2.python-requests.org/zh_CN/latest/
# import json
# import requests
# url = "http://api.lemonban.com/futureloan/member/login"
# # 请求头参数json
# header_data = {
#     "X-Lemonban-Media-Type": "lemonban.v2",
#     "Content-Type": "application/json"
# }
# # 请求体参数json格式
# data = {
#         "mobile_phone": "18717752223",
#         "pwd": "12345678"
# }
# r = requests.post(url=url, headers=header_data, json=data)  # 关键字参数json传参data
# print(r)
# pass
A = "C"*5
B = "C"*5*2
A1 = 10/2
print(str(A1))


