from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu,MenuItem



menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_is_on = True

while machine_is_on:
    wanna_coffee = input('wanna coffee ☕ (y/n)? ')
    if wanna_coffee == 'y':
        machine_is_on = True
    else:
        machine_is_on = False
        print('Okkay, cool!! have a good day!')
        break
    available_menu = menu.get_items()
    order_name = input(f'please select which coffee would you like to have? {available_menu}')
    print('let me check if the order is available')
    is_available = menu.find_drink(order_name)
    if is_available:
        print(f'Okkay we have {is_available.name}')
        print("Ingredients required:")
        for ingredient, amount in is_available.ingredients.items():
            print(
                f"- {ingredient.capitalize()}: {amount}ml" if ingredient != "coffee" else f"- {ingredient.capitalize()}: {amount}g")
        print(f"Cost: ${is_available.cost}")
        resource_sufficient = coffee_maker.is_resource_sufficient(is_available)

        if resource_sufficient:
            payment_successful = money_machine.make_payment(is_available.cost) # Store the result
            if payment_successful:
                coffee_maker.make_coffee(is_available)
                money_machine.report()
            else:
                print("Payment failed. Please try again.") # add message
        else:
            print('Sorry, but we don\'t have enough resources')
            coffee_maker.report()
    else:
        print(f'Sorry but we only have {available_menu}')
