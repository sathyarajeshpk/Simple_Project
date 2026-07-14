import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from OOPS.sample_inherit import Myclassinh

class company(Myclassinh):
        def __init__(self,company_name, var1, var2, var3 = None, var4 = None):
                super().__init__(var1, var2, var3, var4)
                self.company_name = company_name

        def company_info(self):
                print(f"Company Name: {self.company_name}")
                print(f"Variable 1: {self.variable}")
                print(f"Variable 2: {self.variable2}")
                print(f"Variable 3: {self.variable3}")
                print(f"Variable 4: {self.variable4}")

obj = company("TechCorp", "Value 1", "Value 2", "Value 3", "Value 4")
obj.company_info()