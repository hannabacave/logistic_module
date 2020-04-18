#The functions used in this script are coming from other scripts, so we have to import them:
from Mandelbrot2D import *
from Mandelbrot2DAnimation import *


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

#This values of parameters allow to print the Mandelbrot set like we often represent it:
Z = Mandelbrot_2D(hauteur=500, largeur=500, max_iteration=100,
                  xmin=-2, xmax=0.5, ymin=-1.25, ymax=1.25)
Z.__Mandelbrotset__(500, 500, 100,  -2, 0.5, -1.25, 1.25)

from matplotlib import animation
fig = plt.figure()
fig.suptitle("Ensemble de mandelbrot")
im = plt.imshow(Z.__Mandelbrotset__(500, 500, 100,  -2, 0.5, -1.25, 1.25))
plt.colorbar()
plt.show()

#We can see that the shape obtained by printing Z can be seen again by zooming (Mandelbrot set is a fractale set). Changing the values for xmin, xmax, ymin et ymax (by making the interval between min and max values smaller) is in fact like making a zoom on the Mandelbrot set. 
Z_1 = mandelbrot(500, 500, 50, -2, 0.5, -1.25, 1.25)
Z_2 = mandelbrot(500, 500, 50, -1.5, 0.2, -0.85, 0.85)
Z_3 = mandelbrot(500, 500, 50, -1.4, 0, -0.9, 0.5)
Z_4 = mandelbrot(500, 500, 50, -1.4, -0.2, -0.9, 0.3)
Z_5 = mandelbrot(500, 500, 50, -1.4, -0.5, -0.7, 0.2)
Z_6 = mandelbrot(500, 500, 50, -1.4, -0.9, -0.5, 0.1)
Z_7 = mandelbrot(500, 500, 50, -1.4, -1.2, -0.13, 0.07)
Z_8 = mandelbrot(500, 500, 50, -1.4, -1.23, -0.10, 0.07)
Z_9 = mandelbrot(500, 500, 50, -1.4, -1.25, -0.08, 0.07)
Z_10 = mandelbrot(500, 500, 50, -1.4, -1.3, -0.06, 0.04)
Z_11 = mandelbrot(500, 500, 50, -1.4, -1.32, -0.04, 0.04)
Z_12 = mandelbrot(500, 500, 50, -1.4, -1.36, -0.04, 0.04)

fig, ax = plt.subplots(1, 1, figsize=(12, 6),
                       sharey=True)
#We print the original picture of the Mandelbrot set, without any zoom:
im = plt.imshow(Z_1)
#We use the function Animation from matplotlib so that every zoom is printed after the previous one. Tha values for i are the integers between 0 and 11, it corresponds to frames in the parameters:
anim = animation.FuncAnimation(fig, animate, frames=np.arange(11), interval=400, blit=False)
#We save the animation:
anim.save('MandelbrotAnimation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()
fig.suptitle("Fractale de mandelbrot")
plt.colorbar()