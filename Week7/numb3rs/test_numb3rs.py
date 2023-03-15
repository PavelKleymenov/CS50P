from numb3rs import validate

def test_validate():
    assert validate("cat") == False
    assert validate("1.1.1.1") == True
    assert validate("127.0.1") == False
    assert validate("255.255.255.255") == True
    assert validate("25,5.23.25.12") == False
    assert validate("127.32.64.2") == True
    assert validate('1.512.1.1') == False