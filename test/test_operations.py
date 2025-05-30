from src.math.py import add,sub  
def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0

def test_sub():
    assert sub(8,4)==4 
    assert sub(8,2)==6 
    assert sub(3,4)==1 