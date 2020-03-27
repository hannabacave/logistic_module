import Mandelbrot2D

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
%matplotlib notebook
Z=Mandelbrot2D.mandelbrot(500,500, 100,  -2, 0.5, -1.25, 1.25)

fig = plt.figure()
fig.suptitle("Ensemble de mandelbrot")
im = plt.imshow(Z)
plt.colorbar()
plt.show()

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

%matplotlib notebook
fig, ax = plt.subplots(1, 1, figsize=(12, 6),
                       sharey=True)
im = plt.imshow(Z_1)

animate=Mandelbrot2DAnimation.animate

plt.show()
fig.suptitle("Fractale de mandelbrot")
plt.colorbar()
anim = animation.FuncAnimation(fig, animate, frames=np.arange(11), interval=400, blit=False)