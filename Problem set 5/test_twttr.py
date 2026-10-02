from twttr import shorten

def test_shorten():
    assert shorten("mohammed") == "mhmmd"
    assert shorten("mOhAmmEd") == "mhmmd"
    assert shorten("MOHAMMED") == "MHMMD"
    assert shorten("mhmmd") == "mhmmd"
    assert shorten("") == ""
    assert shorten("&!@#") == "&!@#"
    assert shorten("43678iooo") == "43678"
    assert shorten("moh@@@mid") == "mh@@@md"
    assert shorten("moh4536mid") == "mh4536md"
