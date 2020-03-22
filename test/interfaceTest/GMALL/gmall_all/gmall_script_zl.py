import unittest
import random
from interfaceTest.GMALL.gmall_all.account import gmall_account
from interfaceTest.GMALL.gmall_all.stores_compass import gmall_stores_compass
from interfaceTest.GMALL.gmall_all.customer_behavior.customer_behavior import gmall_customer_behavior
from interfaceTest.GMALL.gmall_all.customer_behavior.line_heat import line_heat
from interfaceTest.GMALL.gmall_all.customer_behavior.viscosity import viscosity
from interfaceTest.GMALL.gmall_all.customer_behavior.cus_manage import cus_manage
from interfaceTest.GMALL.gmall_all.customer_behavior.cus_group import cus_group
from interfaceTest.GMALL.gmall_all.customer_behavior.cus_portrait import cus_portrait
from interfaceTest.GMALL.gmall_all.marketing_center_PC import Activities
from interfaceTest.GMALL.gmall_all.quick_shot_records import StoreSnapshoot
from interfaceTest.GMALL.gmall_all.live_playback import LivePlayback
from interfaceTest.GMALL.gmall_all.Store_manage.shop_manage import Shop_manage
# from interfaceTest.GMALL.public_files import guide_id, blacklist_id, user_id, user_name, report_id, product_id
# from interfaceTest.GMALL.public_files import report_id
from interfaceTest.GMALL.gmall_all.Store_manage.settings import settings
from interfaceTest.GMALL.gmall_all.business_aly.Category_sales import business_model


zh = gmall_account()            # 引用[account]表的gmall_account类，账号相关接口简称 zh
md = gmall_stores_compass()     # 引用[stores_compass]表的gmall_stores_compass类，门店罗盘简称 md
xw = gmall_customer_behavior()  # 引用[customer_behavior]表的gmall_customer_behavior类，顾客行为简称 xw
lh = line_heat()                # 引用[line_heat]表的line_heat类，动线&热力简称lh
vy = viscosity()                # 引用[viscosity]表的viscosity类，顾客粘度简称vy
cm = cus_manage()               # 引用[cus_manage]表的cus_manage类，顾客管理简称cm
cg = cus_group()                # 引用[cus_group]表的cus_group类，客群管理简称cg
cp = cus_portrait()             # 引用[cus_portrait]表的cus_portrait类，顾客画像简称cp
act = Activities()              # 引用[marketing_center_PC]表的Activities类，活动简称act
st = StoreSnapshoot()           # 引用[quick_shot_records]表的StoreSnapshoot类，门店巡查—快拍记录简称st
lp = LivePlayback()             # 引用[live_Playback]表的LivePlayback类，门店巡查—直播回放快拍记录简称lp
sm = Shop_manage()
sets = settings()
bm = business_model()


class gmall_script_zl(unittest.TestCase):
    """

    定义一个gmall脚本整体的测试类

    """

    # def test_01_users(self):
    #     """可创建用户角色"""
    #     r_01_new = zh.users()
    #     self.assertEqual(r_01_new["code"], 0)
    #
    # def test_02_old_password(self):
    #     """验证原密码"""
    #     r_02_new = zh.old_password()
    #     self.assertEqual(r_02_new["code"], 0)
    #
    # def test_03_Message_notification_list(self):
    #     """消息通知列表"""
    #     r_03_new = zh.Message_notification_list()
    #     self.assertEqual(r_03_new["code"], 0)

    # def test_role_list(self):
    #     """角色列表"""
    #     role_list()

    # def test_01_role_creat(self):
    #     """角色创建"""
    #     zh.role_creat()
    #
    # def test_02_role_read(self):
    #     """角色查看"""
    #     zh.role_read()
    #
    # def test_03_role_edit(self):
    #     """角色编辑"""
    #     zh.role_edit()
    #
    # def test_04_role_delete(self):
    #     """角色删除"""
    #     zh.role_delete()

    # 该接口暂时有问题
    # def test_03_change_password(self):
    #     """修改密码"""
    #     r_03_new = zl.change_password()
    #     # self.assertEqual(r_03_new["code"], 0)

# # 门店罗盘API
#     def test_04_daily_stats(self):
#         """本门店统计（每天）"""
#         r_04_new = md.daily_stats("2019-01-30")
#         self.assertEqual(r_04_new["code"], 0)
#
#     def test_05_current_stats(self):
#         """本门店在线人数&最热区域"""
#         md.current_stats()
#
#     def test_06_minutelyShopStats(self):
#         """本门店统计（每分钟）"""
#         md.minutelyShopStats()
#
#     def test_07_hourlyShopStats(self):
#         """本门店统计（每小时）"""
#         md.hourlyShopStats()
#
#     def test_08_hourly_stats_export(self):
#         """本门店统计（每小时）导出"""
#         md.hourly_stats_export("2019-01-30")
#
#     def test_09_daily_range_stats(self):
#         """本门店统计（每天）连续多日"""
#         r_09_new = md.daily_range_stats("2019-01-30", "2019-02-02")
#         self.assertEqual(r_09_new["code"], 0)
#
#     def test_10_daily_range_stats_export(self):
#         """本门店统计（每小时）导出"""
#         md.daily_range_stats_export("2019-01-30", "2019-02-02")
#
#     def test_11_store_areas(self):
#         """门店区域信息"""
#         md.store_areas()
#
#     def test_12_dailyZoneStats(self):
#         """区域客流统计（每天）"""
#         r_12_new = md.dailyZoneStats("2019-01-30")
#         self.assertEqual(r_12_new["code"], 0)
#
#     def test_13_hourlyZoneStats(self):
#         """区域客流统计（每小时）"""
#         r_13_new = md.dailyZoneStats("2019-01-30")
#         self.assertEqual(r_13_new["code"], 0)
#
#     def test_14_zone_daily_range_stats(self):
#         """区域客流-连续多日（每日)"""
#         r_14_new = md.daily_range_stats("2019-01-30", "2019-02-02")
#         self.assertEqual(r_14_new["code"], 0)

# # 顾客行为--顾客行为
#     def test_15_zone_sankey_stats(self):
#         """本门店区域动线统计（用于桑基图显示）"""
#         xw.zone_sankey_stats("2019-02-02", "2019-02-02")
#
#     def test_16_depth_stats(self):
#         """深度分析统计（人均逛店深度/次均逛店深度)"""
#         xw.depth_stats("2019-02-02", "2019-02-02")
#
#     def test_17_depth_stats_export(self):
#         """深度分析统计导出（人均逛店深度 / 次均逛店深度"""
#         xw.depth_stats_export("2019-02-02", "2019-02-02")
#
#     def test_18_line_chord(self):
#         """和弦图"""
#         xw.line_chord("2019-02-02", "2019-02-02")
#
#     def test_19_line_chord_export(self):
#         """和弦图 数据导出CSV"""
#         xw.line_chord_export("2019-02-02", "2019-02-02")
#
#     def test_20_stay_time(self):
#         """逛店时长（人次 均次 每天）连续多日---start_date, end_date必填项"""
#         xw.stay_time("2019-02-02", "2019-02-02")
#
#     def test_21_stay_time_export(self):
#         """逛店时长（人次 均次 每天）连续多日-导出CSV---start_date, end_date必填项"""
#         xw.stay_time_export("2019-02-02", "2019-02-02")
#
#     def test_22_enter_shop_frequency_daily(self):
#         """逛店频率（日）---date必填项"""
#         xw.enter_shop_frequency_daily("2019-02-02")
#
#     def test_23_enter_shop_frequency_daily_export(self):
#         """逛店频率（日）导出---date必填项"""
#         xw.enter_shop_frequency_daily_export("2019-02-02")
#
#     def test_24_enter_shop_frequency_weekly(self):
#         """逛店频率（周）---start_date, end_date必填项"""
#         xw.enter_shop_frequency_weekly("2019-02-02", "2019-02-02")
#
#     def test_25_enter_shop_frequency_weekly_export(self):
#         """逛店频率（周）导出CSV---start_date, end_date必填项"""
#         xw.enter_shop_frequency_weekly_export("2019-02-02", "2019-02-02")
#
#     def test_26_enter_shop_frequency_monthly(self):
#         """逛店频率（月）---year, month必填项"""
#         xw.enter_shop_frequency_monthly("2019", "2")
#
#     def test_27_enter_shop_frequency_monthly_export(self):
#         """逛店频率（月）导出CSV---year, month必填项"""
#         xw.enter_shop_frequency_monthly_export("2019", "2")
#
#     def test_28_zone_hourly_range_stats(self):
#         """区域统计（每小时）连续多日---start_date, end_date必填项"""
#         xw.zone_hourly_range_stats("2019-02-02", "2019-02-02")
#
#     def test_29_zone_range_average_time_stats(self):
#         """区域统计连续多日 顾客总数&平均停留时长---start_date, end_date必填项"""
#         xw.zone_range_average_time_stats("2019-02-02", "2019-02-02")
#
#     def test_30_historical_data_compare(self):
#         """本门店历史数据环比"""
#         xw.historical_data_compare("2019-02-02")
#
#     def test_31_branch_line_stats(self):
#         """动线路径"""
#         xw.branch_line_stats("2019-02-02", "2019-02-02")
#
#     def test_32_minutely_last_stats(self):
#         """本门店统计（近X分钟）"""
#         xw.minutely_last_stats("2019-02-02")

# # 顾客行为——动线&热力 API
#     def test_33_line_analysis(self):
#         """动线排行"""
#         r_15_new = lh.line_analysis("2019-01-30")
#         self.assertEqual(r_15_new["code"], 0)
#
#     def test_34_heat_map(self):
#         """店面热力图(每分钟)"""
#         lh.heat_map("2019-01-30 09:00:00", "2019-02-02 22:00:00")
#         # self.assertEqual(r_16_new["code"], 0)

# # 顾客行为——顾客粘度 API
#     def test_35_livenessCompare(self):
#         """活跃度环比"""
#         r_17_new = vy.livenessCompare("2019-01-30")
#         self.assertEqual(r_17_new["code"], 0)
#
#     def test_36_dailyRangeLiveness(self):
#         """活跃度列表"""
#         r_18_new = vy.dailyRangeLiveness("2019-01-30", "2019-02-02")
#         self.assertEqual(r_18_new["code"], 0)
#
#     def test_37_liveness_export(self):
#         """活跃度导出CSV"""
#         vy.liveness_export("2019-01-30", "2019-02-02")
#
#     def test_38_weekLivenessList(self):
#         """活跃天数列表（周)"""
#         r_20_new = vy.weekLivenessList("2019-01-30", "2019-02-02")
#         self.assertEqual(r_20_new["code"], 0)
#
#     def test_39_monthLivenessList(self):
#         """活跃天数列表（月）"""
#         vy.monthLivenessList("2019-01-30", "2019-02-02")
#         # self.assertEqual(r_21_new["code"], 0)
#
#     def test_40_liveness_list_export(self):
#         """活跃天数导出CSV"""
#         vy.liveness_list_export("2019-01-30", "2019-02-02")

# # 顾客行为——顾客管理
#     def test_label_list(self):
#         """获取 标签/客群 列表"""
#         lst = ["标签", "客群"]
#         for tag_type, tag in enumerate(lst, 1):
#             cm.label_list(tag_type, tag)
#
#     def test_42_label_details(self):
#         """获取标签/客群详情,type=1是标签，type=2是客群"""
#         lst = ["标签", "客群"]
#         for index, types in enumerate(lst, 1):
#             tag_id_01 = cm.label_list(index, types)
#             for types_key, types_value in enumerate(lst, 1):
#                 cm.label_details(types_key, types_value, tag_id_01)

    # def test_50_order_list(self):
    #     """订单管理--列表"""
    #     cm.order_list()
    #
    # def test_51_order_sort(self):
    #     """订单管理--品类"""
    #     cm.order_sort()
    #
    # def test_52_order_details(self):
    #     """订单管理--详情"""
    #     cm.order_details()
    #
    # def test_53_order_export(self):
    #     """订单管理--列表导出"""
    #     cm.order_export()
    #
    # def test_41_customer_funnel(self):
    #     """顾客漏斗"""
    #     cm.customer_funnel("2019-01-30", "2019-02-02")
    #
    # def test_42_customer_funnel_export(self):
    #     """顾客漏斗-列表导出"""
    #     cm.customer_funnel_export("2019-01-30", "2019-02-02")
    #
    # # 顾客行为——客群管理
    #
    # def test_43_customer_charts(self):
    #     """客群管理_门店报表"""
    #     cg.customer_charts("2019-02-02")
    #
    # def test_44_customer_visit_list(self):
    #     """顾客历史来店信息"""
    #     cg.customer_visit_list()
    #
    # def test_45_customer_entry_records(self):
    #     """顾客进店记录"""
    #     cg.customer_entry_records("2019-01-30", "2019-02-02")

    # def test_46_user_portrait(self):
    #     """用户画像"""
    #     cg.user_portrait()

    # # 顾客行为——顾客画像
    # def test_47_get_the_whole_race(self):
    #     """获取全部人种"""
    #     cp.get_the_whole_race()
    #
    # def test_48_customers_list(self):
    #     """顾客列表"""
    #     cp.cus_portrait("2019-01-30", "2019-02-02")
    #
    # def test_49_cuslist_export(self):
    #     """顾客列表 导出"""
    #     cp.cuslist_export()
    #
    # def test_50_customer_details(self):
    #     """顾客详情"""
    #     cp.customer_details()
    #
    # def test_51_update_info(self):
    #     """顾客详情部分信息保存"""
    #     cp.update_info()
    #
    # def test_52_guest_group_portrait(self):
    #     """客群画像"""
    #     r_52 = cp.cus_portrait("2019-01-30", "2019-02-02")
    #     self.assertEqual(r_52["code"], 0)
    #
    # def test_53_customers_ranking(self):
    #     """顾客画像Top排名"""
    #     r_53 = cp.customers_ranking("2019-01-30", "2019-02-02")
    #     self.assertEqual(r_53["code"], 0)
    #
    # def test_54_trend_monitoring(self):
    #     """数据趋势"""
    #     lst = ["进店人数", "进店次数", "新客人数", "订单数", "消费金额"]
    #     for index, types in enumerate(lst, 1):
    #         r_54 = cp.trend_monitoring("2019-01-30", "2019-02-02", index, types)
    #         self.assertEqual(r_54["code"], 0)
    #
    #     # lst = [{1:"进店人数"}, {2:"进店次数"}, {3:"新客人数"}, {4:"订单数"}, {5:"消费金额"}]
    #     # for types in lst:
    #     #     r_54 = cp.trend_monitoring("2019-01-30", "2019-02-02", types.keys(), types.values())
    #     #     # self.assertEqual(r_54["code"], 0)
    #
    # def test_55_trend_export(self):
    #     """数据趋势导出 CSV"""
    #     for types in range(1, 6):
    #         r_55 = cp.trend_monitoring_export("2019-01-30", "2019-02-02", types)
    #         # self.assertEqual(r_55["code"], 0)

    # def test_camera_list(self):
    #     """门店监控（摄像头列表）"""
    #     lp.camera_list()
    #
    # def test_camera_zones_lst(self):
    #     """摄像头&区域列表"""
    #     lp.camera_zones_lst()

# 这个接口有问题
    # def test_live_address(self):
    #     """摄像头直播地址（带有效期）"""
    #     lp.live_address("K_SP_001")
    #
    # def test_EZOpen_URL(self):
    #     """摄像头萤石云 EZOpen URL"""
    #     lp.EZOpen_URL("sylvia_001")

    # def test_snapshoot_new(self):
    #     """快照新增"""
    #     st.snapshoot_new("sylvia_001")
    #
    # def test_put_snapshoot_remark(self):
    #     """修改快照备注"""
    #     screenshots_id = st.snapshoot_lst()
    #     st.put_snapshoot_remark(screenshots_id)

    # def test_activity_tpls(self):
    #     """查看所有活动模板"""
    #     act.activity_tpls()
    #
    # def test_index(self):
    #     """门店活动列表"""
    #     act.index()
    #
    # def test_show_details(self):
    #     """门店活动详情"""
    #     act.show_details()
    #
    # def test_01_creat_activities(self):
    #     """创建活动"""
    #     act.creat_activities()
    #
    # def test_02_edit(self):
    #     """活动编辑前操作"""
    #     act.edit()
    #
    # def test_03_update(self):
    #     """更新活动"""
    #     act.update()
    #
    # def test_04_update_prize(self):
    #     """更新活动奖品_实物"""
    #     act.update_prize()
    #
    # def test_05_import_file(self):
    #     """导入活动优惠券文件"""
    #     act.import_file()
    #
    # def test_06_update_prize_coupons(self):
    #     """更新活动奖品_优惠券"""
    #     act.update_prize_coupons()
    #
    # def test_07_change_status(self):
    #     """门店活动暂停/启动"""
    #     act.change_status()
    #
    # def test_08_surplus(self):
    #     """导出剩余优惠券"""
    #     act.surplus()
    #
    # def test_09_delete(self):
    #     """删除奖品优惠券"""
    #     act.delete()
    #
    # def test_10_qr_code(self):
    #     """下载活动二维码"""
    #     act.qr_code()
    #
    # def test_11_coupons_tpl(self):
    #     """下载优惠券模板"""
    #     act.coupons_tpl()

# 门店管理——店铺管理API
#     def test_guide_list(self):
#         """导购-列表"""
#         sm.guide_list()

    # def test_02_guide_add(self):
    #     """导购新增"""
    #     sm.guide_add("杨明宇", 1, "13250511512")

    # def test_03_guide_update(self):
    #     """导购-更新"""
    #     sm.guide_update(guide_id, "杨明宇", 1, "13250511512")
    #
    # def test_04_guide_delete(self):
    #     """导购—删除"""
    #     sm.guide_delete(guide_id)

# 此接口为被调用的公共接口，不需要运行
#     def test_05_blactlist(self):
#         """黑名单列表"""
#         sm.blactlist()
#
#     def test_06_blacklist_add(self):
#         """黑名单--新增"""
#         sm.guide_add("小偷", 1, "就是小偷")
#
#     def test_07_blacklist_detail(self):
#         """黑名单--详情"""
#         sm.blacklist_detail(blacklist_id)
#
#     def test_08_blacklist_update(self):
#         """黑名单--更新"""
#         sm.guide_update(blacklist_id, "小偷", 1, "就是小偷")
#
#     def test_09_blacklist_delete(self):
#         """黑名单--删除"""
#         sm.guide_delete(blacklist_id)
#
#     def test_10_blacklist_batch(self):
#         """黑名单-批量添加"""
#         sm.blacklist_batch("骗子")

    # def test_11_reception_detail(self):
    #     """接待统计详情"""
    #     sm.reception_detail()
    #
    # def test_12_guide_info(self):
    #     """导购信息"""
    #     sm.guide_info(guide_id, "2019-02-01")
    #
    # def test_13_update_message(self):
    #     """修改门店消息"""
    #     sm.update_message()
    #
    # def test_14_notice_show(self):
    #     """门店提醒规则查看"""    # 为什么运行了2遍？？
    #     sm.notice_show()
    #
    # def test_15_notice_update(self):
    #     """门店提醒规则更新"""
    #     sm.notice_update()
    #
    # def test_16_notice_list(self):
    #     """门店提醒规则列表"""
    #     sm.notice_list()

    # def test_11_shop_list(self):
    #     """门店列表"""
    #     sets.shop_list()
    #
    # def test_12_set_default(self):
    #     """设置默认门店"""
    #     sets.set_default()
    #
    # def test_13_account_creat(self):
    #     """账号创建"""
    #     sets.account_creat("aa1111")
    #
    # def test_14_account_read(self):
    #     """账号查看"""
    #     sets.account_read(user_id)
    #
    # def test_15_account_edit(self):
    #     """账号编辑"""
    #     sets.account_edit(user_id)
    #
    # def test_16_account_update_info(self):
    #     """账号更新部分信息"""
    #     sets.account_update_info(user_id, 1, 1)
    #
    # def test_17_account_chect(self):
    #     """账号唯一检查"""
    #     sets.account_chect(user_name)
    #
    # def test_18_account_delete(self):
    #     """账号删除"""
    #     sets.account_delete(user_id)
    #
    # def test_19_report_list(self):
    #     """报表订阅列表"""
    #     sets.report_list()
    #
    # def test_20_report_creat(self):
    #     """订阅者创建"""
    #     sets.report_creat("娱乐")

    # def test_21_report_read(self):
    #     """订阅者查看"""
    #     r = sets.report_read()
    #     self.assertEqual(r["code"], 0)
    #
    # def test_22_report_edit(self):
    #     """订阅者编辑"""
    #     r = sets.report_edit(["体育"])
    #     self.assertEqual(r["code"], 0)
    #
    # def test_23_report_delete(self):
    #     """订阅者删除"""
    #     r = sets.report_delete()
    #     self.assertEqual(r["code"], 0)

    # def test_01_category_stats(self):
    #     """品类占比"""
    #     bm.category_stats("2019-03-01", "2019-03-01")
    #
    # def test_02_category_export(self):
    #     """品类占比--导出"""
    #     bm.category_export("2019-03-01", "2019-03-01")
    #
    # def test_03_Sales_cycle(self):
    #     """销量周期"""
    #     bm.Sales_cycle()
    #
    # def test_04_Sales_export(self):
    #     """销量周期--导出"""
    #     bm.Sales_export()
    #
    # def test_05_Merch_sales_export(self):
    #     """商品销售经营分析--导出"""
    #     bm.Merch_sales_export("2019-01-13", "2019-01-13")
    #
    # def test_06_sales_trend(self):
    #     """商品销售--趋势"""
    #     bm.sales_trend(product_id, "2019-01-13", "2019-01-13")
    #
    # def test_07_sales_trend_export(self):
    #     """商品销售--趋势导出"""
    #     bm.sales_trend_export(product_id, "2019-01-13", "2019-01-13")
    #
    # def test_08_sales_relates(self):
    #     """商品销售--关联"""
    #     bm.sales_relates(product_id, "2019-01-13", "2019-01-13")
    #
    # def test_09_sales_relates_export(self):
    #     """商品销售--关联导出"""
    #     bm.Merch_sales_export("2019-01-13", "2019-01-13")
    #
    # def test_10_shop_list(self):
    #     """门店列表"""
    #     bm.shop_list()
    #
    # def test_11_shop_trend(self):
    #     """门店趋势"""
    #     bm.shop_trend("2019-01-13", "2019-01-13")
    #
    # def test_12_shop_trend_export(self):
    #     """门店趋势--导出"""
    #     bm.shop_trend_export("2019-01-13", "2019-01-13")


if __name__ == "__main__":
    unittest.main()
else:
    print("false")
