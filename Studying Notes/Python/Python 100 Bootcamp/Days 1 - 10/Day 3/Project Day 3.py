print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')

print('''Welcome to Treasure Island.
Your mission is to find the treasure.''')

alive = True
while alive:
    turn = input("Turn Left or Right")
    if turn.upper() != "LEFT":
        print("You've fallen into a spiked pit")
        alive = False
        break
    floating = input("Swim or Wait")
    if floating.upper() != "WAIT":
        print("You've been attacked by alligators.")
        alive = False
        break
    opening = input("Which Door")
    if opening.upper() != "YELLOW":
        if opening.upper() == "BLUE":
            print("You've been trapped in  a room of hungry lions")
            alive = False
            break
        elif opening.upper() == "RED":
            print("You've been trapped in a room of fire")
            alive = False
            break
        else:
            print("You've made a bad choice")
    break
if alive == True:
    print("You Win")
else:
    print("Game Over")

