# Fibonacci sekos generavimas

a = 0
b = 1
print(f"Fibonacci seka: \n{a} \n{b}")

for x in range(1,9):

    c = a + b
    print(f"{c}")
    # a gets the value of b and b gets the value of c
    # (a, b) = (b, c)
    a = b
    b = c
