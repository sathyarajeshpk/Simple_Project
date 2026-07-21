from weather import Weather

w = Weather()

#Test Cases for Weather Check Function

def test_weather_check():
    assert w.get_weather(35) == "Hot"
    assert w.get_weather(25) == "Warm"
    assert w.get_weather(15) == "Cold"
    assert w.get_weather(5) == "Freezing"

def test_rain_possibility():
    assert w.rain_possibility(35, True) == "High"
    assert w.rain_possibility(25, True) == "Low"
    assert w.rain_possibility(15, True) == "Medium"
    assert w.rain_possibility(5, True) == "Low"

if __name__ == "__main__":
    test_weather_check()
    test_rain_possibility()