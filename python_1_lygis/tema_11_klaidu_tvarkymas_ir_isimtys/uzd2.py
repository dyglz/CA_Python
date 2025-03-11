# Saugi dalyba

def safe_divide(number_1: float, number_2: float) -> float:
    try:
        division = number_1 / number_2

    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")

    else:
        print(f"{number_1} / {number_2} = {division:.2f}")
    finally:
        print("Attempt to divide")


safe_divide(number_1=5, number_2="g")