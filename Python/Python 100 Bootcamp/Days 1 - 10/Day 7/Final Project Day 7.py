# Step 1

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# Random means import random module 
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# Step 2

#TODO-1: - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'.
# get solution length then multiple by list with 1 element = '_'
#TODO-2: - Loop through each position in the chosen_word. If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# Same for loop as 1, but set letter to display
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# print with string join on the display array

# Step 3

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# While the user can guess, perform the game. Guess is false on lose or win condition

# Step 4

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#TODO-2: - If guess is not a letter in the chosen_word, change number of lives
#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

# Step 5

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#TODO-2: - Import the stages from hangman_art.py and make this error go away.
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.


import random 
from extras import logo, stages, word_list

print(logo)
solution = random.choice(word_list)

display = ['_']*len(solution)

lives = 6

can_guess = True

while can_guess:
    print(stages[lives])
    print(' '.join(display))

    user_guess = input("\n\nGuess a letter in the word!").lower()
    correct_answer = False

    for i, letter in enumerate(solution):
        if user_guess == letter:
            display[i] = letter
            correct_answer = True

    if correct_answer == False:
        lives -= 1
        print("That letter is not in the word!")
    else:
        print("Correct!")

    if lives == 0 or '_' not in display:
        print("\n\nGame Over")
        if lives == 0:
            print("You Lose!")
        else:
            print("You Win!")
        can_guess = False