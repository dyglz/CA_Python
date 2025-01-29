# Prisijungimo sistema su begaliniu ciklu

username = "admin"
password = "super_password"


while True:
    enter_username = input("Įveskite vartotojo vardą: ")
    enter_password = input("Įveskite slaptažodį: ")

    if (username == enter_username) & (password == enter_password):
        print(f"Prisijungimas sėkmingas! Sveiki, {username}!")
        break