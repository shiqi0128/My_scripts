#————————此文件为3.1所有砍价抽奖的测试用例--------
import unittest
from Atle.interface.framework.base.bargain import Bargain
from Atle.interface.framework.base.Trophy import Trophy

ba = Bargain()
tr = Trophy()

class   Activity(unittest.TestCase):
    """定义一个双十一砍价、抽奖的活动执行类"""
# 砍价模块
#     def test_01_mart_details(self):
#         """砍价详情"""
#         r = ba.mart_details()
#         self.assertEqual(r["code"], 1)
#
#     def test_02_join(self):
#         """参与此砍价活动"""
#         r = ba.join()
#         self.assertEqual(r["code"], 1)

    def test_03_who_list(self):
        """我的砍价列表"""
        r = ba.who_list()
        self.assertEqual(r["code"], 1)

    def test_04_who_list_find(self):
        """我的砍价列表详情"""
        r = ba.who_list_find()
        self.assertEqual(r["code"], 1)

    def test_05_ranking(self):
        """砍价榜单"""
        r = ba.ranking()
        self.assertEqual(r["code"], 1)

# 抽奖模块
    def test_06_begin(self):
        """即将开始"""
        r = tr.begin()
        self.assertEqual(r["code"], 1)

    def test_07_already(self):
        """已开奖"""
        r = tr.already()
        self.assertEqual(r["code"], 1)

    def test_08_progress(self):
        """进行中"""
        r = tr.progress()
        self.assertEqual(r["code"], 1)

    def test_09_details(self):
        """抽奖详情"""
        r = tr.details()
        self.assertEqual(r["code"], 1)


# if __name__ == '__main__':
#     unittest.main()
# else:
#     print("false")




