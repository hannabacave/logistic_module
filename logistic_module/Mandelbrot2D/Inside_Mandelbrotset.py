import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

from Mandelbrot2D import Mandelbrot_2D

def Inside_the_set():
    """Animate a zoom inside the Mandelbrot set
    :return: video of more than 200 frames
    :rtype: video
    """
    fig = plt.figure()
    fig.suptitle("Inside the Mandelbrot fractal")
    Z=Mandelbrot_2D(500, 500, 50, -2, 0.5, -1.25, 1.25)
    im = plt.imshow(Z.Mandelbrotset)
    def animate_200(i):
        if i<=50:
            Z=Mandelbrot_2D(500,500,50,-2+0.02*i,0.5-0.02*i, -1.25+0.02*i, 1.25-0.02*i)
            im.set_data(Z.Mandelbrotset)
        if i>50 and i<=130:
            Z_1=Mandelbrot_2D(500,500,200,-1+0.0026*(i-50),-0.5-0.0021*(i-50), -0.25+0.0044*(i-50), 0.25-0.0003*(i-50))
            im.set_data(Z_1.Mandelbrotset)
        if i>130:
            Z_2=Mandelbrot_2D(500,500,600,-0.74+0.00044*(i-150),-0.71-0.00008*(i-150), 0.19+0.00046*(i-150), 0.22-0.00006*(i-150))
            im.set_data(Z_2.Mandelbrotset)
        return im,
    anim = animation.FuncAnimation(fig, animate_200, frames=np.arange(0,210,1), interval=1, blit=False)
    plt.show()