from bank import value

def test_value_greeting() :
    assert value("Hello, Newman") == 0
    assert value("Hello, how are you?") == 0
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("ohhlala") == 100
    assert value("h5654@#$") == 20
    assert value("hello5904!!!") == 0
    assert value("&*(kr)444") == 100
    assert value("HOLLA") == 20
