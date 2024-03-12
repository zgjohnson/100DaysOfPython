from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print("Welcome to the 'Coffee Machine' ☕!")

machine_on = True
while machine_on:
    order = input(f"What would you like? ({coffee_menu.get_items()}): ")
    if order == 'off':
        machine_on = False
        continue
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = coffee_menu.find_drink(order)
        if drink and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

print(f"Powering Down.")
