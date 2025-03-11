# Kazino amžiaus patikrinimas

name = input("Įveskite savo vardą: ")
last_name = input("Įveskite savo pavardę: ")
age = int(input("Įveskite savo amžių: "))

if age >= 21:
    print(f"{name} {last_name}, jums leidžiama patekti į kazino.")
else:
    print(f"{name} {last_name}, jums neleidžiama patekti į kazino.")
