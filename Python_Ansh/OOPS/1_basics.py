class Myclass:

    variable = "This is a class variable"
    variable2 = "This is another class variable"

    def printvar1(self):
        print(self.variable)
    
    def printvar2(self):
        print(self.variable2)


print1 = Myclass()
print1.printvar1()
print2 = Myclass()
print2.printvar2()