from plates import is_valid

def test_length():
    assert is_valid("ASN456") == True
    assert is_valid("ASD45") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
def test_first_two_letters():
    assert is_valid("234ASX") == False
    assert is_valid("A2BC") == False
    assert is_valid("1ABC") == False
    assert is_valid("ABCD") == True
    assert is_valid("A1") == False
def test_numbers():
    assert is_valid("AS0456") == False
    assert is_valid("AS12D") == False
    assert is_valid("ASD12") == True
def test_symbols():
    assert is_valid("A2@#45") == False
    assert is_valid("AS-45") == False
    assert is_valid("AS 45") == False
