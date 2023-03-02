from plates import is_valid

def test_start_alpha():
    assert is_valid("CS50") == True
    assert is_valid("50") == False
    assert is_valid("0CS") == False
    assert is_valid("great") == True

def test_length():
    assert is_valid("H") == False
    assert is_valid("CS50") == True
    assert is_valid("OUTATIME") == False
    assert is_valid("CS") == True

def test_numbers():
    assert is_valid("12345") == False
    assert is_valid("12CS") == False
    assert is_valid("CS11") == True
    assert is_valid("BS11A1") == False
    assert is_valid("AAA11A") == False

def test_leading_zero():
    assert is_valid("00") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_alphanumeric():
    assert is_valid("PI3.14") == False
    assert is_valid("PI") == True
    assert is_valid("E2.18") == False