# Naujai apibrėžta išimtis

class IntervalExceededError(Exception):
    # exception raised when numbers are not in a valid range/interval
    # print("At least one of the numbers is too high!")
    pass
    


def calculator(number_1: float, number_2: float) -> float:

    try:
        if number_1 > 1000000 or number_2 > 1000000:
            raise IntervalExceededError("At least one of the numbers is too high!")
        else:
            number_1 = float(number_1)
            number_2 = float(number_2)

            sum = number_1 + number_2
            sub = number_1 - number_2
            mul = number_1 * number_2
            div = number_1 / number_2

            print(f"{number_1} + {number_2} = {sum:.2f}")
            print(f"{number_1} - {number_2} = {sub:.2f}")
            print(f"{number_1} * {number_2} = {mul:.2f}")
            print(f"{number_1} / {number_2} = {div:.2f}")

    except TypeError:
        print("Invalid value. Enter a number.")
    except ValueError:
        print("Invalid value.")
    except ZeroDivisionError:
        print("Cannot divide by 0!")
    except IntervalExceededError as e:
        print(e)
    except Exception as e:
        print(f"unexpected error: {e}")

calculator(number_1=5, number_2=2)