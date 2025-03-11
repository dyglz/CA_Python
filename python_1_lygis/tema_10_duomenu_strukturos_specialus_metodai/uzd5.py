# Raidžių dažnių žodynas


# def symbol_count(user_text: str) -> dict:
#     word_dictionary = {}
#     for character in user_text:
#         if character in word_dictionary:
#             word_dictionary[character] += 1
#         else:
#             word_dictionary[character] = 1
#     return word_dictionary

def symbol_count(user_text: str) -> dict:
    return {i: user_text.lower().count(i) for i in user_text.lower() if i.isalpha()}

# string.isalpha() returns True if all the characters are alphabet letters
# (a-z); not alphanumeric: (space)!#%&? etc.

user_text = input("Enter text: ")
letter_occurence = symbol_count(user_text)
print(letter_occurence)




