# Asmeninis pasveikinimas

vartotojas = input("Iveskite savo pilna varda: ")

tarpas = vartotojas.find(" ")
vardas = vartotojas[:tarpas]

vardas_didziosiom = vardas.upper()

pasisveikinimas = f"Labas, {vardas_didziosiom}, sveiki atvyke!"

print(pasisveikinimas)
