#  Delionės detalės

# Parašykite funkciją, kuri priima du sveikųjų skaičių sąrašus ir 
# grąžina True, jei kiekviena atitinkamų elementų poros suma iš abiejų sąrašų 
# turi tą pačią reikšmę. 
# Kitu atveju grąžinkite False.


def puzzle_pieces(first_sequence: list[int], second_sequence: list[int]) -> bool:
    if len(first_sequence) != len(second_sequence):
        return False
    
    sums: list[int] = []
    for i in range(len(first_sequence)):
        sums.append(first_sequence[i] + second_sequence[i])
    print(f"Sums: {sums}")

    if len(set(sums)) == 1:
        return True
    else:
        return False
    

while True:
    try:
        first_sequence: list[int] = []
        second_sequence: list[int] = []
        first_sequence_input = input("Enter the first sequence of integers separated by spaces or 'q': ").lower()
        second_sequence_input = input("Enter the second sequence of integers separated by spaces or 'q': ").lower()

        if first_sequence_input == "q" or second_sequence_input == "q":
            break
        
        for number in first_sequence_input.split():
            first_sequence.append(int(number))
        for number in second_sequence_input.split():
            second_sequence.append(int(number))

        if puzzle_pieces(first_sequence, second_sequence):
            print("The sums of all members are equal.")
        else:
            print("Sums are not equal.")

    except ValueError:
        print("Wrong input! Please enter valid integers separated by spaces.")

