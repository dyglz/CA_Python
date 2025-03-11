# Objektiškai orientuotas skaičiuotuvas

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, number: float) -> float:
        self.result = self.result + number
        return self.result
    
    def multiply(self, number: float) -> float:
        self.result = self.result * number
        return self.result

    def divide(self, number: float) -> float:
        if number != 0:
            self.result = self.result / number
            return self.result
        else:
            print("Impossible to divide by 0! Division is skipped!")
            return None

    def subtract(self, number: float) -> float:
        self.result = self.result - number
        return self.result

    def get_result(self):
        return self.result
        
    def reset_result(self):
        self.result = 0
        return self.result


test_1 = Calculator()
test_1.add(5)
test_1.multiply(6)
test_1.divide(2)
test_1.subtract(2)
print(f"First result:", test_1.get_result())
# test_1.reset_result()

test_2 = Calculator()
test_2.add(60)
test_2.multiply(2)
test_2.divide(0)
test_2.subtract(10)
print(f"Second result:", test_2.get_result())
# test_2.reset_result()
