import random

def roll_dice(number,sides):
    for i in range(0,number):
        rolled = random.randint(1,sides)
        print("You rolled {}!".format(rolled))

while True:
    number = int(input("How many dice do you want to roll? "))
    sides = int(input("How many sides on each dice? "))
    roll_dice(number,sides)
