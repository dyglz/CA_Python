# Restoranų reitingų filtravimas

# user enters number of restaurants
# user enters restaurant name and rating (nested dict: name: rating)
# user should be able to enter the baseline for the grade (default: 4.0)
# function returns a list of restaurants sorted alphabetically, 
# separated by baselin


# restaurants completed with Vytautas


def filtering(restaurants_list: list[dict[str, str | float ]], minimal_rating: float) -> list[str]:
    for r in restaurants_list:
        if r["rating"] >= minimal_rating:
            filtered_list.append(r["name"])
    return filtered_list
    

filtered_list = []
restaurants_list = []
restaurants_count = int(input("Enter number of restaurants: "))
for i in range(restaurants_count):
    restaurant_name = input("Restaurant name:")
    restaurant_rating = float(input("Restaurant rating: "))
    restaurants_list.append({"name": restaurant_name, "rating": restaurant_rating})
minimal_rating = input("Enter the minimum rating: ")
if minimal_rating.isnumeric():
    minimal_rating = float(minimal_rating)
else:
    minimal_rating = 4.0


result = filtering(restaurants_list, minimal_rating)
result.sort()
print(result)








