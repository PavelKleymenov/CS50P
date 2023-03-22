from seasons import get_birthday

def test_get_birthday():
    assert get_birthday("August 1, 1997") == None
    assert get_birthday("1997-8-1") == None
    assert get_birthday("1997-08-01") == ("1997", "08", "01")