"""调试gmall2.2.2脚本"""
# a = {
# 	'code': 0,
# 	'message': 'index',
# 	'data': {
# 		'screenshots': {
# 			'current_page': 1,
# 			'data': [{
# 				'id': 8,
# 				'flow_sn': '190107163300112',
# 				'shop_id': 25,
# 				'zone_id': 50,
# 				'camera_id': 64,
# 				'uid': 2272,
# 				'img_url': 'https://ai-gmall-qa-1251506165.cos.ap-shanghai.myqcloud.com/camera-screenshot/sylvia_入口_190107163300112.jpg',
# 				'remark': '钱钱钱',
# 				'screen_at': '0000-00-00 00:00:00',
# 				'created_at': '2019-01-07 16:34:02',
# 				'updated_at': '2019-01-08 10:34:52',
# 				'zone': {
# 					'id': 50,
# 					'name': 'sylvia_入口',
# 					'type_name': '未知区',
# 					'footprints_hash': 'c0c7c76d30bd3dcaefc96f40275bdc0a'
# 				},
# 				'camera': {
# 					'id': 64,
# 					'name': '入口'
# 				}
# 			}, {
# 				'id': 9,
# 				'flow_sn': '190107163400122',
# 				'shop_id': 25,
# 				'zone_id': 50,
# 				'camera_id': 64,
# 				'uid': 2272,
# 				'img_url': 'https://ai-gmall-qa-1251506165.cos.ap-shanghai.myqcloud.com/camera-screenshot/sylvia_入口_190107163400122.jpg',
# 				'remark': '',
# 				'screen_at': '0000-00-00 00:00:00',
# 				'created_at': '2019-01-07 16:34:06',
# 				'updated_at': '2019-01-07 16:34:06',
# 				'zone': {
# 					'id': 50,
# 					'name': 'sylvia_入口',
# 					'type_name': '未知区',
# 					'footprints_hash': 'c0c7c76d30bd3dcaefc96f40275bdc0a'
# 				},
# 				'camera': {
# 					'id': 64,
# 					'name': '入口'
# 				}
# 			}, {
# 				'id': 10,
# 				'flow_sn': '190107163400132',
# 				'shop_id': 25,
# 				'zone_id': 50,
# 				'camera_id': 64,
# 				'uid': 2272,
# 				'img_url': 'https://ai-gmall-qa-1251506165.cos.ap-shanghai.myqcloud.com/camera-screenshot/sylvia_入口_190107163400132.jpg',
# 				'remark': '',
# 				'screen_at': '0000-00-00 00:00:00',
# 				'created_at': '2019-01-07 16:34:30',
# 				'updated_at': '2019-01-07 16:34:30',
# 				'zone': {
# 					'id': 50,
# 					'name': 'sylvia_入口',
# 					'type_name': '未知区',
# 					'footprints_hash': 'c0c7c76d30bd3dcaefc96f40275bdc0a'
# 				},
# 				'camera': {
# 					'id': 64,
# 					'name': '入口'
# 				}
# 			}, {
# 				'id': 11,
# 				'flow_sn': '190107164200142',
# 				'shop_id': 25,
# 				'zone_id': 50,
# 				'camera_id': 64,
# 				'uid': 2272,
# 				'img_url': 'https://ai-gmall-qa-1251506165.cos.ap-shanghai.myqcloud.com/camera-screenshot/sylvia_入口_190107164200142.jpg',
# 				'remark': '垃圾没打扫干净',
# 				'screen_at': '0000-00-00 00:00:00',
# 				'created_at': '2019-01-07 16:42:48',
# 				'updated_at': '2019-01-07 17:51:08',
# 				'zone': {
# 					'id': 50,
# 					'name': 'sylvia_入口',
# 					'type_name': '未知区',
# 					'footprints_hash': 'c0c7c76d30bd3dcaefc96f40275bdc0a'
# 				},
# 				'camera': {
# 					'id': 64,
# 					'name': '入口'
# 				}
# 			}, {
# 				'id': 151,
# 				'flow_sn': '190107180701542',
# 				'shop_id': 25,
# 				'zone_id': 50,
# 				'camera_id': 64,
# 				'uid': 2272,
# 				'img_url': 'https://ai-gmall-qa-1251506165.cos.ap-shanghai.myqcloud.com/camera-screenshot/入口_190107180701542.jpg',
# 				'remark': '',
# 				'screen_at': '0000-00-00 00:00:00',
# 				'created_at': '2019-01-07 18:07:46',
# 				'updated_at': '2019-01-07 18:07:46',
# 				'zone': {
# 					'id': 50,
# 					'name': 'sylvia_入口',
# 					'type_name': '未知区',
# 					'footprints_hash': 'c0c7c76d30bd3dcaefc96f40275bdc0a'
# 				},
# 				'camera': {
# 					'id': 64,
# 					'name': '入口'
# 				}
# 			}, {
# 				'id': 154,
# 				'flow_sn': '190107194701572',
# 				'shop_id': 25,
# 				'zone_id': 51,
# 				'camera_id': 65,
# 				'uid': 2272,
# 				'img_url': 'https://ai-gmall-qa-1251506165.cos.ap-shanghai.myqcloud.com/camera-screenshot/男装区_190107194701572.jpg',
# 				'remark': '',
# 				'screen_at': '0000-00-00 00:00:00',
# 				'created_at': '2019-01-07 19:48:05',
# 				'updated_at': '2019-01-07 19:48:05',
# 				'zone': {
# 					'id': 51,
# 					'name': 'sylvia_男装区',
# 					'type_name': '未知区',
# 					'footprints_hash': '2838023a778dfaecdc212708f721b788'
# 				},
# 				'camera': {
# 					'id': 65,
# 					'name': '男装区'
# 				}
# 			}, {
# 				'id': 155,
# 				'flow_sn': '190107194801582',
# 				'shop_id': 25,
# 				'zone_id': 52,
# 				'camera_id': 66,
# 				'uid': 2272,
# 				'img_url': 'https://ai-gmall-qa-1251506165.cos.ap-shanghai.myqcloud.com/camera-screenshot/女装区_190107194801582.jpg',
# 				'remark': '',
# 				'screen_at': '0000-00-00 00:00:00',
# 				'created_at': '2019-01-07 19:48:25',
# 				'updated_at': '2019-01-07 19:48:25',
# 				'zone': {
# 					'id': 52,
# 					'name': 'sylvia_女装区',
# 					'type_name': '未知区',
# 					'footprints_hash': '9a1158154dfa42caddbd0694a4e9bdc8'
# 				},
# 				'camera': {
# 					'id': 66,
# 					'name': '女装区'
# 				}
# 			}, {
# 				'id': 156,
# 				'flow_sn': '190107195201592',
# 				'shop_id': 25,
# 				'zone_id': 54,
# 				'camera_id': 68,
# 				'uid': 2272,
# 				'img_url': 'https://ai-gmall-qa-1251506165.cos.ap-shanghai.myqcloud.com/camera-screenshot/收银区_190107195201592.jpg',
# 				'remark': '',
# 				'screen_at': '0000-00-00 00:00:00',
# 				'created_at': '2019-01-07 19:53:03',
# 				'updated_at': '2019-01-07 19:53:03',
# 				'zone': {
# 					'id': 54,
# 					'name': 'sylvia_收银区',
# 					'type_name': '未知区',
# 					'footprints_hash': 'a684eceee76fc522773286a895bc8436'
# 				},
# 				'camera': {
# 					'id': 68,
# 					'name': '收银区'
# 				}
# 			}, {
# 				'id': 165,
# 				'flow_sn': '190108114601682',
# 				'shop_id': 25,
# 				'zone_id': 50,
# 				'camera_id': 64,
# 				'uid': 2272,
# 				'img_url': 'https://ai-gmall-qa-1251506165.cos.ap-shanghai.myqcloud.com/camera-screenshot/入口_190108114601682.jpg',
# 				'remark': '',
# 				'screen_at': '0000-00-00 00:00:00',
# 				'created_at': '2019-01-08 11:46:51',
# 				'updated_at': '2019-01-08 11:46:51',
# 				'zone': {
# 					'id': 50,
# 					'name': 'sylvia_入口',
# 					'type_name': '未知区',
# 					'footprints_hash': 'c0c7c76d30bd3dcaefc96f40275bdc0a'
# 				},
# 				'camera': {
# 					'id': 64,
# 					'name': '入口'
# 				}
# 			}, {
# 				'id': 171,
# 				'flow_sn': '190108152801742',
# 				'shop_id': 25,
# 				'zone_id': 50,
# 				'camera_id': 64,
# 				'uid': 2272,
# 				'img_url': 'https://ai-gmall-qa-1251506165.cos.ap-shanghai.myqcloud.com/camera-screenshot/入口_190108152801742.jpg',
# 				'remark': '',
# 				'screen_at': '0000-00-00 00:00:00',
# 				'created_at': '2019-01-08 15:28:40',
# 				'updated_at': '2019-01-08 15:28:40',
# 				'zone': {
# 					'id': 50,
# 					'name': 'sylvia_入口',
# 					'type_name': '未知区',
# 					'footprints_hash': 'c0c7c76d30bd3dcaefc96f40275bdc0a'
# 				},
# 				'camera': {
# 					'id': 64,
# 					'name': '入口'
# 				}
# 			}],
# 			'first_page_url': 'https://qa.api.gmall.gaopeng.com/api/shops/25/screenshots?page=1',
# 			'from': 1,
# 			'last_page': 3,
# 			'last_page_url': 'https://qa.api.gmall.gaopeng.com/api/shops/25/screenshots?page=3',
# 			'next_page_url': 'https://qa.api.gmall.gaopeng.com/api/shops/25/screenshots?page=2',
# 			'path': 'https://qa.api.gmall.gaopeng.com/api/shops/25/screenshots',
# 			'per_page': 10,
# 			'prev_page_url': None,
# 			'to': 10,
# 			'total': 24
# 		}
# 	},
# 	'elapsed': 0.116
# }
# print(a["data"]["screenshots"]["data"][0]["id"])

"""调试gmall2.2.3脚本"""
# b = {
# 	'code': 0,
# 	'message': 'rfData',
# 	'data': {
# 		'code': 'success',
# 		'list': [{
# 			'shop_id': 25,
# 			'rf_name': 'R≤30天',
# 			'f1': '1',
# 			'f2': '0',
# 			'f3': '0',
# 			'f4': '0',
# 			'f5': '0',
# 			'row_total': '1',
# 			'data_type': 'customer_number',
# 			'stats_date': '2018-12-20',
# 			'created_at': '2019-01-17 19:38:52',
# 			'updated_at': '2019-01-17 19:38:52',
# 			'sort': 1,
# 			'f1_ratio': '100.00%',
# 			'f2_ratio': '0.00%',
# 			'f3_ratio': '0.00%',
# 			'f4_ratio': '0.00%',
# 			'f5_ratio': '0.00%',
# 			'row_ratio': '100.00%'
# 		}, {
# 			'shop_id': 25,
# 			'rf_name': '30天<R≤90天',
# 			'f1': '0',
# 			'f2': '0',
# 			'f3': '0',
# 			'f4': '0',
# 			'f5': '0',
# 			'row_total': '0',
# 			'data_type': 'customer_number',
# 			'stats_date': '2018-12-20',
# 			'created_at': '2019-01-17 19:38:52',
# 			'updated_at': '2019-01-17 19:38:52',
# 			'sort': 2,
# 			'f1_ratio': '0.00%',
# 			'f2_ratio': '0.00%',
# 			'f3_ratio': '0.00%',
# 			'f4_ratio': '0.00%',
# 			'f5_ratio': '0.00%',
# 			'row_ratio': '0.00%'
# 		}, {
# 			'shop_id': 25,
# 			'rf_name': '90天<R≤180天',
# 			'f1': '0',
# 			'f2': '0',
# 			'f3': '0',
# 			'f4': '0',
# 			'f5': '0',
# 			'row_total': '0',
# 			'data_type': 'customer_number',
# 			'stats_date': '2018-12-20',
# 			'created_at': '2019-01-17 19:38:52',
# 			'updated_at': '2019-01-17 19:38:52',
# 			'sort': 3,
# 			'f1_ratio': '0.00%',
# 			'f2_ratio': '0.00%',
# 			'f3_ratio': '0.00%',
# 			'f4_ratio': '0.00%',
# 			'f5_ratio': '0.00%',
# 			'row_ratio': '0.00%'
# 		}, {
# 			'shop_id': 25,
# 			'rf_name': '180天<R≤360天',
# 			'f1': '0',
# 			'f2': '0',
# 			'f3': '0',
# 			'f4': '0',
# 			'f5': '0',
# 			'row_total': '0',
# 			'data_type': 'customer_number',
# 			'stats_date': '2018-12-20',
# 			'created_at': '2019-01-17 19:38:52',
# 			'updated_at': '2019-01-17 19:38:52',
# 			'sort': 4,
# 			'f1_ratio': '0.00%',
# 			'f2_ratio': '0.00%',
# 			'f3_ratio': '0.00%',
# 			'f4_ratio': '0.00%',
# 			'f5_ratio': '0.00%',
# 			'row_ratio': '0.00%'
# 		}, {
# 			'shop_id': 25,
# 			'rf_name': 'R>360天',
# 			'f1': '0',
# 			'f2': '0',
# 			'f3': '0',
# 			'f4': '0',
# 			'f5': '0',
# 			'row_total': '0',
# 			'data_type': 'customer_number',
# 			'stats_date': '2018-12-20',
# 			'created_at': '2019-01-17 19:38:52',
# 			'updated_at': '2019-01-17 19:38:52',
# 			'sort': 5,
# 			'f1_ratio': '0.00%',
# 			'f2_ratio': '0.00%',
# 			'f3_ratio': '0.00%',
# 			'f4_ratio': '0.00%',
# 			'f5_ratio': '0.00%',
# 			'row_ratio': '0.00%'
# 		}, {
# 			'shop_id': 25,
# 			'rf_name': '列合计',
# 			'f1': '1',
# 			'f2': '0',
# 			'f3': '0',
# 			'f4': '0',
# 			'f5': '0',
# 			'row_total': '1',
# 			'data_type': 'customer_number',
# 			'stats_date': '2018-12-20',
# 			'created_at': '2019-01-17 19:38:52',
# 			'updated_at': '2019-01-17 19:38:52',
# 			'sort': 6,
# 			'f1_ratio': '100.00%',
# 			'f2_ratio': '0.00%',
# 			'f3_ratio': '0.00%',
# 			'f4_ratio': '0.00%',
# 			'f5_ratio': '0.00%',
# 			'row_ratio': '100.00%'
# 		}]
# 	},
# 	'elapsed': 0.115
# }
#
# print(b["data"]["list"][0]["f1"])

# c = {
# 	'code': 0,
# 	'message': 'dailyRangeShopStats',
# 	'data': {
# 		'stats': [{
# 			'stats_date': '2018-12-20',
# 			'new_customer_num': 0,
# 			'old_customer_num': 0,
# 			'customer_num_all': 0,
# 			'customer_num': 0,
# 			'customer_times': 0,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '0.00%'
# 		}, {
# 			'stats_date': '2018-12-19',
# 			'new_customer_num': 0,
# 			'old_customer_num': 0,
# 			'customer_num_all': 0,
# 			'customer_num': 0,
# 			'customer_times': 0,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '0.00%'
# 		}, {
# 			'stats_date': '2018-12-18',
# 			'new_customer_num': 0,
# 			'old_customer_num': 0,
# 			'customer_num_all': 0,
# 			'customer_num': 0,
# 			'customer_times': 0,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '0.00%'
# 		}, {
# 			'stats_date': '2018-12-17',
# 			'new_customer_num': 0,
# 			'old_customer_num': 0,
# 			'customer_num_all': 0,
# 			'customer_num': 0,
# 			'customer_times': 0,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '0.00%'
# 		}, {
# 			'stats_date': '2018-12-16',
# 			'new_customer_num': 0,
# 			'old_customer_num': 0,
# 			'customer_num_all': 0,
# 			'customer_num': 0,
# 			'customer_times': 0,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '0.00%'
# 		}, {
# 			'stats_date': '2018-12-15',
# 			'new_customer_num': 0,
# 			'old_customer_num': 0,
# 			'customer_num_all': 0,
# 			'customer_num': 0,
# 			'customer_times': 0,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '0.00%'
# 		}, {
# 			'stats_date': '2018-12-14',
# 			'new_customer_num': 0,
# 			'old_customer_num': 0,
# 			'customer_num_all': 0,
# 			'customer_num': 0,
# 			'customer_times': 0,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '0.00%'
# 		}, {
# 			'stats_date': '2018-12-13',
# 			'new_customer_num': 0,
# 			'old_customer_num': 0,
# 			'customer_num_all': 0,
# 			'customer_num': 0,
# 			'customer_times': 0,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '0.00%'
# 		}, {
# 			'stats_date': '2018-12-12',
# 			'new_customer_num': 0,
# 			'old_customer_num': 0,
# 			'customer_num_all': 0,
# 			'customer_num': 0,
# 			'customer_times': 0,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '0.00%'
# 		}, {
# 			'stats_date': '2018-12-11',
# 			'new_customer_num': 0,
# 			'old_customer_num': 0,
# 			'customer_num_all': 0,
# 			'customer_num': 0,
# 			'customer_times': 0,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '0.00%'
# 		}, {
# 			'stats_date': '2018-12-10',
# 			'new_customer_num': 0,
# 			'old_customer_num': 0,
# 			'customer_num_all': 0,
# 			'customer_num': 0,
# 			'customer_times': 0,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '0.00%'
# 		}, {
# 			'stats_date': '2018-12-09',
# 			'new_customer_num': 0,
# 			'old_customer_num': 0,
# 			'customer_num_all': 0,
# 			'customer_num': 0,
# 			'customer_times': 0,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '0.00%'
# 		}, {
# 			'stats_date': '2018-12-08',
# 			'new_customer_num': 0,
# 			'old_customer_num': 0,
# 			'customer_num_all': 0,
# 			'customer_num': 0,
# 			'customer_times': 0,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '0.00%'
# 		}, {
# 			'stats_date': '2018-12-07',
# 			'new_customer_num': 0,
# 			'old_customer_num': 0,
# 			'customer_num_all': 0,
# 			'customer_num': 0,
# 			'customer_times': 0,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '0.00%'
# 		}, {
# 			'stats_date': '2018-12-06',
# 			'new_customer_num': 0,
# 			'old_customer_num': 0,
# 			'customer_num_all': 0,
# 			'customer_num': 0,
# 			'customer_times': 0,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '0.00%'
# 		}, {
# 			'stats_date': '2018-12-05',
# 			'customer_num_all': 1,
# 			'customer_num': 1,
# 			'customer_times': 1,
# 			'new_customer_num': 1,
# 			'order_num': 0,
# 			'consumption': '0.00',
# 			'weather': '',
# 			'customer_num_outdoor': 0,
# 			'customer_convert_ratio': '100.00%',
# 			'old_customer_num': 0
# 		}]
# 	},
# 	'elapsed': 0.109
# }
#
# s = len(c["data"]["stats"])
# print(s)
# for i in range(s):
# 	customer_number = c["data"]["stats"][i]["customer_num"]
# 	# print(customer_num)
# 	sum = 0  # 先把sum赋值=0
# 	sum += customer_number
# print(sum)

# f = {
# 	'code': 0,
# 	'message': 'indicator',
# 	'data': {
# 		'stats': {
# 			'total': {
# 				'order_amount': '10.00',
# 				'avg_order_amount': '0.32',
# 				'new_order_amount': '10.00',
# 				'avg_new_order_amount': '0.32',
# 				'old_order_amount': '0.00',
# 				'avg_old_order_amount': '0.00'
# 			},
# 			'order': {
# 				'count': 1,
# 				'avg_count': '0.03',
# 				'new_order_count': 1,
# 				'avg_new_order_count': '0.03',
# 				'old_order_count': 0,
# 				'avg_old_order_count': '0.00'
# 			},
# 			'bag': {
# 				'ratio': '50.00%',
# 				'avg_ratio': '3.23%',
# 				'new_ratio': '50.00%',
# 				'avg_new_ratio': '3.23%',
# 				'old_ratio': '0.00%',
# 				'avg_old_ratio': '0.00%'
# 			},
# 			'price': {
# 				'price': 10,
# 				'avg_price': 0.32,
# 				'new_price': 10,
# 				'avg_new_price': 0.32,
# 				'old_price': 0,
# 				'avg_old_price': 0
# 			}
# 		}
# 	},
# 	'elapsed': 0.109
# }
#
# print(f["data"]["stats"]["total"]["avg_order_amount"])


# import datetime
#
# a1 = datetime.datetime.strptime("2018-01-20 10:00:00", "%Y-%m-%d %H:%M:%S")
#
# a2 = datetime.datetime.strptime("2018-01-01 12:00:00", "%Y-%m-%d %H:%M:%S")
# print((a1-a2).days)

t = {
	'code': 0,
	'message': 'index',
	'data': {
		'orderList': {
			'current_page': 1,
			'data': [{
				'order_id': 155,
				'order_no': '3123213216336809',
				'customer_id': 0,
				'third_customer_id': 'vip_090',
				'third_mobile': '13764555678',
				'third_username': 'jack ma',
				'order_at': '2018-12-28 09:00:00',
				'order_amount': '10.00',
				'order_status': 'ORDER_SUCCESS',
				'extend_field': None,
				'order_status_convert': '订单完成'
			}, {
				'order_id': 42,
				'order_no': '3123213216336800',
				'customer_id': 0,
				'third_customer_id': 'vip_090',
				'third_mobile': '13764555678',
				'third_username': 'jack ma',
				'order_at': '2018-10-10 09:00:00',
				'order_amount': '10.00',
				'order_status': 'ORDER_SUCCESS',
				'extend_field': None,
				'order_status_convert': '订单完成'
			}],
			'first_page_url': 'https://qa.api.gmall.gaopeng.com/api/shops/25/orders?page=1',
			'from': 1,
			'last_page': 1,
			'last_page_url': 'https://qa.api.gmall.gaopeng.com/api/shops/25/orders?page=1',
			'next_page_url': None,
			'path': 'https://qa.api.gmall.gaopeng.com/api/shops/25/orders',
			'per_page': 10,
			'prev_page_url': None,
			'to': 2,
			'total': 2
		}
	},
	'elapsed': 0.113
}

p = len(t["data"]["orderList"]["data"])
print(p)
sum = 0
for i in range(p):
	order_amount = t["data"]["orderList"]["data"][i]["order_amount"]
	sum += float(order_amount)
print("销售额总和:", sum)