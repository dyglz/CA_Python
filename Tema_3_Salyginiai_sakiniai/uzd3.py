# Maža skaičiuoklės programa

number_1 = float(input("Įveskite pirmą skaičių: "))
symbol = input("Įveskite simbolį (+, -, *, /): ")
number_2 = float(input("Įveskite antrą skaičių: "))
answer = "negalimas. Neleistini simboliai įvestyje."

if symbol == "+":
    answer = number_1 + number_2
elif symbol == "-":
    answer = number_1 - number_2
elif symbol == "*":
    answer = number_1 * number_2
elif symbol == "/":
    answer = number_1 / number_2
else:
    print("Neteisinga įvestis")

print(f"{number_1} {symbol} {number_2} rezultatas yra {answer}")    