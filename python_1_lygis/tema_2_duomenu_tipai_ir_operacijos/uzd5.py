# Palūkanų skaičiuoklė

pradine_suma = float(input("Iveskite pradine suma: "))
palukanu_norma = float(input("Iveskite palukanu norma (%): "))
laikas = float(input("Iveskite laika (metais): "))

palukanos = (pradine_suma * palukanu_norma * laikas) / 100

print("Paprastosios palukanos yra ", palukanos)