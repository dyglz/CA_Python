
# list comprehension
names = ["Albert", "Alma", "Joseph", "Zoro"]
print([name for name in names if name.startswith("A") or "e" in name])


# dictionary comprehesion
squares = {i: i * i for i in range(10)}
print(squares)



# enumerate(iterable, start=)
def even_items(numbers: list) -> list:
    return [v for i, v in enumerate(numbers, start=1) if not i % 2]

seq = list(range(1, 11))
print(even_items(seq))



# MATH LIBRARY
import math

# math.pi čia yra konstanta, kurią galime iškart naudoti programose
area = 5 * 5 * math.pi 

# 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1
math.factorial(7)

# gauti float reikšmės „grindis“ (floor) arba „lubas“ (ceiling)
print(math.ceil(6.1))
print(math.floor(-11.1))

# kėlimas laipsniu 5^5
print(math.pow(5, 5))

# kvadratinė šaknis
print(math.sqrt(9))





