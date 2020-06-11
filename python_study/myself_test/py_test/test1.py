"""
-------------------------------------------------
  @Time : 2020/4/15 16:40 
  @Auth : 十七
  @File : test1.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
# 1)任给一个数组,其中只有一个元素是单独出现，其他是成对出现，输出单独的元素。
# 例如：输入{2,2,1,1,4,4,7}
# 输出：7

# a = [2, 2, 1, 1, 4, 4, 7]
# a.count(7)


# 任给一个数组，元素有20M，1T，300G之类的，其中1T=1000G，1G=1000M
# 按从小到大输出结果
# 例如：输入：3
# 20M
# 1T
# 300G
# 输出：
# 20M
# 300G
# 1T


# def turnString(str):
# 	length = len(str)
# 	if(str[length-1]=='M'):
# 		return int(str[0:length-1])
# 	if(str[length-1]=='T'):
# 		return int(str[0:length-1])*1000000
# 	if(str[length-1]=='G'):
# 		return int(str[0:length-1])*1000
# 	#return 0
# def compare(str1,str2):
# 	strM1 = turnString(str1)
# 	strM2 = turnString(str2)
# 	return strM1-strM2
# def sort(list):
# 	length = len(list)
# 	for i,value in enumerate(list):
# 		for j,value1 in enumerate(list[0:length-i-1]):
# 			if(compare(list[j],list[j+1])>0):
# 				list[j],list[j+1] = list[j+1],list[j]
# 	return list
#
# if __name__ == '__main__':
# 	#x = input("请输入以M\T\G为单位的数值，并使用，分割，回车键结束")
# 	#list = x.split(",")
# 	list = ['20M','3T','1T','300G']
# 	slist = sort(list)
# 	print(slist)


# dict = {'Name': 'Runoob', 'Age': 7}
# dict2 = {'Sex': 'female'}
# dict2.update(dict)
# import requests
#
#
# def unregistered_mobile():
#     register_url = "http://api.lemonban.com/futureloan/member/login"
#     headers_dict = {
#         "X-Lemonban-Media-Type": "lemonban.v2",
#         "User-Agent": "Mozilla/5.0 LookSky"
#     }
#
#     request_param = {
#         "pwd": "12345678",
#         "type": 0
#     }
#     # 4、发起请求
#     res = requests.post(register_url, headers=headers_dict, json=request_param).json()
#     print(res)
#
#
# unregistered_mobile()


# i = 2
# list = [i]
# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         list.append(i)
#     elif i % 2 != 0:
#         list.append(-i)
# print(list)
# print(sum(list))

    # #从2开始计算
    # i = 2
    # #定义一个变量用于保存结果
    # sum=0
    # while i <= 100:
    #     if i % 2 == 0:
    #         sum = sum + i
    #     else:
    #         sum = sum - i
    #     i += 1
    # print("2-3+4-5+6...+100=",sum)

# while True:
#     try:
#         score=float(input('请输入考试成绩：'))
#         if score>=90:
#             print('A')
#         elif 80<=score<90:
#             print('B')
#         elif 70<=score<80:
#             print('C')
#         elif 60<=score<70:
#             print('D')
#         else:
#             print('E')
#     except Exception as e:
#         print('您输入有误！')
#         break

# principal = 10000
# year = 0
# while principal < 20000:
#     principal = principal * 1.0325
#     year = year + 1
# print('需要%d年一万元的存款才能连本带息翻番' % year)
# print(str(year)+'年以后，一万元的存款才能连本带息翻番')  # 顺便复习str()

# year = 0
# save_money = float(input("请输入你要存入银行的钱："))
# print(f"你存了{save_money}元到银行")
# total_money = save_money * 2
# while save_money < total_money:
#     save_money *= (1 + 3.52%)
#     year += 1
# print(f"{year}年后存款连本带息才能翻番！")

# cases = [
#     ['case_id', 'case_title', 'url', 'data', 'excepted'],
#     [1, '用例1', 'www.baidu.com', '001', 'ok'],
#     [4, '用例4', 'www.baidu.com', '002', 'ok'],
#     [2, '用例2', 'www.baidu.com', '002', 'ok'],
#     [3, '用例3', 'www.baidu.com', '002', 'ok'],
#     [5, '用例5', 'www.baidu.com', '002', 'ok']
# ]
#
# res1 = []
# key = cases[0]
# # 通过切片遍历cases所有的value
# for value in cases[1:]:
#     # print(value)
#     # 将遍历的value和key进行聚合打包，并转换为字典
#     dict_res = dict(zip(key, value))
#     res1.append(dict_res)
# print(f'转换后的格式：\nres1={res1}')

# def func(cases):
#     """
#     数据格式转换
#     """
#     res1 = []
#     key = cases[0]
#     # 通过切片遍历cases所有的value
#     for value in cases[1:]:
#         # print(value)
#         # 将遍历的value和key进行聚合打包，并转换为字典
#         dict_res = dict(zip(key, value))
#         res1.append(dict_res)
#     print(f'转换后的格式：\nres1={res1}')
#
#
# func(cases)

    #将case_id大于3的用例数据获取出来
res1 = [
    {'case_id': 1, 'case_title': '用例1', 'url': 'www.baidu.com', 'data': '001', 'excepted': 'ok'},
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baidu.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 2, 'case_title': '用例2', 'url': 'www.baidu.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 3, 'case_title': '用例3', 'url': 'www.baidu.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baidu.com', 'data': '002', 'excepted': 'ok'}
]

res2 = []
for i in res1:
    if i['case_id'] > 3:
        res2.append(i)
print(f"case_id大于3：\nres={res2}")
# res1=func(cases)