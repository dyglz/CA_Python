# Trys moduliai

from calculator import add, substract, multiply, divide
from string_ops import to_uppercase, to_lowercase, reverse_string, count_characters
from list_ops import add_to_list, remove_from_list, count_items, reverse_list


print("String operations: ")
user_input = input("Enter a phrase: ")
print(f"Uppercase: {to_uppercase(user_input)}")
print(f"Lowercase: {to_lowercase(user_input)}")
print(f"Reversed: {reverse_string(user_input)}")
print(f"Character count: {count_characters(user_input)}")


print("Float operations: ")
number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))
print(f"Sum: {add(number_1, number_2)}")
print(f"Subtraction: {substract(number_1, number_2)}")
print(f"Multiplication: {multiply(number_1, number_2)}")
print(f"Division: {divide(number_1, number_2)}")


print("List operations: ")
my_list = [1, 2, 3, 4, 5]
print(f"Add 6 to list: {add_to_list(my_list, 6)}")
print(f"Remove 3 from list: {remove_from_list(my_list, 3)}")
print(f"Item count in list: {count_items(my_list)}")
print(f"Reversed list: {reverse_list(my_list)}\n")
