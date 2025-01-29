import random

random_number = random.randint(1, 10)


while True:
    user_guess = int(input("Atspėkite skaičių (1 - 10): "))
    if user_guess == random_number:
        print(f"Teisingai! Skaičius yra {random_number}!")
        break
    elif user_guess < random_number:
        print("Per mažas! Bandykite dar kartą!")
    else:
        print("Per didelis! Bandykite dar kartą!")