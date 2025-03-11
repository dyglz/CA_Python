# Valstybių palyginimas

class Country:
    def __init__(self, name: str, population: int, area: float):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.population > 20000000 or self.area > 3000000
    
    def compare_pd(self, other_country: "Country") -> str:
        self_density = self.population / self.area
        other_density = other_country.population / other_country.area

        if self_density > other_density:
            print(f"{self.name} has bigger density than {other_country.name}")
        else:
            print(f"{other_country.name} has bigger density than {self.name}")



australia = Country("Australija", 23_545_500, 7_692_024)
andorra = Country("Andora", 76_098, 468)

print(australia.is_big)  # True
print(andorra.is_big)  # False
andorra.compare_pd(australia)  # Andora turi didesnį gyventojų tankį nei Australija
           
