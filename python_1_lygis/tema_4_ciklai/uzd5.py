# Atspausdinti skaičius ir jų vidurkį

# sukuriu empty list
input_numbers = []

while True:
    number = input("Įveskite skaičių (arba įveskite 'pabaiga'): ")
    if number == "pabaiga":
        break

    input_numbers.append(float(number))

if len(input_numbers) > 0:
    sum = sum(input_numbers)
    average = sum / len(input_numbers)
else:
    average = 0

print(f"Skaičiai: {input_numbers}")
print(f"Vidurkis: {average}")