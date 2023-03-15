from um import count

def test_count():
    assert count('um') == 1
    assert count('Um, thanks for the album.') == 1
    assert count('Hello, world') == 0
    assert count('Um, thanks, um...') == 2
    assert count('Um, I do not, Um, how to say, um, know') == 3