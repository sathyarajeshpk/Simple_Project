import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.decorators import my_decorator


@my_decorator
def fetch_data(url:str, path:str):
    print("Fetching data from source...")
    return f"Data fetched from {url} and saved to {path}"

@my_decorator
def read_data(path:str):
    print("Reading data from source...")
    return f"Data read from {path}"



obj = fetch_data("https://api.example.com/data", "/path/to/save/data.json")
print(obj)

obj_read = read_data("/path/to/save/data.json")
print(obj_read)