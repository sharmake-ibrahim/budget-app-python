


class Calculater:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def Add(self):
        result = self.num1 + self.num2
        return print(result)
    def Subtract(self):
        result = self.num1 - self.num2
        return print(result)
    def Multiply(self):
        result = self.num1 * self.num2
        print(result)

calculate = Calculater(5,6)
calculate.Add()
calculate.Subtract()
calculate.Multiply()