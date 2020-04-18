from numba import jit 
import matplotlib.pyplot as plt
from Mandelbrot2D import Mandelbrot_2D

Z_2 = Mandelbrot_2D(500, 500, 50, -1.5, 0.2, -0.85, 0.85)
Z_3 = Mandelbrot_2D(500, 500, 50, -1.4, 0, -0.9, 0.5)
Z_4 = Mandelbrot_2D(500, 500, 50, -1.4, -0.2, -0.9, 0.3)
Z_5 = Mandelbrot_2D(500, 500, 50, -1.4, -0.5, -0.7, 0.2)
Z_6 = Mandelbrot_2D(500, 500, 50, -1.4, -0.9, -0.5, 0.1)
Z_7 = Mandelbrot_2D(500, 500, 50, -1.4, -1.2, -0.13, 0.07)
Z_8 = Mandelbrot_2D(500, 500, 50, -1.4, -1.23, -0.10, 0.07)
Z_9 = Mandelbrot_2D(500, 500, 50, -1.4, -1.25, -0.08, 0.07)
Z_10 = Mandelbrot_2D(500, 500, 50, -1.4, -1.3, -0.06, 0.04)
Z_11 = Mandelbrot_2D(500, 500, 50, -1.4, -1.32, -0.04, 0.04)
Z_12 = Mandelbrot_2D(500, 500, 50, -1.4, -1.36, -0.04, 0.04)

@jit(nopython=False)
def animate(i):
    """Animated zoom on the mandelbrot set
    :param i: the number of time the functions is to be used
    :type i: integer

    :return: An image with a zoom on the Mandelbrot set
    :rtype: object 
    """
    #The programm passes this function multiples times: it goes from i=0 to a value of i that we are going to chose in the document script.py. For each value of i, we print a different matrice. As i increases, the interval for min values and max values (for x and y) becomes smaller, visuallly it is like if we were zooming on the first picture (obtained by printing Z)
    if i == 0:
        im = plt.imshow(Z_2.__Mandelbrotset__)
    if i == 1:
        im = plt.imshow(Z_3.__Mandelbrotset__)
    if i == 2:
        im = plt.imshow(Z_4.__Mandelbrotset__)
    if i == 3:
        im = plt.imshow(Z_5.__Mandelbrotset__)
    if i == 4:
        im = plt.imshow(Z_6.__Mandelbrotset__)
    if i == 5:
        im = plt.imshow(Z_7.__Mandelbrotset__)
    if i == 6:
        im = plt.imshow(Z_8.__Mandelbrotset__)
    if i == 7:
        im = plt.imshow(Z_9.__Mandelbrotset__)
    if i == 8:
        im = plt.imshow(Z_10.__Mandelbrotset__)
    if i == 9:
        im = plt.imshow(Z_11.__Mandelbrotset__)
    if i == 10:
        im = plt.imshow(Z_12.__Mandelbrotset__)
    return im,


