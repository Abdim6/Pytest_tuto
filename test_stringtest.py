import pytest
@pytest.mark.skip(reason="do not run string2")

def test_string2():
    var1 = "bonjour"
    var2 = "Hello"
    assert "Hello" in var2
    
def test_string1():
    var = "ceci est une phrase"
    assert "hello" not in var

def test_sayhello():
    var = "yes"
    assert "yes" == var

