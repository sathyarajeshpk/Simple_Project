from Python_Ansh.Pytest.main_basics import weather_check

#Test Cases for Weather Check Function

def test_weather_check():
    assert weather_check(35) == "Hot"
    assert weather_check(25) == "Warm"
    assert weather_check(15) == "Cold"
    assert weather_check(5) == "Freezing"

if __name__ == "__main__":
    test_weather_check()

## Use python -m pytest Python_Ansh/Pytest/1_basics/test_main.py
# Since the source code main is one folder above