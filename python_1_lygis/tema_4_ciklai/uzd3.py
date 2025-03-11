# PIN kodo nulaužimas

stored_pin = "9999"

for i in range(10000):
    pin = str(i)
    while len(pin) < 4:
        pin = "0" + pin

    if pin == stored_pin:
        print(f"Surastas PIN: {pin}")
        break