from concurrent.futures import ThreadPoolExecutor
import time


def multi_read(url:str):
    print("Fetching data from source...")
    print(f"Data fetched from {url}")
    time.sleep(2)  # Simulate a delay in fetching data
    return f"Data fetched from {url}"

url_list = ["https://api.example.com/data1", "https://api.example.com/data2", "https://api.example.com/data3", "https://api.example.com/data4", "https://api.example.com/data5", "https://api.example.com/data6", "https://api.example.com/data7", "https://api.example.com/data8", "https://api.example.com/data9", "https://api.example.com/data10", "https://api.example.com/data11", "https://api.example.com/data12", "https://api.example.com/data13", "https://api.example.com/data14", "https://api.example.com/data15", "https://api.example.com/data16", "https://api.example.com/data17", "https://api.example.com/data18", "https://api.example.com/data19", "https://api.example.com/data20", "https://api.example.com/data21", "https://api example.com/data22", "https://api.example.com/data23", "https://api.example.com/data24", "https://api.example.com/data25", "https://api example.com/data26", "https://api example.com/data27", "https://api example.com/data28", "https://api example.com/data29", "https://api example.com/data30"]

results_final = []
with ThreadPoolExecutor(max_workers=int(len(url_list)/2)) as executor:
    results = list(executor.map(multi_read, url_list))
    results_final.extend(results)

print("results_final:", results_final)