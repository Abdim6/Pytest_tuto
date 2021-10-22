import pytest
def PremiereFonction(x):
    return(x+5)

def test_premiereFonction():
    assert PremiereFonction(3)==8
    print("tout est Ok")