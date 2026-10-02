from fuel import convert, gauge
import pytest
def test_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("0/100") == 0
    assert convert("100/100") == 100


def test_convert_round() :
    assert convert("1/3") == 33
    assert convert("2/3") == 67

def test_convert_error() :
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
         convert("-2/4")
    with pytest.raises(ValueError):
        convert("animal/thing")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_guage():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
