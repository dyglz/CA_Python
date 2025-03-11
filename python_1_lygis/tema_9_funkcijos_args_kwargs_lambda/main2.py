# 2) Create a lambda function that 
# takes two numbers and returns their squared sum.


# def calculator(num_1: int, num_2: int) -> int:
#     return (num_1 + num_2) * (num_1 + num_2)


# opt1:
squared_sum = lambda num_1, num_2: (num_1 + num_2) * (num_1 + num_2)
print(squared_sum(2, 5))

# opt2:
squared_sum = (lambda num_1, num_2: (num_1 + num_2) * (num_1 + num_2))(2, 5)
print(squared_sum)

