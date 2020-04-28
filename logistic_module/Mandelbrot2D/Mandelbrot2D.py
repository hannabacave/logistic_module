from numba import int64
from numba import float64
from numba import jitclass
import numpy as np
import numba as nb
import matplotlib.pyplot as plt

spec = [('largeur', int64),
        ('hauteur', int64),
        ('max_iteration', int64),
        ('xmin', float64), ('xmax', float64), ('ymin', float64), ('ymax', float64),
        ('array', int64[:,:]), ]

@jitclass(spec)
class Mandelbrot_2D_jit:
    """Returns a matrix with values 0 if the point is in the Mandelbrot set, 1 if it is not. The number of iterations can be chosen with maxiteration, so that the function return the state of the Mandelbrot set after this number of iterations
    
    :return: A matrix with values 1 (if the point is not in the mandelbrot set) and 0 (if the point is in the Mandlebrot set)
    :rtype: array of integers
    """
    def __init__(self, largeur, hauteur, max_iteration, xmin, xmax, ymin, ymax):
        """Initialization of the parameters

        :param largeur: numbers of columns of the matrix
        :type largeur: integer    

        :param hauteur: numbers of lines of the matrix
        :type hauteur: integer

        :param max_iteration: numbers of iterations to make before returning the matrix
        :type max_iteration: positive integer

        :param xmin: minimum value for x
        :type xmin: float

        :param xmax: maximum value for x
        :type xmax: float

        :param ymin: minimum value for y
        :type ymin: float

        :param ymax: maximum value for y
        :type ymax: float
        """
        self.largeur = largeur
        self.hauteur = hauteur
        self.max_iteration = max_iteration
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    @property
    def fig(self):
        """ returns the matrix at the iteration 0
            :return: a matrix with zeros
            :return type: array of integers
        """
        self.array = np.zeros((self.hauteur, self.largeur), dtype=np.int64)
        return self.array
    
    @property
    def Mandelbrotset(self):
        """returns a matrix of the Mandelbrot set (with zeros and ones) that can be plotted
        
           :return: the state of the Mandelbrot set at the iteration max_iteration
           :return type:array of integers 
        """
        self.array=self.fig
        for x in range(self.hauteur):
            cx = (x * (self.xmax - self.xmin) / self.hauteur + self.xmin)
            for y in range(self.largeur):
                cy = (y * (self.ymin - self.ymax) / self.largeur + self.ymax)
                xn, yn, n = 0, 0, 0
                while (xn**2 + yn**2) < 4 and n < self.max_iteration:
                    tmp_x, tmp_y = xn, yn
                    xn = tmp_x**2 - tmp_y**2 + cx
                    yn = 2 * tmp_x * tmp_y + cy
                    n = n + 1
                if n < self.max_iteration:
                    self.array[y, x] = 1
        return self.array







