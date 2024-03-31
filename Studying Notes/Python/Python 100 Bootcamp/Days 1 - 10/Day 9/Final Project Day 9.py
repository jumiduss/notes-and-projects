logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
# The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually.

# # Welcome to the secret auction program.  

# This is Step 1 
#   A gavil and a print statement


# # What is your name?: Angela
# # What's your bid?: $123

# This is Step 2
#   A function call to request a name and price.
#   Add that name and price to a dictionary or list.
#   The dollar sign should print on the input to avoid type errors


# # Are there any other bidders? Type 'yes' or 'no'.
# # yes

# This is Step 3
#   The function call returns here, then asks for user input.
#   While Loop with if statement question makes the most sense



# # If there are other bidders, the screen should clear, 
# #   so you can pass your phone to the next person. 

# This is Step 4
#   If yes, clear screen and repeat function call.


# # If there are no more bidders, 
# #   then the program should display the name of the winner and their winning bid.
# # The winner is Elon with a bid of $55000000000

# This is Step 5
#   If no, search the set for the highest number
#   Once found, return the name associated to that number
import os

print(logo)
print("Welcome to the secret auction program.")

bidder_dictionary = {}

auction_running = True
while auction_running:
    name = input("What is your name?\n")
    n_bid = int(input("What's your bid amount?\n$"))
    
    bidder_dictionary[n_bid] = name
    another_bidder = input("Are there any other bidders?").lower()
    
    if another_bidder in ['yes','y']:
        os.system('clear')
        continue

    else:    
        max_bid = 0
        max_bidder = ''
        for key in bidder_dictionary:
            if key > max_bid:
                max_bid = key
                max_bidder = bidder_dictionary[key]
        auction_running = False

print("The winner is {} with a bid of ${}!".format(max_bidder,str(max_bid)))