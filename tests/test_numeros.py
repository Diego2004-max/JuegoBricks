from src.numeros import es_primo

def test_es_primo():
    assert es_primo(2) is True
    assert es_primo(3) is True
    assert es_primo(4) is False
    assert es_primo(11) is True
    assert es_primo(25) is False

