from app import additionner


def test_additionner():
    assert additionner(2, 3) == 5


def test_additionner_nombres_negatifs():
    assert additionner(-2, -3) == -5