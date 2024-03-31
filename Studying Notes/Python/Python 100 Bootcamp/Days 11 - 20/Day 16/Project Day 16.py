# Starting Code Start
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# Starting Code End

running = True 
while running:
    menu = Menu()
    machine = CoffeeMaker()
    atm = MoneyMachine()

    choice = input("Select an Option:\n{}\n".format(menu.get_items()))
    if choice == 'report':
        print("{}\n{}".format(machine.report(),atm.report()))
    elif choice == 'off':
        break
    else:
        item = menu.find_drink(choice)
        print("Please insert: ${:.2f}".format(item.cost))
        if item:
            if machine.is_resource_sufficient(item):
                if atm.make_payment(item.cost):
                    machine.make_coffee(item)