# Skriptas ir modulis

# calculator.py -> Makes basic math calculations (+, -. *. /)
from calculator import add, substract, multiply, divide


print("Select arithmetic operation:")
print("1. Add\n2. Substract\n3. Multiply\n4. Divide")
try: 
    user_selection = int(input("Enter your selection: "))
    if 1 <= user_selection <= 4:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))

            if user_selection == 1:
                print(add(number_1, number_2))
            elif user_selection == 2:
                print(substract(number_1, number_2))
            elif user_selection == 3:
                print(multiply(number_1, number_2))
            elif user_selection == 4:
                print(divide(number_1, number_2))
    else:
        print("Invalid selection! ")

except Exception as e:
    print(e)








# sum = addition(number_1, number_2)
# print(f"{number_1} + {number_2} = {sum:.2f}")

# difference = substraction(number_1, number_2)
# print(f"{number_1} - {number_2} = {difference:.2f}")

# product = multiplication(number_1, number_2)
# print(f"{number_1} * {number_2} = {product:.2f}")

# quotient = division(number_1, number_2)
# print(f"{number_1} / {number_2} = {quotient:.2f}")

# power = exponentation(number_1, number_2)
# print(f"{number_1} ^ {number_2} = {power:.2f}")
