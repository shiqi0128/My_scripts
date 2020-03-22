from interfaceTest.GMALL.shop_manage_01 import shop_manage
import unittest
sm = shop_manage()
guide_id = sm.guide_list()


class gmall_script(unittest.TestCase):
    """门店管理——店铺管理API"""
    # def test_01_guide_list(self):
    #     """导购-列表"""
    #     sm().guide_list()

    def test_02_guide_add(self):
        """导购新增"""
        sm.guide_add("杨明宇", 1, "13250511512")

    def test_03_guide_update(self):
        """导购-更新"""
        sm.guide_update(guide_id, "杨明浩", 1, "13250511512")

    def test_04_guide_delete(self):
        """导购—删除"""
        sm.guide_delete(guide_id)


if __name__ == "__main__":
    unittest.main()
else:
    print("false")