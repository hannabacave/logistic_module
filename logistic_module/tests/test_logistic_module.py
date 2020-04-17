from logistic_module.LogisticEquation.Logistic_and_vectorization import Logistic_equation
le = Logistic_equation(n=1)

def test_logistic():
    assert le.logistic(2, 1) == 0

def test_vectorization():
    assert le.vectorization(1,2) == [(1, 0), (1, 0), (0, 0)]