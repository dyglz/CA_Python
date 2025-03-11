# TypeError +
# ValueError
# KeyError
# IndexError
# ZeroDivisionError +
# NameError +
# Exception +
# (viso 7)

import logging

def add_two_numbers(number1: int | float, number2: int | float) -> int | float | None:
    logging.info(f"Adding number {number1} and {number2}")
    try:
        sum = number1 + number2
        return f"Result: {number1} + {number2} = {sum}"
    except TypeError as e:
        logging.exception(f"TypeError {e}")
        return f"Type error {e}"
    except Exception as e:
        logging.exception(f"Unexpected error: {e}")
        return f"Unexpected error {e}"

try:
    print(add_two_numbers(2, 4))
except NameError as e:
    logging.exception(f"NameError error: {e}")
    print(f"Name error: {e}")



def convert_to_float(number: int | str) -> float:
    try:
        float_value = float(number)
        print(f"Converted to float {float_value}")
    except ValueError:
        print("This value cannot be converted to a float number! ")

convert_to_float("d")



def divide_numbers(number1: int | float, number2: int | float)-> float | None:
    try:
        division = number1 / number2
    except ZeroDivisionError as e:
        logging.exception(f"ZeroDivisionError: {e}")
        return f"Division by 0 is impossible!"
    else:
        return f"Result: {number1} / {number2} = {division}"

print(divide_numbers(20, 0))
