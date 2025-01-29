
# # Converts Celsius to Faranheit
# 
def celsius_to_farenheit(celsius):
    farenheit = (9/5*celsius) + 32
    return farenheit


# # Converts Farenheit to Celsius
# 
def farenheit_to_celsius(farenheit):
    celsius = (farenheit - 32) * 5 / 9 
    return celsius


# # Calculate average speed in m/s
# Distance is given in km and time in hours.
# 
def average_speed(distance_km, time_h):
    distance_m = distance_km * 1000
    time_s = time_h * 3600
    return distance_m / time_s


# # Makes basic math calculations (+, -. *. /, **)
# 
def addition(number_1: float, number_2: float):
    return number_1 + number_2

def substraction(number_1: float, number_2: float):
    return number_1 - number_2

def multiplication(number_1: float, number_2: float):
    return number_1 * number_2

def division(number_1: float, number_2: float):
    return number_1 / number_2

def exponentation(number_1: float, number_2: float):
    return number_1 ** number_2


# User input and output of the functions

print("Convert °C to °F")
celsius = float(input("Enter the temperature in Celsius: "))
farenheit = celsius_to_farenheit(celsius)
print(f"{celsius:.2f}°C in Farenheit: {farenheit:.2f}°F\n")


print("Convert °F to °C")
farenheit = float(input("Enter the temperature in Farenheit: "))
celsius = farenheit_to_celsius(farenheit)
print(f"{farenheit:.2f}°F in Celsius: {celsius:.2f}°C \n")


print("Average speed km/h -> m/s")
distance_km = float(input("Enter distance in kilometers: "))
time_h = float(input("Enter time in hours: "))
average_speed_ms = average_speed(distance_km, time_h)
print(f"Average speed: {average_speed_ms:.2f} m/s\n")


print("Calculate 2 numbers (+, -. *. /, **)")
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
sum = addition(number_1, number_2)
print(f"{number_1} + {number_2} = {sum:.2f}")

difference = substraction(number_1, number_2)
print(f"{number_1} - {number_2} = {difference:.2f}")

product = multiplication(number_1, number_2)
print(f"{number_1} * {number_2} = {product:.2f}")

quotient = division(number_1, number_2)
print(f"{number_1} / {number_2} = {quotient:.2f}")

power = exponentation(number_1, number_2)
print(f"{number_1} ^ {number_2} = {power:.2f}")



