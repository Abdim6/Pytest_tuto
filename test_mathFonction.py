import pytest
import math
import math_fun

def racine(x):
    return math.sqrt(x)

def test_racine():
    assert racine(25) == 5

def test_externfun():
    assert math_fun.test_add(3)==5
    assert math_fun.test_product(3)==6