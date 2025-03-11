# Ar skaičius yra kvadratas?

# Parašykite programą, kuri patikrina, ar 
# pateiktas sveikasis skaičius yra kito skaičiaus kvadratas.

import math

def perfect_square(user_number: int) -> bool:
    root = math.sqrt(user_number)
    print(root)
    if root * root == user_number:
        return True
    else:
        return False


user_number = int(input("Enter a number: "))
result = perfect_square(user_number)
print(f"Is {user_number} a perfect square? {result}")