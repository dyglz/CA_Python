# KMI skaičiuoklė | Body Mass Index

def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    print(f"Body Mass Index: {bmi:.2f} kg/m\u00b2")

try:
    weight = float(input("Enter weight in kilograms: "))
    height = float(input("Enter height in meters: "))
    bmi_calculator(weight, height)
except ValueError:
    print("Wrong input!")


# ar geriau output'a rasyti funkcijoje, ar is isores(grazinant reiksme)
