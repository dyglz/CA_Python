# Sudėtinių palūkanų skaičiuoklė

def compound_interest_calculator(principal: float, annual_rate: float, time: int) -> float:
    return round(principal * (1 + annual_rate)**time, 2)


principal = float(input("Enter the principal amount ($): "))
annual_rate = float(input("Enter the annual interest rate (%): ")) / 100
time = int(input("Enter the time (in years): "))

final_interest = compound_interest_calculator(principal, annual_rate, time)
print(f"The resulting amount after {time} years is ${final_interest}.")