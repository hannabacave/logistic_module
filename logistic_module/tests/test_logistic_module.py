from logistic_module.LogisticEquation.Logistic_and_vectorization import Logistic_equation
from logistic_module.Mandelbrot2D.Mandelbrot_without_numba.Mandelbrot2D_without_numba import Mandelbrot_2D
from logistic_module.Mandelbrot2D.Mandelbrot_without_numba.Inside_Mandelbrotset_without_numba import animate_200
from logistic_module.Mandelbrot2D.Mandelbrot2D import Mandelbrot_2D_jit
from logistic_module.Mandelbrot2D.Mandelbrot2DAnimation import animate
from logistic_module.Mandelbrot2D.Inside_Mandelbrotset import Inside_the_set
from logistic_module.Mandelbrot2D.Plot_pattern import plot_patterns
from logistic_module.Mandelbrot3D.Mandelbrot3D import Mand_3D
from scipy.sparse import csr_matrix, isspmatrix
import numpy as np
import time


le = Logistic_equation(n=1)
m2 = Mandelbrot_2D_jit(largeur=2,hauteur=2,max_iteration=4,xmin=1, xmax=2, ymin=1, ymax=2)
M=Mandelbrot_2D_jit(500,500,5,-1,1,-1,1)
M_1=Mandelbrot_2D_jit(500,500,50,-1, -0.5, -0.25, 0.25)
M_2=Mandelbrot_2D_jit(500,500,50,-0.74,-0.71,0.19,0.22)
m3 = Mand_3D(n=200, M=200, L=1.4, dx=-0.6, dy=0.0)


def test_logistic():
    assert le.logistic(2, 1) == 0

def test_vectorization():
    assert le.vectorization(1,2) == [(1, 0), (1, 0), (0, 0)]

    
def test_Mandelbrot_jit():
    start = time.time()
    print(Mandelbrot_2D_jit(500,500,5,-1,1,-1,1))
    end = time.time()
    assert (end - start) < 120.0
   
def test_Mandelbrot_Animation_jit():
    for i in range(8):
        im=animate(i)
        assert str(type(im))=="<class 'tuple'>"

def test_Mandelbrot_Animation_time():
    start = time.time()
    im=animate(0)
    end = time.time()
    assert (end - start) < 30
    
def test_mandelbrotset_jit():
    assert np.any(m2.Mandelbrotset) == 1

def Mandelbrot_2D_fig_jit():
    assert Z.fig.shape==(500,500)
    
def test_plot_patterns():
    assert plot_patterns(x="test")=='It seems like you did not chose one of the patterns of the list...Restart the function if you want to plot a characteristic pattern'

def test_pattern_1():
    im=plot_patterns(x="mini mandelbrot")
    assert str(type(im))=="<class 'matplotlib.image.AxesImage'>"

def test_pattern_2():
    im=plot_patterns(x="Elephant valley")
    assert str(type(im))=="<class 'matplotlib.image.AxesImage'>"

def test_pattern_3():
    im=plot_patterns(x="Triple squared valley")
    assert str(type(im))=="<class 'matplotlib.image.AxesImage'>"    
    
def test_pattern_time():
    start=time.time()
    im=plot_patterns(x="Elephant valley")
    im
    end=time.time()
    assert (end-start) < 15

def test_Inside_the_set_1():
    start=time.time()
    x="no"
    m=Inside_the_set(x)
    m
    end=time.time()
    assert (end -start)<60
    
def test_Inside_the_set_1():
    start=time.time()
    x="yes"
    m=Inside_the_set(x)
    m
    end=time.time()
    assert (end -start)<120
    
def test_Inside_the_set_1():
    x="no"
    im=Inside_the_set(x)
    assert str(type(im))=="<class 'matplotlib.image.AxesImage'>"

def test_sparse_matrix_1():
    assert isspmatrix(csr_matrix(M.Mandelbrotset))==True

def test_sparse_matrix_2():
    assert isspmatrix(csr_matrix(M_1.Mandelbrotset))==True

def test_sparse_matrix_3():
    assert isspmatrix(csr_matrix(M_2.Mandelbrotset))==True
    

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
