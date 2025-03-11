# Skaičių karas

# Parašykite funkciją, kuri nustato skirtumą 
# tarp lyginių ir nelyginių skaičių sumų. 
# Sveikieji skaičiai perduoti į funkciją kaip individualūs argumentai.

def war_of_numbers(*args):
    even_sum = sum(x for x in args if x % 2 == 0)
    odd_sum = sum(x for x in args if x % 2 != 0)
    return abs(even_sum - odd_sum)

# abs() function returns the absolute value of the specified number.

print(war_of_numbers(2, 8, 7, 5))
print(war_of_numbers(12, 90, 75))
print(war_of_numbers(5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243))