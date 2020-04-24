import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.sparse import csr_matrix, isspmatrix
from memory_profiler import profile

from Mandelbrot2D import Mandelbrot_2D

@profile
def plot_patterns():
    """plot the pattern you have chosen from the list

      :param x: A word from the 3 possibilities of the list given
      :type x: string
    """

    x=input('Which one do you want to plot ("Elephant valley", "Triple squared valley" or "mini mandelbrot". Write the answer without quotes)?')

    if x=="mini mandelbrot":
        #plt.imshow(mandelbrot(500, 500, 50, -2, 0.5, -1.25, 1.25)) #Plot of the Mandelbrot set
        #Thanks to this plot and each plot of a sparse matrix, we can precisely find new values of xmin/max and ymin/max to make an over zoom on a characteristic pattern of the set

        #First plot of a characteristic pattern of the Mandelbrot set:
        Z=Mandelbrot_2D(500,500,1000,-1, -0.5, -0.25, 0.25) 
        #This is a sparse matrix:
        isspmatrix(csr_matrix(Z.Mandelbrotset))
        #We found new xmin/max and ymin/max thanks to the sparse matrix and %matplotlibnotebook, but we need an over sparse matrix with a higher zoom to find a pattern:
        Z_1=Mandelbrot_2D(500,500,600,-0.74,-0.71,0.19,0.22)
        isspmatrix(Z_1.Mandelbrotset)
        #Chraracteristic pattern:
        Z_2=Mandelbrot_2D(500,500,600,-0.718,-0.714,0.213,0.217)
        fig = plt.figure()
        fig.suptitle("Minis mandelbrot set")
        im = plt.imshow(Z_2.Mandelbrotset, cmap='binary')
    if x=="Elephant valley":
        #Second plot of a characteristic pattern of the Mandelbrot set (elephant valley):
        Z_3=Mandelbrot_2D(500,500,600,0.25,0.30,-0.01,0.04) #An over sparse matrix
        isspmatrix(csr_matrix(Z_3.Mandelbrotset))
        Z_4=Mandelbrot_2D(500,500,600,0.2615,0.2634,0.0018,0.003) #Sparse matrix again
        #Second plot:
        Z_5=Mandelbrot_2D(500,500,600,0.26185,0.26196,0.002515,0.002573)
        fig = plt.figure()
        fig.suptitle("Elephant valleys")
        im = plt.imshow(Z_5.Mandelbrotset, cmap='binary')
    if x=="Triple squared valley":
        Z=Mandelbrot_2D(500,500,600,-0.057,-0.075,0.6435,0.6544)
        isspmatrix(csr_matrix(Z.Mandelbrotset))
        Z=Mandelbrot_2D(500,500,600,-0.069,-0.0669,0.6478,0.6490)
        fig = plt.figure()
        fig.suptitle("Triple squared valley")
        im = plt.imshow(Z.Mandelbrotset, cmap='binary')
    if x!="mini mandelbrot" and x!="Elephant valley" and x!="Triple squared valley":
        print("It seems like you did not chose one of the patterns of the list...Restart the function if you want to plot a characteristic pattern")
    plt.colorbar()
    plt.show()