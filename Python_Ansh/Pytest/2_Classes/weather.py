class Weather:

    def __init__(self):
        pass

    def get_weather(self, temp:float):
        if temp >= 30:
            return "Hot"
        elif temp >= 20:
            return "Warm"
        elif temp >= 10:
            return "Cold"
        else:
            return "Freezing"

    def rain_possibility(self, temp:float, humidity:bool):
        weather_status = self.get_weather(temp)
        if weather_status == "Hot" and humidity == True:
            return "High"
        elif weather_status == "Cold" and humidity == True:
            return "Medium"
        else:
            return "Low"