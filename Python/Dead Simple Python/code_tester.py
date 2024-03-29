import random

def roll_dice(*dice):
    return tuple(random.randint(1, d) for d in dice)

dice_cup = roll_dice(6,6,6,6,6)
print(dice_cup)