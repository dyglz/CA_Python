# Žodžių dažnių analizė

# Užduoties instrukcijos:

# Paprašykite vartotojo įvesti teksto bloką.
# Patikrinkite, ar įvestis nėra tuščia.
# Normalizuokite tekstą, 
# konvertuodami jį į mažąsias raides ir pašalindami skyrybos ženklus.
# Naudodami žodyną, suskaičiuokite kiekvieno žodžio dažnį.
# Surikiuokite žodyną pagal žodžių dažnį, 
# mažėjimo tvarka, ir atspausdinkite rezultatus.


text_dictionary = {}



while True:
    text_to_count = input("Enter a phrase to count the frequency of words (or 'end'):\n").lower()
    if text_to_count == "end":
        print("End of program.")
        break
    
#     if text_to_count:
            







# # Simbolių dažnis simbolių eilutėje

# word_dict = {}
# user_input = input("Please enter a phrase to count the frequency of each symbol:\n ")

# for character in user_input:
#     if character in word_dict:
#         word_dict[character] += 1
#     else:
#         word_dict[character] = 1

# # rikiuojame, kad būtų išlaikyta nuosekli tvarka
# for char, freq in sorted(word_dict.items()):
#     print(f"{char}: {freq}")