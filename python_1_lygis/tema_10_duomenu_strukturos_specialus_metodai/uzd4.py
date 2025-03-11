# Suskaičiuokite žodžius, ilgesnius nei penki simboliai


# def word_lenght(user_text: str) -> int:
#     answer_list = []
#     for word in user_text.split():
#         if len(word) > 5:
#             answer_list.append(word)
#     print(len(answer_list))


def word_lenght(user_text: str) -> int:
    return len([word for word in user_text.split() if len(word) > 5])

user_text = input("Enter text: ")
words_longer_than_five_symbols = word_lenght(user_text)
print(f"Words count (lenght > 5): {words_longer_than_five_symbols}")

