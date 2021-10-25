import pytest
import math_fun

@pytest.mark.parametrize('var1,var2,result',
                    [
                       (7,5,12),
                       ('hello',' world','hello world'),
                       (10.5,25.5,36) 
                    ]   
                    )
def test_add(var1,var2,result):
    assert math_fun.test_add2 (var1,var2)== result