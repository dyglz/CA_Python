# Skaičius, kuriuose yra devynetas

# def calculator() -> list[int]:
#     answer_list = []
#     for number in range(1, 1001):
#         if "9" in str(number):
#             answer_list.append(number)
#     print(answer_list)


def calculator() -> list[int]:
    return [number for number in range(1, 1001) if "9" in str(number)]

print(calculator())

