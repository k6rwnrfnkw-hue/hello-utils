from greet import greet, shout, farewell


def test_greet_with_name():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_empty():
    assert greet("") == "Hello, World!"


def test_shout():
    assert shout("Alice") == "HELLO, ALICE!"


def test_farewell_with_name():
    assert farewell("Alice") == "Goodbye, Alice!"


def test_farewell_empty():
    assert farewell("") == "Goodbye, World!"
