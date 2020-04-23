#The functions used in this script are coming from other scripts, so we have to import them:
from Mandelbrot2D import Mandelbrot_2D
from Mandelbrot2DAnimation import animate
from Inside_Mandelbrotset  import Inside_the_set
from Plot_pattern import plot_patterns

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

from numba import int64
from numba import float64
from numba import jitclass
from numba import jit 
import time

start = time.time()

#This values of parameters allow to print the Mandelbrot set like we often represent it:
Z = Mandelbrot_2D(hauteur=500, largeur=500, max_iteration=100,
                  xmin=-2, xmax=0.5, ymin=-1.25, ymax=1.25)
fig = plt.figure()
fig.suptitle("Mandelbrot set")
im = plt.imshow(Z.Mandelbrotset)
plt.colorbar()
plt.show()

end=time.time()
print("Time spent to print the Mandelbrotset:  {0:.5f} s.".format(end - start))


start_1=time.time()
#We can see that the shape obtained by printing Z can be seen again by zooming (Mandelbrot set is a fractale set). Changing the values for xmin, xmax, ymin et ymax (by making the interval between min and max values smaller) is in fact like making a zoom on the Mandelbrot set. 
fig = plt.figure()
fig.suptitle("Mandelbrot fractal")
Z_1 = Mandelbrot_2D(500, 500, 50, -2, 0.5, -1.25, 1.25)
#We print the original picture of the Mandelbrot set, without any zoom:
im = plt.imshow(Z_1.Mandelbrotset)
#We use the function Animation from matplotlib so that every zoom is printed after the previous one. Tha values for i are the integers between 0 and 11, it corresponds to frames in the parameters:
anim = animation.FuncAnimation(fig, animate, frames=np.arange(15), interval=400, blit=False)
plt.show()
end_1=time.time()
print("Time spent to animate the zoom on the Mandelbrotset:  {0:.5f} s.".format(end_1 - start_1))

start_2=time.time()
Inside_the_set()
end_2=time.time()
print("Time spent to animate the zoom inside the Mandelbrotset:  {0:.5f} s.".format(end_2 - start_2))

start_3=time.time()
plot_patterns()
end_3=time.time()
print("Time spent to plot a characteristic pattern:  {0:.5f} s.".format(end_3 - start_3))

