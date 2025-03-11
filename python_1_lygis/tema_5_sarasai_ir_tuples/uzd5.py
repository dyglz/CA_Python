# Ilgiausia iš eilės einančių skaičių seka

sequence = []
input_numbers = input("Please, enter integers separated by spaces: ")

# create a list from user input
for number in input_numbers.split():
    sequence.append(int(number))

current_sequence = 1
longest_sequence = 1

for i in range(1, len(sequence)):
    if sequence[i] == sequence[i-1] + 1:
        current_sequence += 1
        if longest_sequence < current_sequence:
            longest_sequence = current_sequence
    else:
        current_sequence = 1

print(f"The longest sequence of consecutive numbers: {longest_sequence}")
    

    




