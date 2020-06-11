# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/15 20:56 
  @Auth : 可优
  @File : lm_02_play_game.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from random import randint


class Player:
    top_score = 0
    score_list = []

    def __init__(self, name):
        self.name = name

    @classmethod
    def display_history_high_score(cls):
        # Player("Fr.墨").name
        cls.top_score = max(cls.score_list)

        return cls.top_score

    def start(self):
        self.show_help()

        print(f"欢迎{self.name}光临, 请愉快玩耍!")
        score = randint(0, 100)
        # Player.score_list.append(score)
        self.score_list.append(score)

    @staticmethod
    def show_help():
        print(f"\n欢迎光临, 植物大战僵尸游戏!")
        print(f"游戏过程中, 要遵守相关规定!")

    # __str__方法是魔术方法
    # a. 名称是固定的
    # b. 当print(对象)时, 会自动调用__str__方法
    # c. 只能返回字符串类型, 其他类型会报错
    def __str__(self):
        return self.name


player1 = Player("小鹿")
player2 = Player("Hua_")
player3 = Player("天亦")

# for i in range(10):
#     player1.start()
#     player2.start()
#     player3.start()
#
# print(f"历史最高分为: {Player.display_history_high_score()}")

print(player1)
print(player2)
print(player3)

