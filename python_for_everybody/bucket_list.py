
# Create 3 separate list (item, price, quanity)
# Ask for user input for: number of items 
# (number of baskets to be created)
# Basket is created randomly picking one value from each list
# Example bucket = {"item":toy, "price": 35, "amount": 56}
# Created buckets are put in a final list.
# 

import random

store_items = ["apple", "cabbage", "pineapple", "bread", "beer", "banana", "meat", "beef", "chicken", "juice"]
prices_list = [3, 4, 5, 7, 2, 1, 10, 34, 12, 9]
items_quantity = [50, 40, 15, 20, 100, 30, 10, 1, 2, 3]
baskets_dict = {}


def basket_generator(number_of_baskets):
    
    random.shuffle(prices_list)
    random.shuffle(items_quantity)
    for item in range(number_of_baskets):
        baskets_dict[item+1] = {
            "item": store_items[item],
            "price": int(prices_list[item]), 
            "quantity": int(items_quantity[item])}
    return baskets_dict  


while True:
    try:
        number_of_baskets = int(input("Please enter the number of baskets you want to generate [5-10]: "))
        if 5 <= number_of_baskets <= 10:
            basket_generator(number_of_baskets)
            print(baskets_dict)
            break
        else:           
            print("Error. Please enter a number in range [5, 10]! ")
    except ValueError:
        print("Error. Wrong input! ")


# Result: print:
# 
# There can be only different items on the final list 
# (can't be same item in different buckets)
# index of the basket/item which has highest price
highest_price = max([basket['price'] for basket in baskets_dict.values()])
print(highest_price)
print(len(baskets_dict))

# Which item is with lowest price? 
lowest_price = min([basket['price'] for basket in baskets_dict.values()])
print(lowest_price)

# Which item has most monetary value in store? (highest_price*quantity)




# min_price = None
# final_index = None
# for i, basket in enumerate(baskets_dict):
#      price = basket['price']
#      if min_price == None:
#           min_price = price
#           final_index = i
#           print(f"Maziausios kainos indeksas: {i}")
#      elif price < min_price:
#           min_price = price
#           final_index = i
#           print(f"Maziausios kainos indeksas: {i}")
# print(f"Maziausia kaina yra {min_price}")
# print(f"Maziausios kainos indeksas: {i} : {baskets_dict[final_index]}")




