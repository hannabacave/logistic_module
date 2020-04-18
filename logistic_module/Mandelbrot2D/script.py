#The functions used in this script are coming from other scripts, so we have to import them:
from Mandelbrot2D import Mandelbrot_2D
from Mandelbrot2DAnimation import animate

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

from numba import int64
from numba import float64
from numba import jitclass
from numba import jit 
import time

start2D = time.time()

#This values of parameters allow to print the Mandelbrot set like we often represent it:
Z = Mandelbrot_2D(hauteur=500, largeur=500, max_iteration=100,
                  xmin=-2, xmax=0.5, ymin=-1.25, ymax=1.25)

fig = plt.figure()
fig.suptitle("Ensemble de mandelbrot")
im = plt.imshow(Z.__Mandelbrotset__)
plt.colorbar()
plt.show()

end2D=time.time()
print("Time spent to print the Mandelbrotset:  {0:.5f} s.".format(end2D - start2D))

start_animation=time.time()
#We can see that the shape obtained by printing Z can be seen again by zooming (Mandelbrot set is a fractale set). Changing the values for xmin, xmax, ymin et ymax (by making the interval between min and max values smaller) is in fact like making a zoom on the Mandelbrot set. 
fig, ax = plt.subplots(1, 1, figsize=(12, 6),
                       sharey=True)
                       
Z_1 = Mandelbrot_2D(500, 500, 50, -2, 0.5, -1.25, 1.25)
#We print the original picture of the Mandelbrot set, without any zoom:
im = plt.imshow(Z_1.__Mandelbrotset__)
#We use the function Animation from matplotlib so that every zoom is printed after the previous one. Tha values for i are the integers between 0 and 11, it corresponds to frames in the parameters:
anim = animation.FuncAnimation(fig, animate, frames=np.arange(11), interval=400, blit=False)
#We save the animation:
anim.save('MandelbrotAnimation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()
fig.suptitle("Fractale de mandelbrot")
plt.colorbar()

end_animation=time.time()
print("Time spent to animate the zoom on the Mandelbrotset:  {0:.5f} s.".format(end_animation - start_animation))