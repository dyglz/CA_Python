# 1) Create a lambda function that 
# takes a number and returns its square.

# def squared(number: int) -> int:
#     return number * number


# opt1:
squared_number = lambda number: number ** 2
print(squared_number(2))

# opt2:
squared_number = (lambda number: number ** 2)(4)
print(squared_number)


