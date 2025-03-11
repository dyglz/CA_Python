# Simbolių dažnis simbolių eilutėje

word_dict = {}
user_input = input("Please enter a phrase to count the frequency of each symbol:\n ")

for character in user_input:
    if character in word_dict:
        word_dict[character] += 1
    else:
        word_dict[character] = 1

# rikiuojame, kad būtų išlaikyta nuosekli tvarka
for char, freq in sorted(word_dict.items()):
    print(f"{char}: {freq}")