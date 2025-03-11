# Simbolių eilutės, prasidedančios balse

# Sukurkite funkciją, kuri išfiltruoja simbolių eilutes ir grąžina 
# sąrašą, kuriame yra tik tos simbolių eilutės, kurios prasideda balse. 
# Simbolių eilutės (strings) perduotos į funkciją kaip individualūs argumentai.

def start_with_vowel(*strings):
    vowels = set('aeiou')
    return [word for word in strings if word[0].lower() in vowels]

print(start_with_vowel("apple", "banana", "orange", "a", "e", "w", "0"))


# def start_with_vowel(*strings):
#     return list(filter(lambda word: word[0].lower() in "aeiou", strings))

# filter() function returns an iterator where the items are 
# filtered through a function to test if the item is accepted or not.