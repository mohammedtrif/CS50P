from jar import Jar
import pytest

def test_init():
    jar = Jar(20)
    assert jar.capacity == 20
    with pytest.raises(ValueError):
        Jar(-3)

def test_size():
    jar = Jar(12)
    jar.size = 5
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.size = -4

    with pytest.raises(ValueError):
        jar.size = 13

def test_deposit():
    jar = Jar(12)

    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(5)
    assert jar.size == 8

    with pytest.raises(ValueError):
        jar.deposit(5)

def test_withdraw():
    jar = Jar(12)

    jar.deposit(8)
    jar.withdraw(3)

    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.withdraw(6)


def test_str():
    jar = Jar(12)

    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
