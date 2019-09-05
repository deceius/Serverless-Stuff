import pytest
def add2Numbers( x, y):
    return x + y

pytest.mark.test1
def test_addition():
    a = 5
    b = 4
    assert add2Numbers(a, b) == 10