import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.sparse import csr_matrix, isspmatrix
from memory_profiler import profile

from logistic_module.Mandelbrot2D.Mandelbrot2D import Mandelbrot_2D

@profile
def plot_patterns():
    """Plot the pattern you have chosen from the list (this choice is made with x). Possible plots: Elephant valleys, Triple squared valleys and mini-mandelbrots
    """

    x=input('Which one do you want to plot ("Elephant valley", "Triple squared valley" or "mini mandelbrot". Write the answer without quotes)?')

    if x=="mini mandelbrot":
        Z_2=Mandelbrot_2D(500,500,600,-0.718,-0.714,0.213,0.217)
        fig = plt.figure()
        fig.suptitle("Minis mandelbrot set")
        im = plt.imshow(Z_2.Mandelbrotset, cmap='binary')
    if x=="Elephant valley":
        Z_5=Mandelbrot_2D(500,500,600,0.26185,0.26196,0.002515,0.002573)
        fig = plt.figure()
        fig.suptitle("Elephant valleys")
        im = plt.imshow(Z_5.Mandelbrotset, cmap='binary')
    if x=="Triple squared valley":
        Z=Mandelbrot_2D(500,500,600,-0.069,-0.0669,0.6478,0.6490)
        fig = plt.figure()
        fig.suptitle("Triple squared valley")
        im = plt.imshow(Z.Mandelbrotset, cmap='binary')
    if x!="mini mandelbrot" and x!="Elephant valley" and x!="Triple squared valley":
        return "It seems like you did not chose one of the patterns of the list...Restart the function if you want to plot a characteristic pattern"
    plt.colorbar()
    plt.show()
