# Paprastas skaičiuotuvas

def calculator(number_1: float, number_2: float) -> float:

    try:
        sum = number_1 + number_2
        sub = number_1 - number_2
        mul = number_1 * number_2
        div = number_1 / number_2

        print(f"{number_1} + {number_2} = {sum:.2f}")
        print(f"{number_1} - {number_2} = {sub:.2f}")
        print(f"{number_1} * {number_2} = {mul:.2f}")
        print(f"{number_1} / {number_2} = {div:.2f}")

    except TypeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

calculator(number_1=5, number_2=3)