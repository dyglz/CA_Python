
# 1
from calculator import add, substract, multiply, divide

print(substract(2, 2))
print(multiply(2, 2))
print(divide(2, 2))
print(f"I am addidng 2 and 2: {add(2, 2)}")


# 2
# import calculator 

# print(calculator.add(2, 2))



# 3
# import calculator as calc

# print(calc.divide(2, 2))



# 4 bad practice
# from calculator import *

# print(substract(2, 2))
# print(multiply(2, 2))
# print(divide(2, 2))


# 5
from echo import echo

print(f"I am in main.py __name__ is {__name__}")
print(echo(text="tekstas kvadratu", repetitions=5))


