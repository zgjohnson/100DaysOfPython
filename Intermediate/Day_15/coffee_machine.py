MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00
}


def print_report():
    print("Here are the current resource levels:")
    print(f"\tWater: {resources['water']}ml")
    print(f"\tMilk: {resources['milk']}ml")
    print(f"\tCoffee: {resources['coffee']}g")
    print("\tMoney: ${:0.2f}".format(resources['money']))


def check_resources(drink):
    for ingredient in drink['ingredients']:
        if resources[ingredient] < drink['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def collect_payment():
    print("Please insert coins: ")
    quarters = 0.25 * int(input("How many quarters?: ") or 0)
    dimes = 0.10 * int(input("How many dimes?: ") or 0)
    nickles = 0.05 * int(input("How many nickles?: ") or 0)
    pennies = 0.01 * int(input("How many pennies?: ") or 0)
    return quarters + dimes + nickles + pennies


def verify_payment(drink_cost):
    payment = collect_payment()
    if payment < drink_cost:
        print(
            f"Sorry that's not enough money. Your order costs ${"{:0.2f}".format(drink_cost)}. "
            f"Money refunded: ${"{:0.2f}".format(payment)}")
        return False
    else:
        resources['money'] += drink_cost
        print(f"Here is ${"{:0.2f}".format(payment - drink_cost)} in change.")
        return True


def make_drink(drink_ingredients):
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]


def fulfill_order(order, drink):
    if check_resources(drink) and verify_payment(drink['cost']):
        make_drink(drink['ingredients'])
        print(f"Here is your {order}. Enjoy!")


def coffee_machine():
    machine_on = True
    while machine_on:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == 'off':
            machine_on = False
            continue
        elif order == 'report':
            print_report()
        elif order in MENU:
            fulfill_order(order, MENU[order])
        else:
            print("We do not serve that item. Please try again.")


print("Welcome to the 'Coffee Machine' ☕!")

coffee_machine()

print("Powering off. ")
