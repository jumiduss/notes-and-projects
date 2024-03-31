import random

def Game():

    again = ""

    round = 0
    nWins = 0

    running = True
    checkrules = True

    while checkrules == True:
        
        seeRules = input("Would you like to see the rules{}?\nY/N (Default is N)".format(again))
        upperSeeRules = seeRules.upper()
        if upperSeeRules == "Y":
            print('''
            Objective: Select a winning hand against the computer's choice.
            Rules: 
                1. If you win, the game continues.
                2. If the computer wins, the game ends.
                3. If you tie, the game continues.
            Winning hands:
                Rock Beats Scissors, Type 0 for Rock
                Scissors Beats Paper, Type 1 for Scissors 
                Paper Beats Rock, Type 2 for Paper\n
            ''')
            again = " again"
        elif upperSeeRules == 'N' or upperSeeRules == '':
            checkrules = False
        else:
            print("\n***Not a valid option***\n\n")

    while running == True:
        round += 1
        print("\n\nRound: {}".format(round))
        roundResult = Round()
        if roundResult == 1:
            print("You Won Round {}!".format(round))
            nWins += 1
        elif roundResult == 2:
            print("You tied the computer this round, the game continues!")
        else:
            print("\n\nThe Computer won this hand.\n\n\n***Game Over***\nYou won {} Rounds".format(nWins))
            running = False
    
    restart = input("\n\nWould you like to play again?\n(Y/N)")
    if restart.upper() == "Y":
        print("\n\n\n\n\n\n")
        Game()
    else:
        print("Application Complete")

def Round():
    print("( Reminder: 0=Rock, 1=Paper, 2=Scissors )")
    playerChoice = int(input("Make your move!\n"))
    if playerChoice in choices:
        return TestChoices(playerChoice)
    else:
        print("Not a valid choice, please try again.")
        Round()

def TestChoices(pChoice):

    print("Your Choice")
    HandImage(pChoice)

    computerChoice = random.choice(choices)
    print("\n Computer's Choice")
    HandImage(computerChoice)

    if pChoice == computerChoice:
        return 2
    elif (pChoice - computerChoice) in winnerValues:
        return 1
    else:
        return 0

def HandImage(choice):
    if choice == 0:
        print('''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    elif choice == 1:
        print('''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
        ''')
    else:
        print('''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')


choices = [0,1,2]
winnerValues = [1,-2]
print("Welcome to the game of rock paper and scissors!")
Game()