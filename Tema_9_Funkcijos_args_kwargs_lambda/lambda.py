# lambda funkcijas galima apibrėžti be pavadinimo
# vienos eilutės funkcija

# lambda funkcija gali priimti bet kokį argumentų skaičių, 
# bet gali turėti tik vieną išraišką

# Pirmenybė teikiama lambda funkcijai:
# Kai norite, kad funkcija būtų naudojama tik vieną kartą.
# Kai funkcijos apibrėžime yra tik viena išraiška.
# Kai norite užrašyti aiškią sintaksę keliomis kodo eilutėmis.

# paprasta daugybos funkcija:
def multiply(num_1: int, num_2: int) -> int:
    return num_1 * num_2

print(multiply(2, 2))


# lambda funkcija
# option 1:
multiplication = lambda num_1, num_2: num_1 * num_2
print(multiplication(2, 7))


# option 2:
answer = (lambda num_1, num_2: num_1 * num_2)(2, 7)
print(answer)


# option 3:
a = 5
b = 7
answer = (lambda num_1, num_2: num_1 * num_2)(a, b)
print(answer)


