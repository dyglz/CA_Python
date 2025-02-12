# Task 2: Dictionary Manipulation with Functions
# Write a function that takes a dictionary of people's names (as keys) and their ages (as values), and:
# Calculates and returns the average age.
# Creates and returns a new dictionary where each value is the age squared.

# {"Alice": 25, "Bob": 30, "Charlie": 35} -> (30.0, {"Alice": 625, "Bob": 900, "Charlie": 1225})


def process_ages(people: dict) -> tuple:
    squared_age = {}
    sum_age = sum(list(people.values()))
    avg_age = sum_age / len(people)
    
    for name, age in people.items():
        squared_age[name] = age * age
    return avg_age, squared_age
    

print(process_ages({"Alice": 25, "Bob": 30, "Charlie": 35}))

