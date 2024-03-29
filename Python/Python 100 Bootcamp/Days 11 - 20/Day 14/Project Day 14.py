import random,os
from project_resources import logo,data,vs

def new_screen():
    os.system('clear')
    print(logo)

def choices(name=None):
    person_list = random.sample(data,2)
    return person_list[0],person_list[1]

def print_person(choice_letter,person_info):
    print("Compare {}: {}, a {} from {}.".format(choice_letter,person_info['name'],person_info['description'],person_info['country']))

def print_round(extra_string=''):
    new_screen()
    print(extra_string)
    a,b = choices()
    print_person('A',a)
    print(vs)
    print_person('B',b)
    return a['follower_count'],b['follower_count']

def check_numbers(a,b,choice):
    if (choice == 'A' and a > b) or (choice =='B' and b > a ):
        return True
    else:
        return False

def game():
    
    running = True
    final_score = 0
    win_message = ''
    while running:
        a,b = print_round(win_message)
        user_choice = input("Who has more followers> Type 'A' or 'B': ")
        if not check_numbers(a,b,user_choice):
            new_screen()
            print("Sorry, that's wrong. Final score: {}".format(final_score))
            running = False
        else:
            final_score += 1
            win_message = "You're right! Current score: {}\n".format(final_score)

game()