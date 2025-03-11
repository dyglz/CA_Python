# Žodžių dažnių analizė

# Užduoties instrukcijos:

# Paprašykite vartotojo įvesti teksto bloką.
# Patikrinkite, ar įvestis nėra tuščia.
# Normalizuokite tekstą, 
# konvertuodami jį į mažąsias raides ir pašalindami skyrybos ženklus.
# Naudodami žodyną, suskaičiuokite kiekvieno žodžio dažnį.
# Surikiuokite žodyną pagal žodžių dažnį, 
# mažėjimo tvarka, ir atspausdinkite rezultatus.

import string

def normalize_text(text_to_count: str) -> str:
    text_to_count = text_to_count.replace("'", "")
    text_to_count = text_to_count.translate(str.maketrans("", "", "0123456789"))
    text_to_count = text_to_count.translate(str.maketrans("", "", string.punctuation))
    return text_to_count


while True:
    text_to_count = input("Enter a phrase to count the frequency of words (or 'end'):\n").lower()
    if text_to_count == "end":
        print("End of program.")
        break
    elif text_to_count == "":
        print("Nothing entered!")
        continue
    elif text_to_count != "":
        normalized_text = normalize_text(text_to_count)
        words = normalized_text.split()
        word_count_dictionary = {}

        for word in words:
            if word in word_count_dictionary:
                word_count_dictionary[word] += 1
            else:
                word_count_dictionary[word] = 1

        for word, freq in sorted(word_count_dictionary.items()):
            print(f"{word} : {freq}")