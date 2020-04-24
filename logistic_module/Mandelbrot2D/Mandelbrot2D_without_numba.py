import numpy as np
import matplotlib.pyplot as plt
from memory_profiler import profile
import cProfile

class Mandelbrot_2D(object):
    """Returns a matrix with values 0 if the point is in the Mandelbrot set, 1 if it is not. The number of iterations can be chosen with maxiteration, so that the function return the state of the Mandelbrit set after this number of iterations
    
    :return: A matrix with values 1 (if the point is not in the mandelbrot set) and 0 (if the point is in the Mandlebrot set)
    :rtype: array of integers
    """
    @profile
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
        
    def fig(self):
        """ returns the matrix at the iteration 0
            :return: a matrix with zeros
            :return type: array of integers
        """
        self.array = np.zeros((self.hauteur, self.largeur), dtype=int64)
        return self.array
    
    def Mandelbrotset(self):
        """returns a matrix of the Mandelbrot set (with zeros and ones) that can be plotted
        
           :return: the state of the Mandelbrot set at the iteration max_iteration
           :return type:array of integers 
        """
        #We first create a matrix with dimensions chosen by the user with the parameters "largeur" and "hauteur". Shes only contains zeros, but some of the values of the matrix will be changed by the function
        self.array = self.array=self.fig
        for x in range(self.hauteur):
            #for each line of the matrix, we define the value cx, that will be used later to change the values of (xn)
            cx = (x * (self.xmax - self.xmin) / self.hauteur + self.xmin)
            for y in range(self.largeur):
                #In the same way, for each column of the matrix, we define cy, that will be used to change the values of (yn)
                cy = (y * (self.ymin - self.ymax) / self.largeur + self.ymax)
                #The first vakues of (xn) and (yn) are zeros. We start the program at time 0, so we are at the ieration 0 (n referes to the number of iterations already made)
                xn, yn, n = 0, 0, 0
                #The user has chosen the number of maximal iteration. While this number si not reached, every value of the matrix can be changed: if the squared norm of the vector (xn,yn) is less than 4, we change the series (xn) and (yn) without changing the value at the coordinate [x,y] of the matrix (the point at the coordinate (x,y) is in the Mandelbrot set): 
                while (xn**2 + yn**2) < 4 and n < self.max_iteration:
                    tmp_x, tmp_y = xn, yn
                    xn = tmp_x**2 - tmp_y**2 + cx
                    yn = 2 * tmp_x * tmp_y + cy
                    n = n + 1
                #If the square norm is higher than 4 and the number of maximal iterations is not reached, we change the value at the coordinate (x,y) of the matrix : the 0 becomes a 1 (this points is no longer is the Mandelbrot set but in is complementary
                if n < self.max_iteration:
                    self.array[y, x] = 1
        #When maxiteration is reached, we return the modifief matrix:
        return self.array

#cProfile.run("Mandelbrot_2D(500, 500, 50, -2, 0.5, -1.25, 1.25).Mandelbrotset")






