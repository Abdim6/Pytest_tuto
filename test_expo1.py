import pytest
def test_newOne():
    x=5
    y=6
    assert x+1 == y

def test_two():
    x=5
    y=6
    assert x == y-1

def test_tree ():
    x=5
    y=6
    if (x==6):
        print("Good")
    else:
        print("False")