"""
-------------------------------------------------
  @Time : 2020/4/19 22:13 
  @Auth : 十七
  @File : test1_shiqi.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
from random import randint

class Player:
    top_score = 0
    score_list = []

    def __init__(self, name):
        self.name = name

    def start(self):
        Player.show_help()
        print(f"欢迎光临{self.name}, 请愉快玩耍！\n")
        score = randint(0, 100)
        self.score_list.append(score)

    @staticmethod
    def show_help():
        print("欢迎光临植物大战僵尸游戏")
        print("游戏过程中要遵守相关规定")

    @classmethod
    def display_top_score(cls):
        cls.score = max(cls.score_list)
        return cls.score


player1 = Player("小鹿")
player2 = Player("Hua_")
player3 = Player("天亦")

for i in range(10):
    player1.start()
    player2.start()
    player3.start()

print(f"历史最高分为{Player.display_top_score()}")