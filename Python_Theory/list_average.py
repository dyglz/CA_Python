# prompt a list
# print list and average

# create an empty list
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
    total_sum = sum(input_numbers)
    average = total_sum / len(input_numbers)
else:
    average = 0

print(f"Skaičiai: {input_numbers}")
print(f"Vidurkis: {average}")





