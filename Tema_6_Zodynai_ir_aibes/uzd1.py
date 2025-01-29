# Žodynas vartotojo informacijai

name = input("Įveskite savo vardą: ")
surname = input("Įveskite savo pavardę: ")
age = (input("Įveskite savo amžių: "))

user_data = {
    "name" : name,
    "surname" : surname,
    "age" : age
    }

for key, value in user_data.items():
    print(f"{key}: {value}")
