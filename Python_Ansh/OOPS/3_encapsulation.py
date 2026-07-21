class Myclass:

    variable = "This is a class variable"
    variable2 = "This is another class variable"
    variable4 = "This is a class variable4"

    def __init__(self, var1, var2, var3 = None, var4 = None):
        self.variable = var1
        self.variable2 = var2
        self.variable3 = var3
        Myclass.variable4 = var4

    def printvar1(self):
        print(self.variable)
    
    def printvar2(self):
        print(self.variable2)

    def printvar3(self):
        print(self.variable3)

    def printvar4(self):
        print(self.variable4)

obj = Myclass("Value 1", "Value 2", "Value 3", "Value 4")
obj.printvar1()
obj.printvar2()
obj.printvar3()
obj.printvar4()