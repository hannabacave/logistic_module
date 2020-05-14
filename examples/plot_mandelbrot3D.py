"""
Mandelbrot set 3D
============================
In this setion, you can see how to plot the Mandelbrot set in 3D.
"""

from logistic_module.Mandelbrot3D.Mandelbrot3D import Mand_3D


n, M, L, dx, dy = 200, 200, 1.4, -0.6, 0.0
m3d = Mand_3D(n,M,L,dx,dy)
fig = m3d.interact()

fig.show()

