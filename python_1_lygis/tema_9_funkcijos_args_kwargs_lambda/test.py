# def random_func() -> None:   
# def division(num_1: int, num_2: int) -> float:



def print_random_stuff(name, age=12, *args, **kwargs) -> None:
    print(name, age)
    print(args)
    print(kwargs)


print_random_stuff(
    "Jonas",
    "Petras",
    "Antanas",
    "Mindaugas",
    random_name="Tomas",
    random_name_2="Tomas",
)


def new_func(a, b, c, d=20, *args, **kwargs) -> None:
    print(a, b, c, d)
    if args:
        # I do whatever I want with args
        # args is a tuple
        print(args)
    if kwargs:
        # I do whatever I want with kwargs
        # kwargs is a dictionary
        print(kwargs)

# try/except 

# def a(a, b):
#     try:
#         return a+b
#     except:
#         print("An exception occured")

# def b(a, b):
#     try:
#         return a-b
#     except:
#         print("An exception occured")


# def anything():
#     alfa = a(5, 5)
#     if alfa != None:
#         raise ("Error happened")
#     beta = b(5, 5)
#     return 0

# anything()