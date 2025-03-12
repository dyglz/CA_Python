# Matematinės funkcijos

import logging
import math



logging.basicConfig(
    filename="uzd2_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)



def sum_of_numbers(*args) -> float:
    total_sum = sum(args)
    logging.info(f"The sum of {args} is: {total_sum}")
    return total_sum


def sqrt_of_number(number: float) -> float:
    try:
        root = math.sqrt(number)
        logging.info(f"The square root of {number} is: {root}")
        return root
    except TypeError:
        logging.exception(f"Error: Square root cannot be calculated. Input must be a number")
        return f"Error: Cannot calculate square root of '{number}' "


def count_characters(sentence: str) -> int:
    character_count = len(sentence)
    logging.info(f"The character count in the sentence '{sentence}' is: {character_count} ")
    return character_count


def divide_numbers(number_1: float, number_2: float) ->float:
    try:
        result = number_1 / number_2
        logging.info(f"Division: {number_1} / {number_2} = {result}")
        return result
    except ZeroDivisionError:
        logging.exception(f"Division by zero is not allowed. Cannot divide {number_1} by {number_2}")
        return "Error. Division by 0 is not allowed."




print(sum_of_numbers(10, 20, 30))
print(sqrt_of_number(16))
print(sqrt_of_number("sixteen"))  # This will log an error
print(count_characters("Python logging is useful"))
print(divide_numbers(10, 2))
print(divide_numbers(10, 0))  # This will also log an error