# calculator.py -> Makes basic math calculations (+, -. *. /, **)


def add(number_1: float, number_2: float):
    return number_1 + number_2

def substract(number_1: float, number_2: float):
    return number_1 - number_2

def multiply(number_1: float, number_2: float):
    return number_1 * number_2

def divide(number_1: float, number_2: float):
    if number_2 != 0:
        return number_1 / number_2
    else:
        return "Cannot divide by zero!"




