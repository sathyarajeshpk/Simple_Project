def weather_check(temp:float)->str:
    if temp >= 30:
        return "Hot"
    elif temp >= 20:
        return "Warm"
    elif temp >= 10:
        return "Cold"
    else:
        return "Freezing"


print(weather_check(25))