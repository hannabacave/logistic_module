from logistic_module.LogisticEquation.Logistic_and_vectorization import Logistic_equation
from logistic_module.Mandelbrot2D.Mandelbrot_without_numba.Mandelbrot2D_without_numba import Mandelbrot_2D
from logistic_module.Mandelbrot2D.Mandelbrot_without_numba.Mandelbrot2DAnimation_without_numba import animate
from logistic_module.Mandelbrot2D.Mandelbrot_without_numba.Inside_Mandelbrotset_without_numba import Inside_the_set
from logistic_module.Mandelbrot3D.Mandelbrot3D import Mand_3D
import numpy as np


le = Logistic_equation(n=1)
m2 = Mandelbrot_2D(largeur=2,hauteur=2,max_iteration=4,xmin=1, xmax=2, ymin=1, ymax=2)
m3 = Mand_3D(n=200, M=200, L=1.4, dx=-0.6, dy=0.0)


def test_logistic():
    assert le.logistic(2, 1) == 0

def test_vectorization():
    assert le.vectorization(1,2) == [(1, 0), (1, 0), (0, 0)]


def test_mandelbrotset():
    assert np.any(m2.Mandelbrotset() == np.array([[1., 1.], [1., 1.]]))

def Mandelbrot_2D_fig():
    Z=Mandelbrot_2D(500,500,5,-1,1,-1,1)
    assert Z.fig.shape==(500,500)
    

def test_m3D_grid():

    """Test if the shape of the grid is right."""

    assert np.shape(m3.grid()) == (2, m3.M, m3.M)

def test_m3D_Xaxis():

    """Test if the X-axis is well set to see the complete fractal."""  
    
    assert (-m3.L + m3.dx <= -1.99) and (m3.L + m3.dx >= 0.79)


def test_m3D_Yaxis():

    """Test if the Y-axis is well set to see the complete fractal."""

    assert (-m3.L + m3.dy <= -1.39) and (m3.L + m3.dy >= 1.39)

     
def test_m3D_mand():

    """Test if the shape of the elevated Mandelbrot set is right."""
    import warnings
    warnings.filterwarnings("ignore")
    assert np.shape(m3.mand()) == (m3.M, m3.M)  


def test_m3D_interact():

    """Test if the 3D modelization of the Mandelbrot set isn't too long."""

    import time
    start = time.time()
    m3.interact()
    end = time.time() 

    assert (end - start) < 2.0