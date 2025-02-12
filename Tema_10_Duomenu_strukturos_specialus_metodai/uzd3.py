#  Suskaičiuokite žodžius su „e“ raide

# def symbol_occurence(user_text: str) -> int:
#     answer_list = []
#     for word in user_text.split():
#         if "e" in word:
#             answer_list.append(word)
#     print(len(answer_list))


def symbol_occurence(user_text: str) -> int:
    return len([word for word in user_text.split() if "e" in word])


user_text = input("Enter text: ")
e_occurence = symbol_occurence(user_text)
print(f"Words with 'e' occurence: {e_occurence}")