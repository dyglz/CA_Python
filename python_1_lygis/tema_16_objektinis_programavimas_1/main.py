

# OBJEKTINIS PROGRAMAVIMAS

name = 'Antanas'


# self -> sutartinis zodis, galetu but ir kitoks

class Car:
    def __init__(self, brand, year, price):
        print("Car created")
        self.brand = brand # instance variable / attribute
        self.year = year
        self.price = price

    # class instance method
    def get_age(self):
        return 2025 - self.year

    def get_price(self):
        return self.price
    
    def create_report(self):
        return f"Brand: {self.brand}, Year: {self.year}, Price: {self.price}"

    def my_new_method(self):
        print("New functionality")
        pass

my_car = Car(brand="Toyota", year=2015, price=10000)
my_car2 = Car(brand="Toyota", year=2015, price=10000)
print(my_car is my_car2) # ?????? kodel False
print(my_car.get_age())
print(my_car.create_report())
print(my_car2.my_new_method())
