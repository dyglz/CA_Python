
# Create 3 separate list (item, price, quanity)
# Ask for user input for: number of items 
# (number of baskets to be created)
# Basket is created randomly picking one value from each list
# Example basket = {"item":toy, "price": 35, "amount": 56}
# Created baskets are put in a final list.
# 
# Result
# There can be only different items on the final list 
# (can't be same item in different baskets)
# 1. index of the basket/item with highest price
# 2. item is with lowest price
# 3. item with most monetary value (price * quantity)


import random

store_items = ["apple", "cabbage", "pineapple", "bread", "beer", "banana", "meat", "beef", "chicken", "juice"]
prices_list = [3, 4, 5, 7, 2, 1, 10, 34, 12, 9]
items_quantity = [50, 40, 15, 20, 100, 30, 10, 1, 2, 3]
baskets_dict = {}


def basket_generator(number_of_baskets: int) -> dict:
    random.shuffle(prices_list)
    random.shuffle(items_quantity)
    for item in range(number_of_baskets):
        baskets_dict[item+1] = {
            "item": store_items[item],
            "price": int(prices_list[item]), 
            "quantity": int(items_quantity[item])}
    return baskets_dict  

# Index of most expensive item
def highest_price(baskets_dict: dict) -> int:
    max_price = None
    max_price_index = None
    for i, basket in baskets_dict.items():
        price = basket['price']
        if max_price == None:
            max_price = price
            max_price_index = i
        elif price > max_price:
            max_price = price
            max_price_index = i
    return max_price_index

# Item with lowest price
def lowest_price(baskets_dict: dict) -> str:
    min_price = None
    min_price_index = None
    for i, basket in baskets_dict.items():
        price = basket['price']
        if min_price == None:
            min_price = price
            min_price_index = basket['item']
        elif price < min_price:
            min_price = price
            min_price_index = basket['item']
    return min_price_index
    
# Item with highest monetary value
def highest_monetary_value(baskets_dict: dict) -> str:
    highest_value = 0
    highest_value_index = None
    for basket in baskets_dict.values():
        value = basket['price'] * basket['quantity']
        if value > highest_value:
            highest_value = value
            highest_value_index = basket['item']
    return highest_value_index



while True:
    try:
        number_of_baskets = int(input("Please enter the number of baskets you want to generate [5-10]: "))
        if 5 <= number_of_baskets <= 10:
            basket_generator(number_of_baskets)
            for i, basket in baskets_dict.items():
                print(f"Basket {i}: {basket}")
            break
        else:           
            print("Error. Please enter a number in range [5, 10]! ")
    except ValueError:
        print("Error. Wrong input! ")



# Result/Output
print(f"\nIndex of the basket with highest price: {highest_price(baskets_dict)}")
print(f"Item with the lowest price: {lowest_price(baskets_dict)}")
print(f"Item with the highest monetary value: {highest_monetary_value(baskets_dict)}")