# 4 klases, su atributais, su instnace metodais (bent 5kiais) 
# ir viskas pratestuota


class Instrument:
    def __init__(self, name: str, instr_type: str, price: float, year: int, country: str):
        self.name = name # instance variable/ attribute
        self.type = instr_type
        self.price = price
        self.year = year
        self.country = country
    
    # class instance methods
    def get_type(self) -> str:
        return self.type
    
    def get_price(self) -> float:
        return self.price
    
    def create_report(self) -> str:
        return f"Name: {self.name}, Type: {self.type}, Price: {self.price}, Year: {self.year}, Country: {self.country}"
    
    def count_age(self) -> int:
        return 2025 - self.year
    
    def origin_country(self) -> str:
        return self.country


instrument_1 = Instrument(name="drums", instr_type="percussion", price=6500, year=2007, country="Germany")
instrument_2 = Instrument(name="guitar", instr_type="string", price=2000, year=1999, country="Spain")

print(instrument_1.get_type())
print(instrument_2.get_price())
print(instrument_1.create_report())
print(instrument_2.create_report())
print(instrument_2.count_age())
print(instrument_1.origin_country())




class People:
    def __init__(self, name: str, dob: int, gender: str, profession: str, start_date: int, hobby: str):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.profession = profession
        self.start_date = start_date
        self.hobby = hobby

    def age(self) -> int:
        return 2025 - self.dob
    
    def years_working_in_field(self) -> int:
        return 2025 - self.start_date
    
    def report(self) -> str:
        return f"Name: {self.name}, Date of Birth: {self.dob}, Gender: {self.gender}, Profession: {self.profession}, Started working in the field: {self.start_date}, Hobby: {self.hobby}"
    
    def report_profession_hobby(self) -> str:
        return f"Name: {self.name}, Profession: {self.profession}, Hobby: {self.hobby}"
    

person_1 = People(name="Bob", dob=1990, gender="man", profession="drummer", start_date=2006, hobby="cooking")
person_2 = People(name="Leya", dob=1995, gender="woman", profession="cook", start_date=2005, hobby="reading")

print(person_1.report())
print(person_2.report_profession_hobby())
print(person_1.years_working_in_field())
print(person_1.age())




    
    
