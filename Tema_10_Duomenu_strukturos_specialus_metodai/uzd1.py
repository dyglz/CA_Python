#  Skaičiai, kurie dalijasi iš 6

# def calculator() -> list[int]:
#     answer_list = []
#     for number in range(1, 1001):
#         if number % 6 == 0:
#             answer_list.append(number)
#     print(answer_list)


def calculator() -> list[int]:
    return [number for number in range(1, 1001) if number % 6 == 0]

print(calculator())