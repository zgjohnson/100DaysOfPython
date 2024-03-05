from calculator_art import logo


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)
    should_continue = True
    number1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))

        operation = operations[operation_symbol]
        answer = operation(number1, number2)

        print(f'{number1} {operation_symbol} {number2} = {answer}')
        decision = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. "
                         f"Type 'q' to quite: ")

        if decision == 'y':
            number1 = answer
        elif decision == 'q':
            should_continue = False
        else:
            should_continue = False
            calculator()


calculator()
