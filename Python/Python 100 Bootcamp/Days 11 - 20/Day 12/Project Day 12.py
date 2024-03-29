from project_resources import logo
import random
print(logo)

print("Welcome to the number guessing game.")

def target_number():
    return random.randrange(1,101,1)

def player_guess():
    return input("What is your first guess?")

def game_start():
    n_guesses = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' \n    ")
    if difficulty in ['e','easy','']:
        n_guesses = 10
    else:
        n_guesses = 5
    print("I'm thinking of a number between 1 and 100.")
    game(n_guesses)
    
    if input("Would you like to play again?\nType y/n:").lower() in ['','y']:
        game_start()
    
def game(attempts):
    running = True
    target = target_number()
    tries = attempts
    while running:
        print("You have {} attempts".format(tries))
        guess = int(input("What is your guess?\n    "))
        
        if target > guess:
            print("You are too low.")
            tries -= 1
        elif target < guess:
            print("You are too high.")
            tries -= 1
        elif target == guess:
            print("You got the right number!\nThe target number was {}!\n\nYou Win!\n\n\n\n\n".format(target))
            running = False
            
        if tries == 0:
            print("You've run out of guesses\n\nThe target number was {}\n\n GAME OVER".format(target))
            running = False

game_start()