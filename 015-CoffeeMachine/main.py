from dictionaries import MENU, resources, coins


# TODO 1: Create a function to report the contents of the machine. (print dictionaries.resources)
def report():
    """Shows the amount of resources remaining in the machine."""

    print('\nResource Report:\n')
    for r in resources:
        print(f'{r}: {resources[r]}')


# TODO 2: Function to check if the machine has enough resources for the chosen beverage (return bool)
def check_resources(selection):
    """Checks the machine's remaining resources to determine if there's enough remaining to make the drink selected
    by the user."""
    for i in MENU[selection]["ingredients"]:
        item_ingredient_amount = MENU[selection]["ingredients"][i]

        if item_ingredient_amount > resources[i]:
            print(f'We are out of {i}.')
            return False
    return True


# TODO 3: Coin the coins given by user. (call transaction())
def process_coins(selection):
    """Calculates the total value of coins provided by the user."""
    
    total_input = 0
    quarters_input = int(input('How many quarters do you input? '))
    dimes_input = int(input('How many dimes do you input? '))
    nickels_input = int(input('How many nickels do you input? '))

    for c in range(0, quarters_input):
        total_input += coins["quarter"]
    for c in range(0, dimes_input):
        total_input += coins["dime"]
    for c in range(0, nickels_input):
        total_input += coins["nickel"]

    print(f"Input: ${total_input}")
    if total_input >= MENU[selection]["cost"]:
        return True
    else:
        return False


# TODO 4: Func to "vend the coffee" by reducing the total resources available in the machine.
def vend_coffee(selection):
    """Reduces resources based on user selection and transaction success."""
    print(f"Enjoy your {selection}!")

    for i in resources:
        if i in MENU[selection]["ingredients"]:
            resources[i] -= MENU[selection]["ingredients"][i]
        elif i == "money":
            resources[i] += MENU[selection]["cost"]


def print_menu():
    """Asks the user what they want from the menu"""
    for index, (item, details) in enumerate(MENU.items(), start=1):
        item_name = item.capitalize()
        item_cost = details["cost"]
        print(f'{index}) {item_name} : ${item_cost:.2f}')


# Main Function
again = True
while again == True:
    menu_items = list(MENU.keys())
    print('☕What drink would you like?☕')
    print_menu()
    user_choice = int(input('Make a selection: '))

    if 1 <= user_choice <= len(MENU):
        menu_items = list(MENU.keys())
        chosen_item = menu_items[user_choice - 1]
        print(f'You chose: {chosen_item.capitalize()}')
        if check_resources(chosen_item) == True:
            if process_coins(chosen_item) == True:
                vend_coffee(chosen_item)
            else:
                print("Not enough coins input.")
        else:
            print('Unable to vend due to lack of resources.')
    elif user_choice == 0:
        report()
    else:
        print("Invalid choice: please try again.")

    try_again = input("Make another selection? Y or N").lower()
    if try_again == 'y':
        again = True
    else:
        again = False

