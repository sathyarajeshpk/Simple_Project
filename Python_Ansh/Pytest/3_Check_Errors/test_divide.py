import pytest
from divide import WeatherwithDivide

# Test Cases for Weather Check Function
def test_weather_check():
    # Pass temp and humidity to __init__, then call the method without arguments
    assert WeatherwithDivide(35, True).get_weather() == "Hot"
    assert WeatherwithDivide(25, True).get_weather() == "Warm"
    assert WeatherwithDivide(15, True).get_weather() == "Cold"
    assert WeatherwithDivide(5, True).get_weather() == "Freezing"

def test_rain_possibility():
    # Pass different conditions to test the conditional logic matrix
    assert WeatherwithDivide(35, True).rain_possibility() == "High"
    assert WeatherwithDivide(25, True).rain_possibility() == "Low"
    assert WeatherwithDivide(15, True).rain_possibility() == "Medium"
    assert WeatherwithDivide(5, True).rain_possibility() == "Low"

def test_divide():
    # The divide method doesn't use temp or humidity, but __init__ still demands them.
    # We pass dummy values (0, False) just to satisfy the class creation.
    w = WeatherwithDivide(0, False)
    
    assert w.divide(10, 2) == 5.0
    assert w.divide(10, -2) == -5.0
    assert w.divide(0, 2) == 0.0
    assert w.divide(10, 3) == 10 / 3
    
    with pytest.raises(ZeroDivisionError):
        w.divide(1, 0)
