class Addition:
    def calculate(self, a, b):
        return a + b
 
class Subtraction:
    def calculate(self, a, b):
        return a - b
 
class Multiplication:
    def calculate(self, a, b):
        return a * b
 
class Division:
    def calculate(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b
 
class Calculator:
    def __init__(self):
        self.operations = {
            'add': Addition(),
            'subtract': Subtraction(),
            'multiply': Multiplication(),
            'divide': Division()
        }
 
    def execute(self, operation, a, b):
        if operation in self.operations:
            return self.operations[operation].calculate(a, b)
        else:
            return "Invalid operation!"
