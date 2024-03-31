from project_resources import MENU,resources
import os

def check_stock_to_order(q_stock, q_order):
    if q_stock >= q_order:
        return True
    else:
        return False

def payment(price):
    quarters = int(input("Number of Quarters: "))
    dimes = int(input("Number of Dimes: "))
    nickles = int(input("Number of Nickles:"))
    
    payment = (quarters * .25) + (dimes * .1) + (nickles * .05)
    if payment < price:
        print("You haven't reached the items cost.\n\nRefunding your payment of ${:.2f} now.".format(payment))
        return False, 0
    elif payment == price:
        return True,0
        
    else:
        return True, (payment - price)
    
def main_function():
    
    running = True
    while running:
        os.system("clear")
        # ask for a choice
        print("Please select a choice:")
        choices = list(MENU.keys())
        user_choice = input("Please Select a Choice by Typying a Number: \n1: {}\n2: {}\n3: {}\n\n".format(choices[0],choices[1],choices[2]))
        
        #turn off the coffee machine off command
        if user_choice == 'off':
            break
        elif user_choice == 'stock':
            for item in resources:
                print("{} : {}".format(item,resources[item]))
            continue
        else:
            user_choice = int(user_choice) - 1
            choice_dictionary = MENU[choices[user_choice]]
    
    # check resources
        choice_ingredients = choice_dictionary['ingredients']
        below_quantity_stock = []
        
        for ingredient in choice_ingredients:
            choice_ingrediant_on_hand = resources[ingredient]
            choice_ingrediant_needed = choice_ingredients[ingredient]
            
            enough_stock = check_stock_to_order(int(choice_ingrediant_on_hand),int(choice_ingrediant_needed))
            
            if enough_stock is False:
                below_quantity_stock.append(ingredient)
        
        if below_quantity_stock:
            print("We don't have enough supplies for your order: ")
            for item in below_quantity_stock:
                print(item)
            print("Please call our number to restock. ##########")
    
    # return cost
        else:
            cost = choice_dictionary['cost']
            print("The cost of {} is ${:.2f}".format(choices[user_choice],cost))

    # accept coins inputs
    #   check if amount is enough for the order
    #   if not enough, cancel everything and return to main
    #   else return extra coins if applicable
            paid,over = payment(cost)
            if paid:
                if over > 0:
                    print("Returning your change to the tray: ${:.2f}".format(over))
    # make coffee
                print("Making your coffee now!")
                for ingrediant in choice_ingredients:
                    if ingrediant in list(resources.keys()):
                        resources[ingrediant] -= choice_ingredients[ingrediant]
                
    # print enjoy
                print("Enjoy!")
main_function()