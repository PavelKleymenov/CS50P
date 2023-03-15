from watch import parse


def test_parse():
    assert parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
    assert parse('<iframe src="https://cs50.harvard.edu/python"></iframe>') == None
    assert parse('<iframe src="http://www.youtube.com/embed/abCDef2GhI1"></iframe>') == 'https://youtu.be/abCDef2GhI1'
    assert parse('<iframe src="https://www.oxfordlearnersdictionaries.com/"></iframe>') == None
