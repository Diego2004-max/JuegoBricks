from src.geometria import calcular_area_rectangulo

def test_calcular_area_rectangulo():
    assert calcular_area_rectangulo(2, 3) == 6
    assert calcular_area_rectangulo(5, 10) == 50
    assert calcular_area_rectangulo(0, 10) == 0
