import pytest
import math

def racine(x):
    return math.sqrt(x)

def test_racine():
    assert racine(25) == 5