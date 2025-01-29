# Sveikųjų skaičių suma ir vidurkis

sum = 0

for i in range(10):
    number = int(input(f"Įveskite sveikąjį skaičių {i + 1}: "))
    sum += number

average = (sum / 10) 
print(f"Suma: {sum}, Vidurkis: {average} ")