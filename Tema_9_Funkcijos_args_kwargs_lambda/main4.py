# Use lambda functions to sort list of 
# strings by their length and then alphabetically.

words = ['word', 'zebra', 'apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'asd']

# x = sorted(words)
# y = sorted(x, key=len)
# print(y)

sorted_words = sorted(words, key = lambda x: (len(x), x))
print(sorted_words)