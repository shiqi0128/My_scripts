import os
import requests
import json
import sys

# host地址
host = "https://qa.api.stadium.wetax.com.cn"

# 请求头
header = {
        "X-APP-ID": "1",
        "Authorization": "Bearer 0c04f7f32fddcd9bb2ba7ad6637aa531ecad8824", 
        "Content-Type": "application/json"
        }

sys.path.insert(0, 'f:/test/interfaceTest')
print("路径:", os.getcwd())

# 首页场馆列表接口 get请求的参数
url_01 = host + '/api/stadiums'
a = {"page": 1, "sort": 1}
stadium_list = requests.get(url=url_01, headers=header, params=a).json()
print("首页场馆列表:", stadium_list, "\n\n\n")


# 首页广告列表接口
url_02 = host + '/api/banners'
Advertising_list = requests.get(url=url_02, headers=header)
print("首页广告列表:", Advertising_list, "\n\n\n")


# 场馆详情接口
stadium_id = stadium_list['data']['stadiums'][0]['id']     # 提取场馆列表接口返回值的场馆id
url_03 = host + '/api/stadiums/' + str(stadium_id)
stadium_details = requests.get(url=url_03, headers=header).json()
print("场馆详情:", stadium_details, "\n\n\n")

# 按关键词检索场馆名列表
url_04 = host + '/api/stadium-names'
keyword = requests.get(url=url_04, headers=header).json()
print("关键字检索场馆列表:", keyword, "\n\n")

# 产品详情
product_id = stadium_details['data']['stadium']['products']['篮球'][0]['id']   # 提取场馆详情接口返回值的产品id
url_05 = host + '/api/products/' + str(product_id)
product_details = requests.get(url=url_05, headers=header).json()
print("产品详情:", product_details, '\n\n')

# 获取可预约日期列表（场票）
url_06 = host + '/api/products/%s/dates' % (str(product_id))
# url_07 = host + '/api/products/{0}/dates'.format(str(d))
available_tickets = requests.get(url=url_06, headers=header).json()
print("获取可预约日期列表:", available_tickets, '\n\n')

# 获取预订信息矩阵（场票）
product_id_01 = product_details['data']['product']['id']  # 提取产品详情接口返回值的产品id
available_date = available_tickets['data']['dates'][3]    # 提取可预约日期列表的date日期
date = {"date": available_date}                           # 给要传的date参数附给一个变量
url_07 = host + '/api/products/%s/matrix' % (product_id_01)
print(available_date, url_07)
tickets_book = requests.get(url=url_07, headers=header, params=date).json()
print("获取预定信息矩阵:", tickets_book, "\n\n")
s = len(tickets_book['data']['matrix']['grounds'])
print(s)
for ground in range(0, s):
        ground_id = tickets_book['data']['matrix']['grounds'][ground]['ground_id']   # 提取该接口下的ground_id
        for period in range(25, 0, -1):
                is_reserved = tickets_book['data']['matrix']['grounds'][ground]['periods'][period]['is_reserved']
                if is_reserved == 0:
                        print("预定成功")
                        period_id = tickets_book['data']['matrix']['grounds'][ground]['periods'][period]['period_id']     # 提取该接口下的period_id
                        print("period_id: ", period_id)
                        break
else:
        print("不能预定")
matrix_id = tickets_book['data']['matrix_id']    # 提取该接口下的matrix_id
# a = True
# for ground in range(0, 10):
#         ground_id = tickets_book['data']['matrix']['grounds'][ground]['ground_id']   # 提取该接口下的ground_id
#         if a:
#                 for period in range(25, 0, -1):
#                         is_reserved = tickets_book['data']['matrix']['grounds'][ground]['periods'][period]['is_reserved']
#                         if is_reserved == 0:
#                                 print("预定成功")
#                                 period_id = tickets_book['data']['matrix']['grounds'][ground]['periods'][period]['period_id']     # 提取该接口下的period_id
#                                 print("period_id: ", period_id)
#                                 a = False
#                                 break
# else:
#         print("不能预定")
# matrix_id = tickets_book['data']['matrix_id']    # 提取该接口下的matrix_id
 
# 订单列表
url_08 = host + '/api/stadium-orders'
pf = {"page": 1, "filter": 1}
order_list = requests.get(url=url_08, headers=header, params=pf).json()
print("订单列表:", order_list, "\n\n")

# 创建预定单[场票]
url_10 = host + '/api/stadium-pre-order'
data_01 = {"product_id": product_id_01, "date": available_date, "selected": {ground_id: [period_id]}, "matrix_id": matrix_id}
print('data_01:', data_01)
create_reservation = requests.post(url=url_10, headers=header, json=data_01).json()
print("创建预定单:", create_reservation, "\n\n")

# 获取预订单详情
url_11 = host + '/api/stadium-pre-order'
get_reservation = requests.get(url=url_11, headers=header).json()
print("获取预定单详情:", get_reservation, "\n\n")

# 创建订单
url_12 = host + '/api/stadium-order'
create_order = requests.post(url=url_12, headers=header).json()
print("创建订单:", create_order, "\n\n")
order_sn_01 = create_order['data']['order_sn']       # 提取创建订单后成功后的order_sn

# 订单支付
url_13 = host + '/api/stadium-orders/%s/payment' % (order_sn_01)
payment_order = requests.post(url=url_13, headers=header).json()
print("订单支付:", payment_order, '\n\n')
payment_sn = payment_order['data']['paymentInfo']['payment_sn']    # 提取订单支付后的payment_sn

# 模拟支付出票
url_14 = host + '/test/pay-notify'
data_02 = {'payment_sn': payment_sn}
payfor = requests.post(url=url_14, headers=header, json=data_02).json()
print("模拟支付出票:", payfor, '\n\n')

# 订单详情
order_sn = order_list['data']['orders'][0]['order_sn']     # 提取订单列表返回值的order_sn
url_09 = host + '/api/stadium-orders/' + order_sn
order_details = requests.get(url=url_09, headers=header).json()
print("订单详情:", order_details, "\n\n")
ticket_id = order_details['data']['order']['tickets'][0]['id']     # 提取订单详情接口返回的ticket_id
print("票id:", ticket_id)

# 票详情
url_15 = host + '/api/tickets/' + str(ticket_id)
ticket_details = requests.get(url=url_15, headers=header).json()
print("票详情:", ticket_details, '\n\n')

# 退款理由列表
url_16 = host + '/api/refund-reasons'
reason_list = requests.get(url=url_16, headers=header).json()
print("退款理由列表:", reason_list, '\n\n')

# 获取退款金额
url_17 = host + '/api/tickets/%s/refund-price' % (ticket_id)
get_refound = requests.get(url=url_17, headers=header).json()
print("获取退款金额:", get_refound, '\n\n')


# 发起退款
url_18 = host + '/api/tickets/%s/refund' % (ticket_id)
'''
r = reason_list['data']['reasons']
for i in r:
        print(i)
'''
param1 = {'phone': 15607656789, 'reason': 1, 'refund_price': get_refound['data']['price']}
# files = {'img_urls[]': open(r'C:\Users\gp002\Pictures\baby2.jpg', 'rb')}
initiate_refund = requests.post(url=url_18, headers=header, json=param1).json()
print("发起退款:", initiate_refund, '\n\n')

# 用户优惠券列表
url_19 = host + '/api/coupons'
parmam2 = {'filter': 1, 'page': 1}
coupons = requests.get(url=url_19, headers=header, params=parmam2).json()
print("用户优惠券列表:", coupons, '\n\n')

# 订单可用优惠券列表
url_20 = host + '/api/coupons/available'
coupons_01 = requests.get(url=url_20, headers=header).json()
print("订单可用优惠券列表:", coupons_01, '\n\n')