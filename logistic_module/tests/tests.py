from logistic_module import *

def test_logistic():
    assert logistic(2, 1) == 0

def test_vectorization():
    assert vectorization(1,2,1) == [(1, 0), (1, 0), (0, 0)]