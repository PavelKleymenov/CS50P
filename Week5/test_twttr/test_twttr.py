from twttr import shorten

def test_title():
    assert shorten("Title") == "Ttl"

def test_upper():
    assert shorten("UPPER") == "PPR"

def test_lower():
    assert shorten("lower") == "lwr"

def test_alphanumeric():
    assert shorten("CS_50") == "CS_50"

def test_consonants():
    assert shorten("PhD") == "PhD"

def test_punctuation():
    assert shorten("CS50!") == "CS50!"