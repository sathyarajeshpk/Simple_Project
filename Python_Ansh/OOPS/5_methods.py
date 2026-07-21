class methods:

    my_var = 100
    title:str = "Going to use in another class"

    #Dunder Method
    def __init__(self):
        print("This is a constructor method")
    
    def __str__(self):
        return "This is a string representation of the class"

    @classmethod
    def _change_value(cls, new_value):
        cls.my_var = new_value

    @staticmethod
    def my_static_method():
        #print initial value of my_var
        print(f"Initial value of my_var: {methods.my_var}")

# obj = methods()
# print(obj.my_var)

# #changing value here
# obj._change_value(200)
# print(obj.my_var)

# #Checking if the value has changed or not
# obj2 = methods()
# print(obj2.my_var)

# obj3 = methods()
# obj3.my_static_method()

obj4 = methods()
print(obj4.__str__())
print(obj4)