import pandas as pd 
import json

class dataextraction:

    def __init__(self, file_path:str):
        self.file_path = file_path

    def fetch_text(self, separator:str):
        #Read the text file and return the data as a pandas dataframe
        text_data = pd.read_csv(self.file_path, sep=separator)
        print(text_data.head())

    def read_excel(self):
        #Read the excel file and capitalze all the column names and return the data as a pandas dataframe
        excel_data = pd.read_excel(self.file_path)
        excel_data.columns = excel_data.columns.str.upper()
        print(excel_data.head())
    
    def read_json(self):
        # Read standard json file, flatten it, capitalize column names, and return the dataframe
        with open(self.file_path, 'r', encoding='utf-8') as f:
            # Change: Read the entire file as a single JSON object
            raw_data = json.load(f)
            
        # Correctly flatten the raw python list or dictionary
        json_data = pd.json_normalize(raw_data)
        json_data.columns = json_data.columns.str.upper()
        print(json_data.head())
        return json_data




read_json_obj = dataextraction("C:/Users/Admin/Python Learning/Python_Ansh/Files/apidata.json")
read_json_obj.read_json()
