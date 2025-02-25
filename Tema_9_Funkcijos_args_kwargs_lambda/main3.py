# 3) Use the lambda function 
# to sort list of tuples based on the second element:

tuples_list = [(1,3), (4,1), (5,2), (2,4)]

tuples_list.sort(key = lambda numbers: numbers[1])
print(tuples_list)


