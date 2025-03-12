# prompts for a list of numbers
# prints out both the maximum and minimum of the numbers

input_numbers = []

while True:
    try:
        user_input = input("Enter an integer or 'done': ")
        if user_input == "done":
            break

        input_numbers.append(float(user_input))

    except ValueError:
        print("Error. Wrong input. Please enter a valid number. ")
        continue
    

if len(input_numbers) > 0:
    highest_value = max(input_numbers)
    lowest_value = min(input_numbers)
else:
    highest_value = None
    lowest_value = None

print(f"Numbers List: {input_numbers}")
print(f"Highest value: {highest_value}")
print(f"Lowest value: {lowest_value}")

