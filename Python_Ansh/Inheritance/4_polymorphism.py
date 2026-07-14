class api_fetch():
    def fetch_data(self):
        print("Fetching data from API...")

class database_fetch():
    def fetch_data(self):
        print("Fetching data from Database...")

class source(api_fetch, database_fetch):
    def fetch_data(self):
        print("Fetching data from source...")
        super().fetch_data()  # Calls the fetch_data method of the first parent class (api_fetch)
        database_fetch.fetch_data(self)  # Calls the fetch_data method of the second parent class (database_fetch)

obj = source()
obj.fetch_data()  # Output: Fetching data from source... Fetching data from API

##Decorators are a powerful feature in Python that allow you to modify the behavior of functions or classes. They are often used to add functionality to existing code without modifying the original code directly. Decorators are commonly used for logging, authentication, caching, and more.

