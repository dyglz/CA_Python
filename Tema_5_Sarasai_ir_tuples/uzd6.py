# Unikalūs elementai

input_set = set()

while True:
    user_input = input("Įveskite sveikąjį skaičių (arba 'pabaiga'): ")
    if user_input == "pabaiga":
        break
    input_set.add(int(user_input))

print(input_set)


# unique_numbers = []

# while True:
#     user_input = input("Įveskite sveikąjį skaičių (arba 'pabaiga'): ")
#     if user_input == "pabaiga":
#         break
#     number = int(user_input)
#     if number not in unique_numbers:
#         unique_numbers.append(number)

# print(unique_numbers)