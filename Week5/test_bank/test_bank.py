from bank import value

def test_invalid():
    assert value("invalid") == 100


def test_casefold():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("howdy") == 20
    assert value("Hey") == 20

def test_string():
    assert value("Hello, world") == 0
    assert value("still invalid") == 100
    assert value("Howdy, you guys") == 20