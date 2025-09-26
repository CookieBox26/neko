from neko import hello


def test_hello():
    h = hello()
    assert h == 'Hello, Neko!'
