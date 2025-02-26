from src.temperature import Temperature


def test_celsius_to_fahrenheit():
    temp = Temperature()
    assert temp.celsius_to_fahrenheit(0) == 32
    assert temp.celsius_to_fahrenheit(100) == 212


def test_fahrenheit_to_celsius():
    temp = Temperature()
    assert temp.fahrenheit_to_celsius(32) == 0
    assert temp.fahrenheit_to_celsius(212) == 100
