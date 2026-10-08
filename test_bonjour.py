from bonjour import saluer
def test_saluer():
    assert saluer("Alice") == "Bonjour, Alice!"
    assert saluer("Bob") == "Bonjour, Bob!"
    assert saluer("") == "Bonjour, !"
def test_saluer_vide():
    assert saluer("") == "Bonjour, !"