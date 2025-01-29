# Sukurti tuščią sąrašą, skirtą skaičiams saugoti
numbers = []

while True:
    # Paprašyti vartotojo įvesti skaičių arba „pabaiga“, kad užbaigtų
    entry = input("Įveskite skaičių (arba įveskite 'pabaiga'): ")
    if entry == "pabaiga":
        break
    # Konvertuoti įvestį į float tipo skaičių ir pridėti jį į sąrašą
    numbers.append(float(entry))

# Patikrinti, ar sąrašas nėra tuščias prieš apskaičiuojant vidurkį
if len(numbers) > 0:
    total = sum(numbers)
    average = total / len(numbers)
else:
    average = 0

# Atspausdinti skaičių sąrašą ir vidurkį
print(f"Skaičiai: {numbers}")
print(f"Vidurkis: {average}")