class Calculator:
    num = 100 # class variables

    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("I am called automatically when an object is created")

    def getData(self):
        print("I am executing methods inside class")

    def Summation(self):
        return self.a + self.b + self.num

obj = Calculator(2,3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4,5)
obj1.getData()
print(obj1.Summation())