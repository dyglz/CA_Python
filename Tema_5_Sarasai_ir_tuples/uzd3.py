# Pusė trikampio

user_input = int(input("Įveskite trikampio dydį: "))

for lines in range(1, user_input + 1):
    for symbols in range(1, lines + 1):
        print(symbols, end="")
    print()