from seasons import minutes
from datetime import date

def test_minutes():
    today = date.today()
    assert minutes(date(2000, 1, 1)) == (today - date(2000, 1, 1)).days * 1440
    assert minutes(date(2020, 1, 1)) == (today - date(2020, 1, 1)).days * 1440
    assert minutes(date(2024, 2, 29)) == (today - date(2024, 2, 29)).days * 1440

    assert minutes(date.today()) == 0
    year_gone = date(today.year - 1, today.month, today.day)
    assert minutes(year_gone) == (today - year_gone).days * 1440
