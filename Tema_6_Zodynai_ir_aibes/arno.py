import random

items_list = ["apple", "cabbage", "pineapple", "bread", "beer", "banana", "meat", "beef", "chicken", "juice"]
prices_list = [3, 4, 5, 7, 2, 1, 10, 34, 12, 9, 12]
quantity = [50, 40, 15, 20, 100, 30, 10, 1, 2, 3, 4]


while True:
        baskets_quantity = int(input("How many baskets would you like me to generate? 5-10 "))
        final_list = []
        if baskets_quantity < 5 or baskets_quantity > 10:
            print("Wrong input. Please, choose between 5-10!")

        else:   
            for i in range(baskets_quantity):
                randomized_item = random.choice(items_list)
                price_index = int(items_list.index(randomized_item))
                basket = {"item":randomized_item, "price":prices_list[price_index], "quantity":random.choice(quantity)}
                items_list.remove(randomized_item)
                final_list.append(basket)
        print(final_list)
        break

highest_value = (max(d["price"] for d in final_list))
print(f"Most expensive item costs {highest_value} euros.")
print(type(final_list))
print(len(final_list))

index = next((i for i, d in enumerate(final_list) if d.get('price') == highest_value), None)
for d in final_list:
     print(d)

print(type(highest_value))  # Print the type of the highest_value
for d in final_list:
    print(d.get('price'), type(d.get('price')))


print(index)

