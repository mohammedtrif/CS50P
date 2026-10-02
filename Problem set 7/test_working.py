
from working import convert
import pytest


def test_valid_times():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_minutes():
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"
    assert convert("12:15 AM to 12:30 PM") == "00:15 to 12:30"


def test_invalid_hours():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")


def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9:30 AM to 5:60 PM")


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")


            