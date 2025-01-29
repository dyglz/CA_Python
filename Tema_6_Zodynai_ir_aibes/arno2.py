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
            print("Netinkamas skaicius, turi but nuo 5 iki 10")
            continue

        else:   
            for i in range(baskets_quantity):
                randomized_item = random.choice(items_list)
                price_index = items_list.index(randomized_item)
                basket = {"item":randomized_item, "Price":prices_list[price_index], "Quantity":random.choice(quantity)}
                items_list.remove(randomized_item)
                final_list.append(basket)
        break


highest_value = max(d["Price"] for d in final_list)
final_price_list = [d['Price'] for d in final_list]
index_of_highest = final_price_list.index(highest_value)
print(f"Index of the final list that contains the must expensive item is {index_of_highest}")

lowest_value = min(d["Price"] for d in final_list)
cheapest_progress = final_price_list.index(lowest_value)
cheapest_indeed = final_list[cheapest_progress]
print(f"The cheapest is {cheapest_indeed["item"]}")


maxim = max(zip(item_price_dict.values(), item_price_dict.keys()))[1]
print(f"the most expensive item is {maxim}")