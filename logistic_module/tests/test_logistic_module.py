from logistic_module.LogisticEquation.Logistic_and_vectorization import Logistic_equation
from logistic_module.Mandelbrot2D.Mandelbrot2D import Mandelbrot_2D
le = Logistic_equation(n=1)
m2 = Mandelbrot_2D(hauteur=2, largeur=2)

def test_logistic():
    assert le.logistic(2, 1) == 0

def test_vectorization():
    assert le.vectorization(1,2) == [(1, 0), (1, 0), (0, 0)]

def test_mandelbrotset():
    assert m2.__Mandelbrotset__(4, 1, 2, 1, 2) == [[0., 1.], [0., 1.]]