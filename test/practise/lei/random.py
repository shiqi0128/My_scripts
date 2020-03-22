# 9-14 骰子
from random import randint
class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

six_die = Die(6)
ten_die = Die(10)
twenty_die = Die(20)

for number in range(1, 11):
    six_die.roll_die()
print("--------------------------")

for number in range(1, 11):
    ten_die.roll_die()
print("--------------------------")

for number in range(1, 11):
    twenty_die.roll_die()
