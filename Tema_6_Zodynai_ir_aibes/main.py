# 21.01.2025

# Žodynai

my_list = [1, 2, 3, 4, 5]
my_dictionary = {"Antanas" : 1, "Jonas" : 2, "Petras" : 3}

print(my_dictionary)

# print(my_dictionary["Antanas"]) # error, jei variable neegzistuojantis
# print(my_dictionary.get("Jonas")) 
# print(my_dictionary.get("Mindaugas")) # output None, jei variable neegzistuoja

my_dictionary["Antanas"] = 100
print(my_dictionary)

# del my_dictionary["Antanas"]
value = my_dictionary.pop("Antanas")
print(value)
print(my_dictionary)













