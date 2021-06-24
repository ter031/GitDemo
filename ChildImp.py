from OopsDemo import Calculator

class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,10,2)

    def getCompleteData(self):
        return self.num + self.num2 + self.Summation()

obj3 = ChildImpl()
print(obj3.getCompleteData())
