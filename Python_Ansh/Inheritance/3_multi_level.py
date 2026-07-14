import sys
import os
import importlib.util

# Load the 1_inheritance module dynamically
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
spec = importlib.util.spec_from_file_location("inheritance_module", os.path.join(os.path.dirname(__file__), "1_inheritance.py"))
inheritance_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inheritance_module)
company = inheritance_module.company

class company3(company):
        def __init__(self, location, company_name, var1, var2, var3 = None, var4 = None):
                super().__init__(company_name, var1, var2, var3, var4)
                self.location = location

        def company3_info(self):
                print(f"Company Name: {self.company_name}")
                print(f"Location: {self.location}")
                print(f"Variable 1: {self.variable}")
                print(f"Variable 2: {self.variable2}")
                print(f"Variable 3: {self.variable3}")
                print(f"Variable 4: {self.variable4}")

obj = company3("New York", "TechCorp", "Value 1", "Value 2", "Value 3", "Value 4")
obj.company3_info()