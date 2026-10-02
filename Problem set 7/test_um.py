from um import count

def test_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("um, um , um") == 3
    assert count("") == 0
    assert count("yummy") == 0
    assert count("Um, UM, uM, um") == 4