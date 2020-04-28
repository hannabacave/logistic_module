from logistic_module.LogisticEquation.Logistic_and_vectorization import Logistic_equation
from logistic_module.Mandelbrot2D.Mandelbrot_without_numba.Mandelbrot2D_without_numba import Mandelbrot_2D
from logistic_module.Mandelbrot2D.Mandelbrot_without_numba.Mandelbrot2DAnimation_without_numba import animate
from logistic_module.Mandelbrot2D.Mandelbrot_without_numba.Inside_Mandelbrotset_without_numba import animate_200
from logistic_module.Mandelbrot2D.Mandelbrot_without_numba.Plot_pattern_without_numba import plot_patterns
from logistic_module.Mandelbrot3D.Mandelbrot3D import Mand_3D
from scipy.sparse import csr_matrix, isspmatrix
import numpy as np


le = Logistic_equation(n=1)
m2 = Mandelbrot_2D(largeur=2,hauteur=2,max_iteration=4,xmin=1, xmax=2, ymin=1, ymax=2)
Z=Mandelbrot_2D(500,500,5,-1,1,-1,1)
Z_1=Mandelbrot_2D(500,500,50,-1, -0.5, -0.25, 0.25)
Z_2=Mandelbrot_2D(500,500,50,-0.74,-0.71,0.19,0.22)
Z_3=Mandelbrot_2D(500,500,50,0.25,0.30,-0.01,0.04)
Z_4=Mandelbrot_2D(500,500,50,-0.057,-0.075,0.6435,0.6544)
m3 = Mand_3D(n=200, M=200, L=1.4, dx=-0.6, dy=0.0)


def test_logistic():
    assert le.logistic(2, 1) == 0

def test_vectorization():
    assert le.vectorization(1,2) == [(1, 0), (1, 0), (0, 0)]


def test_mandelbrotset():
    assert np.any(m2.Mandelbrotset() == np.array([[1., 1.], [1., 1.]]))

def Mandelbrot_2D_fig():
    assert Z.fig.shape==(500,500)
    
def test_plot_patterns():
    assert plot_patterns(x="test")=='It seems like you did not chose one of the patterns of the list...Restart the function if you want to plot a characteristic pattern'

def test_animation_2D():
    for i in range(8):
        im=animate(i)
        assert str(type(im))=="<class 'matplotlib.image.AxesImage'>"

def test_animation_200():
    for i in range(1,201,100):
        im=animate_200(i,"no")
        assert str(type(im))=="<class 'tuple'>"

def test_sparse_matrix_1():
    assert isspmatrix(csr_matrix(Z.Mandelbrotset()))==True

def test_sparse_matrix_2():
    assert isspmatrix(csr_matrix(Z_1.Mandelbrotset()))==True

def test_sparse_matrix_3():
    assert isspmatrix(csr_matrix(Z_2.Mandelbrotset()))==True

def test_sparse_matrix_4():
    assert isspmatrix(csr_matrix(Z.Mandelbrotset()))==True
    

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
