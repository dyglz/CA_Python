# gross pay = hours * rate
# 
# create a function called computepay which takes two parameters
# (hours and rate).

def computepay(pay_rate, hours):
    return pay_rate * hours

try:
    pay_rate = float(input("Enter the pay rate per hour: "))
    hours = float(input("Enter the number of hours: "))

    if hours > 40 :
        extra_pay = 1.5 * pay_rate * (hours - 40)
        gross_pay = extra_pay + computepay(pay_rate, hours)
    else:
        gross_pay = computepay(pay_rate, hours)

    print(f"Pay is {gross_pay}")

except:
    print("Error, please enter numeric input")