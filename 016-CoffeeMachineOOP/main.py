# NOTE: Do not modify any files except main.py

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
coin_bank = MoneyMachine()

# TODO 1) Print Report
# TODO 2) Check resources sufficient?
# TODO 3) Process coins
# TODO 4) Check transaction successful?
# TODO 5) Make Coffee

# MAIN
is_on = True
while is_on:
    print('☕ What drink would you like? ☕')
    print(menu.get_items())
    user_choice = input('Make a selection: ')
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        print('\nResource Report:')
        coffee_maker.report()
        print('\nMoney Report:')
        coin_bank.report()
    elif user_choice in menu.get_items():
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and coin_bank.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print("Invalid selection")
