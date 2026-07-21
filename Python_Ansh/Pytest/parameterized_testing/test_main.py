from main import weather_check
import pytest
#Parameterized Test Cases for Weather Check Function

@pytest.mark.parametrize("temp,expected",[
    (35,"Hot"),
    (25,"Warm"),
    (15,"Cold"),
    (5,"Freezing"),
])

def test_weather_check(temp,expected):
    assert weather_check(temp) == expected