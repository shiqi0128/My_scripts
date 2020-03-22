"""此文件为智能巡查所有方法主调用文件"""
import unittest
from interfaceTest.GMALL.gmall_all.Intelligent_patrol.patrol import Cruise_logic, taskId, parent_id, problem_id, scheduleId

pt = Cruise_logic()


class test_patrol(unittest.TestCase):
    """定义一个智能巡查所有方法的"""

    def test_01_Problem_update(self):
        """问题分类--更新"""
        r = pt.Problem_update()
        self.assertEqual(r["code"], 0)

    def test_02_Problem_delete(self):
        """问题分类--删除"""
        r = pt.Problem_delete()
        self.assertEqual(r["code"], 0)

    def test_03_Patrol_list(self):
        """巡查计划--列表"""
        r = pt.Patrol_list()
        self.assertEqual(r["code"], 0)

    # def Patrol_detail(self):
    #     """巡查计划--详情"""
    #     pt.Patrol_detail()

    def test_04_Patrol_edit(self):
        """巡查计划--修改"""
        scheduleId_02, r = pt.Patrol_detail()   # 调用巡查计划--详情的接口
        pt.Patrol_edit("2019-03-01", "2019-04-30", scheduleId_02)
        self.assertEqual(r["code"], 0)

    def test_05_Record_creat(self):
        """操作巡查记录 - 创建巡查记录"""
        pt.Record_creat()

    # def Record_detail(self):
    #     """操作巡查记录 - 巡查记录详情"""
    #     pt.Record_detail()
    #
    # def patrol(self):
    #     """操作巡查记录 - 巡查"""
    #     pt.patrol()
    #
    # def rectify(self):
    #     """操作巡查记录 - 整改"""
    #     pt.rectify()
    #
    # def alter_rectify(self):
    #     """操作巡查记录 - 变更整改人"""
    #     pt.alter_rectify()
    #
    # def accept(self):
    #     """操作巡查记录 - 验收"""
    #     pt.accept()
    #
    # def inspect_statistical(self):
    #     """巡查统计"""
    #     pt.inspect_statistical("2019-03-01", "2019-04-30")
    #
    # def inspect_problem(self):
    #     """巡查统计--巡查问题详情"""
    #     pt.inspect_problem("2019-03-01", "2019-04-30")
    #
    # def inspect_rectify(self):
    #     """巡查统计 - 巡查整改详情"""
    #     pt.inspect_rectify("2019-03-01", "2019-04-30")
    #
    # def inspect_task(self):
    #     """巡查统计 - 巡查任务详情"""
    #     pt.inspect_task("2019-03-01", "2019-04-30")
    #
    # def comment_list(self):
    #     """巡查记录-评论列表"""
    #     pt.comment_list()
    #
    # def comment_add(self):
    #     """巡查记录-添加评论"""
    #     pt.comment_add()


if __name__ == "__main__":
    unittest.main()