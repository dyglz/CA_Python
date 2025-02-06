import random

items_list = ["apple", "cabbage", "pineapple", "bread", "beer", "banana", "meat", "beef", "chicken", "juice"]
prices_list = [3, 4, 5, 7, 2, 1, 10, 34, 12, 9]
quantity = [50, 40, 15, 20, 100, 30, 10, 1, 2, 3]


while True:
        baskets_quantity = int(input("How many baskets would you like me to generate? 5-10 "))
        final_list = []
        #I'll delete items afterwards so keeping them in another dict for now
        item_price_dict = dict(zip(items_list, prices_list))
        if baskets_quantity <5 or baskets_quantity >10:
            print("Wrong input. It must be between 5 and 10")
            continue

        else:   
            for i in range(baskets_quantity):
                randomized_item = random.choice(items_list)
                price_index = items_list.index(randomized_item)
                basket = {"item":randomized_item, "Price":prices_list[price_index], "Quantity":random.choice(quantity)}
                items_list.remove(randomized_item)
                final_list.append(basket)
        break


min_price = None
print(final_list)
for basket in final_list:
    print(basket["Price"])
    price = basket["Price"]
    if min_price ==None:
         min_price = price
    elif price <min_price:
        min_price = price

print(f"Maziausia kaina yra {min_price}")