# Raidžių dažnių žodynas


def symbol_count(user_text: str) -> dict:
    word_dictionary = {}
    for character in user_text:
        if character in word_dictionary:
            word_dictionary[character] += 1
        else:
            word_dictionary[character] = 1
    return word_dictionary


user_text = input("Enter text: ")
letter_occurence = symbol_count(user_text)
print(letter_occurence)




