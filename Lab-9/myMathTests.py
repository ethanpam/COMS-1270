from myMath import add, divide

def test_add():
    assert add(1,1) == 2
    assert add(1,-1) == 0
    assert add(-1,1) == 0
    assert add(-1,-1) == -2