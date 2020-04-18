import numpy as np
import matplotlib.pyplot as plt
import time
from numba import int32

spec= [
    ('largeur', int32),               
    ('hauteur', int32), 
    ('max_iteration', int32),
    ('xmin', int32),
    ('xmax', int32),
    ('ymin', int32),
    ('ymax', int32),
]
start = time.time()
#@jitclass(spec)
class Mandelbrot_2D(object):
    """Returns a matrix with values 0 if the point is in the Mandelbrot set, 1 if it is not. The number of iterations can be chosen with maxiteration, so that the function return the state of the Mandelbrit set after this number of iterations
    
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

    :return: A matrix with values 1 (if the point is not in the mandelbrot set) and 0 (if the point is in the Mandlebrot set)
    :rtype: integers
    """

    def __init__(self, largeur, hauteur, max_iteration, xmin, xmax, ymin, ymax):
        self.largeur = largeur
        self.hauteur = hauteur
    #@property

    def __Mandelbrotset__(self, largeur, hauteur, max_iteration, xmin, xmax, ymin, ymax):
        #We first create a matrix with dimensions chosen by the user with the parameters "largeur" and "hauteur". Shes only contains zeros, but some of the values of the matrix will be changed by the function
        self = np.zeros((self.hauteur, self.largeur))
        for x in range(self.shape[0]):
            #for each line of the matrix, we define the value cx, that will be used later to change the values of (xn)
            cx = (x * (xmax - xmin) / self.shape[0] + xmin)
            for y in range(self.shape[1]):
                #In the same way, for each column of the matrix, we define cy, that will be used to change the values of (yn)
                cy = (y * (ymin - ymax) / self.shape[1] + ymax)
                #The first vakues of (xn) and (yn) are zeros. We start the program at time 0, so we are at the ieration 0 (n referes to the number of iterations already made)
                xn, yn, n = 0, 0, 0
                #The user has chosen the number of maximal iteration. While this number si not reached, every value of the matrix can be changed: if the squared norm of the vector (xn,yn) is less than 4, we change the series (xn) and (yn) without changing the value at the coordinate [x,y] of the matrix (the point at the coordinate (x,y) is in the Mandelbrot set): 
                while (xn**2 + yn**2) < 4 and n < max_iteration:
                    tmp_x, tmp_y = xn, yn
                    xn = tmp_x**2 - tmp_y**2 + cx
                    yn = 2 * tmp_x * tmp_y + cy
                    n = n + 1
                #If the square norm is higher than 4 and the number of maximal iterations is not reached, we change the value at the coordinate (x,y) of the matrix : the 0 becomes a 1 (this points is no longer is the Mandelbrot set but in is complementary
                if n < max_iteration:
                    self[y, x] = 1
        #When maxiteration is reached, we return the modifief matrix:
        return self

end=time.time()
print("Temps passé pour éxécuter la fonction:  {0:.5f} s.".format(end - start))
