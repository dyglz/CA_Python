
# letter count in a phrase

# def count(word, letter):
#     letter_count = 0
#     for i in word:
#         if i == letter:
#             letter_count = letter_count + 1
#     return letter_count

try:
    word = input("Please enter a phrase: ")
    letter = input("Which letter are we counting? ")

    letter_count = word.count(letter)
    print(f"There are {letter_count} letter '{letter}' in word '{word}'")
except ValueError:
    print("Wrong input!")
