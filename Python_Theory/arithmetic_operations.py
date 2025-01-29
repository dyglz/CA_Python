# Veiksmai (operacijos) su int ir float:

print("Veiksmai (operacijos) su int ir float")
a = int(input("Įveskite pirmą sveikąjį skaičių: "))
b = int(input("Įveskite antrą sveikąjį skaičių: "))

# x + y | Suma
c = a + b
print(f"Suma {' ' * 29}{a} + {b} = {c}")

# x - y | Skirtumas
c = a - b
print(f"Skirtumas {' ' * 24}{a} - {b} = {c}")

# x * y | Sandauga
c = a * b
print(f"Sandauga {' ' * 25}{a} * {b} = {c}")

# x / y | Dalmuo (float)
c = a / b
print(f"Dalmuo (float) {' ' * 19}{a} / {b} = {c}")

# x // y | Dalmens sveikoji dalis (float)
c = a // b
print(f"Dalmens sveikoji dalis (float) {' ' * 3}{a} // {b} = {c}")

# x % y | Liekana (modulis)
c = a % b
print(f"Liekana (modulis) {' ' * 16}{a} % {b} = {c}")

# x ** y | x kėlimas y laipsniu
c = a ** b
print(f"x kėlimas laipsniu y {' ' * 13}{a} ** {b} = {c}")
