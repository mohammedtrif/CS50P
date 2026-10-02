import pytest
from project import show_offers
from project import browse_games
from project import cart_store
from project import checkout
from project import main

def test_show_offers(capsys):
    show_offers(2)
    cap = capsys.readouterr()
    assert "One month of Extra subscription:" in cap.out

    show_offers(1)
    cap1 = capsys.readouterr()
    assert "Free games:" in cap1.out


def test_browse_games():
    result = browse_games("fortnite")
    assert "Game found:" in result

    result1 = browse_games("RESIDENT EVIL VILLAGE")
    assert "Game found:" in result1

    with pytest.raises(ValueError):
        browse_games("rwwqrqw")
    with pytest.raises(ValueError):
        browse_games("777787686")


def test_cart_store(monkeypatch, capsys):
    answers = iter([
        "elden ring","yes","no", "yes"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    result = cart_store()
    assert result == "Total price: $59.99"

    answers1 = iter([
        "fortnite", "yes", "no",
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(answers1))
    cart_store()
    cap = capsys.readouterr()
    assert "The game has been added" in cap.out

    answers2 = iter([
        "Marvel's Spider-Man 2", "yes", "yes", "The Last of Us Part I" ,"yes", "no", "yes"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(answers2))
    result2 = cart_store()
    assert result2 == "Total price: $139.98"

    answers3 = iter([
        "2323ffewf", "fortnite", "no"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(answers3))
    cart_store()
    cap1 = capsys.readouterr()
    assert "Game not found. Please try again" in cap1.out




def test_checkout(monkeypatch, capsys):

    answers = iter([
        "1234567890123467","10/30","123","your name"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    checkout("Test cart")
    cap = capsys.readouterr()
    assert("You have successfully purchased") in cap.out

    answers1 = iter([
        "123456789","10/","1D3","your name"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(answers1))
    checkout("Test cart")
    cap1 = capsys.readouterr()
    assert("Check your information") in cap1.out




def test_main(monkeypatch):
    answers = iter(["2"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    main()
