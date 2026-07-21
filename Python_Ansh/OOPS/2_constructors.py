class Myclass:

    variable = "This is a class variable"
    variable2 = "This is another class variable"

    def __init__(self, var1, var2, var3 = None, var4 = None):
        self.variable = var1
        self.__variable2 = var2
        self._variable3 = var3
        Myclass.variable4 = var4


    def printvar1(self):
        print(self.variable)
    
    def printvar2(self):
        print(self.__variable2)

    def printvar3(self):
        print(self._variable3)

    def printvar4(self):
        print(self.variable4)

print_obj = Myclass("This is a class variable1", "This is another class variable2", "variable3", "This is a class variable4")
print_obj.printvar1()
print_obj.printvar2()
print_obj.printvar3()
print_obj.printvar4()

print_obj._Myclass__variable2 = "Assigning new value for private variable2"
print_obj.printvar2()
