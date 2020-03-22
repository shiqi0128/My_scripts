import unittest
import requests
import os
import sys
from header import test
from time import sleep

# sys.path.insert(0, 'f:/test/interfaceTest')
# print("路径:", os.getcwd())
host, header = test()
print(sys.path)

class GetTest(unittest.TestCase):
    """定义测试场馆类"""

    def stadium_list(self):
        """定义场馆列表的方法，get方法传参"""
        params = {"page": 1, "sort": 1}
        url_01 = host + '/api/stadiums'
        r_01 = requests.get(url=url_01, headers=header, params=params).json()
        self.assertEqual(r_01['code'], 0)
        print("场馆列表:", r_01, '\n\n')
        return r_01

    def test_01_Advertising_list(self):
        """定义首页广告列表的方法，get方法不传参"""
        url_02 = host + "/api/banners"
        r_02 = requests.get(url=url_02, headers=header).json()
        self.assertEqual(r_02['code'], 0)
        print("首页广告列表:", r_02, '\n\n')

    def stadium_details(self):
        """定义场馆详情"""
        stadium_id = self.stadium_list()['data']['stadiums'][0]['id']
        # 提取场馆列表接口返回值的场馆id
        url_03 = host + '/api/stadiums/' + str(stadium_id)
        r_03 = requests.get(url=url_03, headers=header).json()
        print("场馆详情:", r_03, '\n\n')
        return r_03

    def test_02_keyword(self):
        """定义按关键词检索场馆名列表"""
        url_04 = host + '/api/stadium-names'
        r_04 = requests.get(url=url_04, headers=header).json()
        print("按关键字检索:", r_04, '\n\n')

    def product_details(self):
        """定义产品详情"""
        product_id = self.stadium_details()['data']['stadium']['products']['篮球'][0]['id']
        print("产品id:", product_id)
        '''提取场馆详情接口返回值的产品id'''
        url_05 = host + '/api/products/' + str(product_id)
        r_05 = requests.get(url=url_05, headers=header).json()
        self.assertEqual(r_05['code'], 0)
        print("产品详情:", r_05, '\n\n')
        return product_id

    def available_tickets(self):
        """获取可预约日期列表（场票）"""
        product_id_01 = self.product_details()
        url_06 = host + '/api/products/%s/dates' % product_id_01
        r_06 =requests.get(url=url_06, headers=header).json()
        self.assertEqual(r_06['code'], 0)
        print("获取可预约日期列表:", r_06, '\n\n')
        return r_06, product_id_01

    def tickets_book(self):
        """获取预订信息矩阵（场票）"""
        # self.order_details()
        b, a = self.available_tickets()
        available_date = b['data']['dates'][-1]
        '''提取可预约日期列表的日期'''
        date = {'date': available_date}
        url_07 = host + '/api/products/%s/matrix' % a
        r_07 = requests.get(url=url_07, headers=header, params=date).json()
        # self.assertEqual(r_07['code'], 0)
        print("获取预定信息矩阵:", r_07, '\n\n')
        s = len(r_07['data']['matrix']['grounds'])   # 计算grounds的长度
        # print(s)
        for s1 in range(s):
            r = len(r_07['data']['matrix']['grounds'][s1]['periods'])
            for r1 in range(r):
                w = r_07['data']['matrix']['grounds'][s1]['periods'][r1]['is_reserved']
                if w == 0:
                    ground_id = r_07['data']['matrix']['grounds'][s1]['ground_id']
                    period_id = r_07['data']['matrix']['grounds'][s1]['periods'][r1]['period_id']
                    matrix_id = r_07['data']['matrix_id']
                    print("预定成功:", "g:", ground_id, "p:", period_id, "m:", matrix_id)
                    return ground_id, period_id, a, available_date, matrix_id
            print("未找到ground_id&period_id")

    def order_list(self):
        """定义订单列表"""
        url_08 = host + '/api/stadium-orders'
        data = {"filter": 1, "page":1}
        r_08 = requests.get(url=url_08, headers=header, params=data).json()
        print("订单列表:", r_08, '\n\n')
        self.assertEqual(r_08['code'], 0)
        order_sn = r_08['data']['orders'][0]['order_sn']
        return order_sn

    def test_03_create_reservation(self):
        """创建预定单"""
        ground_id_01, period_id_01, product_id_02, date, matrix_id = self.tickets_book()
        # 调用获取预订信息矩阵（场票)接口返回的ground_id, period_id, product_id, date, matrix_id
        print(date, product_id_02)
        url_10 = host + '/api/stadium-pre-order'
        data = {'product_id': product_id_02, 'date': date, 'selected': {ground_id_01: [period_id_01]}, 'matrix_id': matrix_id}
        r_10=requests.post(url=url_10, headers=header, json=data).json()
        print("创建预定单:", r_10, '\n\n')

    def test_04_get_reservation(self):
        """获取预定单详情"""
        url_11 = host + '/api/stadium-pre-order'
        r_11 = requests.get(url=url_11, headers=header).json()
        print("获取预定单详情:", r_11, '\n\n')
        self.assertEqual(r_11['code'], 0)

    def create_order(self):
        """创建订单"""
        url_12 = host + '/api/stadium-order'
        r_12 = requests.post(url=url_12,headers=header).json()
        print("创建订单:", r_12, '\n\n')
        order_sn = r_12['data']['order_sn']
        self.assertEqual(r_12['code'], 0)
        return order_sn

    def payment_order(self):
        """订单支付"""
        order_sn_01 = self.create_order()   # 调用创建订单接口返回的order_sn
        url_13 = host + '/api/stadium-orders/%s/payment' % order_sn_01
        r_13 = requests.post(url=url_13,headers=header).json()
        print("订单支付:", r_13, '\n\n')
        payment_sn = r_13['data']['paymentInfo']['payment_sn']
        self.assertEqual(r_13['code'], 0)
        return payment_sn

    def payment_details(self):
        """模拟支付详情"""
        payment_sn_new = self.payment_order()   # 调用订单支付的接口返回的payment_sn
        url_14 = host + '/test/pay-notify'
        data = {'payment_sn': payment_sn_new}
        r_14 = requests.post(url=url_14, headers=header, json=data).json()
        print("模拟支付详情:", r_14, '\n\n')
        sleep(10)

    def order_details(self):
        """定义订单详情"""
        self.payment_details()
        order_sn_new = self.order_list()  # 调用订单列表接口返回的order_sn
        url_09 = host + '/api/stadium-orders/' + order_sn_new
        r_09 = requests.get(url=url_09, headers=header).json()
        print("订单详情:", r_09, '\n\n')
        ticket_id = r_09['data']['order']['tickets'][0]['id']  # 提取订单详情接口返回的ticket_id
        # self.assertEqual(r_09['code'], 0)
        return ticket_id

    def ticket_details(self):
        """票详情"""
        ticket_id_new = self.order_details()  # 调用订单详情接口返回的ticket_id
        url_15 = host + '/api/tickets/' + str(ticket_id_new)
        r_15 = requests.get(url=url_15, headers=header).json()
        print("票详情:", r_15, '\n\n')
        return ticket_id_new

    def test_05_reason_list(self):
        """退款理由列表"""
        url_16 = host + '/api/refund-reasons'
        r_16 = requests.get(url=url_16, headers=header).json()
        print("退款理由列表:", r_16, '\n\n')

    def get_refound(self):
        """获取退款金额"""
        ticket_id_new_01 = self.ticket_details()   # 调用票详情接口返回的ticket_id_new
        url_17 = host + '/api/tickets/%s/refund-price' % str(ticket_id_new_01)
        r_17 = requests.get(url=url_17, headers=header).json()
        print("获取退款金额:", r_17, '\n\n')
        price = r_17['data']['price']
        return ticket_id_new_01,price

    def test_06_initiate_refund(self):
        """发起退款"""
        ticket_id_new_02, price_new = self.get_refound()  # 调用获取退款金额接口返回的ticket_id_new
        url_18 = host + '/api/tickets/%s/refund' % str(ticket_id_new_02)
        data = {'phone': 15850559383, 'reason': 1, 'refund_price': price_new}
        r_18 = requests.post(url=url_18, headers=header, json=data).json()
        print("发起退款:", r_18, '\n\n')

    def test_07_coupons_01(self):
        """用户优惠券列表"""
        url_19 = host + '/api/coupons'
        data = {'filter': 1, 'page': 1}
        r_19 = requests.get(url=url_19, headers=header, params=data).json()
        print("用户优惠券列表:", r_19, '\n\n')

    def test_08_coupons_02(self):
        """订单可用优惠券列表"""
        url_20 = host + '/api/coupons/available'
        r_20 = requests.get(url=url_20, headers=header).json()
        print("订单可用优惠券列表:", r_20, '\n\n')
        self.assertEqual(r_20['code'], 0)


if __name__ == '__main__':
    unittest.main()
else:
    print("false")


