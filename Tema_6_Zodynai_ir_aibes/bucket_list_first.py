import random

items_list = ["apple", "caffe", "book", "tea", "beer", "cola", "lemon", "orange", "avocado", "pineapple"]
prices_list = [1, 3, 10, 2, 4, 2, 1, 2, 3, 5]
quantity = [50, 40, 15, 20, 100, 30, 10, 60, 70, 80]

my_dictionary = dict(zip(items_list, zip(prices_list, quantity)))

 
while True:
    user_input = int(input("Hom many baskets you wanted to create (min 5, max 10): "))
    if user_input < 5 or user_input > 10:
        print("Wrong input. Please enter the number between 5 and 10!")
        break
    if 5 < user_input <= 10:
        for x in range(user_input):
        my_random = random.choice(list(my_dictionary.items()))
        print(my_random)


