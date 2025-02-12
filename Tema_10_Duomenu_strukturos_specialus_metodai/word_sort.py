# You have a list of ten random words which starts with letters A, C, or P.

# Write a function that takes a list of the word_list and prints new list 
# with all words that starts with letter P.


from typing import List


# def word_sort(word_list: List[str]) -> List[str]:
#     words_starting_p: List[str] = []
#     for word in word_list:
#         if word.upper()[0] == "P":
#             words_starting_p.append(word)
#     print(words_starting_p)


def word_sort(word_list: List[str]) -> List[str]:
    return [name for name in word_list if name.upper().startswith('P')]


word_list = ["Arc", "Aunt", "Cat", "Cold", "pay", "Panda", "Apple", "Cake", "People", "Array"]
print(word_sort(word_list))