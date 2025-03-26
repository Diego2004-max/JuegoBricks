from src.conversor import convertir_celsius_a_fahrenheit

def test_convertir_celsius_a_fahrenheit():
    assert convertir_celsius_a_fahrenheit(0) == 32
    assert convertir_celsius_a_fahrenheit(100) == 212
    assert convertir_celsius_a_fahrenheit(-40) == -40
