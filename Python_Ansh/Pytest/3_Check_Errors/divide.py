class WeatherwithDivide:

#Not recommended to pass the arguments in the init if each method uses it's own argument. 
#If there is a common reusable, argument is there, then we can include in init

    def __init__(self, temp:float, humidity:bool):
        self.temp = temp
        self.humidity = humidity

    def get_weather(self):
        if self.temp >= 30:
            return "Hot"
        elif self.temp >= 20:
            return "Warm"
        elif self.temp >= 10:
            return "Cold"
        else:
            return "Freezing"

    def rain_possibility(self):
        weather_status = self.get_weather()
        if weather_status == "Hot" and self.humidity == True:
            return "High"
        elif weather_status == "Cold" and self.humidity == True:
            return "Medium"
        else:
            return "Low"

    def divide(self, a:float, b:float)->float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b