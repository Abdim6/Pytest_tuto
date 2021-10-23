import pytest

def test_answer(cmd):
    if cmd == "1":
        print("c'est bien un")
    elif cmd == "2":
        print("c'est deux")
    assert 0