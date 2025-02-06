
# # Converts Celsius to Faranheit
# 
def celsius_to_farenheit(celsius: float):
    farenheit = (9/5*celsius) + 32
    print(f"{celsius:.2f}°C in Farenheit: {farenheit:.2f}°F\n")


# # Converts Farenheit to Celsius
# 
def farenheit_to_celsius(farenheit: float):
    celsius = (farenheit - 32) * 5 / 9 
    return celsius


# # Calculate average speed in m/s
# Distance is given in km and time in hours.
# 
def average_speed(distance_km: float, time_h: float):
    distance_m = distance_km * 1000
    time_s = time_h * 60 * 60
    # average_speed_ms = distance_m / time_s
    return distance_m / time_s
    # print(f"Average speed: {average_speed_ms:.2f} m/s\n")


# # Makes basic math calculations (+, -. *. /, **)
# 
def addition(number_1, number_2):
    sum = number_1 + number_2
    print(f"{number_1} + {number_2} = {sum:.2f}")

def substraction(number_1, number_2):
    difference = number_1 - number_2
    print(f"{number_1} - {number_2} = {difference:.2f}")

def multiplication(number_1, number_2):
    product = number_1 * number_2
    print(f"{number_1} * {number_2} = {product:.2f}")

def division(number_1, number_2):
    quotient = number_1 / number_2
    print(f"{number_1} / {number_2} = {quotient:.2f}")

def exponentation(number_1, number_2):
    power = number_1 ** number_2
    print(f"{number_1} ^ {number_2} = {power:.2f}")



# User input and output of the functions

print("Convert °C to °F")
celsius_to_farenheit(float(input("Enter the temperature in Celsius: ")))

print("Convert °F to °C")
farenheit_to_celsius(float(input("Enter the temperature in Farenheit: ")))

print("Average speed km/h -> m/s")
distance_km = float(input("Enter distance in kilometers: "))
time_h = float(input("Enter time in hours: "))
average_speed(distance_km, time_h)

print("Calculate 2 numbers (+, -. *. /, **)")
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
addition(number_1, number_2)
substraction(number_1, number_2)
multiplication(number_1, number_2)
division(number_1, number_2)
exponentation(number_1, number_2)


